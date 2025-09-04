# Generate Legal Pages Command

Create professional legal pages (privacy, terms, disclaimer) for business site with proper compliance.

## Usage
/generate-legal-pages [business-name] [business-type]

## Business Types Supported
- `financial-services` - SEC compliance, investment disclaimers, accredited investor requirements
- `consulting` - Professional services disclaimers, liability limitations
- `e-commerce` - Sales terms, shipping policies, returns
- `saas` - Software licensing, data processing, service availability
- `general` - Basic business website legal requirements

## Prerequisites
- Main website pages should be completed
- Ontraport integration should be implemented (for privacy policy accuracy)
- Business type and regulatory requirements should be understood
- Company legal information should be available

## Process Steps

### Step 1: Business Information Gathering
1. **Company details**: Legal business name, address, contact information
2. **Regulatory context**: Industry requirements (SEC for financial, GDPR for EU, etc.)
3. **Data collection practices**: What data is collected via Ontraport and website
4. **Service description**: What the business actually provides to clients

### Step 2: Legal Page Generation
1. **Privacy Policy**: Data collection, usage, sharing, and retention policies
2. **Terms of Service**: User obligations, service limitations, dispute resolution
3. **Disclaimer Page**: Liability limitations, professional disclaimers
4. **Industry-Specific Pages**: Investment disclosures, regulatory compliance notices

### Step 3: Compliance Integration
1. **Ontraport disclosure**: How visitor data is collected and used
2. **Third-party services**: Analytics, forms, any other data processors
3. **Cookie policy**: If cookies are used for tracking or functionality
4. **Regulatory compliance**: Industry-specific legal requirements

## Critical Rules - Legal Content Standards

### Accuracy Requirements
- **Use business legal name** exactly as registered
- **Include correct jurisdiction** where business operates
- **Reflect actual practices** - don't copy generic templates that don't match reality
- **Update contact information** to match business details

### Compliance Standards
- **Industry-specific requirements** must be included
- **Data protection laws** (GDPR, CCPA) addressed where applicable  
- **Professional disclaimers** appropriate for business type
- **Regulatory disclosures** as required by industry

### Integration Requirements
- **Ontraport data collection** must be disclosed in privacy policy
- **Form data usage** clearly explained
- **Marketing communications** opt-in/opt-out clearly stated
- **Third-party data sharing** accurately described

## Legal Page Templates

### Privacy Policy Structure
```
1. Information We Collect
   - Contact form submissions (Ontraport)
   - Website analytics and tracking
   - Cookies and similar technologies

2. How We Use Information  
   - Client communication and consultation scheduling
   - Marketing automation and follow-up
   - Website performance and improvement

3. Information Sharing
   - Service providers (Ontraport, hosting)
   - Legal requirements and compliance
   - Business transfers (if applicable)

4. Your Rights
   - Access and correction of personal data
   - Opt-out of marketing communications  
   - Data deletion requests (where legally permissible)

5. Contact Information
   - How to reach us with privacy questions
   - Data protection officer (if required)
```

### Financial Services Specific Additions
```
Investment Disclaimers:
- Past performance does not guarantee future results
- All investments involve risk of loss
- Securities offered only to accredited investors
- SEC registration status and limitations
- Fiduciary duty disclosures (where applicable)

Regulatory Compliance:
- Investment Advisers Act compliance
- State registration requirements  
- FINRA/SEC oversight disclaimers
- Professional licensing information
```

## Output Files Created
- `legal/privacy.html` - Comprehensive privacy policy
- `legal/terms.html` - Terms of service agreement  
- `legal/disclaimer.html` - Professional liability disclaimers
- `legal/disclosures.html` - Industry-specific regulatory disclosures (financial services)
- `legal/cookie-policy.html` - Cookie usage policy (if needed)
- `legal/index.html` - Legal pages directory/index

## Legal Navigation Integration
Updates all site pages to include legal page links:
- Footer links to privacy policy and terms
- Contact form privacy policy checkboxes
- Cookie consent notices (if required)
- Easy access to all legal documents

## Industry-Specific Customizations

### Financial Services (Glenorchy Capital)
- **SEC registration disclaimers**: Clear statement of regulatory status
- **Accredited investor requirements**: Who can invest, qualification standards
- **Investment risk disclosures**: Standard risk warnings for investment services
- **Fiduciary disclosures**: Investment advisor responsibilities and limitations
- **Performance disclaimers**: Past performance, risk of loss warnings

### Consulting Services
- **Professional liability limitations**: Scope of responsibility and advice disclaimers
- **Intellectual property**: Ownership of work products and methodologies
- **Confidentiality agreements**: How client information is protected
- **Service limitations**: What is and isn't included in consulting engagements

### General Business
- **Basic privacy protections**: Standard data collection and usage policies
- **Website terms**: Acceptable use, intellectual property, general disclaimers
- **Contact obligations**: How business communicates with website visitors
- **Limitation of liability**: Standard business protection disclaimers

## Compliance Verification Checklist
- [ ] Privacy policy accurately describes Ontraport data collection
- [ ] Terms of service match actual business practices
- [ ] Industry-specific disclaimers included where required
- [ ] Contact information current and accurate
- [ ] Legal pages accessible from all site pages
- [ ] Cookie policy addresses tracking practices (if applicable)
- [ ] Regulatory disclosures appropriate for business type

## Important Legal Disclaimers

**Template Limitation Notice**: These legal page templates provide basic compliance structure but are not legal advice. Businesses should:
- **Consult qualified attorney** for industry-specific requirements
- **Review compliance obligations** in their jurisdiction
- **Update legal pages** as business practices evolve
- **Monitor regulatory changes** that affect their industry

**Industry-Specific Requirements**: 
- Financial services require SEC, FINRA, and state regulatory compliance
- Healthcare requires HIPAA compliance
- EU visitors require GDPR compliance
- California residents require CCPA compliance

## Success Verification
- [ ] All required legal pages created and properly formatted
- [ ] Business-specific information accurately reflected
- [ ] Ontraport integration properly disclosed
- [ ] Industry compliance requirements addressed
- [ ] Legal page navigation integrated throughout site
- [ ] Contact information matches business registration
- [ ] Disclaimer language appropriate for services provided

## Error Handling & Warnings
- If business type unclear: Request clarification before generating content
- If regulatory requirements complex: Recommend attorney consultation
- If Ontraport integration incomplete: Flag privacy policy accuracy concerns
- If industry standards uncertain: Provide general template with attorney review recommendation

## Example Usage
/generate-legal-pages "Glenorchy Capital Management, LLC" financial-services
/generate-legal-pages "Smith Consulting Group" consulting  
/generate-legal-pages "ABC Technologies" general

Next Command: Use /prepare-cloudways-deploy to finalize site for production deployment