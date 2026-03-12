import urllib.request
import urllib.error
import json
import ssl

API_KEY = "19621a22993648559924d3398466764c"
APP_ID = "6989df145d41eebf80a51614"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

endpoints = [
    f"https://app.base44.com/api/apps/{APP_ID}",
    f"https://app.base44.com/api/apps/{APP_ID}/content",
    f"https://api.base44.com/v1/apps/{APP_ID}",
]

print("=== TESTE NEUEN API KEY ===\n")

for url in endpoints:
    try:
        print(f"Testing: {url}")
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req, context=ctx, timeout=10)
        data = response.read().decode('utf-8')
        print(f"✅ Status: {response.status}")
        print(f"Response: {json.dumps(json.loads(data), indent=2)[:1000]}")
        print("\n🎉 ERFOLG! API Key funktioniert!")
        break
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error: {e.code}")
        print(f"Response: {e.read().decode('utf-8')[:300]}\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")
