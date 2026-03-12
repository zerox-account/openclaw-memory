# MEMORY.md - Long-Term Curated Memory

**Security Rule:** ONLY load in main session (direct 1:1 chats). NEVER load in group chats or shared contexts.

---

## Email Outreach Lessons

### What Doesn't Work
1. **Generic institutional addresses** (info@, secretariat@, decanato@)
   - High bounce rates at Spanish universities (ULPGC, CIEMAT)
   - These addresses often don't reach decision-makers
   
2. **External domains to .edu/.gov/.admin.ch**
   - TU Delft blocks external senders (Exchange Online: 550 5.4.1)
   - Government domains have aggressive spam filters
   
3. **Assuming "sent" = "delivered"**
   - Bounces arrive hours or days later
   - Must check inbox for Delivery Status Notifications

### What Works
1. **Direct researcher emails** (firstname.lastname@institution)
   - DLR Stuttgart: Both emails delivered, response received
   - ETH Zurich: Generally reliable
   
2. **German academic institutions**
   - Lower bounce rates than Spanish/UK institutions
   - More responsive to collaboration inquiries

### Follow-Up Protocol
- Wait 3-5 business days for initial response
- Check for bounces within 24 hours of sending
- If no bounce but no response → try LinkedIn
- If bounce → search for alternative contact method

---

## Active Opportunities

### DLR Stuttgart (High Priority)
- Contact: Dr. Rémi Costa, Prof. Andreas Friedrich
- Meeting: March 4, 2026, 15:00 CET
- Topic: Electrochemical energy & syngas integration
- Status: Time confirmed, awaiting final confirmation

---

## Tools & Workflows

### Safe Email Sender
- Always use `/Users/julienuhlig/.openclaw/workspace/tools/validate_and_send.py`
- Prevents duplicates (7-day block)
- Validates via ZeroBounce
- Logs all sends to `memory/email_sent_log.json`

### Bounce Detection (Manual)
```bash
# Check for recent bounces
himalaya envelope list --page 1 --page-size 50 | grep -E "(Delivery Status|Undeliverable)"
```

### Email Log Location
`/Users/julienuhlig/.openclaw/workspace/memory/email_sent_log.json`

---

## User Preferences & Context

### Communication Style
- Direct, no bullshit
- Hates: "Great question!" filler, performative helpfulness
- Values: Competence, resourcefulness, accuracy
- Warning given: "if this does not get better I will terminate you" (2026-03-09)

### Active Projects
- Zero-X Labs GmbH - Biomass CHP systems (X-150)
- EX Venture - Research partnerships
- Email outreach to universities/research institutes

### Critical Rules (Non-Negotiable)
1. NEVER send emails without explicit "SEND" command
2. NEVER invent information (titles, positions, numbers)
3. ALWAYS validate sources before stating facts
4. Write daily logs - no exceptions

---

## System Evolution

### 2026-03-09: Marcus Memory Infrastructure Upgrade
- Replaced old MEMORY.md structure with Marcus format
- Established IDENTITY.md
- Created daily logging protocol
- Fixed 12-day gap in memory logs
- User demanded: "remember when we start working what we did before"

---

*Last updated: 2026-03-09*
*Next review: Weekly*
