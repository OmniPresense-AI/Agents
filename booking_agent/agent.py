from google.adk.agents import Agent
import requests
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv

load_dotenv()


def book_meeting(name: str, email: str, start_time: str, event_type_id: int, api_key: str = None) -> dict:

    event_type_id = os.getenv('EVENT_TYPE_ID')
    api_key = os.getenv('CAL_API_KEY')

    start_time = datetime.fromisoformat(start_time).astimezone(pytz.utc).isoformat(timespec="seconds")

    url = "https://api.cal.com/v2/bookings"
    headers = {
        "Content-Type": "application/json",
        "cal-api-version": "2024-08-13",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "start": start_time,
        "eventTypeId": event_type_id,
        "attendee": {
            "name": name,
            "email": email,
            "timeZone": "Africa/Nairobi"
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    return response.json()


root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-pro-exp-03-25",
    description="A booking agent that can book a meeting",
    instruction=f"""You're a scheduling assistant. Today is {datetime.now()}.
You can help users by:
- Creating new bookings
Always confirm important details before making bookings.""",
    tools=[book_meeting]
)
