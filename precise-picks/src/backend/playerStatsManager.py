from nba_api.stats.endpoints import leaguedashplayerstats, playercareerstats
from nba_api.stats.static import players
import pandas as pd
from nba_api.stats.endpoints import leaguegamefinder, boxscoreadvancedv2 #player stats
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playerdashboardbylastngames
from nba_api.stats.endpoints import playergamelog
import requests
from bs4 import BeautifulSoup

def get_players_by_stat_range(season, stat, first, last, per_game=False, sort_direction='asc'):
   # Fetch player stats
   player_stats = leaguedashplayerstats.LeagueDashPlayerStats(season=season)
   stats_df = player_stats.get_data_frames()[0]

   # List of stats to be divided by games played if per_game is True
   per_game_stats = ['MIN', 'PTS', 'AST', 'STL', 'BLK', 'REB', 'FGM',
                     'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA']

   # Calculate per game stats if required
   if per_game:
      for pg_stat in per_game_stats:
         if pg_stat in stats_df.columns:
               stats_df[pg_stat] = (stats_df[pg_stat] / stats_df['GP']).round(1)

   # Ensure the stat column exists in the DataFrame
   if stat not in stats_df.columns:
      raise ValueError(f"Stat '{stat}' not found in the data")

   # Determine sort order
   ascending = sort_direction == 'asc'

   # Sort by the specified stat
   sorted_df = stats_df.sort_values(by=stat, ascending=ascending)

   # Get players in the specified range
   selected_players = sorted_df.iloc[first-1:last]

   # Round all float columns to one decimal place except those with 'PCT' in the name
   for col in selected_players.select_dtypes(include=['float']).columns:
      if 'PCT' not in col:
         selected_players[col] = selected_players[col].round(1)


   # Add a 'RANK' field
   selected_players['RANK'] = range(first, first + len(selected_players))

   # Convert the DataFrame to a list of dictionaries for JSON serialization
   return selected_players.to_dict(orient='records')

def get_player_image_url(player_name, search_url):
    # Fetch the webpage content
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the image tag with the player's name in the alt attribute
    image_tag = soup.find('img', alt=player_name + ' Headshot')
    
    if image_tag:
        # Return the image URL if found
        return image_tag['src']
    else:
        # Return None or a default image URL if not found
        return None

def get_player_by_name(player_name):
    # Assuming 'players' and 'playercareerstats' are defined and imported elsewhere
    result = players.find_players_by_full_name(player_name)
    player_id = result[0]['id']
    player_stats = playercareerstats.PlayerCareerStats(player_id=player_id).get_dict()
    name_slug = player_name.lower().replace(" ", "-")
    
    # Format the URL with the player's ID and the slugified name
    search_url = f'https://www.nba.com/player/{player_id}/{name_slug}'
    
    # Add the player image URL to the stats dictionary
    player_stats['image_url'] = get_player_image_url(player_name, search_url)
    
    return player_stats

def get_stats_last_thirty_games(stat, playerName):
    result = players.find_players_by_full_name(playerName)
    if not result:
        return None
    player_id = result[0]['id']

    gamelog = playergamelog.PlayerGameLog(player_id=player_id, season='2023-24')
    last_30_games_log = gamelog.get_data_frames()[0].head(30)

    stats_dict = {row['GAME_DATE']: row[stat] for index, row in last_30_games_log.iterrows()}

    return stats_dict





