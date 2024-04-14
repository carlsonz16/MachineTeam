from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder, boxscoreadvancedv2 #player stats
from nba_api.stats.endpoints import boxscoresummaryv2, playbyplayv2
import pandas as pd
import time
import requests
from requests.exceptions import ReadTimeout

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

@retry 
def playByPlayGenerator(gameId):
    attempts = 0
    max_attempts = 5
    success = False
    
    while not success and attempts < max_attempts:
        try:
            pbp_data = playbyplayv2.PlayByPlayV2(game_id=gameId)
            pbp_df = pbp_data.get_data_frames()[0]
            halftime_pbp_df = pbp_df[pbp_df['PERIOD'] <= 2]
            player_stats_list.append(halftime_pbp_df)
            success = True  # If the request is successful, exit the loop
        except ReadTimeout:
            attempts += 1
            print(f"ReadTimeout occurred, retrying... Attempt {attempts}")
            time.sleep(2)  # Wait for 2 seconds before retrying

    if not success:
        print(f"Failed to fetch data for game ID {gameId} after {max_attempts} attempts.")

nba_teams = teams.get_teams()
all_games = []

for team in nba_teams:
   gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team['id'])
   games = gamefinder.get_data_frames()[0]
   all_games.append(games)

combined_games = pd.concat(all_games, ignore_index=True)
home_games_only = combined_games[combined_games['MATCHUP'].str.contains(' vs. ')]
home_games_only['HOME_TEAM'], home_games_only['AWAY_TEAM'] = zip(*home_games_only['MATCHUP'].apply(lambda x: x.split(' vs. ')))
home_games_ids_dates = home_games_only[['GAME_ID', 'GAME_DATE', 'HOME_TEAM', 'AWAY_TEAM']]
   
player_stats_list = []

for gameId in home_games_ids_dates['GAME_ID']:
   halftime_pbp_df = playByPlayGenerator(gameId)
   if halftime_pbp_df != None:
      player_stats_list.append(halftime_pbp_df)

all_halftime_plays = pd.concat(player_stats_list, ignore_index=True)