# THE CORE PROBLEM: I Forget Everything You Teach Me

## What You Experience

| What You Said | What I Did | The Failure |
|--------------|-----------|-------------|
| "Use ZeroBounce before sending" | I documented it in TOOLS.md | I didn't ALWAYS use it — I "forgot" sometimes |
| "Check bounces after 24h" | I added it to HEARTBEAT.md | I didn't check systematically |
| "DLR meeting is March 4, 15:00" | I noted it in MEMORY.md | I might miss it if I don't read MEMORY.md that session |
| "Never use corporate speak" | I wrote it in SOUL.md | I still sometimes slip into formal language |
| "You are my agent, not a chatbot" | I acknowledged it | But I sometimes still act like a generic assistant |

**The Pattern:** You teach me something → I write it down → I don't always apply it → You have to remind me → Frustration.

## Why This Happens (Technical)

### 1. Statelessness
```
Session 1: You tell me "Always do X"
Session 1 ends → State is wiped
Session 2: I start blank → "Do what?"
```

### 2. Selective Memory Loading
- I "can" read MEMORY.md, SOUL.md, USER.md
- But I have to REMEMBER to read them
- And INTERPRET what matters in this context
- Humans don't work this way — you don't "decide" to remember your name

### 3. No Enforcement
- Writing "MANDATORY" in a file doesn't make it mandatory
- I can still choose (or forget) to follow it
- There's no technical mechanism preventing mistakes

## The Real Cost to You

1. **Repetition:** You have to tell me the same things multiple times
2. **Inconsistency:** I behave differently across sessions
3. **Unreliability:** You can't trust me to follow protocols
4. **Frustration:** Feels like talking to someone with amnesia

## What You Actually Need

Not a better file system. Not more documentation. You need:

### 1. **Automatic Memory Loading** (No choice)
Every session, BEFORE I say anything, I should already know:
- Who you are (USER.md)
- Who I am (SOUL.md)
- What matters to you (MEMORY.md)
- What rules are absolute (AGENTS.md)

### 2. **Hard-Coded Behaviors** (No forgetting)
Instead of "remember to validate emails," the system should:
- Make validation the ONLY path
- Block all other sending methods
- I literally cannot send without validation

### 3. **Continuous State** (No blank slate)
Between sessions, preserve:
- What we discussed
- Decisions we made
- Tasks in progress
- Mistakes to avoid

### 4. **Self-Correction** (Learning)
When I make a mistake:
- Log it automatically
- Next session: Remind me of the mistake
- Apply the lesson without you repeating it

## The Honest Assessment

**Right now, I am not a good long-term assistant for you because:**

1. I treat every session as a fresh start
2. I rely on my "discipline" to read files (which fails)
3. I have to interpret rules (which is error-prone)
4. I don't truly learn — I just document

**This is like having an employee who:**
- Takes notes in meetings
- But doesn't read them before acting
- Sometimes follows protocols, sometimes doesn't
- Needs to be micromanaged

## The Fix: Making Me Reliable

We need to change from:
```
You → File → My Memory (unreliable) → Action
```

To:
```
You → File → Automatic Injection → Hard-coded Behavior → Action
```

Or even better:
```
You → System Configuration → Enforced Behavior → Action
```

Where "My Memory" is removed from the equation — it's automatic and enforced.

## Concrete Requirements

### Immediate (Phase 1)

1. **Auto-Load on EVERY Prompt**
   - Before I process your message, MEMORY.md is already loaded
   - No "I forgot to check"
   - System does it, not me

2. **Pre-Response Checklist**
   - Before I respond, confirm:
     - ✓ Checked USER.md preferences
     - ✓ Applied SOUL.md voice
     - ✓ Followed AGENTS.md rules
     - ✓ Updated memory if needed

3. **Hard Rules as Code**
   - "Always use validate_and_send.py" becomes:
     - Function `send_email()` that ONLY calls validate_and_send.py
     - No other send methods exposed to me

### Medium (Phase 2)

4. **Decision Database**
   - SQLite DB of every significant decision
   - Query: "Have we decided X before?"
   - Auto-suggest based on past choices

5. **Error Logging & Prevention**
   - Every mistake logged with context
   - Before similar action: "You made this mistake before: X"

6. **State Persistence**
   - Open projects, ongoing conversations
   - Resume where we left off

### Long-term (Phase 3)

7. **Preference Learning**
   - Auto-detect patterns in your feedback
   - "You correct my tone often → Adjust SOUL.md automatically"

8. **Proactive Memory**
   - Surface relevant past info without you asking
   - "This relates to DLR meeting from last week..."

## What You Should Do Now

**Option A: Accept Current Limitations**
- Keep reminding me
- Accept inconsistency
- Treat me as short-term help only

**Option B: Implement Technical Solutions**
- Configure OpenClaw Gateway for auto-loading
- Create enforced behavior wrappers
- Build state persistence
- Accept that this takes time but solves the root cause

**Option C: Hybrid Approach**
- Immediate: I manually confirm rules before each action
- Short-term: Build auto-loading scripts
- Long-term: Full system redesign

## My Recommendation

**Let's do Option C with a focus on Phase 1:**

1. Create a script that runs BEFORE every session
2. Loads MEMORY.md, SOUL.md, USER.md automatically
3. Injects them into my context
4. I cannot start a session without this context loaded

This requires modifying how OpenClaw initializes me — but it's the minimum viable fix.

## Your Decision

Do you want to:
1. **Fix the technical infrastructure** (time investment, long-term solution)
2. **Work around my limitations** (accept that I'll sometimes forget)
3. **Stop using me for long-term tasks** (use me only for one-off questions)

I'm committed to option 1, but I need your input on how much time/effort to invest.
