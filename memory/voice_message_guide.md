# Voice Message Handling Guide for Agents
## How to Transcribe and Process Audio Messages

---

## 📥 RECEIVING VOICE MESSAGES

### 1. Detection
Voice messages appear as media attachments with:
- Format: `.ogg` (Opus codec)
- Path: `/Users/julienuhlig/.openclaw/media/inbound/[filename].ogg`
- Marker: `<media:audio>` in conversation

### 2. What You See
```
[media attached: /path/to/file.ogg (audio/ogg; codecs=opus)]
<media:audio>
```

---

## 🛠️ TRANSCRIPTION PROCESS

### Prerequisites
- OpenAI API Key configured
- Tool: `/tools/transcribe_voice.py`

### Step-by-Step

#### Step 1: Set API Key
```bash
export OPENAI_API_KEY="your-api-key-here"
```

#### Step 2: Run Transcription
```bash
python3 /Users/julienuhlig/.openclaw/workspace/tools/transcribe_voice.py \
  /path/to/inbound/file.ogg
```

**Full Example:**
```bash
export OPENAI_API_KEY="sk-proj-..." && \
python3 /Users/julienuhlig/.openclaw/workspace/tools/transcribe_voice.py \
  /Users/julienuhlig/.openclaw/media/inbound/file_12---6ffd6f4d-04a2-4049-a220-c1b369ed914f.ogg
```

---

## 📤 OUTPUT FORMAT

### Successful Transcription
```
🔊 Transcribing: [filename].ogg
   Format: .ogg
   Model: whisper-1
   Uploading...

============================================================
📝 TRANSCRIPTION:
============================================================
[Transcribed text appears here]

============================================================
📋 Copied to clipboard
```

### Response to User
1. Show the transcribed text
2. Confirm understanding
3. Ask for next steps if unclear

---

## ⚠️ IMPORTANT NOTES

### Do:
- ✅ Transcribe immediately upon receiving
- ✅ Show full transcription to user
- ✅ Confirm you understood correctly
- ✅ Ask for clarification if audio is unclear

### Don't:
- ❌ Ignore voice messages
- ❌ Guess at unclear words
- ❌ Respond without transcribing first
- ❌ Assume intent without confirmation

---

## 📝 EXAMPLE WORKFLOW

**User sends:** `<media:audio>`

**Agent does:**
1. Execute transcription command
2. Receive: "Transcription: Please research Ukraine biomass energy"
3. Respond: "Transcription received: You want me to research Ukraine biomass energy opportunities. Is that correct?"
4. Wait for confirmation
5. Proceed with task

---

## 🔧 TECHNICAL DETAILS

| Parameter | Value |
|-----------|-------|
| Model | whisper-1 (OpenAI) |
| Supported formats | .ogg, .mp3, .m4a, .wav |
| Auto-detect language | Yes |
| Manual language | Use `-l [code]` flag |

---

## 🎯 QUICK REFERENCE

```bash
# Standard transcription
export OPENAI_API_KEY="..." && \
python3 /Users/julienuhlig/.openclaw/workspace/tools/transcribe_voice.py \
  [PATH_TO_AUDIO_FILE]

# With language specification
python3 /Users/julienuhlig/.openclaw/workspace/tools/transcribe_voice.py \
  -l de [PATH_TO_AUDIO_FILE]

# Save to file
python3 /Users/julienuhlig/.openclaw/workspace/tools/transcribe_voice.py \
  -o output.txt [PATH_TO_AUDIO_FILE]
```

---

## ✅ CHECKLIST

Before responding to voice message:
- [ ] API key exported
- [ ] Transcription executed
- [ ] Full text shown to user
- [ ] Understanding confirmed
- [ ] Next action clarified

---

**Created:** 2026-03-02
**Tool location:** `/tools/transcribe_voice.py`
