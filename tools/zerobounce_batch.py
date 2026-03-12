#!/usr/bin/env python3
"""
ZeroBounce Batch Email Validation Tool
Validates multiple emails before sending outreach campaigns

Usage:
  export ZEROBOUNCE_API_KEY="your-key"
  python3 zerobounce_batch.py --file emails.txt
  python3 zerobounce_batch.py --researchers researcher_db.json
  python3 zerobounce_batch.py --check "email1@example.com,email2@example.com"
"""

import sys
import os
import json
import requests
import time
from datetime import datetime

API_KEY = os.environ.get("ZEROBOUNCE_API_KEY", "")
API_URL = "https://api.zerobounce.net/v2/validate"

def validate_email(email):
    """Validate a single email address"""
    if not API_KEY:
        print("❌ Error: ZEROBOUNCE_API_KEY not set")
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
            print(f"❌ API Error {response.status_code} for {email}: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Error validating {email}: {e}")
        return None

def validate_from_file(filepath):
    """Validate emails from a text file (one per line)"""
    try:
        with open(filepath, 'r') as f:
            emails = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return None
    
    return validate_list(emails)

def validate_list(emails):
    """Validate a list of emails"""
    results = {
        "timestamp": datetime.now().isoformat(),
        "total": len(emails),
        "valid": [],
        "invalid": [],
        "catch_all": [],
        "unknown": [],
        "spamtrap": [],
        "errors": []
    }
    
    print(f"\n🔍 Validating {len(emails)} email addresses...")
    print("=" * 60)
    
    for i, email in enumerate(emails, 1):
        print(f"\n[{i}/{len(emails)}] {email} ...", end=" ", flush=True)
        
        result = validate_email(email)
        
        if result:
            status = result.get('status', 'unknown')
            sub_status = result.get('sub_status', '')
            
            entry = {
                "email": email,
                "status": status,
                "sub_status": sub_status,
                "firstname": result.get('firstname'),
                "lastname": result.get('lastname'),
                "full_result": result
            }
            
            if status == "valid":
                results["valid"].append(entry)
                print("✅ VALID", end="")
                if entry["firstname"] and entry["lastname"]:
                    print(f" ({entry['firstname']} {entry['lastname']})")
                else:
                    print()
            elif status == "invalid":
                results["invalid"].append(entry)
                print(f"❌ INVALID ({sub_status})")
            elif status == "catch-all":
                results["catch_all"].append(entry)
                print(f"⚠️  CATCH-ALL")
            elif status == "unknown":
                results["unknown"].append(entry)
                print(f"❓ UNKNOWN")
            elif status == "spamtrap":
                results["spamtrap"].append(entry)
                print(f"🚫 SPAMTRAP!")
            else:
                results["errors"].append(entry)
                print(f"❓ UNEXPECTED STATUS: {status}")
        else:
            results["errors"].append({"email": email, "error": "API call failed"})
            print("❌ ERROR")
        
        # Rate limiting - be nice to the API
        time.sleep(0.5)
    
    return results

def print_summary(results):
    """Print validation summary"""
    print("\n" + "=" * 60)
    print("📊 VALIDATION SUMMARY")
    print("=" * 60)
    print(f"Total checked:    {results['total']}")
    print(f"✅ Valid:         {len(results['valid'])} ({len(results['valid'])/results['total']*100:.1f}%)")
    print(f"❌ Invalid:       {len(results['invalid'])} ({len(results['invalid'])/results['total']*100:.1f}%)")
    print(f"⚠️  Catch-all:     {len(results['catch_all'])} ({len(results['catch_all'])/results['total']*100:.1f}%)")
    print(f"❓ Unknown:       {len(results['unknown'])} ({len(results['unknown'])/results['total']*100:.1f}%)")
    print(f"🚫 Spamtrap:      {len(results['spamtrap'])} ({len(results['spamtrap'])/results['total']*100:.1f}%)")
    print(f"❌ Errors:        {len(results['errors'])} ({len(results['errors'])/results['total']*100:.1f}%)")
    print("=" * 60)
    
    # Safe to send
    safe_count = len(results['valid']) + len(results['catch_all']) + len(results['unknown'])
    print(f"\n📧 Safe to send: {safe_count} emails")
    print(f"🚫 DO NOT SEND:  {len(results['invalid']) + len(results['spamtrap'])} emails")
    
    # Show invalid emails
    if results['invalid']:
        print("\n" + "-" * 60)
        print("❌ INVALID EMAILS (Remove from list):")
        print("-" * 60)
        for entry in results['invalid']:
            print(f"  • {entry['email']} ({entry['sub_status']})")
    
    # Show valid emails with names
    if results['valid']:
        print("\n" + "-" * 60)
        print("✅ VALID EMAILS (Safe to send):")
        print("-" * 60)
        for entry in results['valid']:
            name = f"{entry['firstname'] or ''} {entry['lastname'] or ''}".strip()
            print(f"  • {entry['email']}" + (f" ({name})" if name else ""))

def save_results(results, output_file="/tmp/validation_results.json"):
    """Save results to JSON file"""
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n💾 Results saved to: {output_file}")
    
    # Also save valid emails to a clean list
    valid_file = output_file.replace('.json', '_valid.txt')
    with open(valid_file, 'w') as f:
        for entry in results['valid']:
            f.write(entry['email'] + '\n')
    print(f"💾 Valid emails saved to: {valid_file}")
    
    # Save invalid emails
    if results['invalid']:
        invalid_file = output_file.replace('.json', '_invalid.txt')
        with open(invalid_file, 'w') as f:
            for entry in results['invalid']:
                f.write(f"{entry['email']} ({entry['sub_status']})\n")
        print(f"💾 Invalid emails saved to: {invalid_file}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Batch email validation with ZeroBounce')
    parser.add_argument('--file', '-f', help='Text file with emails (one per line)')
    parser.add_argument('--check', '-c', help='Comma-separated list of emails')
    parser.add_argument('--output', '-o', default='/tmp/validation_results.json', help='Output file')
    args = parser.parse_args()
    
    if not API_KEY:
        print("❌ Error: ZEROBOUNCE_API_KEY environment variable not set")
        print("Set it with: export ZEROBOUNCE_API_KEY='your-api-key'")
        sys.exit(1)
    
    emails = []
    
    if args.file:
        try:
            with open(args.file, 'r') as f:
                emails = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        except FileNotFoundError:
            print(f"❌ File not found: {args.file}")
            sys.exit(1)
    elif args.check:
        emails = [e.strip() for e in args.check.split(',')]
    else:
        # Demo mode - test some known emails
        print("📝 No input provided. Running demo with test emails...")
        print("Usage: python3 zerobounce_batch.py --file emails.txt")
        print("       python3 zerobounce_batch.py --check 'email1@example.com,email2@example.com'")
        print()
        emails = [
            "remi.costa@dlr.de",
            "andreas.friedrich@dlr.de",
            "k.yoshikawa@aist.go.jp",
            "herman.reizer@tudelft.nl",
            "sandra.hermle@bfe.admin.ch"
        ]
    
    if not emails:
        print("❌ No emails to validate")
        sys.exit(1)
    
    results = validate_list(emails)
    print_summary(results)
    save_results(results, args.output)

if __name__ == "__main__":
    main()
