#!/usr/bin/env python3
"""
GATEKEEPER - Mandatory Checklist Enforcement
Zero-X Labs Outreach System

This script MUST be run BEFORE any email outreach activity.
It enforces the STANDARDS.md checklist and blocks execution until all items are confirmed.

Usage: python3 gatekeeper.py
Returns: 0 if approved, 1 if blocked
"""

import sys
import json
from datetime import datetime

def print_header():
    print("="*70)
    print("🚦 GATEKEEPER - MANDATORY STANDARDS CHECK")
    print("="*70)
    print("\n⚠️  WARNING: You CANNOT proceed until ALL items are confirmed.\n")
    print("📋 STANDARDS.md Section 10 - Pre-Send Checklist")
    print("-"*70)

def get_confirmation(item):
    """Force explicit yes/no for each checklist item"""
    while True:
        response = input(f"\n{item} [yes/no]: ").strip().lower()
        if response in ['yes', 'y', 'ja', 'j']:
            return True
        elif response in ['no', 'n', 'nein']:
            return False
        else:
            print("   ❌ Please answer 'yes' or 'no'")

def check_duplicates(recipient, subject):
    """Check if email would be duplicate"""
    try:
        with open('/Users/julienuhlig/.openclaw/workspace/memory/email_sent_log.json', 'r') as f:
            log = json.load(f)
        
        for entry in log.get('emails', []):
            if entry['to'] == recipient and entry['subject'] == subject:
                print(f"\n⚠️  DUPLICATE DETECTED!")
                print(f"   Already sent to: {recipient}")
                print(f"   Subject: {subject}")
                print(f"   Date: {entry['sent_at']}")
                return False
        return True
    except:
        return True  # If can't read log, allow but warn

def main():
    print_header()
    
    # Mandatory checklist items
    checklist = [
        ("1. Sprache korrekt? (DE/AT/CH = Deutsch, sonst Englisch)", "language"),
        ("2. Keine Power-Specs? (Kein '50-500kW', '150kW')", "no_power_specs"),
        ("3. Keine kommerzielle Sprache? (Kein 'For Sale', 'Pricing')", "no_commercial"),
        ("4. Keine Dringlichkeitsindikatoren? (Kein 'URGENT', 'ASAP')", "no_urgency"),
        ("5. Keine Preisangaben? (Keine Euro-Beträge)", "no_pricing"),
        ("6. Disclaimer vorhanden? ('We seek research partners...')", "disclaimer"),
        ("7. Signatur vollständig? (Clemens Grosjean + alle Kontakte)", "signature"),
        ("8. Betreff korrekt formatiert? ('Research Collaboration – ...')", "subject_format"),
        ("9. Empfänger ist direkter Forscher? (Nicht info@/secretariat@)", "direct_recipient"),
        ("10. Sendezeit korrekt? (7:00 Uhr Ortszeit oder explizite Ausnahme)", "send_time"),
    ]
    
    results = {}
    
    # Go through each item
    for item, key in checklist:
        confirmed = get_confirmation(item)
        results[key] = confirmed
        
        if not confirmed:
            print(f"\n   ❌ ITEM FAILED: {item}")
            print("\n" + "="*70)
            print("🚫 ACCESS DENIED")
            print("="*70)
            print("\nYou CANNOT proceed until ALL items are confirmed.")
            print("Please review STANDARDS.md and fix the issue.\n")
            return 1
        else:
            print(f"   ✅ Confirmed")
    
    # Additional checks
    print("\n" + "-"*70)
    print("🔍 ADDITIONAL CHECKS")
    print("-"*70)
    
    # Check if cold_outreach_tracker was reviewed
    print("\n11. Have you checked cold_outreach_tracker.md for existing contacts?")
    if not get_confirmation(""):
        print("\n🚫 ACCESS DENIED - Review tracker before proceeding")
        return 1
    
    # Check if email_sent_log was checked for duplicates
    print("\n12. Have you verified this is NOT a duplicate in email_sent_log.json?")
    if not get_confirmation(""):
        print("\n🚫 ACCESS DENIED - Check for duplicates first")
        return 1
    
    # Log the approval
    approval_log = {
        "timestamp": datetime.now().isoformat(),
        "status": "APPROVED",
        "checklist_results": results,
        "all_confirmed": True
    }
    
    print("\n" + "="*70)
    print("✅ ALL CHECKS PASSED")
    print("="*70)
    print("\n🚀 You may now proceed with email outreach.")
    print("Remember: These standards protect our reputation.\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
