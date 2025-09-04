# Ontraport Integration Guide - Glenorchy Capital

This document provides step-by-step instructions for integrating Ontraport CRM with the Glenorchy Capital website for lead capture and tracking.

## Integration Overview

The website has been prepared with placeholder comments and JavaScript handlers for seamless Ontraport integration. All consultation forms are designed to capture qualified leads and sync with your CRM system.

## Prerequisites

1. Active Ontraport account with API access
2. Ontraport tracking script (to be provided by Ontraport)
3. Form configuration in Ontraport dashboard
4. API credentials for form submissions

## Integration Points

### 1. Tracking Script Integration

**Location**: All HTML pages contain this placeholder:
```html
<!-- ONTRAPORT_TRACKING_SCRIPT_PLACEHOLDER -->
```

**Action Required**: Replace with your Ontraport tracking script:
```html
<script type="text/javascript" src="https://app.ontraport.com/js/ontraport/opt_assets/..."></script>
```

### 2. Consultation Form Integration

**Primary Location**: `contact.html#consultation`

**Current Structure**:
```html
<div id="ontraport-consultation-form">
    <!-- ONTRAPORT_CONSULTATION_FORM_PLACEHOLDER -->
    <!-- Fallback form currently visible -->
</div>
```

**Action Required**: Replace placeholder with Ontraport form embed code or iframe.

### 3. Form Fields Mapping

The fallback form captures these fields that should be mapped in Ontraport:

| HTML Field ID | Field Type | Ontraport Field | Required |
|---------------|------------|-----------------|----------|
| `fullName` | Text | First Name + Last Name | Yes |
| `email` | Email | Email | Yes |
| `phone` | Tel | Phone | Yes |
| `investmentAmount` | Select | Custom Field: Investment Range | Yes |
| `accreditedStatus` | Select | Custom Field: Accredited Status | Yes |
| `investmentGoals` | Textarea | Custom Field: Investment Goals | No |

### Investment Amount Options:
- $200K - $500K
- $500K - $1M
- $1M - $5M
- $5M+

### Accredited Status Options:
- Yes, I am an accredited investor
- I need to verify my status

## JavaScript Integration

### Tracking Functions Available

The `main.js` file includes these functions ready for Ontraport:

```javascript
// Track consultation request
function trackConsultationRequest(formData) {
    if (typeof ontraport !== 'undefined' && ontraport.track) {
        ontraport.track('consultation_request', formData);
    }
}

// Initialize Ontraport integration
function initializeOntraportIntegration() {
    if (typeof ontraport !== 'undefined') {
        console.log('Ontraport tracking active');
        
        if (ontraport.trackPageView) {
            ontraport.trackPageView({
                page: window.location.pathname,
                title: document.title,
                timestamp: new Date().toISOString()
            });
        }
    }
}
```

### Custom Events Tracked

1. **Page Views**: Automatic on all pages
2. **Consultation Requests**: When form is submitted
3. **Navigation Clicks**: CTA button clicks
4. **Download Events**: When implemented

## Implementation Steps

### Step 1: Add Tracking Script

1. Log into your Ontraport account
2. Navigate to Tracking → Tracking Scripts
3. Generate tracking script for your domain
4. Replace `<!-- ONTRAPORT_TRACKING_SCRIPT_PLACEHOLDER -->` in all HTML files

### Step 2: Create Form in Ontraport

1. Go to Forms → Create New Form
2. Add fields matching the table above
3. Configure form actions:
   - Add to sequence: "Consultation Requests"
   - Assign tags: "Website Lead", "Accredited Investor"
   - Send notification to team
4. Copy form embed code

### Step 3: Replace Form Placeholder

Replace this placeholder in `contact.html`:
```html
<!-- ONTRAPORT_CONSULTATION_FORM_PLACEHOLDER -->
```

With your Ontraport form embed code:
```html
<script type="text/javascript" src="https://app.ontraport.com/form/..."></script>
```

### Step 4: Configure Automation

Set up these automations in Ontraport:

1. **Immediate Response**:
   - Send confirmation email to prospect
   - Include next steps and contact information

