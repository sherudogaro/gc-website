# Prepare Cloudways Deploy Command

Optimize and package HTML site for deployment to Cloudways static hosting.

## Usage
/prepare-cloudways-deploy

## Prerequisites
- All HTML pages completed and tested locally
- Ontraport integration working correctly  
- Legal pages generated and properly linked
- CSS and assets organized in proper directory structure
- Site tested in local browser environment

## Pre-Deployment Validation Steps

### Step 1: Content Validation
1. **HTML validation**: Check all pages for syntax errors and broken tags
2. **Link verification**: Test all internal links, navigation, and footer links
3. **Image optimization**: Compress images, convert to WebP where appropriate
4. **Content accuracy**: Verify all text, contact information, and business details

### Step 2: Technical Optimization  
1. **CSS minification**: Compress main.css for faster loading
2. **JavaScript optimization**: Minify any custom JavaScript files
3. **Image compression**: Optimize all images for web delivery
4. **File organization**: Ensure proper directory structure for deployment

### Step 3: Integration Testing
1. **Ontraport tracking**: Verify tracking script fires on all pages
2. **Form functionality**: Test all contact forms submit to CRM properly
3. **Mobile responsiveness**: Test site on mobile devices and tablets
4. **Browser compatibility**: Test on major browsers (Chrome, Firefox, Safari)

## Critical Rules - Pre-Deployment Standards

### File Organization Requirements
- All HTML files in root directory for clean URLs
- Assets organized in `/assets/css/`, `/assets/js/`, `/assets/images/`
- Legal pages in `/legal/` subdirectory
- No broken file paths or missing resources
- Consistent file naming (lowercase, hyphen-separated)

### Performance Standards
- Page load time under 3 seconds on standard connection
- Images optimized and properly sized for web
- CSS file under 50KB when minified
- No render-blocking resources in critical path

### Integration Requirements
- Ontraport tracking functional on every page
- All forms submit successfully to CRM
- SSL certificate requirements documented
- Mobile experience tested and functional

## Cloudways Deployment Process

### Step 1: Create Static Site Application
1. **Log into Cloudways**: Access your Cloudways account
2. **Add New Application**: Choose "Static Site" (NOT WordPress)
3. **Select Server**: Choose appropriate server size and location
4. **Configure Basic Settings**: Set application name and domain preferences

### Step 2: Upload Site Files
**Method 1: SFTP Upload**
```
Host: [Cloudways server IP]
Username: [Cloudways SFTP username] 
Password: [Cloudways SFTP password]
Port: 22
Directory: /public_html/
```

**Method 2: File Manager**
- Use Cloudways built-in file manager
- Upload files directly to `public_html` directory
- Maintain directory structure during upload

**Method 3: Git Deployment** 
- Connect repository to Cloudways Git integration
- Configure auto-deployment on push
- Set up proper build/deploy workflow

### Step 3: Domain and SSL Configuration
1. **Domain Setup**: Point existing domain to new Cloudways application
2. **SSL Certificate**: Enable free SSL certificate (required for Ontraport forms)
3. **CDN Configuration**: Enable Cloudways CDN for better performance
4. **DNS Configuration**: Update DNS records to point to new application

### Step 4: Post-Deployment Testing
1. **Page Loading**: Test all pages load correctly on live domain
2. **Form Submission**: Submit test contacts through all forms
3. **CRM Integration**: Verify test contacts appear in Ontraport
4. **Mobile Testing**: Test mobile experience on live site
5. **SSL Verification**: Confirm SSL certificate working properly

## WordPress to Static Site Migration

### Cloudways Migration Steps
1. **Create new Static Site application** (separate from WordPress app)
2. **Upload HTML files** to new application's public_html directory
3. **Test new static site** thoroughly on temporary domain
4. **Update DNS records** to point domain to new static application
5. **Archive WordPress application** (keep as backup, pause to save costs)

### DNS Configuration Changes
```
A Record: @ -> [New Static Site IP]
CNAME: www -> [New Static Site Domain]
```

### Post-Migration Cleanup
- Monitor traffic and functionality for 24-48 hours
- Update any external services pointing to old WordPress URLs
- Archive WordPress app files and database (backup)
- Cancel WordPress-specific services if no longer needed

## Output Files and Documentation

