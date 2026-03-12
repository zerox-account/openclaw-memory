#!/usr/bin/env python3
"""
ZeroBounce Email Validation Tool - Direct API Version
Usage: ZEROBOUNCE_API_KEY="your-key" python3 zerobounce_check.py <email>
"""

import sys
import os
import requests
import json

API_KEY = os.environ.get("ZEROBOUNCE_API_KEY", "")
API_URL = "https://api.zerobounce.net/v2/validate"

def validate_email(email):
    """Validate a single email address using ZeroBounce API v2"""
    if not API_KEY:
        print("❌ Error: ZEROBOUNCE_API_KEY not set")
        print("Set it with: export ZEROBOUNCE_API_KEY='your-api-key'")
        return None
    
    params = {
        "api_key": API_KEY,
        "email": email,
        "ip_address": ""  # Optional
    }
    
    try:
        response = requests.get(API_URL, params=params, timeout=30)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ API Error: {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: ZEROBOUNCE_API_KEY='key' python3 zerobounce_check.py <email>")
        print("Example: ZEROBOUNCE_API_KEY='key' python3 zerobounce_check.py test@example.com")
        sys.exit(1)
    
    email = sys.argv[1]
    print(f"🔍 Validating: {email}")
    print("-" * 50)
    
    result = validate_email(email)
    
    if result:
        print(f"✅ Status: {result.get('status', 'Unknown')}")
        print(f"📧 Sub-status: {result.get('sub_status', 'N/A')}")
        print(f"📊 Confidence: {result.get('confidence', 'N/A')}")
        if result.get('did_you_mean'):
            print(f"💡 Did you mean: {result['did_you_mean']}")
        print(f"📝 Full response:")
        print(json.dumps(result, indent=2))
    else:
        print("❌ Validation failed")

if __name__ == "__main__":
    main()
