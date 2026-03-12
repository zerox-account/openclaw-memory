import urllib.request
import urllib.error
import json
import ssl

API_KEY = "19621a22993648559924d3398466764c"
APP_ID = "6989df145d41eebf80a51614"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Test different auth methods
auth_methods = [
    ("Bearer Token", {"Authorization": f"Bearer {API_KEY}"}),
    ("X-API-Key", {"X-API-Key": API_KEY}),
    ("api_key header", {"api-key": API_KEY}),
    ("App-ID + Key", {"X-App-ID": APP_ID, "X-API-Key": API_KEY}),
]

url = f"https://app.base44.com/api/apps/{APP_ID}"

print("=== TESTE VERSCHIEDENE AUTH METHODEN ===\n")

for method_name, headers in auth_methods:
    try:
        print(f"Testing: {method_name}")
        headers["Content-Type"] = "application/json"
        headers["User-Agent"] = "Mozilla/5.0"
        
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req, context=ctx, timeout=10)
        data = response.read().decode('utf-8')
        print(f"✅ ERFOLG! Status: {response.status}")
        print(f"Response: {data[:500]}")
        print(f"\n🎉 AUTH METHODE GEFUNDEN: {method_name}")
        break
    except urllib.error.HTTPError as e:
        print(f"❌ {method_name}: HTTP {e.code}\n")
    except Exception as e:
        print(f"❌ {method_name}: {e}\n")

# Try POST to update content
print("\n=== VERSUCHE CONTENT UPDATE ===")
update_headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

content_data = {
    "title": "Zero-X Group - Waste to Energy",
    "description": "Transforming waste into clean energy with modular gasification systems"
}

try:
    update_url = f"https://app.base44.com/api/apps/{APP_ID}/content"
    req = urllib.request.Request(
        update_url,
        data=json.dumps(content_data).encode('utf-8'),
        headers=update_headers,
        method='POST'
    )
    response = urllib.request.urlopen(req, context=ctx, timeout=10)
    print(f"✅ Update erfolgreich: {response.status}")
except urllib.error.HTTPError as e:
    print(f"❌ Update fehlgeschlagen: {e.code}")
    print(f"Response: {e.read().decode('utf-8')[:300]}")
except Exception as e:
    print(f"❌ Error: {e}")
