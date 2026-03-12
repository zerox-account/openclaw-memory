# Crawl4AI Skill

**Status:** ✅ Installed (v0.5.0)  
**Purpose:** Web scraping for OpenClaw  
**Added:** 2026-03-09

---

## Quick Start

```bash
# Scrape any website
python3 ~/.openclaw/workspace/skills/crawl4ai/scripts/crawl4ai-skill.py <URL> [output_dir]

# Example
python3 crawl4ai-skill.py https://zim.de ./zim-content/
```

## What It Does

- Extracts clean markdown from websites
- Removes ads, navigation, clutter
- Preserves structure and formatting
- Saves metadata (title, URL, timestamp)

## Output Format

```
./output_dir/
├── example_com.md          # Main content
└── _index.json             # Metadata
```

## Use Cases

- Research funding programs
- Extract competitor information
- Archive web content
- Prepare training data

---

*Part of OpenClaw Mission Control*
