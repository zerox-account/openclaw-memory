# Available Tools
**Protocol:** MASTER AGENT PROTOCOL v5.0 | Section 3

---

## Core Tools

### File Operations
| Tool | Purpose |
|------|---------|
| `read` | Read file contents |
| `write` | Create/overwrite files |
| `edit` | Precise text replacement |

### System & Shell
| Tool | Purpose |
|------|---------|
| `exec` | Run shell commands |
| `process` | Manage background processes |

### Web & Browser
| Tool | Purpose | Status |
|------|---------|--------|
| `web_search` | Brave Search | ⚠️ Needs BRAVE_API_KEY |
| `web_fetch` | Extract content from URLs | ✅ Available |
| `browser` | Browser automation | ✅ Available |

### Communication
| Tool | Purpose |
|------|---------|
| `message` | Send messages (Telegram, etc.) |
| `sessions_send` | Send to other sessions |
| `sessions_spawn` | Spawn sub-agents |
| `tts` | Text-to-speech |

### Memory & Status
| Tool | Purpose | Status |
|------|---------|--------|
| `memory_search` | Search MEMORY.md | ⚠️ Currently disabled |
| `memory_get` | Read specific memory snippets | ✅ Available |
| `session_status` | Show session status card | ✅ Available |
| `sessions_list` | List active sessions | ✅ Available |

### Scheduling
| Tool | Purpose |
|------|---------|
| `cron` | Manage cron jobs |

### Skills
| Skill | Purpose | Location |
|-------|---------|----------|
| `outreach-campaign` | Client-centric email campaigns | `~/.openclaw/skills/outreach-campaign/` |
| `skill-creator` | Create/edit agent skills | `/opt/homebrew/lib/node_modules/openclaw/skills/skill-creator/` |
| `github` | GitHub operations | `/opt/homebrew/lib/node_modules/openclaw/skills/github/` |

### Gateway
| Tool | Purpose |
|------|---------|
| `gateway` | Config management, restart |

---

## API Endpoints & Credentials

### Email — AgentMail
```bash
Endpoint: https://api.agentmail.to/v0/
Key: $AGENTMAIL_KEY (see credentials)
Inbox: zero-x@agentmail.to
```

### Research — Perplexity
```bash
Endpoint: https://api.perplexity.ai/chat/completions
Model: sonar-pro
Key: $PERPLEXITY_API_KEY
```

### Validation — ZeroBounce
```bash
Endpoint: https://api.zerobounce.net/v2/validate
Key: $ZEROBOUNCE_KEY
```

### AI — OpenAI GPT-4o
```bash
Endpoint: https://api.openai.com/v1/chat/completions
Key: $OPENAI_API_KEY
```

### Supabase — X-150 Sales Hub
```bash
Endpoint: See credentials file
Tables: contacts, outreach, opportunities
```

---

## Credential Files

Load credentials before any API call:
```bash
source ~/.openclaw/credentials/agentmail.env
source ~/.openclaw/credentials/openai.env
source ~/.openclaw/credentials/perplexity.env
source ~/.openclaw/credentials/zerobounce.env
```

---

## Current Connections

| Service | Status | Notes |
|---------|--------|-------|
| Telegram | ✅ Active | Bot connected |
| Gmail | ✅ Via himalaya | Email sending/receiving |
| GitHub | ✅ Token set | gh CLI available |
| Web Search | ⚠️ Needs API key | BRAVE_API_KEY not set |
| Browser | ✅ Available | Chrome/Playwright |

---

## Quick Commands

### Email (via himalaya)
```bash
# Check inbox
himalaya envelope list

# Read message
himalaya message read <ID>
```

### GitHub
```bash
# Check PRs
gh pr list

# View issues
gh issue list
```

### Status
```bash
# OpenClaw status
openclaw status

# Gateway status
openclaw gateway status
```

### Memory Scripts
```bash
# Manual save
bash ~/.openclaw/scripts/save_memory.sh

# GitHub backup
bash ~/.openclaw/scripts/github_backup.sh

# Check emails
bash ~/.openclaw/scripts/check_emails.sh
```

---

## Security Protocols

- **Email:** ALWAYS use validate_and_send.py
- **External:** Ask before posting/sending
- **Files:** Prefer trash > rm
- **Secrets:** Never log or expose tokens
- **Credentials:** Path only, NEVER log contents

---

## Workspace Shortcuts

| Path | Purpose |
|------|---------|
| `~/.openclaw/workspace/` | Main workspace |
| `~/.openclaw/workspace/memory/` | Daily logs |
| `~/.openclaw/workspace/tools/` | Custom scripts |
| `~/.openclaw/scripts/` | Automation scripts |
| `~/.openclaw/credentials/` | API keys (NEVER log) |

---

## Dashboards & Endpoints

| Service | URL / Path |
|---------|------------|
| OpenClaw | http://127.0.0.1:18789/?token=julien-openclaw-2026 |
| Mission Control | http://localhost:4000 |

---

_Last updated: 2026-03-12 — Migrated to MASTER AGENT PROTOCOL v5.0_
