# Create HTML Foundation Command

Initialize HTML business site with Ontraport integration template.

## Usage
/create-html-foundation [site-name] [business-type]

## Process
1. Create complete HTML site directory structure
2. Generate template HTML files with Ontraport tracking placeholders
3. Set up main.css foundation with CSS variables
4. Create project documentation files
5. Add Ontraport integration checklist

## Critical Rules
- Every HTML file must include Ontraport tracking script placeholder
- Use semantic HTML5 structure throughout
- Single CSS file approach - no embedded styles
- Mobile-first responsive design by default

## Output
- Complete site structure with 7+ HTML files
- main.css with design system foundation
- project-brief.md and progress.md
- ontraport-integration.md with setup instructions

## Directory Structure Created
```
project-name/
├── index.html              # Homepage
├── contact.html           # Contact/consultation page
├── team.html             # Team/about page
├── performance.html       # Performance/track record
├── strategy.html         # Investment strategy
├── legal/               # Legal pages directory
│   ├── privacy.html
│   ├── terms.html
│   └── disclaimer.html
├── assets/
│   ├── css/
│   │   └── main.css      # Single stylesheet
│   ├── js/
│   │   └── main.js       # Site JavaScript
│   └── images/           # Optimized images
├── project-brief.md      # Business requirements
├── progress.md          # Status tracking
└── ontraport-integration.md  # Integration notes
```

## Example Usage
/create-html-foundation glenorchy-capital financial-services

## Success Verification
- [ ] All HTML files created with proper structure
- [ ] Ontraport tracking placeholder in every page
- [ ] main.css foundation ready for styling
- [ ] Project documentation files created
- [ ] Directory structure matches business requirements

Next: Use /build-css-from-homepage to establish styling foundation