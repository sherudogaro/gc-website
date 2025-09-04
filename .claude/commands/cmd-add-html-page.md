# Add HTML Page Command

Create new HTML page using existing main.css and Ontraport integration.

## Usage
/add-html-page [page-name] [page-type]

## Page Types Available
- `about` - About/team information page
- `contact` - Contact/consultation page with forms
- `team` - Team member profiles and bios
- `strategy` - Investment or business strategy
- `performance` - Track record, results, testimonials
- `legal` - Privacy, terms, disclaimer pages

## Prerequisites
- main.css should exist from /build-css-from-homepage
- css-reference.md should document available classes
- Homepage should be completed as foundation

## Process Steps
1. **Read CSS Reference**: Load css-reference.md to understand available classes
2. **Plan Page Structure**: Determine layout using existing CSS classes
3. **Create HTML Structure**: Build semantic HTML5 structure
4. **Apply Existing Styles**: Use documented CSS classes wherever possible
5. **Add New Styles Only If Needed**: Add to main.css only for genuinely new elements
6. **Add Ontraport Integration**: Include tracking script and forms as needed
7. **Update Documentation**: Record any new CSS classes created

## Critical Rules - CSS Class Management
- **Reference existing classes FIRST** before creating new ones
- **Search main.css** to confirm class doesn't already exist
- **Use semantic naming** if new classes needed (.contact-form, not .form1)
- **Update css-reference.md** immediately when new classes added
- **Report class usage**: "Used 12 existing classes, added 2 new classes"

## Critical Rules - HTML Structure  
- Use semantic HTML5 structure consistent with other pages
- Every page must have Ontraport tracking script in `<head>`
- Maintain navigation consistency across all pages
- Include proper meta descriptions and page titles

## HTML Template Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>[Page Title] - [Site Name]</title>
    <meta name="description" content="[Page description]">
    <link rel="stylesheet" href="assets/css/main.css">
    
    <!-- Ontraport Tracking Script -->
    <script>
    // Ontraport tracking code goes here
    </script>
</head>
<body>
    <header class="site-header">
        <!-- Use existing header structure -->
    </header>
    
    <main class="site-main">
        <!-- Page content using existing CSS classes -->
        <section class="hero-section">
            <div class="container">
                <!-- Content here -->
            </div>
        </section>
    </main>
    
    <footer class="site-footer">
        <!-- Use existing footer structure -->
    </footer>
</body>
</html>
```

## New CSS Class Guidelines
Only create new classes for elements that are:
- **Genuinely unique** to this page type
- **Cannot be achieved** with existing utility classes
- **Will be reused** on similar pages

Example new classes that might be needed:
- `.contact-form` for contact page specific form styling
- `.team-grid` for team member photo layouts
- `.performance-metrics` for data display tables

## Output Files
- New HTML page file (e.g., contact.html)
- Updated main.css (only if new styles needed)
- Updated css-reference.md (if new classes added)
- page-creation-report.txt (documents process and decisions)

## Page-Specific Integration Notes

### Contact Page
- Must include Ontraport form embed codes
- Test form submission reaches CRM properly
- Include consultation scheduling if relevant

### Team Page  
- Use consistent photo sizing and layout
- Include professional bios and credentials
- Link to individual LinkedIn profiles if appropriate

### Legal Pages
- Include proper disclaimers for business type
- Link to other legal pages in footer
- Ensure compliance with industry requirements

## Success Verification Checklist
- [ ] Page displays correctly using existing CSS classes
- [ ] Ontraport tracking script present and functional
- [ ] Navigation links updated on all pages
- [ ] Mobile responsive design maintained
- [ ] New classes documented in css-reference.md
- [ ] CSS validation passes with no errors
- [ ] Page loads quickly with optimized images

## Error Handling
- If existing classes insufficient: Create minimal new classes, document rationale
- If Ontraport integration fails: Provide troubleshooting steps
- If page layout breaks: Revert to working state, identify specific issue
- If mobile responsive issues: Address with existing utility classes first

## Example Usage
/add-html-page contact consultation-page
/add-html-page team company-bios
/add-html-page strategy investment-approach

Next Command: Use /integrate-ontraport-tracking after building core pages to ensure proper CRM integration