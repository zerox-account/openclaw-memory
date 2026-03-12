#!/usr/bin/env python3
"""
Safe Email Sender - Verhindert doppelte E-Mail-Versendungen
"""

import smtplib
import ssl
import json
import os
import sys
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENT_LOG = "/Users/julienuhlig/.openclaw/workspace/memory/email_sent_log.json"
SENDER = "zerox@exventure.co"
PASSWORD_FILE = "/Users/julienuhlig/.config/himalaya/.pass"

def load_log():
    """Lädt das Sende-Log"""
    if not os.path.exists(SENT_LOG):
        return {'emails': [], 'blocked_duplicates': [], 'last_updated': datetime.now().isoformat()}
    with open(SENT_LOG, 'r') as f:
        return json.load(f)

def save_log(log):
    """Speichert das Sende-Log"""
    log['last_updated'] = datetime.now().isoformat()
    with open(SENT_LOG, 'w') as f:
        json.dump(log, f, indent=2)

def check_duplicate(to_email, subject):
    """
    Prüft ob E-Mail bereits in den letzten 7 Tagen gesendet wurde
    Returns: (is_duplicate, previous_send_date)
    """
    # Skip duplicate check for replies/follow-ups
    subject_lower = subject.strip().lower()
    is_reply = (
        subject_lower.startswith("re:") or
        subject_lower.startswith("aw:") or  # German "Antwort"
        subject_lower.startswith("antwort:") or
        "entschuldigung" in subject_lower or  # Apology emails
        "nachfrage" in subject_lower or  # Follow-up
        "wiedervorlage" in subject_lower  # Rescheduling
    )
    
    if is_reply:
        return (False, None)  # Skip duplicate check for replies
    
    log = load_log()
    
    for entry in log.get('emails', []):
        if entry['to'] == to_email and entry['subject'] == subject:
            sent_str = entry['sent_at']
            # Handle both offset-aware and offset-naive formats
            if sent_str.endswith('Z'):
                sent_str = sent_str[:-1] + '+00:00'
            sent_date = datetime.fromisoformat(sent_str)
            # Make sent_date offset-aware for comparison
            if sent_date.tzinfo is None:
                from datetime import timezone
                sent_date = sent_date.replace(tzinfo=timezone.utc)
            if datetime.now().astimezone() - sent_date < timedelta(days=7):
                return True, sent_date
    
    return False, None

def verify_via_imap(to_email, subject, minutes_back=60):
    """
    Prüft Gmail Sent Mail ob E-Mail bereits existiert
    """
    try:
        import imaplib
        from email.header import decode_header
        from email import message_from_bytes
        
        password = open(PASSWORD_FILE).read().strip()
        context = ssl.create_default_context()
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993, ssl_context=context)
        mail.login(SENDER, password)
        mail.select('[Gmail]/Sent Mail')
        
        # Suche nach E-Mails an diesen Empfänger
        result, data = mail.search(None, f'TO "{to_email}"')
        if result == 'OK':
            email_ids = data[0].split()
            for e_id in email_ids[-20:]:  # Letzte 20 prüfen
                result, msg_data = mail.fetch(e_id, '(RFC822)')
                if result == 'OK':
                    msg = message_from_bytes(msg_data[0][1])
                    msg_subject = decode_header(msg['Subject'])[0][0]
                    if isinstance(msg_subject, bytes):
                        msg_subject = msg_subject.decode()
                    if msg_subject == subject:
                        mail.logout()
                        return True
        mail.logout()
    except Exception as e:
        print(f"⚠️  IMAP-Verifizierung fehlgeschlagen: {e}")
    
    return False

def send_email(to_email, subject, body, dry_run=False):
    """
    Sendet E-Mail mit Duplikat-Schutz
    """
    print(f"\n{'='*60}")
    print(f"📧 E-Mail-Versand-Prüfung")
    print(f"{'='*60}")
    print(f"An: {to_email}")
    print(f"Betreff: {subject}")
    print(f"Länge: {len(body)} Zeichen")
    
    # Check 1: Lokales Log
    is_dup, prev_date = check_duplicate(to_email, subject)
    if is_dup:
        print(f"\n🚫 BLOCKIERT: E-Mail wurde bereits am {prev_date} gesendet!")
        print(f"   Keine doppelte Sendung erlaubt.")
        
        # Logge blockierten Versuch
        log = load_log()
        log['blocked_duplicates'].append({
            'to': to_email,
            'subject': subject,
            'attempted_at': datetime.now().isoformat(),
            'reason': 'Duplicate within 7 days'
        })
        save_log(log)
        return False
    
    # Check 2: IMAP-Verifizierung (doppelte Sicherheit)
    if verify_via_imap(to_email, subject):
        print(f"\n🚫 BLOCKIERT: E-Mail bereits in Gmail Sent Mail gefunden!")
        
        # Füge zu Log hinzu falls verpasst
        log = load_log()
        log['emails'].append({
            'to': to_email,
            'subject': subject,
            'sent_at': datetime.now().isoformat(),
            'method': 'imap_detected',
            'verified': True
        })
        save_log(log)
        return False
    
    # Dry-Run Mode
    if dry_run:
        print(f"\n🔍 DRY-RUN: E-Mail würde gesendet werden (kein Duplikat gefunden)")
        print(f"   Inhalt (erste 200 Zeichen):\n   {body[:200]}...")
        return True
    
    # User-Bestätigung
    print(f"\n⚠️  Diese E-Mail wurde NOCH NICHT gesendet.")
    confirm = input("   Senden? (ja/nein): ").strip().lower()
    
    if confirm not in ['ja', 'yes', 'j', 'y']:
        print("   ❌ Abgebrochen durch User")
        return False
    
    # Senden
    try:
        print(f"   📤 Sende...")
        password = open(PASSWORD_FILE).read().strip()
        
        msg = MIMEMultipart()
        msg['From'] = SENDER
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(SENDER, password)
            server.sendmail(SENDER, to_email, msg.as_string())
        
        # Erfolg loggen
        log = load_log()
        log['emails'].append({
            'to': to_email,
            'subject': subject,
            'sent_at': datetime.now().isoformat(),
            'method': 'python_smtp_safe',
            'verified': True
        })
        save_log(log)
        
        print(f"   ✅ Erfolgreich gesendet und geloggt")
        return True
        
    except Exception as e:
        print(f"   ❌ Fehler beim Senden: {e}")
        return False

def main():
    """CLI Interface"""
    if len(sys.argv) < 4:
        print("Verwendung:")
        print(f"  {sys.argv[0]} <to> <subject> <body_file> [--dry-run]")
        print(f"\nBeispiel:")
        print(f"  {sys.argv[0]} 'info@dbfz.de' 'Test' /tmp/mail.txt --dry-run")
        sys.exit(1)
    
    to_email = sys.argv[1]
    subject = sys.argv[2]
    body_file = sys.argv[3]
    dry_run = '--dry-run' in sys.argv
    
    with open(body_file, 'r') as f:
        body = f.read()
    
    success = send_email(to_email, subject, body, dry_run)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
