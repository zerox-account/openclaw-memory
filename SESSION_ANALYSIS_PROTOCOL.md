# Session Analysis Protocol

## Purpose
Read all session transcripts to understand complete conversation history with this user.

## Location
~/.openclaw/agents/main/sessions/*.jsonl

## Steps

### 1. List All Sessions
- Find all .jsonl files (excluding .deleted. files)
- Sort by modification time (newest first)
- Count total sessions

### 2. Read Current Session (789fc150)
- This is today's active session
- Contains all conversation from March 11, 2026

### 3. Read Recent Sessions (Last 7 Days)
- March 10, 2026
- March 9, 2026
- March 8, 2026
- March 4, 2026
- February 27, 2026
- February 26, 2026
- February 25, 2026

### 4. Extract Key Information
For each session, identify:
- Date and time
- User requests
- Agent actions taken
- Failures/mistakes
- Corrections made by user
- Systems/tools built
- Email campaigns sent

### 5. Build User Profile
- Communication style preferences
- Common corrections (what I get wrong)
- Active projects and priorities
- Successful patterns to replicate
- Failed patterns to avoid

### 6. Summarize Findings
Create comprehensive summary of:
- Total conversations
- Key learnings
- Recurring issues
- User expectations
- Action items
