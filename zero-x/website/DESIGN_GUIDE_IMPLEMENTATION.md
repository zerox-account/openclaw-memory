# ZERO-X GROUP WEBSITE - DESIGN GUIDE IMPLEMENTATION
## Base44 Project: 6989df145d41eebf80a51614
## Design System v2.0 - Dark Mode First

---

## COLOR SYSTEM

### Primary Palette
| Color | Hex | Usage |
|-------|-----|-------|
| **Carbon Black** | `#0A0A0A` | Primary backgrounds, hero sections |
| **Zero-X Green** | `#00D26A` | Primary accent, CTAs, highlights |
| **Syngas Orange** | `#FF6B35` | Secondary accent, warnings, energy |
| **Platinum** | `#F5F5F7` | Primary text on dark backgrounds |

### Neutral Scale
| Name | Hex | Usage |
|------|-----|-------|
| **White** | `#FFFFFF` | Headlines, icons |
| **Gray 100** | `#E5E5E7` | Body text |
| **Gray 200** | `#C5C5C7` | Secondary text |
| **Gray 300** | `#86868B` | Muted text, captions |
| **Gray 400** | `#424245` | Borders, dividers |
| **Gray 500** | `#1D1D1F` | Card backgrounds |
| **Carbon Black** | `#0A0A0A` | Page backgrounds |

### Gradients
- **Hero Gradient:** `linear-gradient(135deg, #0A0A0A 0%, #1D1D1F 50%, #0A0A0A 100%)`
- **Green Glow:** `radial-gradient(circle, rgba(0,210,106,0.15) 0%, transparent 70%)`
- **Orange Accent:** `linear-gradient(90deg, #FF6B35 0%, #FF8F5A 100%)`
- **Text Gradient:** `linear-gradient(135deg, #FFFFFF 0%, #00D26A 100%)`

---

## TYPOGRAPHY

### Font Families
- **Primary:** Inter (Google Fonts)
- **Technical/Monospace:** JetBrains Mono

### Type Scale

| Style | Size | Weight | Line Height | Letter Spacing | Usage |
|-------|------|--------|-------------|----------------|-------|
| **Hero** | 72px | 800 | 1.1 | -2px | Main headlines |
| **H1** | 56px | 700 | 1.2 | -1px | Page titles |
| **H2** | 42px | 700 | 1.2 | -0.5px | Section headers |
| **H3** | 32px | 600 | 1.3 | 0 | Subsection titles |
| **H4** | 24px | 600 | 1.4 | 0 | Card titles |
| **H5** | 20px | 600 | 1.4 | 0 | Small headers |
| **Body Large** | 20px | 400 | 1.6 | 0 | Lead paragraphs |
| **Body** | 16px | 400 | 1.6 | 0 | Standard text |
| **Body Small** | 14px | 400 | 1.5 | 0 | Captions, metadata |
| **Label** | 12px | 600 | 1.4 | 1px | Tags, labels (uppercase) |
| **Data** | 16px | 500 | 1.4 | 0 | Stats, numbers (JetBrains Mono) |

---

## LAYOUT PRINCIPLES

### Grid System
- **12-column grid**
- **Gutter:** 24px (desktop), 16px (mobile)
- **Max Widths:**
  - Content: 1200px
  - Full-width sections: 1440px
  - Text blocks: 720px (optimal reading)

### Spacing Scale
```
4px   - xs (tight gaps)
8px   - sm (element spacing)
16px  - md (component padding)
24px  - lg (section gaps)
32px  - xl (card padding)
48px  - 2xl (section breaks)
64px  - 3xl (major sections)
96px  - 4xl (hero spacing)
128px - 5xl (page breaks)
```

### Responsive Breakpoints
| Breakpoint | Width | Usage |
|------------|-------|-------|
| **Mobile** | < 640px | Single column, stacked |
| **Tablet** | 640-1024px | 2 columns, adjusted spacing |
| **Desktop** | 1024-1440px | Full layout |
| **Large** | > 1440px | Max-width containers |

---

## COMPONENTS

### Buttons

**Primary Button (Zero-X Green)**
```
Background: #00D26A
Text: #0A0A0A
Padding: 16px 32px
Border-radius: 8px
Font: 16px, weight 600
Hover: brightness(1.1), translateY(-2px)
Transition: all 300ms ease
```

**Secondary Button (Outline)**
```
Background: transparent
Border: 2px solid #00D26A
Text: #00D26A
Padding: 14px 30px
Border-radius: 8px
Hover: background #00D26A, text #0A0A0A
```

**Ghost Button**
```
Background: transparent
Text: #F5F5F7
Padding: 12px 24px
Hover: background rgba(255,255,255,0.1)
```

### Cards

**Feature Card**
```
Background: #1D1D1F
Border-radius: 16px
Padding: 32px
Border: 1px solid #424245
Hover: border-color #00D26A, translateY(-4px)
Box-shadow: 0 4px 24px rgba(0,0,0,0.3)
```

**Project Card**
```
Background: #1D1D1F
Border-radius: 12px
Overflow: hidden
Image: aspect-ratio 16/9
Content padding: 24px
```

