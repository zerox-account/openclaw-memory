# Email Outreach Standards - Zero-X Labs

## 1. Email Validation (MANDATORY)

### Pre-Send Checkliste
- [ ] **ZeroBounce-Validierung** durchführen (KEINE Ausnahmen)
- [ ] `validate_and_send.py` verwenden (NICHT safe_email_sender.py direkt)
- [ ] Duplikat-Check (7-Tage-Block beachten)

### Blockierte Status (NIEMALS senden)
| Status | Bedeutung | Aktion |
|--------|-----------|--------|
| `invalid` + `mailbox_not_found` | Adresse existiert nicht | Alternative suchen |
| `invalid` + `domain_not_found` | Domain existiert nicht | Löschen |
| `spamtrap` | Falle | Löschen, niemals senden |

### Riskante Status (Vorsicht)
| Status | Bedeutung | Aktion |
|--------|-----------|--------|
| `catch-all` | Akzeptiert alle Mails | Nur bei wichtigen Kontakten |
| `unknown` | Nicht verifizierbar | Alternative bevorzugen |

---

## LEARNINGS FROM 2026-02-26

### Automation Fixes Implemented
- **7-Day Duplicate Block Fixed:** Script now detects "Re:" in subject and skips duplicate check for legitimate replies
- **Available Time Slots:** Always confirm 15:00-17:00 Bali Time before suggesting meetings - never assume availability

### Data Quality Critical
- **"134 Contacts" List Reality:** Only 45 unique emails, 35% invalid. Always validate BEFORE writing drafts.
- **Institutional Diversity:** Filter early - avoid suggesting 4x NREL or 3x MIT in one batch
- **Validation First:** Validate emails BEFORE drafting, not after (time saved on invalid addresses)

### Messaging Improvements
- **"Research partners, not customers" is MANDATORY:** Must be explicitly stated, otherwise sounds like sales
- **Our Expertise as Hook:** Lead with operational data (1,000+ hours), commercial deployment (Project Cométha with Fraunhofer), real-world validation
- **Clear CTA:** "next week" converts better than "sometime"

### Targeting Lessons
- **Methodological Overlap Check:** Ronny Neumann declined - electrochemical CO2 reduction (low temp) vs thermochemical syngas (high temp) are competing approaches, not complementary
- **Gatekeepers Work:** Bart Hommez (Business Dev) as entry to Kevin Van Geem (skeptical professor) more effective than direct PI contact

---

## 2. Email Content Standards

### MUST-HAVE Elemente (in jeder Email)
1. **Projekt Cométha Paris** erwähnen
   - "validated through Project Cométha in Paris (1,000+ operating hours)"
   - "developed in collaboration with the Fraunhofer Institute"
2. **X-150 System** kurz beschreiben
3. **"We seek research partners, not customers"** – Klärung der Absicht
4. **Signatur (FIXED - niemals ändern):**
   ```
   Clemens Grosjean
   Zero-X Labs GmbH
   zerox@exventure.co
   +49 341 92881290
   ```

### Tonalität
- **Selbstbewusst**, nicht entschuldigend
- "Perhaps our first email wasn't as clear as it should have been" ✅
- "My apologies for..." ❌ (Zu defensiv)

### Sprache je nach Land
| Land | Sprache |
|------|---------|
| Deutschland, Österreich, Schweiz | Deutsch |
| Alle anderen Länder | Englisch |

---

## 3. Timing Standards

### Optimale Sendezeiten (lokale Zeit)
| Region | Beste Zeit | Vermeiden |
|--------|-----------|-----------|
| Europa | 07:30-08:30 Uhr | Nachmittag |
| USA/Canada | 08:00-09:00 EST | Später Nachmittag |
| Japan | 08:00-09:00 JST | Mittag |
| Allgemein | Morgens | Freitag Nachmittag |

### Scheduling
- Cron nutzen für präzise Zeitpunkte
- Heartbeats für Batch-Checks (E-Mails, Kalender)

---

## 4. Adress-Qualität (Was funktioniert/nicht)

### ✅ Funktioniert (niedrige Bounce-Rate)
- Direkte Forscher-Emails: `vorname.nachname@institution.de`
- Deutsche akademische Institutionen (DLR, Uni Stuttgart, etc.)
- ETH Zurich

### ❌ Funktioniert NICHT (hohe Bounce-Rate)
- Generische Adressen: `info@`, `secretariat@`, `decanato@`
- Spanische Universitäten (ULPGC, CIEMAT) – Adressen oft ungültig
- TU Delft – blockt externe Sender (550 5.4.1)
- Japanische Regierungsdomains – strikte Filter
- .gov / .admin.ch Domains – aggressive Spam-Filter

