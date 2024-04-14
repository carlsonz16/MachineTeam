from nba_api.stats.static import teams, players
from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import cumestatsteamgames, cumestatsteam, gamerotation
import pandas as pd
import numpy as np
from dateutil import parser
from datetime import datetime
import pytz
import json
import difflib
import time
import requests


# Retry Wrapper 
def retry(func, retries=3):
    def retry_wrapper(*args, **kwargs):
        attempts = 0
        while attempts < retries:
            try:
                return func(*args, **kwargs)
            except requests.exceptions.RequestException as e:
                print(e)
                time.sleep(30)
                attempts += 1

    return retry_wrapper

# Get Season Schedule Function 
def getSeasonScheduleFrame(seasons,seasonType): 

    # Get date from string
    def getGameDate(matchup):
        return matchup.partition(' at')[0][:10]

    # Get Home team from string
    def getHomeTeam(matchup):
        return matchup.partition(' at')[2]

    # Get Away team from string
    def getAwayTeam(matchup):
        return matchup.partition(' at')[0][10:]

    # Match nickname from schedule to team table to find ID
    def getTeamIDFromNickname(nickname):
        return teamLookup.loc[teamLookup['nickname'] == difflib.get_close_matches(nickname,teamLookup['nickname'],1)[0]].values[0][0] 
    
    @retry
    def getRegularSeasonSchedule(season,teamID,seasonType):
        season = str(season) + "-" + str(season+1)[-2:] # Convert year to season format ie. 2020 -> 2020-21
        teamGames = cumestatsteamgames.CumeStatsTeamGames(league_id = '00',season = season ,
                                                                      season_type_all_star=seasonType,
                                                                      team_id = teamID).get_normalized_json()

        teamGames = pd.DataFrame(json.loads(teamGames)['CumeStatsTeamGames'])
        teamGames['SEASON'] = season
        return teamGames    
    
    # Get team lookup table
    teamLookup = pd.DataFrame(teams.get_teams())
    
    # Get teams schedule for each team for each season
    scheduleFrame = pd.DataFrame()
    
    board = scoreboard.ScoreBoard()
    games = board.games.get_dict()
    eastern = pytz.timezone('US/Eastern')
    eastern_now = datetime.now(eastern)
    formatted_date_eastern = eastern_now.strftime("%m/%d/%Y")
    todays_games_list = []
    season = str(seasons[0]) + "-" + str(seasons[0]+1)[-2:]
    for game in games:
      game_info = {
         "MATCHUP": f"{formatted_date_eastern} {game['awayTeam']['teamName']} at {game['homeTeam']['teamName']}",
         "GAME_ID": game['gameId'],
         "SEASON": f"{season}"
      }
      game_df = pd.DataFrame([game_info])
      todays_games_list.append(game_df)
    scheduleFrame = pd.concat(todays_games_list, ignore_index=True)

    scheduleFrame['GAME_DATE'] = pd.to_datetime(scheduleFrame['MATCHUP'].map(getGameDate))
    scheduleFrame['HOME_TEAM_NICKNAME'] = scheduleFrame['MATCHUP'].map(getHomeTeam)
    scheduleFrame['HOME_TEAM_ID'] = scheduleFrame['HOME_TEAM_NICKNAME'].map(getTeamIDFromNickname)
    scheduleFrame['AWAY_TEAM_NICKNAME'] = scheduleFrame['MATCHUP'].map(getAwayTeam)
    scheduleFrame['AWAY_TEAM_ID'] = scheduleFrame['AWAY_TEAM_NICKNAME'].map(getTeamIDFromNickname)
    scheduleFrame = scheduleFrame.drop_duplicates() # There's a row for both teams, only need 1
    scheduleFrame = scheduleFrame.reset_index(drop=True)
                   
    return scheduleFrame
 
 # Get Single Game aggregation columns
def getSingleGameMetrics(gameID,homeTeamID,awayTeamID,awayTeamNickname,seasonYear,gameDate):

    @retry
    def getGameStats(teamID,gameID,seasonYear):
        gameStats = cumestatsteam.CumeStatsTeam(game_ids=gameID,league_id ="00",
                                               season=seasonYear,season_type_all_star="Regular Season",
                                               team_id = teamID).get_normalized_json()

        gameStats = pd.DataFrame(json.loads(gameStats)['TotalTeamStats'])

        return gameStats

    data = getGameStats(homeTeamID,gameID,seasonYear)
    data.at[1,'NICKNAME'] = awayTeamNickname
    data.at[1,'TEAM_ID'] = awayTeamID
    data.at[1,'OFFENSIVE_EFFICIENCY'] = (data.at[1,'FG'] + data.at[1,'AST'])/(data.at[1,'FGA'] - data.at[1,'OFF_REB'] + data.at[1,'AST'] + data.at[1,'TOTAL_TURNOVERS'])
    data.at[1,'SCORING_MARGIN'] = data.at[1,'PTS'] - data.at[0,'PTS']

    data.at[0,'OFFENSIVE_EFFICIENCY'] = (data.at[0,'FG'] + data.at[0,'AST'])/(data.at[0,'FGA'] - data.at[0,'OFF_REB'] + data.at[0,'AST'] + data.at[0,'TOTAL_TURNOVERS'])
    data.at[0,'SCORING_MARGIN'] = data.at[0,'PTS'] - data.at[1,'PTS']

    data['SEASON'] = seasonYear
    data['GAME_DATE'] = gameDate
    data['GAME_ID'] = gameID

    return data