**Stats Card**
```
Background: transparent
Border-left: 3px solid #00D26A
Padding-left: 24px
Number: JetBrains Mono, 48px, #00D26A
Label: 14px, #86868B, uppercase
```

### Navigation

**Header (Fixed)**
```
Position: fixed
Background: rgba(10,10,10,0.9)
Backdrop-filter: blur(20px)
Border-bottom: 1px solid #424245
Height: 80px
Z-index: 1000
```

**Nav Links**
```
Color: #C5C5C7
Font: 14px, weight 500
Hover: #00D26A
Active: #00D26A with underline
```

---

## SECTIONS SPECIFICATIONS

### 1. HERO SECTION (100vh)

**Layout:**
- Full viewport height
- Centered content
- Background: Carbon Black with gradient overlay
- Floating green glow elements (decorative)

**Content:**
```
Label: "WASTE TO ENERGY" (12px, uppercase, #00D26A)
Headline: "Transforming Waste into Clean Energy" (72px, white)
Subheadline: "Zero-X Group: Advanced modular gasification systems." (20px, gray-200)
CTAs: [Explore Technology] [Partner With Us]
Stats Bar: 4 stats at bottom
```

**Visual Elements:**
- X-150 container image (right side, 60% opacity)
- Animated particles (subtle, green)
- Gradient overlay: bottom fade to black

### 2. STATS BAR

**Layout:**
- Horizontal flex, space-between
- Background: #1D1D1F
- Padding: 48px 0
- Border-top: 1px solid #424245

**Stats:**
```
1,000+     86%        ~650kW      Multi-fuel
Operating  Thermal    Power       Capable
Hours      Efficiency Output
```

### 3. TECHNOLOGY OVERVIEW

**Layout:**
- Two-column grid (image left, content right)
- Background: Carbon Black
- Padding: 128px 0

**Content:**
```
Section Label: "THE TECHNOLOGY" (#00D26A, uppercase)
Headline: "The X-150 System" (56px)
Subheadline: "Containerized. Modular. Validated." (24px, gray-300)

Features Grid (3x2):
- Containerized Design
- Downdraft Gasification
- Multi-Fuel Capability
- Oxy-Steam Process
- High Efficiency
- Proven Performance

Specs Table:
| Spec | Value |
|------|-------|
| System Type | X-150 Modular Gasifier |
| Configuration | 20ft Containerized |
| Efficiency | 86% |
| Output | ~650kW |
```

### 4. FEATURED PROJECTS

**Layout:**
- Background: #1D1D1F
- Padding: 128px 0
- 3-column grid

**Section Header:**
```
Label: "VALIDATED PROJECTS"
Headline: "Real-World Performance"
Subheadline: "Proven in industrial environments"
```

**Project Cards:**
1. **Cométha** - Paris, 1,000+ hours, ✅ Completed
2. **Verkoso** - Dresden, SOFC integration, 🔄 Active
3. **MINEBASE** - Africa, Mining diesel replacement, 🔄 Active

### 5. IMPACT SECTION

**Layout:**
- Full-width background image
- Overlay: gradient from transparent to Carbon Black
- Centered content
- Padding: 160px 0

**Content:**
```
Headline: "2.8M Tonnes CO₂"
Subheadline: "Potential annual reduction with full deployment"

3-Column Impact Grid:
- Environmental (icon: Leaf)
- Economic (icon: TrendingUp)
- Social (icon: Users)
```

### 6. PARTNERS

**Layout:**
- Background: Carbon Black
- Padding: 96px 0
- Logo grid (5 columns)

**Content:**
```
Label: "THE ECOSYSTEM"
Headline: "Powered by Partnership"

Partner Logos:
- Zero-X Labs
- MFC Energy
- Equation Labs
- MFC Germany
- Zero-Labs Germany
```

### 7. NEWS/INSIGHTS

**Layout:**
- Background: #1D1D1F
- Padding: 128px 0
- 3-column blog grid

**Content:**
```
Label: "LATEST UPDATES"
Headline: "News & Insights"

3 Blog Cards:
1. German Research Outreach (Feb 9)
2. Cométha Milestone (Jan 15)
3. Data Center Cooling (Feb 7)

Newsletter CTA at bottom
```

### 8. CONTACT CTA

