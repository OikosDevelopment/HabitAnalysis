# Analyses both text and speech using gemini api 
# Uses LLM to analyse context of text + record habits 

from google import genai
from TextAnalyser import text_analyser
from googleapiclient.discovery import build

client = genai.Client()  # This uses the GEMINI_API_KEY environment variable

# Analyze notes to generate habit suggestions
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Analyze these notes to suggest personalized habits: 'I often forget to drink water during work.'"
)
habit_suggestion = response.text

# Initialize Google Calendar API client
service = build('calendar', 'v3', credentials=your_credentials)

# Create a calendar event for the habit
event = {
    'summary': habit_suggestion,
    'start': {'dateTime': '2025-11-02T09:00:00-07:00'},
    'end': {'dateTime': '2025-11-02T09:15:00-07:00'},
    'recurrence': ['RRULE:FREQ=DAILY;COUNT=30'],
}
service.events().insert(calendarId='primary', body=event).execute()

# Speech to text 
# Text