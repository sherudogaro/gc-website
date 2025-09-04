# Glenorchy Capital HTML Website - Project Context

**Reference:** Lucas's Global Standards (all coding principles, business context, engineering standards apply)

**Project Brief:** See project-brief.md (comprehensive planning document)

**Current Phase:** Website Completion & Launch Preparation

**Last Updated:** September 3, 2025

## 🎯 PROJECT TYPE: STATIC HTML WEBSITE
**NOT WordPress - Static HTML/CSS/JS website for Glenorchy Capital**

**Repository:** [To be set up on GitHub]
**Deployment:** Cloudways Static HTML hosting
**Live Site:** [To be deployed]

### Standard Workflow:
1. Build HTML/CSS/JS files locally
2. Test thoroughly in browser
3. Deploy to Cloudways via Git or direct upload
4. **Static files only - no PHP/WordPress**

**Key Project Constraints:**
- Timeline: September 30th, 2025 launch (28 days remaining)
- Budget: Internally funded with existing resources
- Technical: Static HTML website with multiple pages

**Integration Requirements:**
- Ontraport CRM integration for consultation forms (JavaScript/iframe)
- Google Analytics 4 with conversion tracking
- Mobile-first responsive design (LinkedIn audience)

**Success Definition:**
- Primary KPI: Consultation form fills from qualified prospects
- $200K+ minimum, accredited investors only
- Target: High-quality leads for Chris MacIntosh and Brad McFadden

## 🚨 CRITICAL HTML DEVELOPMENT RULES 🚨

### HTML Structure Rules:
1. **Clean semantic HTML5** - proper header, main, section, footer structure
2. **Mobile-first responsive CSS** - mobile design first, desktop enhanced
3. **Fast loading** - optimized images, minified CSS/JS
4. **SEO optimized** - proper meta tags, structured data, alt texts

### File Structure:
```
/gc_html_website/
├── index.html (Home)
├── strategy.html (Strategy)
├── performance.html (Performance)  
├── team.html (Team)
├── contact.html (Contact)
├── css/
│   ├── main.css
│   └── responsive.css
├── js/
│   ├── main.js
│   └── ontraport.js
├── images/
└── assets/
```

**Navigation Structure:**
- Home → Strategy → Performance → Team → Contact → Schedule Consultation (CTA)

### HTML Testing Protocol:
1. Test homepage first - if CSS loads, foundation is solid
2. Test all pages in mobile view first (primary audience)
3. Check form integrations with real Ontraport connection
4. Verify all links work and pages load quickly
5. Test across Chrome, Safari, Firefox before deployment

### Compliance Requirements (SEC Regulated Business):
- All content must be compliant with SEC regulations
- Investment disclaimers required on all pages
- Clear accredited investor language
- No promises of returns or performance claims

**Session Handoff:**
- Current Status: See PROGRESS.md for detailed completion status
- Next Priority: Complete remaining pages (fees.html, faq.html) + legal pages + Zapier integration
- Blockers: Need Zapier account access for contact form integration
- Context: All main pages updated with consistent header/footer structure