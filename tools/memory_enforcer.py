#!/usr/bin/env python3
"""
Memory Enforcer - Lean Version
Loads critical memory files and creates session context
"""

from pathlib import Path
from datetime import datetime

WORKSPACE = Path.home() / ".openclaw" / "workspace"
OUTPUT_FILE = WORKSPACE / ".session_context.txt"

def load_file(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"# {filepath.name} not found"

def main():
    # Load critical files
    files = {
        "SOUL": WORKSPACE / "SOUL.md",
        "USER": WORKSPACE / "USER.md", 
        "MEMORY": WORKSPACE / "MEMORY.md",
        "AGENTS": WORKSPACE / "AGENTS.md"
    }
    
    content = {k: load_file(v) for k, v in files.items()}
    
    # Build context summary
    lines = []
    lines.append("=" * 60)
    lines.append("🔒 MANDATORY SESSION CONTEXT")
    lines.append(f"Loaded: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("=" * 60)
    lines.append("")
    
    # USER
    lines.append("👤 USER (Who I'm helping):")
    lines.append("-" * 40)
    for line in content["USER"].split('\n')[:10]:
        if line.strip() and not line.startswith('#'):
            lines.append(f"  {line}")
    lines.append("")
    
    # SOUL  
    lines.append("🎭 SOUL (Who I am):")
    lines.append("-" * 40)
    for line in content["SOUL"].split('\n')[:8]:
        if line.strip() and not line.startswith('#'):
            lines.append(f"  {line}")
    lines.append("")
    
    # MANDATORY RULES from AGENTS
    lines.append("🚨 MANDATORY RULES:")
    lines.append("-" * 40)
    agents = content["AGENTS"]
    if "MANDATORY RULES" in agents:
        start = agents.find("MANDATORY RULES")
        section = agents[start:start+1500]
        for line in section.split('\n')[:25]:
            if line.strip():
                lines.append(f"  {line}")
    lines.append("")
    
    # ACTIVE MEMORY
    lines.append("🧠 KEY MEMORY:")
    lines.append("-" * 40)
    memory = content["MEMORY"]
    for line in memory.split('\n')[:15]:
        if line.strip().startswith('##'):
            lines.append(f"  {line}")
    lines.append("")
    
    lines.append("=" * 60)
    lines.append("✅ Context loaded. Follow these rules.")
    lines.append("=" * 60)
    
    # Write to file
    result = '\n'.join(lines)
    with open(OUTPUT_FILE, 'w') as f:
        f.write(result)
    
    # Print to console
    print(result)
    print(f"\n💾 Saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
