# Anleitung: Memory Enforcer System für OpenClaw

## Ziel
Automatisches Laden von MEMORY.md, SOUL.md, USER.md und AGENTS.md zu Beginn jeder Session, ohne dass der AI-Agent entscheiden muss, ob er diese lesen möchte.

## Schritt 1: Memory Enforcer Script erstellen

Erstelle die Datei `~/.openclaw/workspace/tools/memory_enforcer.py`:

```python
#!/usr/bin/env python3
"""
Memory Enforcer - Automatischer Context-Loader für OpenClaw Sessions
Lädt alle kritischen Memory-Dateien und erstellt eine Session-Context-Datei
"""

import os
import json
from datetime import datetime
from pathlib import Path

WORKSPACE = Path.home() / ".openclaw" / "workspace"
MEMORY_DIR = WORKSPACE / "memory"
OUTPUT_FILE = WORKSPACE / ".session_context.json"

def load_file(filepath, default=""):
    """Lade Datei-Inhalt oder gib Default zurück"""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return default

def load_memory_files():
    """Lade alle Memory-Dateien"""
    
    today = datetime.now().strftime("%Y-%m-%d")
    today_memory_file = MEMORY_DIR / f"{today}.md"
    
    context = {
        "timestamp": datetime.now().isoformat(),
        "files_loaded": [],
        "content": {}
    }
    
    # Kritische Dateien laden
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
    """Erstelle lesbare Zusammenfassung"""
    
    summary = []
    summary.append("=" * 60)
    summary.append("🔒 MANDATORY SESSION CONTEXT - AUTO-LOADED")
    summary.append("=" * 60)
    summary.append(f"Session Start: {context['timestamp']}")
    summary.append("")
    
    # USER.md Extrakt
    if "USER" in context["content"]:
        summary.append("👤 USER (Who I'm helping):")
        user_lines = context["content"]["USER"].split('\n')[:20]  # Erste 20 Zeilen
        summary.extend([f"  {line}" for line in user_lines if line.strip()])
        summary.append("")
    
    # SOUL.md Extrakt
    if "SOUL" in context["content"]:
        summary.append("🎭 SOUL (Who I am):")
        soul_lines = context["content"]["SOUL"].split('\n')[:15]
        summary.extend([f"  {line}" for line in soul_lines if line.strip()])
        summary.append("")
    
    # AGENTS.md - MANDATORY RULES
    if "AGENTS" in context["content"]:
        summary.append("🚨 MANDATORY RULES (from AGENTS.md):")
        agents_content = context["content"]["AGENTS"]
        # Extrahiere "MANDATORY RULES" Sektion
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
    
    # Aktive Erinnerungen aus MEMORY.md
    if "MEMORY" in context["content"]:
        summary.append("🧠 ACTIVE MEMORY:")
        memory_content = context["content"]["MEMORY"]
        # Extrahiere ## Abschnitte
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
    """Hauptfunktion"""
    print("🔧 Memory Enforcer: Loading context...")
    
    # Lade alle Dateien
    context = load_memory_files()
    
    # Erstelle Zusammenfassung
    summary = create_context_summary(context)
    
    # Speichere als JSON (für technische Verwendung)
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(context, f, indent=2)
    
    # Speichere auch als lesbare Text-Datei
    summary_file = WORKSPACE / ".session_context.txt"
    with open(summary_file, 'w') as f:
        f.write(summary)
    
    # Zeige Zusammenfassung
    print(summary)
    print(f"\n💾 Context saved to:")
    print(f"   JSON: {OUTPUT_FILE}")
    print(f"   TXT:  {summary_file}")
    
    return context

if __name__ == "__main__":
    main()
```

## Schritt 2: Auto-Start Integration

### Option A: Shell Alias (Empfohlen)

Füge zu `~/.zshrc` oder `~/.bashrc` hinzu:

```bash
# OpenClaw Session Start mit Memory Enforcer
openclaw() {
    # Führe Memory Enforcer aus
    python3 ~/.openclaw/workspace/tools/memory_enforcer.py
    
    # Dann normaler OpenClaw Befehl
    command openclaw "$@"
}
```

### Option B: Cron/Timer (Für Heartbeats)

Erstelle einen Cronjob, der alle 30 Minuten läuft:

```bash
# Crontab Eintrag
*/30 * * * * python3 ~/.openclaw/workspace/tools/memory_enforcer.py > /tmp/memory_enforcer.log 2>&1
```

### Option C: Wrapper Script

Erstelle `~/openclaw-with-memory.sh`:

