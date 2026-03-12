#!/usr/bin/env python3
"""
Google Calendar Auth Setup - One Time
Run this to authenticate and generate token.json
"""

import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    creds = None
    
    # Check if token.json exists
    if os.path.exists('token.json'):
        with open('token.json', 'rb') as token:
            creds = pickle.load(token)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                print("❌ ERROR: credentials.json not found!")
                print("Please download it from Google Cloud Console first.")
                return
            
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.json', 'wb') as token:
            pickle.dump(creds, token)
    
    # Test the connection
    service = build('calendar', 'v3', credentials=creds)
    print("✅ SUCCESS! Connected to Google Calendar.")
    
    # List calendars
    calendars_result = service.calendarList().list().execute()
    calendars = calendars_result.get('items', [])
    
    print("\n📅 Available Calendars:")
    for calendar in calendars:
        print(f"  - {calendar['summary']} (ID: {calendar['id']})")
    
    print("\n📝 Save the Calendar ID you want to use!")
    print("Token saved to: token.json")

if __name__ == '__main__':
    main()
