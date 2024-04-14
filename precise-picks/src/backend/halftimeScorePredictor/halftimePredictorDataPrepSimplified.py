from nba_api.live.nba.endpoints import playbyplay
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd
import numpy as np
import time
import requests
from json.decoder import JSONDecodeError
import re
from sklearn.preprocessing import OneHotEncoder
import os
import joblib
from sklearn.preprocessing import MinMaxScaler

# Specifying columns to be one-hot encoded
#fields_to_encode = ['actionType', 'subType', 'descriptor', 'area', 'timeUntilHalftime', 'personId']
fields_to_encode = ['actionType', 'area']
columns_to_scale = ['scoreHome', 'scoreAway', 'timeUntilEnd']

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
 
def save_data(pbp_df_list_padded, score_results_array, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Save each DataFrame in the list as a separate CSV file
    for index, df in enumerate(pbp_df_list_padded):
        file_path = os.path.join(output_folder, f'pbp_data_{index}.csv')
        df.to_csv(file_path, index=False)
    
    # Save score_results_array as a CSV file
    scores_file_path = os.path.join(output_folder, 'score_results.csv')
    # Convert the array to a DataFrame for easy saving
    scores_df = pd.DataFrame(score_results_array, columns=['scoreHome', 'scoreAway'])
    scores_df.to_csv(scores_file_path, index=False)
    
    print("Data saved successfully.")

def convert_clock_format(clock_str, period):
    match = re.search(r'PT(\d+)M(\d+)(?:\.(\d+))?S', clock_str)
    if match:
        minutes, seconds, milliseconds = match.groups()
        minutes = int(minutes)
        seconds = int(seconds)
        milliseconds = milliseconds or '00'
        
        # Time left in the current period in seconds.
        time_left_current_period = minutes * 60 + seconds
        
        # Calculate the total time left until the end, considering each period is 12 minutes (720 seconds).
        # Adjust the calculation based on the period.
        total_time_left = (4 - period) * 720 + time_left_current_period
        
        # Return the total time left in seconds.
        return total_time_left
    else:
        # Return a default value indicating an invalid input or match failure.
        return 0


     
def preprocessData(df, encoder):
    # Transform with the encoder within this function
    encoded = encoder.transform(df[fields_to_encode].astype(str)) # Use transform here
    new_cols = encoder.get_feature_names_out(fields_to_encode)
    encoded_df = pd.DataFrame(encoded, columns=new_cols)
    df.drop(columns=fields_to_encode, inplace=True)
    result_df = pd.concat([df, encoded_df], axis=1)
    return result_df

def pad_dataframe(df, max_length):
    num_rows_to_add = max_length - len(df)
    if num_rows_to_add > 0:
        # Specify a data type for the padding if all columns are expected to be of the same type
        # Adjust this as needed (e.g., create a padding row with the correct types for each column)
        padding_df = pd.DataFrame(0, index=np.arange(num_rows_to_add), columns=df.columns)  # Using 0 for padding
        df = pd.concat([df, padding_df], ignore_index=True)
    
    return df
 
def apply_global_min_max_scaling(df, columns, global_min, global_max):
    # Ensure global_min and global_max are dictionaries with column names as keys
    for column in columns:
        min_val = global_min[column]
        max_val = global_max[column]
        df[column] = (df[column] - min_val) / (max_val - min_val)
    return df

def convert_columns_to_numeric(df):
    for column in df.columns:
        try:
            df[column] = pd.to_numeric(df[column], errors='coerce')
        except ValueError:
            # Handle or log columns that cannot be converted to numeric
            print(f"Column {column} cannot be converted to numeric.")
    df.fillna(0, inplace=True)  # Replace NaNs introduced by 'coerce' with 0 or another placeholder as appropriate

@retry
def getFirstHalfPlayByPlays(game_id, home_team_tricode):
    try:
        pbp_data = playbyplay.PlayByPlay(game_id)
        full_actions = pbp_data.get_dict()['game']['actions']
        
        filtered_actions = [
           {
              **{key: action.get(key, 'None') if key in ['actionType', 'area'] else action.get(key, None) for key in ['actionType', 'area', 'scoreHome', 'scoreAway']},
              'timeUntilEnd': convert_clock_format(action['clock'], action['period']) if 'clock' in action and 'period' in action else "24:00:00",
              'homeTeamDidAction': action.get('teamTricode') == home_team_tricode
           }
           for action in full_actions
        ]

        
        return filtered_actions
    except JSONDecodeError as e:
        print(f"JSONDecodeError encountered for game ID {game_id}: {e}")

def get_pbp_data():
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

    pbp_data_list = []

    #for index, row in home_games_ids_dates.head(200).iterrows(): #for testing
    for index, row in home_games_ids_dates.iterrows():
        game_pbp_data = getFirstHalfPlayByPlays(row['GAME_ID'], row['HOME_TEAM'])
        if game_pbp_data:
            pbp_data_list.append(game_pbp_data)
    
    #get score results
    score_results = {}

    # Extract final score and update pbp_data_list
    for index, game_actions in enumerate(pbp_data_list):
       # Extract the final score from the last entry of each list
       final_score = game_actions[-1]
       scoreHome = final_score['scoreHome']
       scoreAway = final_score['scoreAway']
       
       # Store these scores in score_results
       score_results[index] = {'scoreHome': scoreHome, 'scoreAway': scoreAway}
       
       # Remove the last entry (final score entry) from each list
       #pbp_data_list[index] = game_actions[:-1]
    
    # Data collected, time to process
    pbp_data_df_list = [pd.DataFrame(game) for game in pbp_data_list]
 
    # Initialize and fit the encoder on the concatenated DataFrame
    flattened_pbp_df_list = pd.concat(pbp_data_df_list, ignore_index=True)
    encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
    encoder.fit(flattened_pbp_df_list[fields_to_encode].astype(str))  # Only fit here
    
    # Force to int because the type is off
    for df in pbp_data_df_list:
       for column in df.columns:
          if column not in fields_to_encode + ['homeTeamDidAction']:  # Exclude already handled columns
                df[column] = pd.to_numeric(df[column], errors='coerce')
    
    # Concatenate all DataFrames to calculate global min and max
    all_data_concatenated = pd.concat(pbp_data_df_list, ignore_index=True)
    
    # Calculate global min and max for each column
    global_min = all_data_concatenated[columns_to_scale].min()
    global_max = all_data_concatenated[columns_to_scale].max()
    
    # Apply the scaling to each DataFrame
    pbp_data_df_list = [apply_global_min_max_scaling(df, columns_to_scale, global_min, global_max) for df in pbp_data_df_list]
 
    # Process each DataFrame in the list
    preprocessed_pbp_df_list = [preprocessData(df, encoder) for df in pbp_data_df_list]
    #for future use
    joblib.dump(encoder, 'minmaxsimpleencoder.joblib')
 
    # Pad each DataFrame in the list
    #max_length = max(len(df) for df in preprocessed_pbp_df_list)
    #pbp_df_list_padded = [pad_dataframe(df, max_length) for df in preprocessed_pbp_df_list]
 
    # Apply the conversion after padding
    for df in preprocessed_pbp_df_list:
       convert_columns_to_numeric(df)  # Assuming this function iterates through the columns of df
 
    # Replace None with 0
    for df in preprocessed_pbp_df_list:
       df.fillna(0, inplace=True)
 
     
    #replace true with 1 and false with 0
    for df in preprocessed_pbp_df_list:
      df.replace({True: 1, False: 0}, inplace=True)
    
    #convert to array, stored [scoreHome, scoreAway]
    score_results_array = [[float(details['scoreHome']), float(details['scoreAway'])] for details in score_results.values()]
    
    output_folder = r'C:\Users\jdbas\Documents\code\precise-picks\excelPBPDataMinMaxSimplified'
    save_data(preprocessed_pbp_df_list, score_results_array, output_folder)

    return pbp_df_list_padded, score_results_array

if __name__ == '__main__':
    pbp_df = get_pbp_data()