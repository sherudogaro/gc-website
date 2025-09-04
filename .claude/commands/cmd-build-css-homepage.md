# Build CSS From Homepage Command

Extract CSS from homepage design to create main.css foundation for entire site.

## Usage
/build-css-from-homepage [homepage-file]

## Prerequisites
Homepage HTML file should exist (from v0, Claude, or manual creation)

## Process
1. Read homepage HTML file completely
2. Extract all CSS from `<style>` blocks  
3. Create main.css with proper organization
4. Generate CSS reference guide with available classes
5. Remove embedded CSS from homepage, link to main.css
6. Validate homepage still displays correctly

## Critical Rules
- Extract ALL CSS rules, no assumptions about what's needed
- Organize CSS logically: variables, base, components, utilities
- Create CSS class reference document for future pages
- Test homepage displays identically after extraction

## CSS Organization Structure
```css
/* CSS Variables */
:root {
  --primary-color: #value;
  --font-primary: 'Font Name';
}

/* Base Styles */
* { box-sizing: border-box; }
body { font-family: var(--font-primary); }

/* Layout Components */
.container { max-width: 1200px; margin: 0 auto; }
.section { padding: 4rem 0; }

/* UI Components */
.button { padding: 1rem 2rem; }
.hero-section { background: gradient; }

/* Utilities */
.text-center { text-align: center; }

/* Media Queries */
@media (max-width: 768px) { }
```

## Output Files
- `assets/css/main.css` (organized stylesheet)
- `css-reference.md` (available classes guide) 
- Updated homepage HTML (links to main.css)
- `css-extraction-report.txt` (process documentation)

## CSS Reference Document Format
The css-reference.md file will include:
- **Layout Classes**: .container, .section, .grid
- **Typography**: .heading, .subheading, .body-text
- **Buttons**: .button, .cta-primary, .cta-secondary  
- **Components**: .hero, .card, .form-group
- **Utilities**: .text-center, .mb-2, .hidden-mobile

## Success Verification
- [ ] All CSS extracted from homepage HTML
- [ ] main.css file created with logical organization
- [ ] css-reference.md documents all available classes
- [ ] Homepage displays identically after CSS extraction
- [ ] No embedded styles remain in homepage HTML

## Error Handling
- If CSS extraction fails: Report specific errors, continue with partial extraction
- If homepage breaks: Restore original file, identify problematic CSS
- If organization unclear: Create flat CSS structure, document for manual cleanup

Next Command: Use /add-html-page to build additional pages using the CSS foundation

## Example Usage
/build-css-from-homepage index.html