### Fallback-Strategien bei geblockten Adressen
1. **FREA-Ansatz** (für AIST): Spezialisierte Institute statt Zentrale
2. **LinkedIn** suchen (persönliches Profil)
3. **Telefon** – Hauptnummer anrufen und durchstellen lassen
4. **Internationales Büro** kontaktieren (bei Großen Instituten)

---

## 5. Bounce Detection & Monitoring

### Post-Send Check (5 Minuten nach Versand)
```bash
# Bounces der letzten 10 Mails prüfen (5 Min nach Senden)
himalaya envelope list --page 1 --page-size 10 | grep -E "(Delivery Status|Undeliverable|No se puede)"
```
**Wichtig:** Sofort prüfen, nicht warten. Bounces kommen oft innerhalb weniger Minuten.

### Typische Fehlermuster
| Fehler | Institution | Lösung |
|--------|-------------|--------|
| `550 5.4.1 Access denied` | TU Delft, AIST | LinkedIn/Telefon |
| `Undeliverable` | ULPGC, CIEMAT | Adresse löschen |
| `No se puede entregar` | Spanische Institute | Alternative suchen |

### Dokumentation
- Bounces SOFORT in `memory/YYYY-MM-DD.md` dokumentieren
- Adresse aus zukünftigen Kampagnen entfernen
- Alternative Kontaktmethode suchen

---

## 6. Follow-Up Standards

### Zeitplan
| Phase | Zeitpunkt | Aktion |
|-------|-----------|--------|
| Initial | T+0 | Erste Email senden |
| Bounce-Check | T+5 Minuten | Sofort auf Bounces prüfen |
| Follow-up | T+5-7 Tage | Erinnerung bei Nicht-Antwort |
| LinkedIn | T+7-10 Tage | Alternative Kontaktaufnahme |
| Letzter Versuch | T+14 Tage | Abschließende Email |

### Bei positiver Antwort
- **Schnell reagieren** (idealerweise < 24h)
- **Konkret sein** – auf spezifische Fragen eingehen
- **Keine Entschuldigungen** – sachlich bleiben
- **Nächsten Schritt vorschlagen** (Call, Meeting, etc.)

---

## 7. Tools & Workflows

### Mandatory Scripts
| Tool | Zweck | Pfad |
|------|-------|------|
| `validate_and_send.py` | Validierung + Versand | `/tools/validate_and_send.py` |
| `zerobounce_check.py` | Einzel-Email-Check | `/tools/zerobounce_check.py` |
| `zerobounce_batch.py` | Batch-Validierung | `/tools/zerobounce_batch.py` |

### Email-Log
- Location: `memory/email_sent_log.json`
- 7-Tage-Duplikat-Block aktiv
- Manuell prüfen bei Verdacht auf Fehler

---

## 8. Institution-Specific Learnings

### DLR Stuttgart ✅
- Direkte Forscher-Emails funktionieren (Friedrich, Costa)
- Schnelle Antwortzeiten (24h)
- Meeting bereits geplant (4. März 15:00 CET)

### TU Delft ❌
- Blockiert externe Sender komplett
- LinkedIn oder Telefon als Alternative
- Herman Reizer: invalid (mailbox_not_found)

### AIST Japan ⚠️
- Direkte Adressen (yoshikawa@aist.go.jp) geblockt
- FREA als Alternative: frea-info-ml@aist.go.jp ✅
- Oder International Affairs Office Formular

### Spanische Institute (ULPGC, CIEMAT) ❌
- Generische Adressen oft ungültig
- Direkte Forscher-Adressen nötig
- LinkedIn oft besserer Kanal

---

## 9. Compliance & Reputation

### Wichtige Regeln
1. **Niemals** an unvalidierte Adressen senden
2. **Niemals** Bounce-Overrides (manuelles Senden nach Block)
3. **Immer** ZeroBounce vor Bulk-Sendungen nutzen
4. **Bounces dokumentieren** – für zukünftige Kampagnen
5. **Signatur niemals ändern** – Clemens Grosjean Signatur ist FIXED

### Reputation-Schutz
- Niedrige Bounce-Rate = Bessere Zustellbarkeit
- Spam-Traps vermeiden (Blacklist-Risiko)
- Duplikat-Block verhindert Überlastung

---

## 10. Checkliste vor jeder Kampagne

- [ ] Alle Adressen durch ZeroBounce validiert?
- [ ] Duplikate ausgeschlossen?
- [ ] Cométha Paris erwähnt?
- [ ] "Research partners, not customers" drin?
- [ ] Signatur exakt wie vorgegeben (Clemens Grosjean)?
- [ ] Richtige Sprache für Zielland?
- [ ] Optimale Sendezeit gewählt?
- [ ] Bounce-Check in 5 Minuten eingeplant?

---

*Last Updated: 2026-02-25*
*Next Review: Nach jeder großen Kampagne*
