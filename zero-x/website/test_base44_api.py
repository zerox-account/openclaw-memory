import requests
import json

API_KEY = "8e72cea1a5da495b8a54016a261abbc2"
APP_ID = "6989df145d41eebf80a51614"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Test different endpoints
endpoints = [
    f"https://api.base44.com/v1/apps/{APP_ID}",
    f"https://api.base44.com/api/apps/{APP_ID}",
    f"https://app.base44.com/api/apps/{APP_ID}",
    f"https://api.base44.com/v1/projects/{APP_ID}",
    f"https://api.base44.com/v1/entities?appId={APP_ID}",
]

print("=== TESTE BASE44 ENDPOINTS ===\n")

for url in endpoints:
    try:
        print(f"Testing: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print(f"✅ SUCCESS!")
            print(json.dumps(response.json(), indent=2)[:500])
            break
        else:
            print(f"Response: {response.text[:200]}\n")
    except Exception as e:
        print(f"Error: {e}\n")

# Try to list all accessible apps
print("\n=== VERSUCHE APPS ZU LISTEN ===")
try:
    url = "https://api.base44.com/v1/apps"
    response = requests.get(url, headers=headers, timeout=10)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=2)[:1000])
except Exception as e:
    print(f"Error: {e}")
