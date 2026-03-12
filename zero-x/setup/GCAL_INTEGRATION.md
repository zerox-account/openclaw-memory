# GOOGLE CALENDAR INTEGRATION - SETUP GUIDE

## ZIEL
Vollautomatische Kalender-Einträge durch Zero-X Global Control Center.

## SCHRITT 1: Google Cloud Setup (Clemens)

### 1.1 Projekt erstellen
- Gehe zu: https://console.cloud.google.com/
- Neues Projekt: "Zero-X Calendar"

### 1.2 API aktivieren
- Suche: "Google Calendar API"
- Klicke: "Enable"

### 1.3 OAuth Consent Screen
- Sidebar: "OAuth consent screen"
- User Type: "External"
- App Name: "Zero-X Calendar"
- User Support Email: zerox@exventure.co
- Developer Contact: zerox@exventure.co
- Scopes: Add "Google Calendar API" (auth/calendar)

### 1.4 Credentials erstellen
- Sidebar: "Credentials"
- Create Credentials > OAuth client ID
- Application Type: "Desktop app"
- Name: "Zero-X Desktop"
- Download: `credentials.json`

### 1.5 Datei senden
- Schicke `credentials.json` an mich (Telegram/Upload)

---

## SCHRITT 2: Authentifizierung (Agent)

Ich führe aus:
```bash
python3 zero-x/setup/google_calendar_auth.py
```

- Öffnet Browser-Tab
- Du klickst: "Allow"
- Fertig! Token gespeichert.

---

## SCHRITT 3: Automation

Danach kann ich automatisch:
- Termine erstellen
- Einladungen senden
- Erinnerungen setzen
- Wiederkehrende Events

Beispiel:
```python
add_event(
    summary="DBFZ Call",
    start_time=datetime(2026, 2, 10, 9, 15),
    end_time=datetime(2026, 2, 10, 10, 0),
    attendees=["Karen.Deprie@dbfz.de"],
    description="Horizon Europe partnership"
)
```

---

## SICHERHEIT

- `credentials.json` = Client ID (öffentlich)
- `token.json` = Access Token (privat, gespeichert lokal)
- Token erneuert sich automatisch

---

## TROUBLESHOOTING

**"Token expired"**
→ Ich erneuere automatisch

**"Access denied"**
→ OAuth Consent Screen auf "Production" statt "Testing"

**"Calendar not found"**
→ Prüfe Calendar ID (meist "primary")

---

**Status: Warte auf `credentials.json` von Clemens**
