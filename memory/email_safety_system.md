# E-Mail Safety System

## Problem: Doppelte E-Mail-Versendung

**Ursache:** Himalaya zeigte Fehlermeldung "Folder doesn't exist", aber E-Mails wurden trotzdem gesendet. Neue Sendung wurde ausgelöst ohne Verifizierung.

## Lösung: Multi-Layer Sicherheit

### Layer 1: Sent-Log Datenbank

**Datei:** `memory/email_sent_log.json`

Struktur:
```json
{
  "emails": [
    {
      "to": "info@dbfz.de",
      "subject": "Kollaborationsmöglichkeit...",
      "sent_at": "2026-02-16T22:41:49-08:00",
      "method": "himalaya",
      "verified": true
    }
  ]
}
```

**Regel:** Vor jedem Senden wird geprüft, ob (to + subject) bereits im Log existiert.

### Layer 2: Pre-Send Verification

**Pflichtschritte vor E-Mail-Versand:**

1. **Sent-Ordner prüfen** (nicht nur auf Fehlermeldungen hören)
   ```python
   # Prüfe letzte 50 E-Mails im Sent-Ordner
   # Suche nach gleichem Empfänger + ähnlichem Betreff
   ```

2. **Zeitfenster-Check**
   - Keine E-Mail an denselben Empfänger innerhalb von 7 Tagen
   - Ausnahme: Explizite Anweisung vom User

3. **Dry-Run Mode**
   - Zeige E-Mail-Inhalt + Empfänger
   - Warte auf Bestätigung vor tatsächlichem Versand

### Layer 3: Automatische Deduplizierung

**Python-Script mit eingebautem Schutz:**

```python
import json
import os
from datetime import datetime, timedelta

SENT_LOG = "/Users/julienuhlig/.openclaw/workspace/memory/email_sent_log.json"

def check_duplicate(to_email, subject):
    """Prüft ob E-Mail bereits gesendet wurde"""
    if not os.path.exists(SENT_LOG):
        return False
    
    with open(SENT_LOG, 'r') as f:
        log = json.load(f)
    
    for entry in log.get('emails', []):
        if entry['to'] == to_email and entry['subject'] == subject:
            # Prüfe ob innerhalb letzter 7 Tage
            sent_date = datetime.fromisoformat(entry['sent_at'])
            if datetime.now() - sent_date < timedelta(days=7):
                return True
    return False

def log_email(to_email, subject, method):
    """Loggt gesendete E-Mail"""
    log = {'emails': []}
    if os.path.exists(SENT_LOG):
        with open(SENT_LOG, 'r') as f:
            log = json.load(f)
    
    log['emails'].append({
        'to': to_email,
        'subject': subject,
        'sent_at': datetime.now().isoformat(),
        'method': method,
        'verified': True
    })
    
    with open(SENT_LOG, 'w') as f:
        json.dump(log, f, indent=2)
```

### Layer 4: Himalaya-Spezifische Prüfung

**Problem:** Himalaya sendet trotz IMAP-Fehler

**Lösung:** Nach Himalaya-Fehler immer IMAP-Check:
```python
def verify_himalaya_send(to_email, subject):
    """Prüft ob E-Mail tatsächlich gesendet wurde"""
    # Verbinde mit Gmail IMAP
    # Suche in Sent Mail nach E-Mail an to_email mit subject
    # Warte 10 Sekunden (Gmail-Verzögerung)
    # Return True/False
```

## Implementierung

### Sofortmaßnahmen:

1. ✅ **Sent-Log erstellen** (dieses Dokument)
2. ✅ **Pre-send Check-Script** implementieren
3. ✅ **TOOLS.md aktualisieren** mit neuem Protokoll
4. ⏳ **Alle bestehenden Sendungen** in Log eintragen

### Neues E-Mail-Protokoll:

**Vor jedem Senden:**
1. Prüfe `email_sent_log.json` auf Duplikat
2. Prüfe Gmail Sent Mail via IMAP (letzte 20 E-Mails)
3. Zeige Empfänger + Betreff + erste 200 Zeichen
4. Frage: "Soll diese E-Mail gesendet werden? (ja/nein)"
5. Nach Senden: Eintrag in Log + IMAP-Verifizierung

### Cron-Job Updates:

**Nie automatisch senden ohne:**
- Duplikat-Check
- User-Bestätigung
- Logging

**Für scheduled sends:**
- Erstelle Draft in Gmail
- Benachrichtige User zur Bestätigung
- Sende erst nach explizitem Go

## Rollback-Plan

**Falls doch doppelt gesendet:**
1. Sofort Stop aller E-Mail-Aktivitäten
2. Analyse: Welche E-Mails waren betroffen?
3. Entschuldigungs-E-Mail senden (wenn angemessen)
4. System-Patch implementieren
5. Dokumentation aktualisieren

## Verantwortlichkeiten

**Ich muss:**
- IMMER Duplikat-Check durchführen
- NIE auf Tool-Fehlermeldungen allein vertrauen
- IMMER IMAP-Verifizierung nach Himalaya-Fehlern
- JEDE Sendung loggen

**User kann:**
- Log jederzeit prüfen
- Force-send bei bewusster Wiederholung
- Quota-Limits setzen
