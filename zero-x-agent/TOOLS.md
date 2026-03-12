# TOOLS.md - Zero-X Agent Tools & Commands

## Command Triggers

| Command | Action |
|---------|--------|
| `/validate` | Run ZeroBounce email validation |
| `/send` | Send prepared emails (after explicit approval) |
| `/research` | Search for university contacts |
| `/dashboard` | Update Mission Control dashboard |
| `/status` | Show current task status |

## Current Connections

| Service | Status | Use Case |
|---------|--------|----------|
| Email (Himalaya) | ✅ Active | Send/receive emails |
| ZeroBounce API | ✅ Active | Email validation |
| Web Search | ✅ Active | Research contacts |
| Browser | ✅ Active | Navigate websites |
| Local HTTP Server | ✅ Active | Serve dashboard |

## Quick Commands

### Email Validation
```bash
export ZEROBOUNCE_API_KEY="0b04da592b884ce6aaf94181d50f2d4d"
python3 ~/.openclaw/workspace/tools/validate_and_send.py 'email@example.com' 'Subject' /path/to/body.txt
```

### Check Email Log
```bash
cat ~/.openclaw/workspace/memory/email_sent_log.json
```

### Start Dashboard Server
```bash
cd ~/.openclaw/workspace && python3 -m http.server 8080
```

### Validate Single Email
```bash
python3 ~/.openclaw/workspace/tools/zerobounce_check.py "email@example.com"
```

## Security Protocols

### Email Sending (CRITICAL)
1. Read AGENTS.md first
2. Check memory for context
3. Create email file
4. Show user full content
5. WAIT for explicit "SEND"
6. Validate with ZeroBounce
7. Send and log

### External Actions
- Ask before: emails, posts, public messages
- Proceed freely: reading, organizing, learning
- When in doubt: ask

## File Locations

| File | Path |
|------|------|
| Dashboard | ~/.openclaw/workspace/dashboard/zero-x-dashboard/ |
| Email Templates | ~/.openclaw/workspace/outreach/emails/ |
| Tools | ~/.openclaw/workspace/tools/ |
| Memory | ~/.openclaw/workspace/memory/ |
| Sent Log | ~/.openclaw/workspace/memory/email_sent_log.json |

## Key URLs

- Dashboard: http://localhost:8080/dashboard/zero-x-dashboard/
- Mission Control: http://localhost:8080/dashboard/zero-x-dashboard/index.html
