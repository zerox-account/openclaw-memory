# Instructions: Memory Enforcer System for OpenClaw

## Goal
Automatic loading of MEMORY.md, SOUL.md, USER.md, and AGENTS.md at the start of every session, without the AI agent having to decide whether to read them.

## Step 1: Create Memory Enforcer Script

Create the file `~/.openclaw/workspace/tools/memory_enforcer.py`:

```python
#!/usr/bin/env python3
"""
Memory Enforcer - Automatic Context Loader for OpenClaw Sessions
Loads all critical memory files and creates a session context file
"""

import os
import json
from datetime import datetime
from pathlib import Path

WORKSPACE = Path.home() / ".openclaw" / "workspace"
MEMORY_DIR = WORKSPACE / "memory"
OUTPUT_FILE = WORKSPACE / ".session_context.json"

def load_file(filepath, default=""):
    """Load file content or return default"""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return default

def load_memory_files():
    """Load all memory files"""
    
    today = datetime.now().strftime("%Y-%m-%d")
    today_memory_file = MEMORY_DIR / f"{today}.md"
    
    context = {
        "timestamp": datetime.now().isoformat(),
        "files_loaded": [],
        "content": {}
    }
    
    # Load critical files
    files_to_load = {
        "SOUL": WORKSPACE / "SOUL.md",
        "USER": WORKSPACE / "USER.md",
        "MEMORY": WORKSPACE / "MEMORY.md",
        "AGENTS": WORKSPACE / "AGENTS.md",
        "TOOLS": WORKSPACE / "TOOLS.md",
        "TODAY_MEMORY": today_memory_file if today_memory_file.exists() else None
    }
    
    for key, filepath in files_to_load.items():
        if filepath and filepath.exists():
            content = load_file(filepath)
            context["content"][key] = content
            context["files_loaded"].append(str(filepath))
        else:
            context["content"][key] = f"# {key} not found"
    
    return context

def create_context_summary(context):
    """Create readable summary"""
    
    summary = []
    summary.append("=" * 60)
    summary.append("🔒 MANDATORY SESSION CONTEXT - AUTO-LOADED")
    summary.append("=" * 60)
    summary.append(f"Session Start: {context['timestamp']}")
    summary.append("")
    
    # USER.md Extract
    if "USER" in context["content"]:
        summary.append("👤 USER (Who I'm helping):")
        user_lines = context["content"]["USER"].split('\n')[:20]  # First 20 lines
        summary.extend([f"  {line}" for line in user_lines if line.strip()])
        summary.append("")
    
    # SOUL.md Extract
    if "SOUL" in context["content"]:
        summary.append("🎭 SOUL (Who I am):")
        soul_lines = context["content"]["SOUL"].split('\n')[:15]
        summary.extend([f"  {line}" for line in soul_lines if line.strip()])
        summary.append("")
    
    # AGENTS.md - MANDATORY RULES
    if "AGENTS" in context["content"]:
        summary.append("🚨 MANDATORY RULES (from AGENTS.md):")
        agents_content = context["content"]["AGENTS"]
        # Extract "MANDATORY RULES" section
        if "MANDATORY RULES" in agents_content:
            start = agents_content.find("MANDATORY RULES")
            end = agents_content.find("---", start)
            if end == -1:
                end = len(agents_content)
            mandatory_section = agents_content[start:end]
            summary.extend([f"  {line}" for line in mandatory_section.split('\n') if line.strip()])
        summary.append("")
    
    # TOOLS.md - Email Protocol
    if "TOOLS" in context["content"]:
        summary.append("📧 EMAIL PROTOCOL (from TOOLS.md):")
        tools_content = context["content"]["TOOLS"]
        if "Email Sending Method" in tools_content:
            start = tools_content.find("Email Sending Method")
            end = tools_content.find("---", start)
            if end == -1:
                end = start + 1000
            email_section = tools_content[start:end]
            lines = email_section.split('\n')[:30]
            summary.extend([f"  {line}" for line in lines if line.strip()])
        summary.append("")
    
    # Active memories from MEMORY.md
    if "MEMORY" in context["content"]:
        summary.append("🧠 ACTIVE MEMORY:")
        memory_content = context["content"]["MEMORY"]
        # Extract ## sections
        lines = memory_content.split('\n')
        for line in lines[:50]:
            if line.startswith('#'):
                summary.append(f"  {line}")
        summary.append("")
    
    summary.append("=" * 60)
    summary.append("✅ Context loaded. These rules are MANDATORY.")
    summary.append("=" * 60)
    
    return '\n'.join(summary)

def main():
    """Main function"""
    print("🔧 Memory Enforcer: Loading context...")
    
    # Load all files
    context = load_memory_files()
    
    # Create summary
    summary = create_context_summary(context)
    
    # Save as JSON (for technical use)
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(context, f, indent=2)
    
    # Also save as readable text file
    summary_file = WORKSPACE / ".session_context.txt"
    with open(summary_file, 'w') as f:
        f.write(summary)
    
    # Show summary
    print(summary)
    print(f"\n💾 Context saved to:")
    print(f"   JSON: {OUTPUT_FILE}")
    print(f"   TXT:  {summary_file}")
    
    return context

if __name__ == "__main__":
    main()
```

