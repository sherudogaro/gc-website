# Cloudways Staging Deployment Checklist

## Pre-Deployment Verification
- [x] All changes committed to git
- [x] All pages using relative URLs (no hardcoded domains)
- [x] Customer flows separated (MA vs Rebel Fund)
- [x] Forms tested locally

## Files Structure for Upload
```
/public_html/
├── index.html
├── strategy.html
├── performance.html
├── team.html
├── fees.html
├── faq.html
├── consultation.html
├── rebel-fund.html
├── schedule-ma.html
├── schedule-fund.html
├── contact.html
├── legal/
│   ├── terms.html
│   ├── privacy.html
│   ├── disclaimer.html
│   └── performance-disclaimer.html
├── css/
│   └── (all CSS files)
├── js/
│   └── (all JS files)
├── images/
│   └── (all image files)
└── assets/
    └── (PDF files, etc.)
```

## Cloudways Deployment Steps

### 1. Access Cloudways Application
- Log into Cloudways platform
- Navigate to your application
- Access Public_html folder via File Manager or SSH/SFTP

### 2. Upload Methods

#### Option A: Git Deployment (Recommended)
```bash
# SSH into server
ssh [username]@[server-ip]

# Navigate to public_html
cd applications/[app-name]/public_html/

# Clone repository
git clone https://github.com/sherudogaro/gc-website.git .

# Or if already cloned, pull latest
git pull origin main
```

#### Option B: SFTP Upload
- Use FileZilla or similar SFTP client
- Connect using Cloudways SFTP credentials
- Upload all files maintaining folder structure
- Ensure file permissions are correct (644 for files, 755 for directories)

#### Option C: Cloudways File Manager
- Use built-in File Manager in Cloudways console
- Upload files maintaining structure
- May be slower for large number of files

### 3. Post-Deployment Testing

#### Critical Pages to Test:
- [ ] Homepage loads with proper CSS
- [ ] Navigation menu works on all pages
- [ ] consultation.html - Ontraport form displays
- [ ] rebel-fund.html - Ontraport form displays
- [ ] schedule-ma.html - Calendly widget loads
- [ ] schedule-fund.html - Calendly widget loads
- [ ] Mobile responsiveness (test on phone)
- [ ] All internal links work
- [ ] Legal pages accessible from footer

#### Form Testing:
- [ ] Test consultation form submission
- [ ] Test Rebel Fund form submission
- [ ] Verify Calendly scheduling works
- [ ] Check form redirect URLs (may need configuration in Ontraport)

### 4. DNS & Domain Setup (if custom domain)
- [ ] Add domain in Cloudways application settings
- [ ] Update DNS A records to point to Cloudways server IP
- [ ] Install SSL certificate (Let's Encrypt free SSL)
- [ ] Force HTTPS redirect in .htaccess

### 5. Performance Optimization
- [ ] Enable Cloudways Breeze cache
- [ ] Configure CloudwaysCDN if available
- [ ] Test page load speeds

### 6. Monitoring Setup
- [ ] Enable Cloudways monitoring
- [ ] Set up uptime monitoring
- [ ] Configure backup schedule

## Environment Variables & Configurations

### Ontraport Forms
Current form IDs in use:
- Consultation form: `p2c193653f71`
- Rebel Fund form: `p2c193653f72`

After deployment, configure redirect URLs in Ontraport:
- Consultation success: `/thank-you.html` or custom page
- Rebel Fund success: `/schedule-fund.html`

### Google Analytics (To be added)
- GA4 Measurement ID: [To be provided]
- Add tracking code to all pages before `</head>`

### URLs to Update After Domain Setup
Currently using relative URLs - no changes needed unless switching to absolute URLs

## Troubleshooting

### Common Issues:

1. **CSS not loading**
   - Check file paths are relative
   - Verify CSS files uploaded to /css/ directory
   - Clear browser cache

2. **Forms not displaying**
   - Ensure JavaScript is enabled
   - Check Ontraport script tags are present
   - Verify no Content Security Policy blocking

3. **Calendly not loading**
   - Check widget script is included
   - Verify data-url parameter is correct
   - Test in incognito mode

4. **404 errors**
   - Verify all HTML files uploaded
   - Check file extensions (.html)
   - Ensure proper case sensitivity (Linux servers)

## Support Contacts

- Cloudways Support: Available 24/7 via live chat
- Ontraport Support: For form configuration issues
- Calendly Support: For scheduling widget issues

## Final Checklist

- [ ] All pages load correctly
- [ ] Forms capture data in Ontraport
- [ ] Scheduling works for both MA and Fund flows
- [ ] Mobile experience is smooth
- [ ] Legal/compliance pages accessible
- [ ] No console errors in browser
- [ ] Site loads under 3 seconds
- [ ] SSL certificate active (https://)

## Notes
- Staging URL: [To be provided by Cloudways]
- Production URL: https://glenorchycapital.net
- Deployment Date: September 2025
- Last Updated: September 23, 2025