**Layout:**
- Background: gradient (Carbon Black to #1D1D1F)
- Centered content
- Padding: 160px 0
- Large green glow element (decorative)

**Content:**
```
Headline: "Ready to Transform Waste into Energy?"
Subheadline: "Let's discuss how Zero-X can power your operations."

CTA: [Schedule a Consultation]

Contact Methods:
- Email: zerox@exventure.co
- Phone: +49 341 92881290
- Location: Spinlab, Leipzig
```

### 9. FOOTER

**Layout:**
- Background: #0A0A0A
- Border-top: 1px solid #424245
- Padding: 64px 0 32px

**Content:**
```
4-Column Grid:
- Company (About, Partners, Careers)
- Technology (X-150, Projects, Research)
- Resources (Blog, Documentation, FAQ)
- Legal (Privacy, Terms, Imprint)

Bottom Bar:
© 2026 Zero-X Group. All rights reserved.
[LinkedIn] [Twitter] [YouTube]
```

---

## ANIMATIONS & INTERACTIONS

### Scroll Reveal
```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
Duration: 600ms
Easing: cubic-bezier(0.16, 1, 0.3, 1)
Stagger: 100ms between elements
```

### Hover Effects
```css
/* Cards */
transform: translateY(-4px);
border-color: #00D26A;
box-shadow: 0 8px 32px rgba(0,210,106,0.15);
Duration: 300ms

/* Buttons */
transform: translateY(-2px);
filter: brightness(1.1);
Duration: 200ms

/* Links */
color: #00D26A;
Duration: 150ms
```

### Hero Animation Sequence
```
1. Background fade in (0ms)
2. Label fade in + slide up (200ms delay)
3. Headline fade in + slide up (400ms delay)
4. Subheadline fade in (600ms delay)
5. CTAs fade in + slide up (800ms delay)
6. Stats bar slide up (1000ms delay)
```

### Micro-interactions
- **Button click:** Scale 0.98, then back
- **Card hover:** Subtle glow increase
- **Link hover:** Underline animation (left to right)
- **Image hover:** Scale 1.05 with overflow hidden

---

## IMAGERY GUIDELINES

### Photography Style
- **Industrial elegance:** Clean, professional, modern
- **Lighting:** High contrast, dramatic shadows
- **Color treatment:** Desaturated with green/orange accents
- **Subject:** X-150 containers, industrial settings, team

### Image Treatment
```css
filter: contrast(1.1) saturate(0.9);
/* Add subtle vignette */
/* Green accent lighting on key elements */
```

### Icons
- **Style:** Thin line, 2px stroke
- **Color:** Platinum (#F5F5F7) or Zero-X Green (#00D26A)
- **Library:** Lucide or Heroicons

### Data Visualization
- **Charts:** Dark backgrounds, green/orange data points
- **Typography:** JetBrains Mono for numbers
- **Style:** Clean, minimal, high contrast

---

## ACCESSIBILITY

### Contrast Ratios
- **White on Carbon Black:** 21:1 ✅
- **Green on Carbon Black:** 7:1 ✅
- **Gray-200 on Carbon Black:** 11:1 ✅
- **Orange on Carbon Black:** 8:1 ✅

### Focus States
```css
outline: 2px solid #00D26A;
outline-offset: 4px;
```

### Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## BASE44 IMPLEMENTATION NOTES

### Theme Setup
1. Set primary color: `#00D26A`
2. Set secondary color: `#FF6B35`
3. Set background: `#0A0A0A`
4. Set text: `#F5F5F7`
5. Import Inter font (Google Fonts)
6. Import JetBrains Mono (Google Fonts)

### Custom CSS Variables
```css
:root {
  --carbon-black: #0A0A0A;
  --zero-x-green: #00D26A;
  --syngas-orange: #FF6B35;
  --platinum: #F5F5F7;
  --gray-100: #E5E5E7;
  --gray-200: #C5C5C7;
  --gray-300: #86868B;
  --gray-400: #424245;
  --gray-500: #1D1D1F;
}
```

### Performance Targets
- **First Contentful Paint:** < 1.5s
- **Largest Contentful Paint:** < 2.5s
- **Time to Interactive:** < 3.5s
- **Lighthouse Score:** > 90

---

## CONTENT TONE

### Voice
- **Confident:** "We transform waste into clean energy"
- **Precise:** Technical specifications, exact data
- **Ambitious:** "2.1 billion opportunity", "revolutionizing"
- **Authentic:** Real projects, validated results

### Example Copy
```
❌ "We make gasification systems"
✅ "We transform waste streams into high-value syngas"

❌ "Our product is good"
✅ "1,000+ operating hours validated"

❌ "Contact us for more info"
✅ "Ready to power your operations sustainably?"
```

---

## IMPLEMENTATION CHECKLIST

### Phase 1: Foundation
- [ ] Set up Base44 project with dark theme
- [ ] Configure color system
- [ ] Import fonts (Inter, JetBrains Mono)
- [ ] Set up custom CSS variables
- [ ] Configure responsive breakpoints

### Phase 2: Components
- [ ] Build button variants (Primary, Secondary, Ghost)
- [ ] Build card components (Feature, Project, Stats)
- [ ] Build navigation (fixed header, mobile menu)
- [ ] Build footer component

### Phase 3: Sections
- [ ] Hero section (100vh, animated)
- [ ] Stats bar
- [ ] Technology overview
- [ ] Featured projects grid
- [ ] Impact section
- [ ] Partners logo grid
- [ ] News/insights section
- [ ] Contact CTA

### Phase 4: Content
- [ ] Add all text content
- [ ] Upload images (X-150, projects, team)
- [ ] Configure blog posts (8 posts)
- [ ] Add partner logos
- [ ] Configure SEO meta tags

### Phase 5: Polish
- [ ] Add scroll animations
- [ ] Add hover effects
- [ ] Test responsive design
- [ ] Test accessibility
- [ ] Performance optimization
- [ ] Deploy

---

**Design Guide Complete - Ready for Implementation**
