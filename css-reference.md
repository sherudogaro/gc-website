# Glenorchy Capital - CSS Reference Guide

This document provides the definitive reference for the Glenorchy Capital website design system, based on the actual implementation.

## CSS Variables (Custom Properties)

### Brand Colors
- `--glenorchy-gold: #B89676` - **Primary brand color** (brown/gold)
- `--glenorchy-navy: #272727` - **Dark text and accent color**
- `--glenorchy-dark-blue: #1a3a52` - **Button hover states and dark accents**
- `--off-white: #FAFAFA` - **Main background color**
- `--warm-grey: #8A8A8A` - **Secondary text and muted content**
- `--steel-blue: #5B7C99` - **Supporting accent color**
- `--deep-green: #2D5A3D` - **Positive numbers and success states**
- `--charcoal: #3D3D3D` - **Main body text color**

### Typography System
- `--font-primary: 'Merriweather', serif` - **Headlines and main titles**
- `--font-secondary: 'Inter', sans-serif` - **Body text and UI elements**
- `--font-mono: 'JetBrains Mono', monospace` - **Performance data and tables**

### Google Fonts Import
```css
@import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap');
```

## Typography Scale

### Heading Hierarchy
- `h1`: 2.5rem (40px) - 3rem (48px) desktop | Merriweather, weight 700
- `h2`: 2rem (32px) | Merriweather, weight 400
- `h3`: 1.5rem (24px) | Inter, weight 600

### Body Text
- Base font size: 1rem (16px)
- Line height: 1.6
- Font family: Inter
- Color: var(--charcoal)

### Performance Data
- Font family: JetBrains Mono
- Used for all financial metrics and performance tables

## Layout System

### Container
- `.container` - Max-width: 1200px, centered with auto margins
- Mobile: padding 0 1rem
- Desktop: padding 0 2rem

### Grid Systems
- Mobile-first responsive design
- Single column on mobile
- 2-column on tablet (769px+)
- 3-column on desktop (1025px+)

## Component Classes

### Header & Navigation
- `.site-header` - Sticky header with border bottom
- `.site-logo` - Merriweather font, glenorchy-navy color
- `.nav-menu` - Flex navigation menu
- `.nav-menu a` - Inter font, weight 500, hover: glenorchy-gold

### Buttons (CTA System)
- `.cta-button` - Base button styles
- `.cta-primary` - Background: glenorchy-gold, hover: glenorchy-dark-blue
- `.cta-secondary` - Outline style with glenorchy-navy

### Hero Section
- `.hero-section` - Gradient background, 4rem padding
- `.hero-content` - Grid layout for hero content
- `.hero-tagline` - glenorchy-gold color accent
- `.hero-credentials` - Flex layout for credentials

### Performance Components
- `.performance-snapshot` - White background with shadow
- `.metric-value` - JetBrains Mono, large size, glenorchy-gold
- `.metric-label` - glenorchy-navy, weight 600
- `.metric-period` - warm-grey, smaller size

### Strategy Cards
- `.strategy-card` - White background, rounded corners, hover effects
- `.strategy-type` - glenorchy-gold, uppercase, small size
- `.strategy-metrics` - Grid layout for metrics
- `.strategy-metric-value` - glenorchy-gold color

### Philosophy Section
- `.philosophy-section` - off-white background
- `.philosophy-item` - Individual philosophy cards
- `.philosophy-icon` - SVG icon styling

### Performance Tables
- `.performance-table` - JetBrains Mono font family
- `.positive` - deep-green color for positive returns
- `.negative` - #d32f2f color for negative returns
- Headers: glenorchy-navy background, white text

### Forms
- `.form-section` - glenorchy-navy background
- `.consultation-form` - Form styling with proper spacing
- `.submit-button` - glenorchy-gold background, hover: glenorchy-dark-blue

### Footer
- `.site-footer` - glenorchy-navy background, glenorchy-gold top border
- `.footer-column h4` - glenorchy-gold headings
- `.footer-contact a` - glenorchy-gold links

## Color Usage Guidelines

### Primary Brand Color (Glenorchy Gold #B89676)
- Main CTA buttons
- Links and interactive elements
- Section headings and accents
- Performance metrics
- Footer headings

### Navy (#272727)
- Main headlines and titles
- Form backgrounds
- Footer background
- High contrast text

### Charcoal (#3D3D3D)
- Body text and paragraphs
- Default text color

### Warm Grey (#8A8A8A)
- Secondary text
- Metadata and captions
- Muted content

### Deep Green (#2D5A3D)
- Positive performance numbers
- Success states

## Responsive Breakpoints

### Mobile First Design
- **Base**: < 768px (mobile)
- **Tablet**: 768px+
  - Navigation becomes horizontal
  - 2-column grids
  - Larger hero text
- **Desktop**: 1025px+
  - 3-column grids
  - Maximum content width
  - Enhanced spacing

### Grid Behavior
- Mobile: Single column stack
- Tablet: 2-column layout
- Desktop: 3-column where appropriate

## Interactive States

### Hover Effects
- Cards: `translateY(-2px)` with shadow
- Buttons: Color transition + shadow
- Links: Color change to glenorchy-gold

### Transitions
- Standard: `all 0.3s ease`
- Fast interactions: `0.15s ease`

## Accessibility Features

### Focus States
- Visible focus outlines on all interactive elements
- Keyboard navigation support

### Color Contrast
- All text meets WCAG AA standards
- High contrast mode support

### Typography
- Scalable font sizes
- Readable line heights (1.6)
- Clear font weight hierarchy

## Performance Table Styling

### Table Structure
- `.performance-table` - JetBrains Mono font
- `.performance-table th` - glenorchy-navy background
- `.performance-table td` - Center aligned data
- `.year-cell` - Bold styling for year column
- `.positive` - Green color for gains
- `.negative` - Red color for losses
- `.empty-cell` - Grey styling for N/A data

### Responsive Tables
- Horizontal scroll on mobile
- Smaller font sizes on mobile devices
- Touch-friendly padding

## File Organization

CSS is structured in this order:
1. CSS Variables (colors, fonts, etc.)
2. Reset & Base Styles
3. Typography System
4. Layout Components (container, grids)
5. Header & Navigation
6. Button System
7. Hero Sections
8. Content Sections
9. Performance Components
10. Forms
11. Footer
12. Responsive Design
13. Accessibility Features

This structure ensures consistency and maintainability across the entire website.

## Brand Implementation Notes

- **Primary typeface**: Merriweather for headlines creates professional, trustworthy feel
- **Secondary typeface**: Inter for body text ensures excellent readability
- **Monospace**: JetBrains Mono for all financial data maintains precision and clarity
- **Gold color**: Used strategically for calls-to-action and key metrics to drive conversion
- **Navy**: Provides strong contrast and professional appearance
- **Responsive design**: Mobile-first approach ensures optimal experience across devices