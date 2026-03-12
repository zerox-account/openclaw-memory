# ZERO-X GROUP WEBSITE DESIGN
## Base44 Platform | API Key: 8e72cea1a5da495b8a54016a261abbc2

---

## PROJECT OVERVIEW

**Entity:** Zero-X Group (Merged: MFC Energy + Zero-X + Partners)
**Partners:** Equation Labs, MFC Germany, Zero-Labs Germany
**Platform:** Base44 (base44.com)
**API Key:** 8e72cea1a5da495b8a54016a261abbc2
**Status:** Design Phase

---

## WEBSITE ARCHITECTURE

### Domain Strategy
**Primary:** zero-x.group (new domain)
**Redirects:**
- mfc-energy.com → zero-x.group/mfc
- zero-x.co → zero-x.group

### Brand Hierarchy

```
ZERO-X GROUP
├── Zero-X Labs (R&D, Technology)
├── MFC Energy GmbH (Operations, Germany)
├── Equation Labs (Partner - Software/AI)
├── MFC Germany (Partner - Local Operations)
└── Zero-Labs Germany (Partner - Research)
```

---

## SITE STRUCTURE

### 1. HOMEPAGE
**URL:** /

**Sections:**
1. **Hero Section**
   - Headline: "Transforming Waste into Clean Energy"
   - Subheadline: "Zero-X Group: Advanced Gasification Technology for a Sustainable Future"
   - CTA: "Explore Our Technology" | "Partner With Us"
   - Background: X-150 system video/image

2. **Partner Ecosystem**
   - Grid of 5 partner logos
   - Zero-X Labs | MFC Energy | Equation Labs | MFC Germany | Zero-Labs Germany
   - Brief tagline per partner

3. **Technology Showcase**
   - X-150 Container System
   - Cométha Project results (1000+ hours)
   - Verkozo SOFC integration
   - Visual: Technical diagrams

4. **Latest Blog Posts**
   - Dynamic feed (3 most recent)
   - Categories: Research, Projects, Partnerships

5. **Newsletter Signup**
   - "Stay updated on Zero-X developments"
   - Email capture

### 2. ABOUT / GROUP STRUCTURE
**URL:** /about

**Content:**
- Group overview
- Partner descriptions
- Organizational chart
- History timeline (MFC → Zero-X merger)
- Leadership team

### 3. TECHNOLOGY
**URL:** /technology

**Subpages:**
- /technology/x-150 (Detailed X-150 specs)
- /technology/cometha (Project results)
- /technology/verkozo (SOFC integration)
- /technology/process (How it works - visual)

**Content:**
- Technical specifications
- Process diagrams
- Performance data
- Validation results

### 4. PARTNERS
**URL:** /partners

**Sections per Partner:**

**Zero-X Labs:**
- R&D focus
- Technology development
- Research partnerships

**MFC Energy GmbH:**
- Operations
- Commercial deployment
- Contact: Spinlab Leipzig

**Equation Labs:**
- Software development
- AI integration
- Digital solutions

**MFC Germany:**
- Local operations
- Market presence
- German market focus

**Zero-Labs Germany:**
- Research collaboration
- Academic partnerships
- Innovation focus

### 5. BLOG
**URL:** /blog

**Categories:**
- Research Updates (Cométha, Verkozo)
- Partnership News
- Technology Insights
- Industry Commentary
- Events & Conferences

**Features:**
- Daily updates (as requested)
- Category filtering
- Author profiles
- Social sharing
- RSS feed

### 6. PROJECTS
**URL:** /projects

**Featured Projects:**
- Cométha (Paris, 1000+ hours)
- Verkozo (Fraunhofer IKTS)
- X-150 Development
- Future: Golden Foods, Neom

**Format:**
- Project cards
- Status indicators
- Technical data
- Partner logos

### 7. RESEARCH / COLLABORATION
**URL:** /research

**Content:**
- Open collaboration opportunities
- Horizon Europe focus
- Academic partnerships
- Research publications
- Contact form for researchers