2. **Team Notification**:
   - Send email to Chris MacIntosh and Brad McFadden
   - Include all form data and qualification status

3. **Follow-up Sequence**:
   - Schedule follow-up tasks based on investment amount
   - Different sequences for different investor tiers

### Step 5: Test Integration

1. Submit test form with fake data
2. Verify data appears in Ontraport contacts
3. Confirm automation emails are sent
4. Test tracking in Ontraport reports

## Lead Qualification Setup

### Automatic Tagging

Configure these tags based on form responses:

**Investment Amount Tags**:
- `inv-200k-500k`
- `inv-500k-1m`
- `inv-1m-5m`
- `inv-5m-plus`

**Status Tags**:
- `accredited-confirmed`
- `accredited-needs-verification`
- `website-lead`
- `consultation-requested`

### Lead Scoring

Implement lead scoring based on:
- Investment amount (higher amounts = higher score)
- Accredited status (confirmed = higher score)
- Source: Website consultation form
- Investment goals detail level

## Custom Fields Required

Create these custom fields in Ontraport:

1. **Investment Amount** (Dropdown)
   - Options as listed above

2. **Accredited Status** (Dropdown)
   - "Confirmed"
   - "Needs Verification"

3. **Investment Goals** (Text Area)
   - Capture detailed goals from form

4. **Lead Source** (Text)
   - Auto-populate with "Website - Consultation Form"

5. **Website Page** (Text)
   - Track which page generated the lead

## Compliance Considerations

### GDPR/Privacy Compliance

- Ensure privacy policy link is included in form
- Add GDPR consent checkbox if serving EU visitors
- Configure data retention policies

### SEC Compliance

- Track accredited investor verification status
- Maintain audit trail of all communications
- Store verification documents securely

## Analytics Integration

### Google Analytics 4 Events

When Ontraport form is submitted, trigger these GA4 events:

```javascript
gtag('event', 'consultation_request', {
    'event_category': 'Lead Generation',
    'event_label': 'Consultation Form',
    'investment_amount': formData.investmentAmount,
    'accredited_status': formData.accreditedStatus,
    'value': 1
});
```

### Conversion Tracking

Set up conversions for:
- Form submissions
- Qualified leads (accredited investors)
- High-value leads ($1M+ investment amounts)

## Troubleshooting

### Common Issues

1. **Form Not Displaying**:
   - Check Ontraport script loading
   - Verify embed code syntax
   - Check browser console for errors

2. **Data Not Syncing**:
   - Verify API credentials
   - Check field mapping
   - Test with simple form first

3. **Tracking Not Working**:
   - Ensure tracking script loads before form script
   - Check domain configuration in Ontraport
   - Test in incognito mode

### Debug Mode

Add this to test tracking:
```javascript
// Add to main.js for debugging
window.ontraportDebug = true;
```

## Performance Considerations

### Loading Optimization

- Load Ontraport scripts asynchronously
- Implement fallback form for slow connections
- Monitor page load speeds after integration

### Fallback Handling

The current implementation includes a fallback form that:
- Collects all required data
- Provides user feedback
- Can be manually processed if Ontraport fails

## Post-Integration Checklist

- [ ] Tracking script installed on all pages
- [ ] Form displays correctly on contact page
- [ ] Test submissions sync to Ontraport
- [ ] Automation emails are sent
- [ ] Team notifications work
- [ ] Analytics events fire correctly
- [ ] Page load speed is acceptable
- [ ] Fallback form is hidden when Ontraport loads
- [ ] Mobile form display tested
- [ ] Cross-browser compatibility verified

## Support Contacts

For integration support:
- Ontraport Support: [Your support contact]
- Developer Support: [Technical contact]
- Compliance Questions: [Legal/compliance contact]

## Security Notes

- Never expose API credentials in frontend code
- Use HTTPS for all form submissions
- Implement CSRF protection if handling server-side processing
- Regular security audits of form handling

This integration will capture high-quality leads and automate your follow-up process while maintaining SEC compliance and providing excellent user experience.