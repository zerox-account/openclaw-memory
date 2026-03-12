#!/bin/bash
# Zero-X Email Checker - Runs every 15 minutes
# Checks AgentMail inbox for unread emails from master agent

curl -s -X GET "https://api.agentmail.to/v0/inboxes/zero-x@agentmail.to/messages" \
  -H "Authorization: Bearer am_us_328c7c711eb4ad0cf6b7acad7cd9b94377c66bdc71d719963002e9a371884f82" \
  | jq -r '.messages[] | select(.labels | contains(["unread"])) | "NEW EMAIL: From: \(.from) | Subject: \(.subject) | ID: \(.message_id)"' \
  >> /Users/julienuhlig/.openclaw/workspace/memory/email_alerts.log
