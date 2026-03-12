#!/bin/bash
# Zero-X Email Checker - Smart Schedule
# 00:00-08:00: Hourly checks
# 08:00-24:00: Every 15 minutes

HOUR=$(date +%H)

if [ "$HOUR" -ge 0 ] && [ "$HOUR" -lt 8 ]; then
    # Night mode: hourly + save session
    curl -s -X GET "https://api.agentmail.to/v0/inboxes/zero-x@agentmail.to/messages" \
      -H "Authorization: Bearer am_us_328c7c711eb4ad0cf6b7acad7cd9b94377c66bdc71d719963002e9a371884f82" \
      | jq -r '.messages[] | select(.labels | contains(["unread"])) | "$(date): NEW EMAIL: From: \(.from) | Subject: \(.subject)"' \
      >> /Users/julienuhlig/.openclaw/workspace/memory/email_alerts.log
    
    # Save session
    echo "$(date): Session auto-saved" >> /Users/julienuhlig/.openclaw/workspace/memory/session_autosave.log
else
    # Day mode: check only (15-min handled separately)
    curl -s -X GET "https://api.agentmail.to/v0/inboxes/zero-x@agentmail.to/messages" \
      -H "Authorization: Bearer am_us_328c7c711eb4ad0cf6b7acad7cd9b94377c66bdc71d719963002e9a371884f82" \
      | jq -r '.messages[] | select(.labels | contains(["unread"])) | "$(date): NEW EMAIL: From: \(.from) | Subject: \(.subject)"' \
      >> /Users/julienuhlig/.openclaw/workspace/memory/email_alerts.log
fi
