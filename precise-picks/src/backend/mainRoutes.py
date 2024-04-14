from flask import Flask, jsonify, request
from datetime import date
from playerStatsManager import get_players_by_stat_range, get_player_by_name, get_stats_last_thirty_games
from liveScoreboardManager import get_todays_nba_games, get_games_by_date, get_live_boxscore, get_predictions_games, generate_prediction
from bettingOddsManager import get_betting_lines
from halftimeScorePredictor.halftimePredictorLSTMModelingSimplified import LSTMModel
import torch
from sklearn.preprocessing import OneHotEncoder
import joblib
import pandas as pd

app = Flask(__name__)

model_path = r'C:\Users\jdbas\Documents\code\precise-picks\src\backend\200hid-3layer-500ranbatch-simplified2.pth'  # Path to saved model
file_path = r'C:\Users\jdbas\Documents\code\precise-picks\src\backend\minMaxData.csv'
encoder_path = r'C:\Users\jdbas\Documents\code\precise-picks\src\backend\unpaddedSecondsEncoder.joblib'
# Load the CSV file into a DataFrame
pbp_training_example = pd.read_csv(file_path)
#max_length = pbp_training_example.shape[0]
input_dim = 3  # Number of features per event
hidden_dim = 200
output_dim = 2 
num_layers = 3
loaded_model = LSTMModel(input_dim, hidden_dim, output_dim, num_layers)
loaded_model = loaded_model.to('cpu')
# Load the model weights
loaded_model.load_state_dict(torch.load(model_path))
loaded_model.eval()  # Set to evaluation mode
# Initialize encoder from past data
#encoder = joblib.load(encoder_path)

#get_predictions_games()

@app.route('/api/current-games', methods=['GET'])
def api_todays_games():
    # Format today's date as YYYY-MM-DD to match the expected format of selectedDate
    todaysDate = date.today().strftime('%Y-%m-%d')

    # Retrieve selectedDate from the request's query parameters
    selectedDate = request.args.get('date', default='', type=str)

    # Compare today's date with the selected date
    if todaysDate == selectedDate:
        games = get_todays_nba_games()
    else:
        games = get_games_by_date(selectedDate)
   
    return jsonify(games)


@app.route('/api/betting-lines', methods=['GET'])
def api_get_betting_lines():
    print("Fetching betting lines...")  # Confirm route is hit
    try:
        betting_lines_data = get_betting_lines()
        print("Data fetched:", betting_lines_data)  # Confirm data is fetched
        return jsonify(betting_lines_data)
    except Exception as e:
        print(f"Error fetching betting lines: {e}")  # Log any errors
        return jsonify({"error": "Error fetching betting lines"}), 500


@app.route('/api/players-stats', methods=['GET'])
def api_get_players_by_stat_range():
   # Extracting parameters from the request URL
   season = request.args.get('season', default='2023-24', type=str)
   stat = request.args.get('stat', default='PTS', type=str)
   first = request.args.get('first', default=1, type=int)
   last = request.args.get('last', default=10, type=int)
   sort_direction = request.args.get('sort_direction', default='desc', type=str) 
   per_game_str = request.args.get('per_game', default='false', type=str)
   
   # Convert the string to a boolean
   per_game = per_game_str.lower() in ['true', '1', 't', 'y', 'yes']

   players_stats = get_players_by_stat_range(season, stat, first, last, per_game, sort_direction)
   return jsonify(players_stats)

@app.route('/api/single-players-stats', methods=['GET'])
def api_get_players_by_name():
   # Extracting parameters from the request URL
   player = request.args.get('player', default='', type=str)

   players_stats = get_player_by_name(player)
   return jsonify(players_stats)

@app.route('/api/single-players-stats-graph', methods=['GET'])
def api_get_single_player_graph():
   # Extracting parameters from the request URL
   player = request.args.get('player', default='', type=str)
   stat = request.args.get('stat', default='', type=str)

   statsReturned = get_stats_last_thirty_games(stat, player)
   return jsonify(statsReturned)

@app.route('/api/predictions-games', methods=['GET'])
def api_get_predictions_games():
   gamesReturned = get_predictions_games()
   return jsonify(gamesReturned)

@app.route('/api/get-prediction', methods=['POST'])
def api_generate_prediction():
    request_data = request.get_json()
    homeTeam = request_data.get('homeTeam')
    gameId = request_data.get('gameId') 
    prediction = generate_prediction(gameId, homeTeam, loaded_model)

    # Return the prediction in JSON format
    return jsonify(prediction)

if __name__ == '__main__':
   app.run(debug=True, threaded=True)

