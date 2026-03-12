#!/usr/bin/env python3
"""
Add Event to Google Calendar - Used by Agent
"""

import pickle
import os.path
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from datetime import datetime, timedelta

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_service():
    """Authenticate and return Calendar service"""
    creds = None
    
    if os.path.exists('/Users/julienuhlig/.openclaw/workspace/zero-x/setup/token.json'):
        with open('/Users/julienuhlig/.openclaw/workspace/zero-x/setup/token.json', 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            # Save refreshed token
            with open('/Users/julienuhlig/.openclaw/workspace/zero-x/setup/token.json', 'wb') as token:
                pickle.dump(creds, token)
        else:
            raise Exception("Token not valid. Run google_calendar_auth.py first.")
    
    return build('calendar', 'v3', credentials=creds)

def add_event(summary, start_time, end_time, description="", attendees=None, timezone='Europe/Berlin'):
    """
    Add event to Google Calendar
    
    Args:
        summary: Event title
        start_time: datetime object
        end_time: datetime object  
        description: Event details
        attendees: list of email addresses
        timezone: e.g., 'Europe/Berlin' or 'Asia/Singapore'
    """
    service = get_service()
    
    # Default calendar (primary)
    calendar_id = 'primary'
    
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': timezone,
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': timezone,
        },
    }
    
    if attendees:
        event['attendees'] = [{'email': email} for email in attendees]
    
    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    
    print(f"✅ Event created: {event.get('htmlLink')}")
    return event.get('id')

if __name__ == '__main__':
    # Example usage
    start = datetime(2026, 2, 10, 9, 15, 0)
    end = datetime(2026, 2, 10, 10, 0, 0)
    
    add_event(
        summary="DBFZ Call - Karen Deprie",
        start_time=start,
        end_time=end,
        description="Horizon Europe partnership discussion\nZoom: https://eu02web.zoom-x.de/j/63842530704",
        attendees=["Karen.Deprie@dbfz.de"]
    )
