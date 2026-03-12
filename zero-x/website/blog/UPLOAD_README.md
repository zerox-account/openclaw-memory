# BLOG POSTS UPLOAD PACKAGE
## Ready for Base44 API
## Project: 6989df145d41eebf80a51614

---

## 📁 FILES READY

### JSON Format (for API upload)
- `post1-german-research.json` - 21 German Research Institutions Join Zero-X Network
- `post2-cometha.json` - Cométha Project: 1,000 Hours of Validated Performance  
- `post3-verkoso.json` - Verkoso: SOFC Integration Progress Update

### Markdown Format (for manual entry)
- `BLOG_POSTS_CONTENT.md` - All 6 posts with full content

---

## 📝 POSTS SUMMARY

| # | Title | Category | Date | Status |
|---|-------|----------|------|--------|
| 1 | 21 German Research Institutions Join Zero-X Network | Partnerships | 2026-02-09 | Published |
| 2 | Cométha Project: 1,000 Hours of Validated Performance | Projects | 2026-01-15 | Published |
| 3 | Verkoso: SOFC Integration Progress Update | Technology | 2025-12-20 | Published |
| 4 | X-150 Modular Gasification System: Technical Specifications | Technology | 2025-11-10 | Published |
| 5 | Partner Spotlight: Equation Labs | Partners | 2025-10-05 | Published |
| 6 | Horizon Europe: Collaboration Opportunities | Research | 2025-09-15 | Published |

---

## 🔌 API ENDPOINT (when deployed)

**Method:** POST
**URL:** https://base44.app/api/apps/6989df145d41eebf80a51614/entities/BlogPost
**Headers:**
```
Authorization: Bearer 8e72cea1a5da495b8a54016a261abbc2
Content-Type: application/json
```

**Body:** (see JSON files)

---

## 📤 UPLOAD COMMANDS

### Option 1: cURL (once API is live)
```bash
for post in *.json; do
  curl -X POST \
    https://base44.app/api/apps/6989df145d41eebf80a51614/entities/BlogPost \
    -H "Authorization: Bearer 8e72cea1a5da495b8a54016a261abbc2" \
    -H "Content-Type: application/json" \
    -d @$post
  echo "Uploaded: $post"
done
```

### Option 2: SDK (once deployed)
```javascript
const { createClient } = require('@base44/sdk');
const client = createClient({ 
  apiKey: '8e72cea1a5da495b8a54016a261abbc2',
  appId: '6989df145d41eebf80a51614'
});

const posts = require('./post1-german-research.json');
client.entities.BlogPost.create(posts);
```

### Option 3: Manual Entry
Copy content from BLOG_POSTS_CONTENT.md into Base44 editor

---

## ✅ READY FOR UPLOAD

All content prepared. Waiting for API deployment confirmation.

**Last Updated:** 2026-02-09 05:47 CET
**Prepared by:** Zero-X Global Control Center
