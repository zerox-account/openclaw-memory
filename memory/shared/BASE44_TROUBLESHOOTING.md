# BASE44 API TROUBLESHOOTING GUIDE
## For All Agents | Zero-X Global Control Center

---

## API CREDENTIALS

```json
{
  "api_key": "8e72cea1a5da495b8a54016a261abbc2",
  "service": "AI Website/App Builder",
  "website": "https://base44.com",
  "docs": "https://docs.base44.com",
  "sdk_path": "~/.openclaw/workspace/node_modules/@base44/sdk",
  "test_script": "~/.openclaw/workspace/node_modules/openclaw/scripts/test-base44.js"
}
```

---

## COMMON ERRORS & SOLUTIONS

### Error 1: "Module not found" / SDK Path Issues

**Symptom:**
```
Error: Cannot find module '@base44/sdk'
or
Error: Cannot find module '/Users/.../.openclaw/workspace/node_modules/@base44/sdk'
```

**Causes:**
- SDK not installed
- Wrong path
- Node modules corrupted

**Solutions:**

**Option A: Install SDK**
```bash
cd ~/.openclaw/workspace
npm install @base44/sdk
```

**Option B: Use Absolute Path**
```javascript
const { createClient } = require('/Users/julienuhlig/.openclaw/workspace/node_modules/@base44/sdk');
```

**Option C: Check if exists**
```bash
ls -la ~/.openclaw/workspace/node_modules/@base44/
```
If missing:
```bash
mkdir -p ~/.openclaw/workspace/node_modules/@base44
cd ~/.openclaw/workspace/node_modules/@base44
npm init -y
npm install @base44/sdk
```

---

### Error 2: "Invalid API Key" / Authentication Failed

**Symptom:**
```
Error: 401 Unauthorized
Error: Invalid API key
```

**Causes:**
- Wrong API key
- Key not passed correctly
- Account issues

**Solutions:**

**Verify Key:**
```javascript
const API_KEY = '8e72cea1a5da495b8a54016a261abbc2';
console.log('Key length:', API_KEY.length); // Should be 32
```

**Correct Usage:**
```javascript
const base44 = createClient({
  apiKey: '8e72cea1a5da495b8a54016a261abbc2'
});
```

**Test Script:**
```bash
node ~/.openclaw/workspace/node_modules/openclaw/scripts/test-base44.js
```

**Check Account Status:**
- Visit: https://base44.com
- Login and verify API key is active
- Check billing status

---

### Error 3: "Entity not found" / Project Issues

**Symptom:**
```
Error: Entity 'YourEntity' not found
Error: Project not found
```

**Causes:**
- Wrong entity name
- Project not initialized
- Case sensitivity

**Solutions:**

**List Available Entities:**
```javascript
const entities = await base44.entities.list();
console.log(entities);
```

**Correct Entity Access:**
```javascript
// Wrong
const data = await base44.entities.yourentity.list();

// Right
const data = await base44.entities.YourEntity.list();
```

**Initialize Project First:**
```javascript
await base44.projects.create({
  name: 'zero-x-website',
  description: 'Zero-X Group Website'
});
```

---

### Error 4: Network / Connection Errors

**Symptom:**
```
Error: ETIMEDOUT
Error: ECONNREFUSED
Error: Network error
```

**Causes:**
- Internet connectivity
- Base44 service down
- Firewall/proxy

**Solutions:**

**Check Base44 Status:**
```bash
curl -I https://base44.com
```

**Test Connection:**
```javascript
const https = require('https');
https.get('https://base44.com', (res) => {
  console.log('Status:', res.statusCode);
});
```

**Retry Logic:**
```javascript
async function withRetry(fn, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      return await fn();
    } catch (err) {
      if (i === retries - 1) throw err;
      await new Promise(r => setTimeout(r, 1000 * (i + 1)));
    }
  }
}
```

---

### Error 5: Rate Limiting / Quota Exceeded

