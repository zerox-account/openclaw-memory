# MEMORY.md - Zero-X Long-Term Memory

## Email Outreach Lessons

### What Works
- Direct researcher emails (firstname.lastname@institution)
- German academic institutions (lower bounce rates)
- Personalized subject lines with Horizon Europe reference
- "We seek research partners, not customers" disclaimer

### What Doesn't Work
- Generic institutional addresses (info@, secretariat@)
- External domains to .edu/.gov/.admin.ch (often blocked)
- Assuming "sent" = "delivered" (check for bounces)

### Validation Results Pattern
- ~27% valid emails
- ~30% catch-all (risky but often works)
- ~40% unknown (university server protection)
- ~3% invalid (don't send)

## Active Opportunities

### DLR Stuttgart (High Priority)
- Contact: Dr. Rémi Costa, Prof. Andreas Friedrich
- Meeting: March 4, 2026, 15:00 CET
- Topic: Electrochemical energy & syngas integration
- Status: Time confirmed

### Universities Contacted (March 6, 2026)
- 16 emails sent to mining/engineering departments
- Countries: USA, Canada, Australia, Germany, Sweden, Greece
- Awaiting responses (check in 3-5 days)

## Tools & Workflows

### ZeroBounce Validation
- Always validate before sending
- Catch-all acceptable for universities
- Never override "invalid" results

### Safe Email Sender
- Uses validate_and_send.py wrapper
- Prevents duplicates (7-day block)
- Logs to email_sent_log.json

### Dashboard
- Location: ~/.openclaw/workspace/dashboard/zero-x-dashboard/
- URL: http://localhost:8080/dashboard/zero-x-dashboard/
- Features: X-150 monitoring, CCM projects, sales pipeline

## Competitive Intelligence

### Sierra Energy
- 20 years development, still demo phase
- $33M funding, not commercially scaled
- Complex FastOx technology
- Zero-X advantage: simpler, modular, pragmatic

### Market Position
- Not direct competitors (different scale)
- Zero-X: 50-500kW, decentralized
- Sierra: 100-500 tons/day, centralized

## Target Markets (Prioritized)

1. **Remote Mining** - Diesel replacement, high value
2. **Island Communities** - Expensive grid, waste problem
3. **Forestry** - Biomass availability, Scandinavia
4. **Agriculture** - Remote farms, seasonal needs

## Military/Defense Entry Points

### US
- SBIR Program (Phase I: $300K)
- DIU (Commercial Solutions Opening)
- xTechSearch (annual competition)

### Germany
- IDZ (Innovation für die Bundeswehr)
- UniBw München (Institut für Energietechnik)
- BAAINBw (Bedarfsanzeige)

### International
- FOI Sweden (Energy Security)
- Dstl UK (Waste-to-Energy research)
- NATO SPS (Science for Peace)

## Key Learnings

- Never multiple emails to same institution
- One contact per university
- English for international, German for DACH
- Self-confident tone: "When would you have time..." not "Would you be open..."

## Ongoing Todos

- [ ] Monitor email responses (check March 11-13)
- [ ] Follow up on non-responders after 1 week
- [ ] Research additional mining universities
- [ ] Prepare Horizon Europe proposal template
- [ ] Update dashboard with real data when available
