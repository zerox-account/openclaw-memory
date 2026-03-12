# GOOGLE CLOUD PROJEKT ERSTELLEN - Schritt-für-Schritt

## SCHRITT 1: Google Cloud Console öffnen

1. Öffne Browser: https://console.cloud.google.com/
2. Melde dich mit deinem Google-Konto an (z.B. zerox@exventure.co)

---

## SCHRITT 2: Neues Projekt erstellen

**Oben im blauen Banner:**
1. Klicke auf den **Projekt-Namen** (steht meist „My First Project" oder ähnlich)
2. Klicke oben rechts: **„+ NEW PROJECT"**

**Im Formular:**
- **Project name:** `Zero-X Calendar`
- **Location:** (Optional, kann leer bleiben)
- Klicke: **„CREATE"**

---

## SCHRITT 3: Auf neues Projekt wechseln

1. Warte 10 Sekunden
2. Klicke wieder auf den **Projekt-Namen** oben
3. Wähle aus der Liste: **„Zero-X Calendar"**

---

## SCHRITT 4: Google Calendar API aktivieren

**In der Suchleiste oben:**
1. Tippe ein: `Google Calendar API`
2. Klicke auf **„Google Calendar API"** im Dropdown
3. Klicke blauen Button: **„ENABLE"**

**Oder über Menü:**
- Sidebar > APIs & Services > Library
- Suche: „Google Calendar API"
- Klicke: „Google Calendar API"
- Klicke: „ENABLE"

---

## SCHRITT 5: OAuth Consent Screen

**Sidebar links:**
1. Klicke: **„OAuth consent screen"**
2. Wähle: **„External"**
3. Klicke: **„CREATE"**

**App Information:**
- **App name:** `Zero-X Calendar`
- **User support email:** Wähle `zerox@exventure.co`
- **App logo:** (Optional, kannst du überspringen)
- **Developer contact information:**
  - Email addresses: `zerox@exventure.co`

Klicke: **„SAVE AND CONTINUE"**

**Scopes (Berechtigungen):**
1. Klicke: **„ADD OR REMOVE SCOPES"
2. Suche nach: `calendar`
3. Setze Häkchen bei:
   - `.../auth/calendar` (Google Calendar API)
   - `.../auth/calendar.events` (Google Calendar Events)
4. Klicke: **„UPDATE"
5. Klicke: **„SAVE AND CONTINUE"**

**Test Users:**
- Klicke: **„ADD USERS"
- Email: `zerox@exventure.co`
- Klicke: **„ADD"
- Klicke: **„SAVE AND CONTINUE"**

**Summary:**
- Klicke: **„BACK TO DASHBOARD"**

---

## SCHRITT 6: Credentials erstellen

**Sidebar links:**
1. Klicke: **„Credentials"**
2. Klicke oben: **„+ CREATE CREDENTIALS"**
3. Wähle: **„OAuth client ID"**

**Application type:**
- Wähle: **„Desktop app"**
- Name: `Zero-X Desktop`

Klicke: **„CREATE"**

---

## SCHRITT 7: Datei herunterladen

**Pop-up erscheint:**
1. Klicke: **„DOWNLOAD JSON"**
2. Datei wird gespeichert als: `client_secret_xxxx.json`
3. **WICHTIG:** Benenne um in: `credentials.json`

---

## SCHRITT 8: Datei an mich schicken

**Option A (Einfach):**
- Öffne Telegram
- Sende mir die Datei `credentials.json`

**Option B (E-Mail):**
- Sende an: clemente@exventure.co oder zerox@exventure.co

---

## ✅ CHECKLISTE

- [ ] Bei https://console.cloud.google.com/ eingeloggt
- [ ] Projekt „Zero-X Calendar" erstellt
- [ ] Google Calendar API aktiviert
- [ ] OAuth consent screen erstellt (External)
- [ ] Scopes hinzugefügt (calendar, calendar.events)
- [ ] Credentials erstellt (Desktop app)
- [ ] Datei heruntergeladen (`credentials.json`)
- [ ] Datei an mich gesendet

---

**Dauer:** 5-10 Minuten
**Schwierigkeit:** Einfach (nur klicken, kein Code)

Sobald ich die Datei habe → Ich richte die Automation ein! 🚀