### 8. CONTACT
**URL:** /contact

**Sections:**
- General inquiry form
- Partner-specific contacts
- Map (Spinlab Leipzig)
- Phone: +49 341 92881290
- Email: zerox@exventure.co

---

## DESIGN SPECIFICATIONS

### Visual Identity

**Colors:**
- Primary: #0066CC (Blue - Trust, Technology)
- Secondary: #00AA44 (Green - Sustainability, Energy)
- Accent: #FF6600 (Orange - Innovation, Warmth)
- Dark: #1A1A2E (Deep blue-black - Professional)
- Light: #F5F5F5 (Clean background)

**Typography:**
- Headlines: Montserrat Bold
- Body: Open Sans Regular
- Technical: Roboto Mono (for specs)

**Imagery:**
- X-150 container shots
- Industrial settings
- Clean energy visuals
- Team photos
- Technical diagrams

### Layout Principles
- Clean, scientific aesthetic
- Mobile-first responsive
- Fast loading (<3 seconds)
- Accessibility compliant
- Multilingual ready (DE/EN)

---

## TECHNICAL IMPLEMENTATION

### Base44 Configuration
```javascript
const base44 = createClient({
  apiKey: '8e72cea1a5da495b8a54016a261abbc2',
  project: 'zero-x-website'
});
```

### Required Features
1. **Blog System**
   - Daily update capability
   - Markdown support
   - Image uploads
   - Category management

2. **Contact Forms**
   - Multi-recipient routing
   - Spam protection
   - Auto-responses

3. **Analytics**
   - Visitor tracking
   - Blog engagement
   - Contact form conversions

4. **SEO**
   - Meta tags per page
   - Sitemap generation
   - Schema markup

### Integrations
- Email: zerox@exventure.co
- Social: LinkedIn, Twitter (X)
- Newsletter: Mailchimp/ConvertKit
- Analytics: Google Analytics 4

---

## CONTENT STRATEGY

### Blog Update Schedule
**Daily updates by:**
- Research progress
- Partnership announcements
- Industry insights
- Event coverage

**Responsible:** Clemens Grosjean (Zero-X)

### Content Pillars
1. **Technology** (40%) - X-150, processes, innovations
2. **Research** (30%) - Cométha, Verkozo, academic collabs
3. **Partnerships** (20%) - New partners, joint projects
4. **Industry** (10%) - Market trends, policy updates

---

## LAUNCH PLAN

### Phase 1: Foundation (Week 1)
- [ ] Base44 project setup
- [ ] Homepage design
- [ ] About page
- [ ] Contact page

### Phase 2: Content (Week 2)
- [ ] Technology pages
- [ ] Partner pages
- [ ] Initial blog posts (5)

### Phase 3: Features (Week 3)
- [ ] Blog system live
- [ ] Newsletter integration
- [ ] Analytics setup

### Phase 4: Launch (Week 4)
- [ ] Domain configuration
- [ ] Redirects (mfc-energy.com, zero-x.co)
- [ ] SEO optimization
- [ ] Soft launch

---

## SUCCESS METRICS

**Traffic:**
- 1000+ monthly visitors (Month 1)
- 5000+ monthly visitors (Month 6)

**Engagement:**
- Blog: 3+ posts/week
- Newsletter: 100+ subscribers (Month 3)
- Contact forms: 5+ inquiries/month

**Partnerships:**
- Track research collaboration leads
- Monitor Horizon Europe opportunities

---

## IMMEDIATE NEXT STEPS

1. **Create Base44 Project**
   - Initialize with API key
   - Set up development environment

2. **Design Homepage Mockup**
   - Hero section
   - Partner grid
   - Technology preview

3. **Content Collection**
   - X-150 photos/videos
   - Partner logos
   - Team photos
   - Technical diagrams

4. **Domain Setup**
   - Register zero-x.group
   - Configure redirects
   - Set up DNS

**Ready to proceed with Base44 development?**
