from flask import jsonify
from datetime import datetime, timezone
from dateutil import parser
from nba_api.live.nba.endpoints import scoreboard, boxscore, playbyplay
from nba_api.stats.endpoints import leaguegamefinder, boxscoresummaryv2
from nba_api.stats.static import players
from halftimeScorePredictor.halftimePredictorDataPrep import convert_clock_format, preprocessData, pad_dataframe, convert_columns_to_numeric
from halftimeScorePredictor.halftimePredictorDataPrepSimplified import apply_global_min_max_scaling
import pandas as pd
import numpy as np
import torch
import random

fields_to_encode = ['actionType', 'subType', 'descriptor', 'area',]
columns_to_scale = ['scoreHome', 'scoreAway', 'timeUntilEnd']

team_to_tricode = {
    "Hawks": "ATL",
    "Celtics": "BOS",
    "Nets": "BKN",
    "Hornets": "CHA",
    "Bulls": "CHI",
    "Cavaliers": "CLE",
    "Mavericks": "DAL",
    "Nuggets": "DEN",
    "Pistons": "DET",
    "Warriors": "GSW",
    "Rockets": "HOU",
    "Pacers": "IND",
    "Clippers": "LAC",
    "Lakers": "LAL",
    "Grizzlies": "MEM",
    "Heat": "MIA",
    "Bucks": "MIL",
    "Timberwolves": "MIN",
    "Pelicans": "NOP",
    "Knicks": "NYK",
    "Thunder": "OKC",
    "Magic": "ORL",
    "76ers": "PHI",
    "Suns": "PHX",
    "Trail Blazers": "POR",
    "Kings": "SAC",
    "Spurs": "SAS",
    "Raptors": "TOR",
    "Jazz": "UTA",
    "Wizards": "WAS",
}

def get_tricode_by_team_name(team_name):
    # Normalize the team name to match the dictionary keys
    normalized_team_name = team_name.strip()  # Remove leading/trailing whitespace
    
    # Attempt to get the tricode from the dictionary
    return team_to_tricode.get(normalized_team_name, "Unknown")


def get_todays_nba_games():
    """
    Fetches NBA games for the current day and returns a list of dictionaries 
    with each game's details including id, home team, away team, and time.
    """
    todays_games_list = []
    f = "{gameId}: {awayTeam} vs. {homeTeam} @ {gameTimeLTZ}" 

    try:
      board = scoreboard.ScoreBoard()
      print("ScoreBoardDate: " + board.score_board_date)
      games = board.games.get_dict()
      for game in games:
         gameTimeLTZ = parser.parse(game["gameTimeUTC"]).replace(tzinfo=timezone.utc).astimezone(tz=None)
         game_info = {
            "gameId": game['gameId'],
            "awayTeam": game['awayTeam']['teamName'],
            "homeTeam": game['homeTeam']['teamName'],
            "gameTimeLTZ": gameTimeLTZ,
            "gameStatusText": game['gameStatusText'],
            "gameClock": game['gameClock'],
            "currentQuarter": game['period'],
            "homeTeamScore": game['homeTeam']['score'],
            "awayTeamScore": game['awayTeam']['score']
         }
         todays_games_list.append(game_info)
         print(f.format(**game_info))
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    return todays_games_list
 
def get_live_boxscore(game_id):
    """
    Fetches the live box score for a given NBA game using its game ID.
    """
    try:
        live_boxscore_data = boxscore.BoxScore(game_id=game_id)
        # Assuming we want to print the box score stats
        return live_boxscore_data.game.get_dict()
    except Exception as e:
        print(f"An error occurred while fetching the live box score: {e}")
        
def get_games_by_date():
   return get_todays_nba_games()

def get_predictions_games(): #loaded_model, encoder, sample_max_length
    games = get_todays_nba_games()
    # Filter out games where gameStatusText is 'FINAL' to fix for future games
    games = [
      game for game in games 
      if game['gameStatusText'] != 'Final' and not game['gameStatusText'].endswith('ET')
    ]

    # Loop through each game
    for game in games:
       gameId = game['gameId']
       homeTeamTricode = get_tricode_by_team_name(game['homeTeam'])
       pbp = playbyplay.PlayByPlay(gameId)  # Fetch play-by-play data for the game
       actions = pbp.get_dict()['game']['actions']  # Get the actions/plays
       
       # Initialize empty lists to hold formatted data
       playByPlayData = []
       
       # Loop through each action/play
       for action in actions:
          player_name = ''
          # Attempt to find the player by ID and get their full name
          player = players.find_player_by_id(action.get('personId', ''))
          if player is not None:
                player_name = player['full_name']
          
          # Format the line with the available action details
          line = f"{action['actionNumber']}: {action['period']}:{action['clock']} {player_name} ({action['actionType']})"
          playByPlayData.append(line)
       
       # Append the formatted data to the game object
       game['playByPlayData'] = playByPlayData
     
    return games

def generate_prediction(gameId, homeTeamName, loaded_model):
   pbp = playbyplay.PlayByPlay(gameId)  # Fetch play-by-play data for the game
   actions = pbp.get_dict()['game']['actions']  # Get the actions/plays
   playByPlayDataEncoded = []
   homeTeamTricode = get_tricode_by_team_name(homeTeamName)
   # Loop through each action/play
   for action in actions:
      # Construct the filtered action with only scoreHome, scoreAway, and timeUntilEnd
      filtered_action = {
         'scoreHome': action.get('scoreHome', None),
         'scoreAway': action.get('scoreAway', None),
         'timeUntilEnd': convert_clock_format(action['clock'], action['period']) if 'clock' in action and 'period' in action else "24:00:00",
      }
      playByPlayDataEncoded.append(filtered_action)

   # Convert playByPlayDataEncoded to a DataFrame and preprocess
   playByPlayDF = pd.DataFrame(playByPlayDataEncoded)
   playByPlayDF = playByPlayDF.astype(int)
   #preprocessedPlayByPlay = preprocessData(playByPlayDF, encoder)
   global_min_dict = {'scoreHome': 0, 'scoreAway': 0, 'timeUntilEnd': 0}
   global_max_dict = {'scoreHome': 175, 'scoreAway': 175, 'timeUntilEnd': 2880}


   preprocessedPlayByPlay = apply_global_min_max_scaling(playByPlayDF, ['scoreHome', 'scoreAway', 'timeUntilEnd'], global_min_dict, global_max_dict)
   
   for column in preprocessedPlayByPlay.columns:
      if column not in fields_to_encode + ['homeTeamDidAction']:  # Exclude already handled columns
            preprocessedPlayByPlay[column] = pd.to_numeric(preprocessedPlayByPlay[column], errors='coerce')
   
   # Pad dataframe
   #pbp_df_padded = pad_dataframe(preprocessedPlayByPlay, sample_max_length)
   convert_columns_to_numeric(preprocessedPlayByPlay)
   preprocessedPlayByPlay.fillna(0, inplace=True)
   preprocessedPlayByPlay.replace({True: 1, False: 0}, inplace=True)
   
   sequences = preprocessedPlayByPlay.to_numpy()
   sequence_tensor = torch.tensor(sequences, dtype=torch.float32).unsqueeze(0)
   with torch.no_grad():
      prediction = loaded_model(sequence_tensor)
   
   prediction = np.array(prediction).flatten().tolist()
   
   return prediction