### Deployment Package Structure
```
deployment-package/
├── index.html
├── contact.html
├── team.html
├── performance.html  
├── strategy.html
├── legal/
│   ├── privacy.html
│   ├── terms.html
│   └── disclaimer.html
├── assets/
│   ├── css/
│   │   └── main.min.css (minified)
│   ├── js/
│   │   └── main.min.js (minified)
│   └── images/ (optimized)
└── sitemap.xml
```

### Documentation Created
- `cloudways-setup-instructions.md` - Step-by-step deployment guide
- `pre-deploy-checklist.txt` - Validation checklist completed
- `post-deploy-testing-guide.md` - Live site testing procedures
- `dns-configuration-guide.md` - Domain setup instructions
- `backup-procedures.md` - How to backup and restore site

## Performance Optimization Features

### Image Optimization
- **Compression**: Reduce file sizes by 60-80% without quality loss
- **Format conversion**: Convert PNG to WebP where supported
- **Responsive images**: Multiple sizes for different screen resolutions
- **Lazy loading**: Implement lazy loading for images below the fold

### CSS/JS Optimization  
- **Minification**: Remove whitespace and comments from CSS/JS
- **Concatenation**: Combine multiple files where appropriate
- **Critical CSS**: Inline critical path CSS for faster rendering
- **Asset optimization**: Optimize font loading and external resources

### Caching Configuration
- **Browser caching**: Set appropriate cache headers for static assets
- **CDN integration**: Configure Cloudways CDN for global delivery
- **Compression**: Enable gzip compression for text-based files

## Security and Compliance

### SSL Certificate Setup
- **Free SSL**: Enable Cloudways free SSL certificate
- **Force HTTPS**: Redirect all HTTP traffic to HTTPS
- **Security headers**: Configure appropriate security headers
- **Form security**: Ensure all Ontraport forms submit over HTTPS

### Backup Configuration
- **Automated backups**: Set up regular backup schedule in Cloudways
- **File archiving**: Keep local copies of all site files
- **Database backup**: Not applicable for static sites (benefit!)
- **Recovery procedures**: Document how to restore from backup

## Testing and Validation Checklists

### Pre-Deployment Checklist
- [ ] All HTML pages validated and error-free
- [ ] All internal links working correctly
- [ ] Images optimized and loading properly
- [ ] CSS and JavaScript minified
- [ ] Ontraport tracking tested on all pages
- [ ] All forms submit to CRM successfully
- [ ] Mobile responsiveness verified
- [ ] Legal pages linked and accessible

### Post-Deployment Checklist  
- [ ] Domain resolves to correct Cloudways application
- [ ] SSL certificate active and working
- [ ] All pages load without errors on live site
- [ ] Contact forms submit and reach Ontraport CRM
- [ ] Mobile site functions properly
- [ ] Analytics and tracking active
- [ ] Site performance meets standards (<3 second load time)
- [ ] All legal pages accessible and properly formatted

## Error Handling and Troubleshooting

### Common Deployment Issues
- **File permissions**: Ensure proper file permissions for web serving
- **Missing files**: Check for broken asset links and missing resources
- **HTTPS issues**: Verify SSL certificate configuration for forms
- **Mobile problems**: Test responsive design on actual mobile devices

### CRM Integration Issues
- **Form failures**: Check Ontraport embed codes and SSL requirements
- **Tracking problems**: Verify tracking script placement and syntax
- **Contact flow**: Test end-to-end contact capture and automation

### Performance Problems
- **Slow loading**: Check image optimization and server configuration
- **Mobile issues**: Verify responsive design and mobile optimization
- **CDN problems**: Configure Cloudways CDN properly for asset delivery

## Success Verification Metrics
- **Page Load Speed**: <3 seconds on standard connection
- **Mobile Performance**: Good Core Web Vitals scores
- **CRM Integration**: 100% of test forms reach Ontraport
- **SSL Security**: All pages served over HTTPS with valid certificate
- **Uptime**: Site accessible 99.9% of time after deployment
- **SEO Readiness**: Proper meta tags, sitemap, and structured data

## Business Continuity Notes

### Contact Information Updates
After successful deployment, update:
- **Business cards and marketing materials** with new site performance
- **Email signatures** if site URLs changed
- **Social media profiles** with updated website links
- **Directory listings** (Google My Business, industry directories)

### Monitoring and Maintenance
- **Regular backups**: Ensure automated backups continue working
- **Performance monitoring**: Monitor site speed and uptime
- **CRM integration health**: Regularly test contact form functionality  
- **Content updates**: Establish process for updating site content as needed

Final Step: After successful deployment, monitor site performance and CRM integration for 48 hours to ensure stable operation.