**Symptom:**
```
Error: 429 Too Many Requests
Error: Quota exceeded
```

**Solutions:**

**Check Rate Limits:**
- Default: 100 requests/minute
- Upgrade plan if needed

**Implement Throttling:**
```javascript
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));

async function throttledRequests(requests) {
  const results = [];
  for (const req of requests) {
    results.push(await req());
    await delay(100); // 100ms between requests
  }
  return results;
}
```

**Monitor Usage:**
```javascript
const usage = await base44.account.usage();
console.log('Remaining:', usage.remaining);
```

---

## TESTING PROCEDURES

### Test 1: SDK Installation
```bash
cd ~/.openclaw/workspace
node -e "console.log(require.resolve('@base44/sdk'))"
```
**Expected:** Path to SDK

### Test 2: API Key Validity
```javascript
const { createClient } = require('/Users/julienuhlig/.openclaw/workspace/node_modules/@base44/sdk');

const base44 = createClient({
  apiKey: '8e72cea1a5da495b8a54016a261abbc2'
});

base44.account.info()
  .then(info => console.log('✅ API Key valid:', info))
  .catch(err => console.log('❌ API Key invalid:', err.message));
```

### Test 3: Create Test Entity
```javascript
(async () => {
  try {
    const test = await base44.entities.create({
      name: 'TestEntity',
      fields: {
        name: { type: 'text' },
        status: { type: 'text' }
      }
    });
    console.log('✅ Entity created:', test);
  } catch (err) {
    console.log('❌ Error:', err.message);
  }
})();
```

### Test 4: Full Workflow
```bash
node ~/.openclaw/workspace/node_modules/openclaw/scripts/test-base44.js
```

---

## DEBUGGING TIPS

### Enable Debug Mode
```javascript
const base44 = createClient({
  apiKey: '8e72cea1a5da495b8a54016a261abbc2',
  debug: true // Enable verbose logging
});
```

### Check Environment
```bash
node --version  # Should be v16+
npm --version   # Should be v7+
which node
```

### Verify File Paths
```bash
echo $OPENCLAW_WORKSPACE
ls -la ~/.openclaw/workspace/node_modules/@base44/sdk/dist/
```

### Clear Cache
```bash
rm -rf ~/.openclaw/workspace/node_modules/.cache
npm cache clean --force
```

---

## WORKAROUNDS

### Workaround 1: REST API Direct
If SDK fails, use REST directly:
```bash
curl -X GET \
  https://api.base44.com/v1/entities \
  -H 'Authorization: Bearer 8e72cea1a5da495b8a54016a261abbc2'
```

### Workaround 2: Local Development Mode
```javascript
const base44 = createClient({
  apiKey: '8e72cea1a5da495b8a54016a261abbc2',
  endpoint: 'https://api.base44.com',
  timeout: 30000 // Increase timeout
});
```

### Workaround 3: Fallback to Web Interface
If API completely down:
- https://base44.com
- Manual website builder
- Export and host separately

---

## EMERGENCY CONTACTS

**Base44 Support:**
- Docs: https://docs.base44.com
- Status: https://status.base44.com
- Email: support@base44.com

**Internal:**
- Master Agent: julienagent@exventure.co
- Zero-X: zerox@exventure.co

---

## QUICK REFERENCE CARD

```javascript
// Quick Test
const { createClient } = require('/Users/julienuhlig/.openclaw/workspace/node_modules/@base44/sdk');
const base44 = createClient({ apiKey: '8e72cea1a5da495b8a54016a261abbc2' });
base44.entities.list().then(console.log).catch(console.error);

// Quick Fix Commands
npm install @base44/sdk --prefix ~/.openclaw/workspace
node -e "require('@base44/sdk')"
curl -H 'Authorization: Bearer 8e72cea1a5da495b8a54016a261abbc2' https://api.base44.com/v1/account
```

---

**Last Updated:** 2026-02-09  
**Author:** Zero-X Global Control Center  
**Status:** Ready for distribution to all agents