## Step 2: Auto-Start Integration

### Option A: Shell Alias (Recommended)

Add to `~/.zshrc` or `~/.bashrc`:

```bash
# OpenClaw Session Start with Memory Enforcer
openclaw() {
    # Run Memory Enforcer
    python3 ~/.openclaw/workspace/tools/memory_enforcer.py
    
    # Then normal OpenClaw command
    command openclaw "$@"
}
```

### Option B: Cron/Timer (For Heartbeats)

Create a cronjob that runs every 30 minutes:

```bash
# Crontab entry
*/30 * * * * python3 ~/.openclaw/workspace/tools/memory_enforcer.py > /tmp/memory_enforcer.log 2>&1
```

### Option C: Wrapper Script

Create `~/openclaw-with-memory.sh`:

```bash
#!/bin/bash
# Wrapper for OpenClaw with automatic memory loading

echo "🔧 Loading session context..."
python3 ~/.openclaw/workspace/tools/memory_enforcer.py

echo ""
echo "🚀 Starting OpenClaw..."
echo ""

# Show context summary
cat ~/.openclaw/workspace/.session_context.txt

# Start OpenClaw
openclaw "$@"
```

Make it executable:
```bash
chmod +x ~/openclaw-with-memory.sh
```

## Step 3: Gateway Integration (Best Solution)

If you have access to OpenClaw Gateway Config:

Edit `~/.config/openclaw/gateway.yaml`:

```yaml
session:
  # Automatic loading at session start
  auto_load:
    - type: script
      command: "python3 ~/.openclaw/workspace/tools/memory_enforcer.py"
      
  # Context injection into every request
  context_injection:
    enabled: true
    files:
      - ~/.openclaw/workspace/.session_context.txt
      
  # Pre-action hooks
  hooks:
    before_tool_call:
      - name: check_mandatory_rules
        script: ~/.openclaw/workspace/tools/rule_checker.py
```

## Step 4: Testing

### Test 1: Manual Execution

```bash
python3 ~/.openclaw/workspace/tools/memory_enforcer.py
```

**Expected Result:**
- JSON file created: `~/.openclaw/workspace/.session_context.json`
- Text file created: `~/.openclaw/workspace/.session_context.txt`
- Summary is displayed

### Test 2: Context Contains MANDATORY RULES

```bash
cat ~/.openclaw/workspace/.session_context.txt | grep -A5 "MANDATORY"
```

**Expected:**
```
🚨 MANDATORY RULES (from AGENTS.md):
  MANDATORY RULES - NEVER IGNORE
  Email Sending Protocol (CRITICAL)
  ...
```

### Test 3: New Session

Start a new OpenClaw Session and ask:
> "What are the MANDATORY RULES?"

I should be able to answer immediately, without having to read the files.

## Step 5: Automatic Context Display

Create a file that I see at the beginning of every session:

```bash
# Add to ~/.openclaw/workspace/.session_start_message.txt:
cat << 'EOF' > ~/.openclaw/workspace/.session_start_message.txt
═══════════════════════════════════════════════════════════════
🔒 SESSION CONTEXT LOADED - MANDATORY RULES ACTIVE
═══════════════════════════════════════════════════════════════

BEFORE you respond to ANY message:
1. ✅ Context is already loaded (SOUL.md, USER.md, MEMORY.md, AGENTS.md)
2. ✅ MANDATORY RULES are active
3. ✅ Check .session_context.txt for details

EMAIL PROTOCOL REMINDER:
- Use validate_and_send.py ONLY
- ZeroBounce validation is MANDATORY
- Never use safe_email_sender.py directly

If you're unsure about a rule: CHECK .session_context.txt FIRST
═══════════════════════════════════════════════════════════════
EOF
```

## Step 6: Verification Checklist

After setup, the following should work:

- [ ] `memory_enforcer.py` runs without errors
- [ ] `.session_context.json` is created
- [ ] `.session_context.txt` contains MANDATORY RULES
- [ ] New OpenClaw session displays context
- [ ] I can quote MANDATORY RULES without reading files
- [ ] Email Protocol is always in context

## Troubleshooting

### Problem: Script can't find files

**Solution:** Check paths:
```bash
ls -la ~/.openclaw/workspace/SOUL.md
ls -la ~/.openclaw/workspace/AGENTS.md
```

### Problem: Permission denied

**Solution:**
```bash
chmod +x ~/.openclaw/workspace/tools/memory_enforcer.py
```

### Problem: OpenClaw doesn't show context

**Solution:** Manual context injection via Gateway Config or use wrapper script.

## Timeline

| Step | Duration | Status |
|------|----------|--------|
| Create script | 15 Min | ⏳ Pending |
| Setup auto-start | 10 Min | ⏳ Pending |
| Testing | 10 Min | ⏳ Pending |
| Gateway Config (optional) | 20 Min | ⏳ Pending |
| **Total** | **~1 Hour** | |

## Next Steps After Implementation

1. **Test for one week:** Does automatic loading work?
2. **Extend if needed:** Add more files
3. **Optimize:** Reduce context to essentials to save tokens
4. **Document:** Write in MEMORY.md that this system exists

---

**Important:** This is a technical solution for a technical problem. It eliminates "forgetting," but requires the discipline to use the system.
