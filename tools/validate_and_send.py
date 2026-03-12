#!/usr/bin/env python3
"""
MANDATORY Pre-Send Email Validation Wrapper
This script MUST be used before ANY email is sent.
It enforces ZeroBounce validation as a hard requirement.

Usage:
  python3 validate_and_send.py <recipient> <subject> <body_file>
  
This will:
  1. Validate email via ZeroBounce
  2. If valid: proceed to safe_email_sender.py
  3. If invalid: BLOCK sending and report error
"""

import sys
import os
import subprocess
import json

# API Configuration
API_KEY = os.environ.get("ZEROBOUNCE_API_KEY", "")
API_URL = "https://api.zerobounce.net/v2/validate"

def validate_email(email):
    """Validate email via ZeroBounce API"""
    import requests
    
    if not API_KEY:
        print("❌ CRITICAL: ZEROBOUNCE_API_KEY not set!")
        print("   Set it with: export ZEROBOUNCE_API_KEY='your-key'")
        return None
    
    params = {
        "api_key": API_KEY,
        "email": email.strip(),
        "ip_address": ""
    }
    
    try:
        response = requests.get(API_URL, params=params, timeout=30)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ API Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Validation error: {e}")
        return None

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 validate_and_send.py <recipient> <subject> <body_file>")
        print("       python3 validate_and_send.py 'test@example.com' 'Subject' /tmp/mail.txt")
        sys.exit(1)
    
    recipient = sys.argv[1]
    subject = sys.argv[2]
    body_file = sys.argv[3]
    
    print("=" * 60)
    print("🔒 MANDATORY PRE-SEND VALIDATION")
    print("=" * 60)
    print(f"📧 Recipient: {recipient}")
    print(f"📝 Subject: {subject}")
    print()
    
    # Step 1: Validate email
    print("🔍 Step 1: Validating email via ZeroBounce...")
    result = validate_email(recipient)
    
    if not result:
        print("❌ VALIDATION FAILED - Cannot proceed")
        print("❌ EMAIL NOT SENT")
        sys.exit(1)
    
    status = result.get('status', 'unknown')
    sub_status = result.get('sub_status', '')
    
    print(f"   Status: {status}")
    if sub_status:
        print(f"   Sub-status: {sub_status}")
    
    # Step 2: Check if safe to send
    if status == "valid":
        print("   ✅ Email is VALID - Proceeding...")
    elif status == "catch-all":
        print("   ⚠️  Email is CATCH-ALL (risky but allowed)")
        print("   ⚠️  Proceeding with caution...")
    elif status == "unknown":
        print("   ❓ Email status is UNKNOWN")
        print("   ❌ BLOCKED: Cannot send to unverified addresses")
        print("=" * 60)
        sys.exit(1)
    elif status == "invalid":
        print(f"   ❌ Email is INVALID ({sub_status})")
        print("   ❌ BLOCKED: Will not send to invalid address")
        print("=" * 60)
        
        # Log the invalid email
        log_entry = {
            "timestamp": subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"]).decode().strip(),
            "email": recipient,
            "status": status,
            "sub_status": sub_status,
            "subject": subject,
            "blocked": True
        }
        
        # Append to blocked log
        log_file = "/Users/julienuhlig/.openclaw/workspace/memory/blocked_emails.json"
        try:
            with open(log_file, 'r') as f:
                blocked = json.load(f)
        except:
            blocked = {"blocked": []}
        
        blocked["blocked"].append(log_entry)
        
        with open(log_file, 'w') as f:
            json.dump(blocked, f, indent=2)
        
        print(f"   📝 Logged to: {log_file}")
        sys.exit(1)
    elif status == "spamtrap":
        print("   🚫 SPAM TRAP DETECTED!")
        print("   🚫 BLOCKED: This is a known spam trap")
        print("=" * 60)
        sys.exit(1)
    else:
        print(f"   ❓ Unexpected status: {status}")
        print("   ❌ BLOCKED: Unknown validation result")
        print("=" * 60)
        sys.exit(1)
    
    print()
    print("🔒 Step 2: Checking for duplicates...")
    
    # Step 3: Check duplicate log
    log_file = "/Users/julienuhlig/.openclaw/workspace/memory/email_sent_log.json"
    try:
        with open(log_file, 'r') as f:
            sent_log = json.load(f)
    except:
        sent_log = {"emails": [], "blocked_duplicates": []}
    
    # Check for duplicates within 7 days
    from datetime import datetime, timedelta
    now = datetime.now()
    
    # Skip duplicate check for replies (subject starts with "Re:" or contains reply indicators)
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
        print("   📧 Reply/Follow-up detected - Skipping duplicate check")
        print("   ✅ Replies are exempt from 7-day duplicate protection")
    else:
        # Check for duplicates within 7 days (only for cold outreach)
        for email in sent_log.get("emails", []):
            if email["to"] == recipient:
                sent_time = datetime.fromisoformat(email["sent_at"].replace('Z', '+00:00'))
                if (now - sent_time) < timedelta(days=7):
                    print(f"   ❌ DUPLICATE DETECTED!")
                    print(f"   ❌ Already sent on: {email['sent_at']}")
                    print(f"   ❌ Subject: {email['subject']}")
                    print("=" * 60)
                    print("   ❌ EMAIL NOT SENT (duplicate within 7 days)")
                    
                    # Log blocked duplicate
                    blocked_entry = {
                        "timestamp": now.isoformat(),
                        "to": recipient,
                        "subject": subject,
                        "reason": "Duplicate within 7 days",
                        "original_sent": email["sent_at"]
                    }
                    sent_log["blocked_duplicates"].append(blocked_entry)
                    
                    with open(log_file, 'w') as f:
                        json.dump(sent_log, f, indent=2)
                    
                    sys.exit(1)
    
    print("   ✅ No duplicates found")
    print()
    print("=" * 60)
    print("✅ ALL CHECKS PASSED - Proceeding to send...")
    print("=" * 60)
    print()
    
    # Step 4: Call safe_email_sender.py
    sender_script = "/Users/julienuhlig/.openclaw/workspace/tools/safe_email_sender.py"
    subprocess.run([
        "python3", sender_script,
        recipient,
        subject,
        body_file
    ])

if __name__ == "__main__":
    main()