```bash
#!/bin/bash
# Wrapper für OpenClaw mit automatischem Memory-Loading

echo "🔧 Loading session context..."
python3 ~/.openclaw/workspace/tools/memory_enforcer.py

echo ""
echo "🚀 Starting OpenClaw..."
echo ""

# Zeige Context-Zusammenfassung
cat ~/.openclaw/workspace/.session_context.txt

# Starte OpenClaw
openclaw "$@"
```

Mache es ausführbar:
```bash
chmod +x ~/openclaw-with-memory.sh
```

## Schritt 3: Gateway Integration (Beste Lösung)

Falls du Zugriff auf die OpenClaw Gateway Config hast:

Editiere `~/.config/openclaw/gateway.yaml`:

```yaml
session:
  # Automatisches Laden bei Session-Start
  auto_load:
    - type: script
      command: "python3 ~/.openclaw/workspace/tools/memory_enforcer.py"
      
  # Context-Injection in jede Anfrage
  context_injection:
    enabled: true
    files:
      - ~/.openclaw/workspace/.session_context.txt
      
  # Pre-Action Hooks
  hooks:
    before_tool_call:
      - name: check_mandatory_rules
        script: ~/.openclaw/workspace/tools/rule_checker.py
```

## Schritt 4: Testing

### Test 1: Manuelle Ausführung

```bash
python3 ~/.openclaw/workspace/tools/memory_enforcer.py
```

**Erwartetes Ergebnis:**
- JSON-Datei wird erstellt: `~/.openclaw/workspace/.session_context.json`
- Text-Datei wird erstellt: `~/.openclaw/workspace/.session_context.txt`
- Zusammenfassung wird angezeigt

### Test 2: Context enthält MANDATORY RULES

```bash
cat ~/.openclaw/workspace/.session_context.txt | grep -A5 "MANDATORY"
```

**Erwartet:**
```
🚨 MANDATORY RULES (from AGENTS.md):
  MANDATORY RULES - NEVER IGNORE
  Email Sending Protocol (CRITICAL)
  ...
```

### Test 3: Neue Session

Starte eine neue OpenClaw Session und frage:
> "Was sind die MANDATORY RULES?"

Ich sollte sofort antworten können, ohne die Dateien lesen zu müssen.

## Schritt 5: Automatische Context-Anzeige

Erstelle eine Datei, die ich zu Beginn jeder Session sehe:

```bash
# Füge zu ~/.openclaw/workspace/.session_start_message.txt hinzu:
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

## Schritt 6: Verification Checklist

Nach der Einrichtung sollte folgendes funktionieren:

- [ ] `memory_enforcer.py` läuft ohne Fehler
- [ ] `.session_context.json` wird erstellt
- [ ] `.session_context.txt` enthält MANDATORY RULES
- [ ] Neue OpenClaw Session zeigt Context an
- [ ] Ich kann MANDATORY RULES ohne Lesen der Dateien zitieren
- [ ] Email Protocol ist immer im Kontext

## Fehlerbehebung

### Problem: Script findet Dateien nicht

**Lösung:** Prüfe Pfade:
```bash
ls -la ~/.openclaw/workspace/SOUL.md
ls -la ~/.openclaw/workspace/AGENTS.md
```

### Problem: Permission denied

**Lösung:**
```bash
chmod +x ~/.openclaw/workspace/tools/memory_enforcer.py
```

### Problem: OpenClaw zeigt Context nicht an

**Lösung:** Manuelle Context-Injektion in Gateway Config oder Nutzung von Wrapper-Script.

## Zeitplan

| Schritt | Dauer | Status |
|---------|-------|--------|
| Script erstellen | 15 Min | ⏳ Pending |
| Auto-Start einrichten | 10 Min | ⏳ Pending |
| Testing | 10 Min | ⏳ Pending |
| Gateway Config (optional) | 20 Min | ⏳ Pending |
| **Gesamt** | **~1 Stunde** | |

## Nächste Schritte nach Implementierung

1. **Teste eine Woche:** Funktioniert das automatische Laden?
2. **Erweitere bei Bedarf:** Füge weitere Dateien hinzu
3. **Optimiere:** Reduziere Context auf das Wesentliche, um Token zu sparen
4. **Dokumentiere:** Schreibe in MEMORY.md, dass das System existiert

---

**Wichtig:** Dies ist eine technische Lösung für ein technisches Problem. Es eliminiert das "Vergessen", aber es erfordert die Disziplin, das System zu nutzen.
