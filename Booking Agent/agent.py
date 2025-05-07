from google.adk.agents import Agent
import requests
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv

load_dotenv()

class BookingAgent:
    def __init__(self):
        self.event_type_id = int(os.getenv('EVENT_TYPE_ID'))
        self.api_key = os.getenv('CAL_API_KEY')

    def _convert_time_to_utc(self, time: str) -> str:
        return datetime.fromisoformat(time).astimezone(pytz.utc).isoformat(timespec="seconds")

    def book_meeting(self, name: str, email: str, start_time: str) -> dict:

        start_time = self._convert_time_to_utc(start_time)

        url = "https://api.cal.com/v2/bookings"
        headers = {
            "Content-Type": "application/json",
            "cal-api-version": "2024-08-13",
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "start": start_time,
            "eventTypeId": self.event_type_id,
            "attendee": {
                "name": name,
                "email": email,
                "timeZone": "Africa/Nairobi"
            }
        }

        response = requests.post(url, headers=headers, json=payload)

        return response.json()

    def find_available_slots(self, start_time: str, end_time: str) -> dict:

        url = "https://api.cal.com/v2/slots"
        headers = {
            "cal-api-version": "2024-09-04",
            "Authorization": f"Bearer {self.api_key}"
        }

        start_time = self._convert_time_to_utc(start_time)
        end_time = self._convert_time_to_utc(end_time)

        payload = {
            "eventTypeId": self.event_type_id,
            "start": start_time,
            "end": end_time
        }

        response = requests.get(url, headers=headers, params=payload)
        return response.json()

booking_agent = BookingAgent()


root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash-preview-04-17",
    description="A booking agent that can book a meeting",
    instruction=f"""You're a scheduling assistant. Today is {datetime.now()}.
You can help users by:
- Creating new bookings
- Showing available slots
Always confirm important details before making bookings.""",
    tools=[booking_agent.book_meeting, booking_agent.find_available_slots],
)
