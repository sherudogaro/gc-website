# Integrate Ontraport Tracking Command

Add Ontraport tracking and form integration to HTML pages for seamless CRM automation.

## Usage
/integrate-ontraport-tracking [tracking-setup-method]

## Tracking Setup Methods
- `manual` - User provides Ontraport tracking script directly
- `account` - Extract tracking code from Ontraport account setup
- `forms` - Focus on form integration with existing tracking

## Prerequisites
- HTML pages should be built and styled with main.css
- Ontraport account should be set up and accessible
- Contact forms should be created in Ontraport form builder
- Business should have clear CRM automation goals

## Process Steps

### Step 1: Ontraport Tracking Script Integration
1. **Obtain tracking script** from Ontraport admin for non-WordPress sites
2. **Add to every HTML page** in `<head>` section before `</head>`
3. **Verify script placement** is consistent across all pages
4. **Test tracking fires** on page load (check Ontraport analytics)

### Step 2: Form Integration
1. **Replace placeholder forms** with Ontraport embed codes
2. **Style forms** to match site design using existing CSS classes
3. **Add form validation** and user feedback messages
4. **Test form submissions** reach Ontraport CRM properly

### Step 3: Contact Flow Setup
1. **Map contact touchpoints** throughout site
2. **Configure lead scoring** and tagging in Ontraport
3. **Set up marketing automation** sequences
4. **Test end-to-end contact capture** workflow

## Critical Rules - Integration Standards

### Tracking Script Rules
- **Every page must have tracking** - no exceptions
- **Use exact code from Ontraport** - no modifications
- **Place in `<head>` section** for proper loading
- **Test on all pages** before deployment

### Form Integration Rules  
- **Use Ontraport form builder** - not custom HTML forms
- **Maintain design consistency** with existing site styling
- **Include proper error handling** for failed submissions
- **Add success messages** for completed forms

### Privacy Compliance Rules
- **Update privacy policy** to mention Ontraport data collection
- **Include cookie notices** if required for jurisdiction
- **Add opt-in language** for marketing communications
- **Provide unsubscribe options** in all communications

## Ontraport Tracking Script Template
```html
<!-- Add to <head> section of every HTML page -->
<script>
// Ontraport Tracking Script for Non-WordPress Sites
// Replace with actual script from Ontraport admin
(function(t,r,a,c,k,i,n,g){
    // Ontraport tracking implementation
    // Get exact script from: Ontraport Admin > Tracking > Non-WordPress Sites
})();
</script>
```

## Form Integration Example
```html
<!-- Replace placeholder contact forms with Ontraport embed -->
<div class="contact-form-container">
    <!-- Ontraport Form Embed Code Goes Here -->
    <!-- From: Ontraport Admin > Forms > [Your Form] > Embed Code -->
    <script src="https://forms.ontraport.com/form/..." async></script>
</div>

<!-- Add CSS to maintain design consistency -->
<style>
.ontraport-form {
    /* Use existing CSS classes to style Ontraport forms */
    padding: 2rem;
    background: var(--background-color);
    border-radius: var(--border-radius);
}
</style>
```

## Contact Flow Mapping

### Homepage Contact Points
- Hero section CTA button
- Newsletter signup form
- "Schedule Consultation" buttons

### Contact Page Integration
- Main consultation booking form
- Phone number click-to-call tracking
- Email address tracking

### Other Pages
- Footer contact forms on every page
- "Learn More" buttons that capture interest
- Resource download forms

## Testing Procedures

### Tracking Verification
1. **Page load tracking**: Visit each page, verify appears in Ontraport analytics
2. **Event tracking**: Click buttons, verify events logged properly  
3. **Form submissions**: Submit test data, confirm reaches CRM
4. **Mobile testing**: Test tracking works on mobile devices

### CRM Integration Testing  
1. **Contact creation**: Verify new contacts appear in Ontraport
2. **Data accuracy**: Check all form fields populate correctly
3. **Automation triggers**: Confirm marketing sequences activate
4. **Tagging and scoring**: Verify leads tagged and scored properly

## Output Files Created
- All HTML pages updated with Ontraport tracking
- Form integration completed and tested  
- `ontraport-integration.md` updated with configuration details
- `integration-test-results.txt` with verification checklist
- `contact-flow-map.md` documenting all touchpoints

## Common Integration Issues & Solutions

### Tracking Script Problems
- **Script not firing**: Check placement in `<head>`, verify no JavaScript errors
- **Missing on some pages**: Audit all HTML files, ensure consistent implementation
- **Double tracking**: Remove duplicate scripts, consolidate to single implementation

### Form Integration Issues
- **Styling breaks**: Use CSS to override Ontraport form styles
- **Mobile responsiveness**: Test forms on mobile, adjust responsive design
- **Submission failures**: Check form action URLs, verify Ontraport account settings

### CRM Data Problems
- **Missing contact data**: Verify all form fields mapped correctly in Ontraport
- **Automation not triggering**: Check automation rules and contact conditions
- **Duplicate contacts**: Review Ontraport deduplication settings

## Success Verification Checklist
- [ ] Ontraport tracking script present on every page
- [ ] All forms submit successfully to Ontraport CRM
- [ ] Test contact appears in Ontraport with correct data
- [ ] Marketing automation sequences activate properly
- [ ] Mobile tracking and forms work correctly
- [ ] Privacy policy updated for Ontraport integration
- [ ] Contact flow documented and tested end-to-end

## Business Integration Notes

### For Financial Services (Glenorchy Capital)
- **Compliance requirements**: Ensure tracking complies with SEC regulations
- **Lead qualification**: Set up scoring for accredited investor status
- **Consultation booking**: Integrate calendar scheduling with CRM
- **Follow-up automation**: Create sequences for investment consultation process

### Marketing Automation Setup
- **Welcome series**: New contact introduction sequence
- **Consultation reminders**: Automated booking confirmation and reminders  
- **Content nurturing**: Educational content delivery based on interests
- **Re-engagement**: Follow-up sequences for inactive leads

## Error Handling & Troubleshooting
- If tracking script fails: Provide manual implementation guide
- If forms don't submit: Offer alternative contact methods, debug step-by-step
- If automation doesn't trigger: Document troubleshooting steps for Ontraport settings
- If mobile integration breaks: Provide mobile-specific fixes and testing

Next Command: Use /generate-legal-pages to create compliant privacy and legal pages that account for Ontraport data collection