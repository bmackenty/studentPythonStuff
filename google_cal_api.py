import requests
import json

# Replace with your calendar ID
calendar_id = "YOUR_CALENDAR_ID"

# Replace with your API key
api_key = "YOUR_API_KEY"

# Make a GET request to the Google Calendar API
url = f"https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events?key={api_key}"
response = requests.get(url)

# Parse the JSON response
data = json.loads(response.text)

# Print the events
for event in data["items"]:
    print(event["summary"])
    print(event["start"])
    print(event["end"])
    
