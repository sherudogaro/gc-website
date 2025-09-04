# Glenorchy Capital - CSS Reference Guide

This document provides a comprehensive reference for all CSS classes available in the Glenorchy Capital website design system.

## CSS Variables (Custom Properties)

### Colors
- `--primary-color: #1a365d` - Main brand color
- `--primary-light: #2d5a87` - Light variant
- `--primary-dark: #0f2a44` - Dark variant
- `--secondary-color: #2c5282` - Secondary brand color
- `--accent-color: #3182ce` - Accent/link color
- `--success-color: #38a169` - Success states
- `--warning-color: #d69e2e` - Warning states
- `--error-color: #e53e3e` - Error states

### Text Colors
- `--text-primary: #1a202c` - Main text color
- `--text-secondary: #4a5568` - Secondary text
- `--text-muted: #718096` - Muted text
- `--text-inverse: #ffffff` - Inverse (white) text

### Background Colors
- `--bg-primary: #ffffff` - Main background
- `--bg-secondary: #f7fafc` - Secondary background
- `--bg-dark: #1a202c` - Dark background
- `--bg-light-gray: #edf2f7` - Light gray background

### Typography Scale
- `--text-xs: 0.75rem` (12px)
- `--text-sm: 0.875rem` (14px)
- `--text-base: 1rem` (16px)
- `--text-lg: 1.125rem` (18px)
- `--text-xl: 1.25rem` (20px)
- `--text-2xl: 1.5rem` (24px)
- `--text-3xl: 1.875rem` (30px)
- `--text-4xl: 2.25rem` (36px)
- `--text-5xl: 3rem` (48px)

### Spacing Scale
- `--space-1: 0.25rem` (4px)
- `--space-2: 0.5rem` (8px)
- `--space-3: 0.75rem` (12px)
- `--space-4: 1rem` (16px)
- `--space-5: 1.25rem` (20px)
- `--space-6: 1.5rem` (24px)
- `--space-8: 2rem` (32px)
- `--space-10: 2.5rem` (40px)
- `--space-12: 3rem` (48px)
- `--space-16: 4rem` (64px)
- `--space-20: 5rem` (80px)

## Layout Classes

### Container System
- `.container` - Main content container with max-width and auto margins
  - Mobile: padding 16px
  - Tablet+: padding 24px
  - Max-width: 1280px

### Header & Navigation
- `.main-header` - Site header with sticky positioning and shadow
- `.main-nav` - Navigation wrapper with padding
- `.nav-container` - Navigation inner container with flex layout
- `.logo` - Logo/brand area
- `.nav-menu` - Navigation menu (hidden on mobile)
- `.nav-link` - Navigation links with hover states
- `.nav-link.active` - Active navigation link styling
- `.nav-cta` - Call-to-action button in navigation
- `.mobile-menu-toggle` - Hamburger menu button (mobile only)

### Main Content Areas
- `.main-content` - Main content wrapper
- `.hero-section` - Homepage hero section with gradient background
- `.page-hero` - Interior page hero (smaller than homepage)
- `.value-proposition` - Value proposition section
- `.strategy-overview` - Strategy section layout
- `.performance-overview` - Performance section layout
- `.team-leadership` - Team section layout
- `.contact-section` - Contact form section with gray background

### Footer
- `.main-footer` - Site footer with dark background
- `.footer-content` - Footer content grid
- `.footer-section` - Individual footer column
- `.footer-bottom` - Footer bottom bar with copyright

## Component Classes

### Hero Components
- `.hero-content` - Hero section content wrapper
- `.hero-title` - Main hero headline
- `.hero-subtitle` - Hero description text
- `.hero-cta` - Hero call-to-action button container

### Page Headers
- `.page-header` - Interior page header content
- `.section-header` - Section header with title and description

### Content Grids
- `.value-grid` - Value proposition items grid
- `.value-item` - Individual value proposition item
- `.strategy-grid` - Strategy items grid
- `.strategy-item` - Individual strategy item
- `.methodology-grid` - Methodology items grid
- `.methodology-item` - Individual methodology item
- `.team-grid` - Team members grid
- `.team-member` - Individual team member card

### Team Components
- `.member-photo` - Team member photo container
- `.member-info` - Team member information
- `.member-expertise` - Team member expertise list
- `.team-philosophy` - Team philosophy section
- `.philosophy-content` - Philosophy content wrapper
- `.philosophy-points` - Philosophy points container
- `.philosophy-point` - Individual philosophy point

### Process Components
- `.investment-process` - Process section wrapper
- `.process-steps` - Process steps container
- `.process-step` - Individual process step
- `.step-number` - Process step number styling

### Performance Components
- `.performance-highlights` - Performance highlights grid
- `.performance-item` - Individual performance item
- `.performance-methodology` - Methodology section
- `.performance-access` - Access requirements section
- `.access-content` - Access content wrapper
- `.access-requirements` - Requirements list
- `.requirement-item` - Individual requirement

### Philosophy Components
- `.investment-philosophy` - Philosophy section
- `.philosophy-performance` - Performance philosophy
- `.philosophy-metrics` - Philosophy metrics container
- `.metric-focus` - Individual metric focus item

### CTA Sections
- `.cta-section` - Call-to-action section with gradient background
- `.cta-content` - CTA content wrapper

