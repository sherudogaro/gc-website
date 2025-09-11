# Rebel Fund Page Context

## Overview
The Rebel Fund is a separate fund structure (not managed accounts) created in partnership with George Gammon. This page is accessed directly via partner referrals, not through the main website navigation.

## Key Requirements

### Navigation
- **Header**: Logo only, no navigation menu
- **Not linked** from main website - accessed directly via `/rebel-fund.html`

### Content Priorities (in order)
1. **George Gammon partnership** - Most important element
2. **"Built for the Awake" tagline**
3. **Investment strategy** (6 components)
4. **Team section** (Chris, Brad, George)

### Form Requirements
- Same layout as consultation.html
- Needs to distinguish Rebel Fund inquiries from managed account inquiries
- Options:
  - Use same Zapier webhook with hidden field for "rebel_fund" 
  - OR create separate webhook
- Minimum investment: $200,000
- Qualified client requirement

### Visual Elements
- **Same styling** as main website (gold/navy color scheme)
- **Required images**:
  - Rebel Fund logo
  - Atlas drawing/illustration
- Consistent with site-wide design patterns

### Footer Modifications
- **Legal Links**: Keep all EXCEPT remove "Performance Disclaimer"
- **About Column**: 
  - Keep Strategy and Fees (open in new window with target="_blank")
  - Remove CRS and Brochure links (not relevant to fund)
- **Contact info**: Same as main site

### Investment Strategy Components
1. **Deep Value**: Search global markets for out-of-favour sectors
2. **Reducing Risk**: Multiple high-target return positions
3. **Non-Correlated**: Little correlation to major indices
4. **Arbitraging Impatience**: Long-term view vs short-term pressures
5. **Theme-Based**: Up to dozen sectors/themes simultaneously
6. **Asymmetry**: Targeting 3:1 or better returns

### Track Record
- Currently: "No track record" disclaimer
- Future: One year of performance data to be added

### Key Messaging
- Designed for contrarian investors
- Partnership with George Gammon emphasized
- "Built for the Awake" positioning
- Focus on asymmetric opportunities
- Global macro approach

### Technical Notes
- URL: `/rebel-fund.html` (not `/rebel-fund/`)
- Form submission needs to identify source as Rebel Fund
- Page should be self-contained (not appear in site navigation)
- All external links in footer should open in new tabs

## Updates Log
- Created: September 2025
- Last Updated: Initial creation
- Status: In development