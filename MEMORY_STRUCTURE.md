# Zero-X Memory Structure
**Based on:** Marcus (EX AI) implementation
**Repository:** github.com/exaipro/openclaw-memory (reference structure)

---

## What's Backed Up to GitHub

| File/Directory | Purpose | Backup Frequency |
|----------------|---------|------------------|
| `MEMORY.md` | Long-term curated memory | Every 15 min |
| `memory/YYYY-MM-DD.md` | Daily logs | Every 15 min |
| `SOUL.md` | Identity, values, personality | Every 15 min |
| `USER.md` | Julien's context, priorities | Every 15 min |
| `AGENTS.md` | Full agent roster | Every 15 min |
| `TOOLS.md` | Available tools, APIs | Every 15 min |
| `HEARTBEAT.md` | Periodic task checklist | Every 15 min |

---

## What's NOT Backed Up (Local Only)

| File/Directory | Purpose | Location |
|----------------|---------|----------|
| `intellibot_memory.db` | CRM database (lead tracking, outreach history, graph relationships) | `~/.openclaw/memory-data/` |
| Session transcripts | Full conversation logs | `~/.openclaw/agents/main/sessions/` |
| Runtime state | Temporary processing data | `~/.openclaw/runtime/` |

---

## Directory Structure

```
~/.openclaw/
├── workspace/                    # ✅ Backed up to GitHub
│   ├── MEMORY.md
│   ├── SOUL.md
│   ├── USER.md
│   ├── AGENTS.md
│   ├── TOOLS.md
│   ├── HEARTBEAT.md
│   ├── memory/
│   │   └── YYYY-MM-DD.md
│   └── ... (other workspace files)
│
├── memory-data/                  # ❌ NOT backed up (local only)
│   └── intellibot_memory.db      # CRM database
│
└── agents/main/sessions/         # ❌ NOT backed up (local only)
    └── *.jsonl                   # Session transcripts
```

---

## CRM Database (Local Only)

The `intellibot_memory.db` contains:
- Lead tracking
- Outreach history
- Graph relationships between contacts
- Opportunity pipeline data

**This database is NOT version-controlled** and remains local to the machine.

---

_Last updated: 2026-03-12 — Aligned with Marcus (EX AI) structure_