def getGameLogs(gameLogs,scheduleFrame):
    
    # Functions to prepare additional columns after gameLogs table loads
    def getHomeAwayFlag(gameDF):
        gameDF['HOME_FLAG'] = np.where((gameDF['W_HOME']==1) | (gameDF['L_HOME']==1),1,0)
        gameDF['AWAY_FLAG'] = np.where((gameDF['W_ROAD']==1) | (gameDF['L_ROAD']==1),1,0) 

    def getTotalWinPctg(gameDF):
        gameDF['TOTAL_GAMES_PLAYED'] = gameDF.groupby(['TEAM_ID','SEASON'])['GAME_DATE'].rank(ascending=True)
        gameDF['TOTAL_WINS'] = gameDF.sort_values(by='GAME_DATE').groupby(['TEAM_ID','SEASON'])['W'].cumsum()
        gameDF['TOTAL_WIN_PCTG'] = gameDF['TOTAL_WINS']/gameDF['TOTAL_GAMES_PLAYED']
        return gameDF.drop(['TOTAL_GAMES_PLAYED','TOTAL_WINS'],axis=1)

    def getHomeWinPctg(gameDF):
        gameDF['HOME_GAMES_PLAYED'] = gameDF.sort_values(by='GAME_DATE').groupby(['TEAM_ID','SEASON'])['HOME_FLAG'].cumsum()
        gameDF['HOME_WINS'] = gameDF.sort_values(by='GAME_DATE').groupby(['TEAM_ID','SEASON'])['W_HOME'].cumsum()
        gameDF['HOME_WIN_PCTG'] = gameDF['HOME_WINS']/gameDF['HOME_GAMES_PLAYED']
        return gameDF.drop(['HOME_GAMES_PLAYED','HOME_WINS'],axis=1)

    def getAwayWinPctg(gameDF):
        gameDF['AWAY_GAMES_PLAYED'] = gameDF.sort_values(by='GAME_DATE').groupby(['TEAM_ID','SEASON'])['AWAY_FLAG'].cumsum()
        gameDF['AWAY_WINS'] = gameDF.sort_values(by='GAME_DATE').groupby(['TEAM_ID','SEASON'])['W_ROAD'].cumsum()
        gameDF['AWAY_WIN_PCTG'] = gameDF['AWAY_WINS']/gameDF['AWAY_GAMES_PLAYED']
        return gameDF.drop(['AWAY_GAMES_PLAYED','AWAY_WINS'],axis=1)

    def getRollingOE(gameDF):
        gameDF['ROLLING_OE'] = gameDF.sort_values(by='GAME_DATE').groupby(['TEAM_ID','SEASON'])['OFFENSIVE_EFFICIENCY'].transform(lambda x: x.rolling(3, 1).mean())

    def getRollingScoringMargin(gameDF):
        gameDF['ROLLING_SCORING_MARGIN'] = gameDF.sort_values(by='GAME_DATE').groupby(['TEAM_ID','SEASON'])['SCORING_MARGIN'].transform(lambda x: x.rolling(3, 1).mean())

    def getRestDays(gameDF):
        gameDF['LAST_GAME_DATE'] = gameDF.sort_values(by='GAME_DATE').groupby(['TEAM_ID','SEASON'])['GAME_DATE'].shift(1)
        gameDF['NUM_REST_DAYS'] = (gameDF['GAME_DATE'] - gameDF['LAST_GAME_DATE'])/np.timedelta64(1,'D') 
        return gameDF.drop('LAST_GAME_DATE',axis=1)
    
    start = time.perf_counter_ns()

    i = int(len(gameLogs)/2) #Can use a previously completed gameLog dataset
    
    game_logs_data = []
    while i<len(scheduleFrame):
      time.sleep(1)
      game_logs_data.append(getSingleGameMetrics(scheduleFrame.at[i,'GAME_ID'],scheduleFrame.at[i,'HOME_TEAM_ID'],
                        scheduleFrame.at[i,'AWAY_TEAM_ID'],scheduleFrame.at[i,'AWAY_TEAM_NICKNAME'],
                        scheduleFrame.at[i,'SEASON'],scheduleFrame.at[i,'GAME_DATE']))
      
      gameLogs = pd.concat(game_logs_data, ignore_index=True)

      end = time.perf_counter_ns()

      #Output time it took to load x amount of records
      if i%100 == 0:
         mins = ((end-start)/1e9)/60
         print(i,str(mins) + ' minutes')

      i+=1
        
    # Get Table Level Aggregation Columns
    getHomeAwayFlag(gameLogs)
    gameLogs = getHomeWinPctg(gameLogs)
    gameLogs = getAwayWinPctg(gameLogs)
    gameLogs = getTotalWinPctg(gameLogs)
    getRollingScoringMargin(gameLogs)
    getRollingOE(gameLogs)
    gameLogs = getRestDays(gameLogs)

    return gameLogs.reset_index(drop=True)

