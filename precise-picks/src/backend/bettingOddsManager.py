from datetime import datetime, date
import sys

# Assuming your PySBR setup is correctly configured
sys.path.append(r"C:\Users\jdbas\Documents\code\nba tests\client\src\flask-server\PySBR")

from pysbr import *

def get_betting_lines():
    try:
        today_str = date.today().strftime('%Y-%m-%d')
        dt = datetime.strptime(today_str, '%Y-%m-%d')

        nba = NBA()
        sb = Sportsbook()

        # Fetching events by date
        e = EventsByDate(nba.league_id, dt)
        # Fetching current lines for the fetched events
        cl = CurrentLines(e.ids(), nba.market_ids(['moneyline']), sb.ids(['Bovada']))
        # Listing events data
        events_data = cl.list(e)

        formatted_output = []

        # Ensure each event has the expected fields
        for event in events_data:
            if 'entrid' in event and 'american odds' in event:
                formatted_output.append({
                    'entrid': event['entrid'],
                    'american odds': event['american odds'],
                    'participant': event.get('participant', 'Unknown'),  # Use .get for optional fields
                    'participant full name': event.get('participant full name', 'Unknown')
                })
        
        # Uncomment the below line for debugging with hardcoded data
        # return [{'entrid': 12345, 'american odds': -150, 'participant': 'Test Team A', 'participant full name': 'Test Team Alpha'}]
        
        return formatted_output
    except Exception as e:
        print(f"Error fetching betting lines: {e}")
        return []  # Return an empty list in case of error
