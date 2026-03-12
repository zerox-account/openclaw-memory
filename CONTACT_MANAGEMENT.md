# ZERO-X CONTACT MANAGEMENT SYSTEM

## 1. CONTACT SOURCING (Where to Find Researchers)

### Primary Sources
- **University websites** - Faculty directories, research group pages
- **ResearchGate** - Profile search by keywords (gasification, biomass, CHP)
- **Google Scholar** - Author search, publication tracking
- **LinkedIn** - Academic profiles, research institutions
- **Conference proceedings** - Authors in relevant fields
- **Horizon Europe project database** - Current/past participants
- **DLR, Fraunhofer directories** - Researcher listings

### Search Keywords (German & English)
- Biomass gasification / Biomassevergasung
- CHP / Kraft-Wärme-Kopplung
- Tar reforming / Teer-Reforming
- Syngas / Synthesegas
- Waste-to-energy / Abfallverwertung
- Circular economy / Kreislaufwirtschaft
- Biochar / Biokohle
- Hydrogen production / Wasserstoffgewinnung

---

## 2. CONTACT SCREENING CRITERIA

### Must-Have (Required)
- [ ] Direct email address (firstname.lastname@institution)
- [ ] Active researcher (publication within last 2 years)
- [ ] Relevant research field (gasification, biomass, CHP, waste)
- [ ] University or research institute (not private company)
- [ ] Based in EU (for Horizon Europe eligibility)

### Nice-to-Have (Preferred)
- [ ] Previous Horizon Europe experience
- [ ] Existing partnerships with industry
- [ ] Access to pilot/demo facilities
- [ ] German-speaking (for easier collaboration)
- [ ] Geographic proximity to Leipzig or Spain

### Red Flags (Reject)
- [ ] Generic email only (info@, secretariat@)
- [ ] No recent publications
- [ ] Completely unrelated field
- [ ] Private company (no research focus)
- [ ] Outside EU

---

## 3. VALIDATION WORKFLOW

### Step 1: Email Validation (ZeroBounce)
```bash
# Validate before adding to database
python3 /Users/julienuhlig/.openclaw/workspace/tools/validate_and_send.py \
  'test@example.com' \
  'Validation Test' \
  /tmp/test.txt \
  --validate-only
```

### Step 2: Duplicate Check
- Check email_sent_log.json (7-day block)
- Check contact_database.json (never contact same person twice)

### Step 3: Domain Check
- Reject .edu/.gov if external sender blocked
- Check institution domain reputation

### Step 4: Manual Review
- Verify researcher profile matches criteria
- Check recent publications relevance
- Confirm Horizon Europe eligibility

---

## 4. CONTACT DATABASE STRUCTURE

### File: contact_database.json
```json
{
  "contacts": [
    {
      "id": "uuid-1234",
      "name": "Dr. Max Mustermann",
      "email": "max.mustermann@kit.edu",
      "institution": "Karlsruher Institut für Technologie",
      "department": "Institut für Technische Chemie",
      "research_field": "Biomass Gasification",
      "keywords": ["tar reforming", "syngas", "fluidized bed"],
      "h_index": 25,
      "recent_publications": 5,
      "horizon_europe_experience": true,
      "source": "Google Scholar",
      "date_added": "2026-03-11",
      "validation_status": "validated",
      "email_status": "not_sent",
      "priority": "high",
      "notes": "Perfect match for X-150 project"
    }
  ]
}
```

### Fields Explained
- **id**: Unique identifier (UUID)
- **name**: Full name with title
- **email**: Validated direct email
- **institution**: University/institute name
- **department**: Specific department
- **research_field**: Primary research area
- **keywords**: Relevant research topics
- **h_index**: Academic impact score
- **recent_publications**: Papers in last 2 years
- **horizon_europe_experience**: Previous EU projects
- **source**: Where contact was found
- **date_added**: When added to database
- **validation_status**: pending/validated/rejected
- **email_status**: not_sent/sent/replied/bounced
- **priority**: high/medium/low
- **notes**: Free text observations

---

## 5. TRACKING WORKFLOW

### Status Flow
```
DISCOVERED → VALIDATED → QUEUED → SENT → REPLIED/NO_REPLY/BOUNCED
```

### Status Definitions
- **DISCOVERED**: Found but not validated
- **VALIDATED**: Email verified, criteria met
- **QUEUED**: Ready to send (waiting for batch or timing)
- **SENT**: Email delivered
- **REPLIED**: Received response
- **NO_REPLY**: No response after 7 days
- **BOUNCED**: Email failed delivery

### Follow-Up Schedule
- Day 0: Initial email sent
- Day 7: Check for reply
- Day 14: First follow-up (if no reply)
- Day 21: Second follow-up (if no reply)
- Day 30: Move to "no_reply" status

---

## 6. AUTOMATION TOOLS

### Contact Scraper (Future)
```python
# Pseudo-code for scraper
from contact_scraper import ResearcherFinder

finder = ResearcherFinder(
    keywords=["biomass gasification", "CHP"],
    location="EU",
    min_h_index=10
)

contacts = finder.search_google_scholar()
contacts += finder.search_researchgate()
contacts += finder.search_university_dirs()

for contact in contacts:
    if validate_contact(contact):
        add_to_database(contact)
```

### Validation Script
```python
# validate_contact.py
import json
import requests

def validate_contact(contact):
    # Check email format
    if not is_valid_email(contact['email']):
        return False
    
    # Check ZeroBounce
    if not zerobounce_validate(contact['email']):
        return False
    
    # Check duplicates
    if is_duplicate(contact['email']):
        return False
    
    # Check criteria
    if not meets_criteria(contact):
        return False
    
    return True
```

---

## 7. REPORTING & ANALYTICS

### Weekly Reports
- New contacts discovered
- Validation success rate
- Emails sent
- Response rate
- Pipeline status

### Monthly Reviews
- Database growth
- Conversion rates
- Priority contact identification
- Strategy adjustments

---

## 8. INTEGRATION WITH STARTUP PROTOCOL

### Add to 91-Step Checklist
**92. Contact Database Maintenance**
- [ ] Check for new contacts to validate
- [ ] Review pending follow-ups
- [ ] Update contact statuses
- [ ] Generate weekly report

**93. Outreach Pipeline Review**
- [ ] Check queued contacts
- [ ] Prepare next batch of emails
- [ ] Review response rates
- [ ] Adjust targeting criteria

---

*Zero-X Contact Management System*
*Version: 2026-03-11*