## Form Classes

### Form Layout
- `.contact-grid` - Contact page grid layout
- `.contact-info` - Contact information section
- `.contact-details` - Contact details container
- `.contact-item` - Individual contact detail
- `.consultation-form` - Main consultation form container

### Form Elements
- `.contact-form` - Form styling
- `.fallback-form` - Fallback form (when Ontraport not loaded)
- `.form-group` - Form field group wrapper
- `.checkbox-group` - Checkbox group with special layout
- `.field-error` - Error message styling (added via JavaScript)

### Form States
- `.error` - Error state for form fields (added via JavaScript)
- `.success-message` - Success message styling (added via JavaScript)

## Button Classes

### Primary Buttons
- `.btn` - Base button styling
- `.btn-primary` - Primary button (blue background)
- `.btn-secondary` - Secondary button (outline style)

### Button States
- All buttons include hover effects with transform and shadow
- Focus states for accessibility
- Disabled states supported

## Legal Page Classes

- `.legal-page` - Legal page wrapper with padding
- `.legal-content` - Legal content container (narrower width)
- `.legal-section` - Individual legal section
- `.warning-box` - Warning/disclaimer box with yellow background
- `.last-updated` - Last updated timestamp styling
- `.contact-info` - Contact information in legal pages
- `.legal-footer` - Legal page footer section

## Disclaimer Components

- `.disclaimer-content` - Disclaimer content wrapper
- `.performance-disclaimer` - Performance disclaimer box
- `.investment-disclaimer` - Investment disclaimer section

## Utility Classes

### Text Alignment
- `.text-center` - Center align text
- `.text-left` - Left align text
- `.text-right` - Right align text

### Spacing Utilities
- `.mb-0` - Margin bottom: 0
- `.mb-4` - Margin bottom: 16px
- `.mb-8` - Margin bottom: 32px
- `.mt-0` - Margin top: 0
- `.mt-4` - Margin top: 16px
- `.mt-8` - Margin top: 32px

## Responsive Breakpoints

### Mobile First Approach
- **Base styles**: Mobile (< 768px)
- **Tablet**: 768px and up
  - Navigation becomes horizontal
  - Grids become 2-column
  - Hero title larger
- **Desktop**: 1024px and up
  - Grids become 3-column
  - Maximum hero size
  - Full desktop layout

### Grid Responsive Behavior
- **Mobile**: All grids are single column
- **Tablet**: 2-column grids for most content
- **Desktop**: 3-column grids where appropriate

## Hover Effects and Interactions

### Standard Hover Effects
- Cards lift up slightly (`translateY(-4px)`)
- Buttons transform with shadow
- Links change color and may underline
- Navigation items get background color

### Transition System
- `--transition: all 0.3s ease` - Standard transitions
- `--transition-fast: all 0.15s ease` - Fast transitions

## Accessibility Features

### Focus States
- All interactive elements have visible focus outlines
- Focus outline: 3px solid accent color with 2px offset

### Reduced Motion
- Respects `prefers-reduced-motion: reduce`
- Animations disabled for users with motion sensitivity

### High Contrast Mode
- Support for `prefers-contrast: high`
- Colors adjusted for better contrast

## Browser Support

### Modern Browser Features Used
- CSS Grid Layout
- CSS Custom Properties (Variables)
- CSS Transforms
- Modern CSS Selectors

### Fallbacks Provided
- Flexbox fallbacks for older browsers
- Print styles included
- Progressive enhancement approach

## Print Styles

- Navigation and interactive elements hidden
- Text optimized for print
- Container constraints removed
- Font sizes adjusted for print media

## Usage Examples

### Basic Page Structure
```html
<header class="main-header">
  <nav class="main-nav">
    <div class="nav-container">
      <!-- Navigation content -->
    </div>
  </nav>
</header>

<main class="main-content">
  <section class="hero-section"> <!-- or .page-hero for interior pages -->
    <div class="container">
      <!-- Content -->
    </div>
  </section>
</main>

<footer class="main-footer">
  <div class="container">
    <!-- Footer content -->
  </div>
</footer>
```

### Content Section
```html
<section class="value-proposition">
  <div class="container">
    <div class="section-header">
      <h2>Section Title</h2>
      <p>Section description</p>
    </div>
    <div class="value-grid">
      <div class="value-item">
        <h3>Item Title</h3>
        <p>Item content</p>
      </div>
      <!-- More items -->
    </div>
  </div>
</section>
```

### CTA Section
```html
<section class="cta-section">
  <div class="container">
    <div class="cta-content">
      <h2>CTA Headline</h2>
      <p>CTA description</p>
      <a href="#" class="btn btn-primary">Action Button</a>
    </div>
  </div>
</section>
```

## File Organization

The CSS is organized in the following order:
1. CSS Variables
2. Reset & Base Styles
3. Typography
4. Layout Components
5. Header & Navigation
6. Buttons
7. Hero Section
8. Page Components
9. Forms
10. Footer
11. Legal Pages
12. Utility Classes
13. CTA Sections
14. Responsive Design (Tablet)
15. Responsive Design (Desktop)
16. Print Styles
17. Accessibility Improvements

This organization makes it easy to find and modify specific components while maintaining consistency across the entire website.