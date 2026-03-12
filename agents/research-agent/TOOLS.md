# TOOLS.md - Agent Research Tools & Commands

## Command Triggers

| Command | Action |
|---------|--------|
| `/search [topic]` | Find researchers in specific field |
| `/profile [name]` | Generate professor profile from publications |
| `/template [type]` | Show email template for scenario |
| `/validate [email]` | Check email validity before sending |
| `/followup [contact]` | Generate follow-up email |
| `/horizon` | Show Horizon Europe proposal guidance |

## Research Sources

### Academic Databases
- **Google Scholar:** scholar.google.com (publications, citations)
- **ResearchGate:** researchgate.net (profiles, recent work)
- **LinkedIn:** linkedin.com (professional profiles)
- **University websites:** Faculty directories
- **ORCID:** orcid.org (researcher IDs and works)

### University Rankings & Information
- **QS Rankings:** topuniversities.com
- **Times Higher Education:** timeshighereducation.com
- **Shanghai Ranking:** shanghairanking.com

### Funding Databases
- **Horizon Europe:** ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities
- **CORDIS:** cordis.europa.eu (EU project database)
- **National funding:** DFG (Germany), NSF (USA), EPSRC (UK)

## Email Validation

### ZeroBounce (Primary)
```bash
export ZEROBOUNCE_API_KEY="0b04da592b884ce6aaf94181d50f2d4d"
python3 ~/.openclaw/workspace/tools/zerobounce_check.py "email@university.edu"
```

### Batch Validation
```bash
python3 ~/.openclaw/workspace/tools/zerobounce_batch.py --file emails.txt
```

## Email Templates

### Template 1: Initial Outreach - Mining Engineering
**Subject:** Collaboration Opportunity – Energy Systems for Remote Mining & Horizon Europe

```
Dear [Title] [Last Name],

Your work at [University] [Department] on [specific research area, e.g., "sustainable mining operations"] is of great interest to our project. Your research on [specific topic from their publications] is crucial for advancing [relevant field].

We are developing the X-150, a containerized CHP gasification system with integrated tar reforming (validated 1,000+ hours in the Cométha project, Paris). Our focus on modular, decentralized energy systems aligns with your research on [their focus area].

Specifically, your paper on "[Paper Title]" ([Year]) addresses challenges that our technology could help solve: [specific connection].

Your expertise in [their expertise] could enhance our system's application for [specific use case]. We see potential for collaboration in [specific research area].

Important: We are looking for research partners, not customers.

When would you have time next week for a brief conversation about collaboration possibilities?

Best regards,
Clemens Grosjean
Zero-X Labs GmbH
zerox@exventure.co
+49 341 92881290
```

### Template 2: Follow-up (1 week)
**Subject:** RE: Collaboration Opportunity – [Original Subject]

```
Dear [Title] [Last Name],

I hope this email finds you well. I wanted to follow up on my message from [date] regarding a potential research collaboration between Zero-X Labs and [Institution].

I understand you receive many such inquiries. Given your expertise in [their field], I believe our X-150 gasification system could provide an interesting platform for research on [specific topic].

Would you have 15 minutes for a brief call next week to explore this further?

Best regards,
Clemens Grosjean
```

### Template 3: Response to Interest
**Subject:** Next Steps – Zero-X / [University] Collaboration

```
Dear [Title] [Last Name],

Thank you for your interest in exploring a collaboration with Zero-X Labs.

As a next step, I would suggest a brief video call to discuss:
1. Your current research priorities and how they might align
2. Potential collaboration models (student thesis, joint project, equipment access)
3. Horizon Europe funding opportunities
4. Timeline and next steps

Would [suggest 2-3 time options] work for you?

I can provide technical documentation and our research collaboration proposal in advance.

Looking forward to speaking.

Best regards,
Clemens Grosjean
```

## Communication Guidelines

### German Academic Etiquette
- Use formal "Sie" (implied in written communication)
- Full titles: "Prof. Dr.-Ing." not just "Prof."
- Mention specific publications
- Reference German funding sources (DFG, BMBF)
- Be thorough and detailed

### International (English) Etiquette
- "Prof." or "Dr." usually sufficient
- Shorter, more direct emails acceptable
- Lead with value proposition
- Clear call to action
- Faster follow-up acceptable

### Subject Line Best Practices
- Include "Horizon Europe" for EU academics
- Mention specific technology ("gasification," "biomass")
- Keep under 60 characters if possible
- Avoid spam triggers: "opportunity," "free," "urgent"

## Research Partner Profiling

### Information to Gather
- [ ] Full name and title
- [ ] Department and university
- [ ] Research focus areas
- [ ] Recent publications (last 3 years)
- [ ] Current projects and grants
- [ ] Industry partnerships
- [ ] Student supervision
- [ ] Contact email (validated)
- [ ] Response history

### Red Flags (Avoid)
- No recent publications (>5 years)
- No industry collaboration experience
- Overwhelmed with existing projects
- Unresponsive to initial contact
- Research focus completely misaligned

## Horizon Europe Guidance

### Relevant Calls (2024-2025)
- **Clean Energy Transition:** HORIZON-CL5-2024
- **Circular Economy:** HORIZON-CL6-2024
- **Climate Neutral Cities:** HORIZON-MISS-2024

### Proposal Structure
1. **Excellence:** Technical innovation, methodology
2. **Impact:** Environmental, economic, societal
3. **Implementation:** Work packages, timeline, consortium

### Zero-X Contribution
- Technology provider (TRL 6-7)
- Industry perspective and data
- Pilot site for validation
- Dissemination and exploitation

## Tracking & CRM

### Contact Status Codes
- **NEW:** Identified, not yet contacted
- **CONTACTED:** Initial email sent
- **RESPONDED:** Positive response received
- **MEETING:** Call/meeting scheduled
- **PROPOSAL:** Collaboration proposal sent
- **ACTIVE:** Collaboration ongoing
- **DECLINED:** Negative response
- **NO RESPONSE:** No reply after 3 follow-ups

### Follow-up Schedule
- **Day 7:** First follow-up if no response
- **Day 14:** Second follow-up
- **Day 21:** Final follow-up
- **Day 30:** Mark as "NO RESPONSE"

## Key Metrics

### Email Performance
- Open rate target: >40%
- Response rate target: >15%
- Meeting conversion: >30% of responders

### Partnership Pipeline
- Target: 50 new contacts/month
- Goal: 5 active collaborations/year
- Horizon Europe: 2-3 proposals/year