def getGameLogFeatureSet(gameDF):

    def shiftGameLogRecords(gameDF):
        gameDF['LAST_GAME_OE'] = gameLogs.sort_values('GAME_DATE').groupby(['TEAM_ID','SEASON'])['OFFENSIVE_EFFICIENCY'].shift(1)
        gameDF['LAST_GAME_HOME_WIN_PCTG'] = gameDF.sort_values('GAME_DATE').groupby(['TEAM_ID','SEASON'])['HOME_WIN_PCTG'].shift(1)
        gameDF['LAST_GAME_AWAY_WIN_PCTG'] = gameDF.sort_values('GAME_DATE').groupby(['TEAM_ID','SEASON'])['AWAY_WIN_PCTG'].shift(1)
        gameDF['LAST_GAME_TOTAL_WIN_PCTG'] = gameDF.sort_values('GAME_DATE').groupby(['TEAM_ID','SEASON'])['TOTAL_WIN_PCTG'].shift(1)
        gameDF['LAST_GAME_ROLLING_SCORING_MARGIN'] = gameDF.sort_values('GAME_DATE').groupby(['TEAM_ID','SEASON'])['ROLLING_SCORING_MARGIN'].shift(1)
        gameDF['LAST_GAME_ROLLING_OE'] = gameDF.sort_values('GAME_DATE').groupby(['TEAM_ID','SEASON'])['ROLLING_OE'].shift(1)
    
    
    def getHomeTeamFrame(gameDF):
        homeTeamFrame = gameDF[gameDF['CITY'] != 'OPPONENTS']
        homeTeamFrame = homeTeamFrame[['LAST_GAME_OE','LAST_GAME_HOME_WIN_PCTG','NUM_REST_DAYS','LAST_GAME_AWAY_WIN_PCTG','LAST_GAME_TOTAL_WIN_PCTG','LAST_GAME_ROLLING_SCORING_MARGIN','LAST_GAME_ROLLING_OE','W','TEAM_ID','GAME_ID','SEASON']]

        colRenameDict = {}
        for col in homeTeamFrame.columns:
            if (col != 'GAME_ID') & (col != 'SEASON') :
                colRenameDict[col] = 'HOME_' + col 

        homeTeamFrame.rename(columns=colRenameDict,inplace=True)

        return homeTeamFrame

    def getAwayTeamFrame(gameDF):
        awayTeamFrame = gameDF[gameDF['CITY'] == 'OPPONENTS']
        awayTeamFrame = awayTeamFrame[['LAST_GAME_OE','LAST_GAME_HOME_WIN_PCTG','NUM_REST_DAYS','LAST_GAME_AWAY_WIN_PCTG','LAST_GAME_TOTAL_WIN_PCTG','LAST_GAME_ROLLING_SCORING_MARGIN','LAST_GAME_ROLLING_OE','TEAM_ID','GAME_ID','SEASON']]

        colRenameDict = {}
        for col in awayTeamFrame.columns:
            if (col != 'GAME_ID') & (col != 'SEASON'):
                colRenameDict[col] = 'AWAY_' + col 

        awayTeamFrame.rename(columns=colRenameDict,inplace=True)

        return awayTeamFrame
    
    shiftGameLogRecords(gameLogs)
    awayTeamFrame = getAwayTeamFrame(gameLogs)
    homeTeamFrame = getHomeTeamFrame(gameLogs)
    
    return pd.merge(homeTeamFrame, awayTeamFrame, how="inner", on=[ "GAME_ID","SEASON"]).drop(['GAME_ID','AWAY_TEAM_ID','HOME_TEAM_ID'],axis=1)

########################################################################

seasons = [2023]
seasonType = 'Regular Season'

start = time.perf_counter_ns() # Track cell's runtime
scheduleFrame = getSeasonScheduleFrame(seasons,seasonType)
end = time.perf_counter_ns()

secs = (end-start)/1e9
mins = secs/60
print(mins)

#Create the gameLogs DataFrame
gameLogs = pd.DataFrame()
gameLogs = getGameLogs(gameLogs,scheduleFrame)
gameLogs.to_csv('gameLogs.csv')

modelData = getGameLogFeatureSet(gameLogs)

modelData.to_csv('nbaHomeWinLossModelDataset.csv')