# DefiPrime Blog Image Style Guide

Visual reference for generating consistent blog post graphics with AI tools.

---

## Color Palette

### Brand Colors

| Role | Hex | Swatch | Usage |
|------|------|--------|-------|
| **Navy (Primary)** | `#292984` | ![#292984](https://placehold.co/20x20/292984/292984) | Headings, logo text, primary identity |
| **Purple (Accent)** | `#8F68FC` | ![#8F68FC](https://placehold.co/20x20/8F68FC/8F68FC) | Links, CTAs, secondary brand color |
| **Cyan / Teal** | `#05D2DD` | ![#05D2DD](https://placehold.co/20x20/05D2DD/05D2DD) | Accent highlights, positive indicators |
| **Orange** | `#FF961C` | ![#FF961C](https://placehold.co/20x20/FF961C/FF961C) | Tertiary accent, alerts, warmth |

### Extended Palette

| Role | Hex | Usage |
|------|------|-------|
| Light Blue | `#7ECAF6` | Secondary accent in diagrams |
| Mint | `#7BD0C1` | Tertiary accent in diagrams |
| Pink | `#C75B9B` | Highlight accent |
| Lavender | `#AE85CA` | Soft accent |
| Periwinkle | `#8499E7` | Soft accent |
| Deep Blue | `#2D5888` | Dark gradient base |
| Banner Blue | `#2266A2` | Gradient midtone |
| Neon Cyan | `#23FFE9` | Glow effects on dark backgrounds |

### Neutrals

| Role | Hex | Usage |
|------|------|-------|
| White | `#FFFFFF` | OGP backgrounds |
| Off-white | `#F6F6F6` | Alternate backgrounds |
| Light border | `#EAEAF3` | Subtle separators |
| Body text | `#585858` | Paragraph text |
| Muted | `#8B8BB8` | Captions, secondary text |
| Dark gray | `#333333` | Strong body text |
| Black | `#000000` | Rarely used directly |

### Dark Background Palette (for inline diagrams)

| Role | Hex | Usage |
|------|------|-------|
| Dark navy base | `#0D1B2A` – `#1B2838` | Primary dark backgrounds |
| Dark gradient start | `#141E30` | Gradient dark end |
| Dark gradient end | `#243B55` | Gradient lighter end |
| Subtle grid lines | `rgba(255,255,255,0.05)` | Background grid/texture |

---

## Typography

### Font Families

| Role | Font | Weight | Style |
|------|------|--------|-------|
| **Headings** | Kanit | 500 (Medium) | Sans-serif, slightly condensed feel |
| **Body** | Open Sans / Source Sans Pro | 300–400 | Clean, readable sans-serif |
| **Display / Banner** | Baloo Bhai 2 | 600–800 | Rounded, friendly (limited use) |
| **Monospace** | Courier New / Menlo | 400 | Code blocks |

### Heading Behavior

- All-caps with wide letter-spacing (`0.35em`) for section labels
- Title case for blog post titles
- Color: Navy `#292984` for titles on light backgrounds, white `#FFFFFF` on dark backgrounds

---

## Image Types & Specifications

### 1. OGP / Header Images (Featured Image)

**Dimensions:** 1200 x 630 px (2:1.05 ratio)
**Used in:** Social sharing cards (og:image, twitter:image), blog hero banner
**File naming:** `{slug}-ogp.png`
**Frontmatter:** `featured-image: /images/blog/{slug}-ogp.png`

**Visual Template:**
- **Background:** Clean white (`#FFFFFF`) with subtle off-white tint
- **Logo:** DefiPrime cross-mark logo + "defiprime.com" wordmark, positioned top-left corner (~60px from edges)
- **Title:** Large navy (`#292984`) text, left-aligned, positioned in the lower-left quadrant. Font: bold sans-serif (Kanit-style), 48–64px equivalent
- **Decorative element:** Thin vertical lines/bars in brand palette colors (purple, cyan, orange, light blue, peach) scattered across the right side of the image. Lines are slightly translucent, varying heights, spaced irregularly — creating a subtle abstract "data visualization" feel
- **No:** heavy gradients, stock photos, or busy backgrounds

### 2. Inline Diagrams / Infographics

**Dimensions:** 1024 x 576 px (16:9) or similar widescreen ratio
**Used in:** Within blog post body as explanatory visuals
**File naming:** `{topic}-{descriptor}.png`

**Visual Template:**
- **Background:** Deep dark navy gradient (`#0D1B2A` → `#1B2838` → `#243B55`), sometimes with a faint grid pattern or subtle radial glow
- **Illustration style:** Modern flat/semi-flat vector iconography. Clean geometric shapes. Slight 3D depth through layering and subtle glow effects
- **Color coding:** Green/teal for "positive/pass/success," red for "negative/fail/risk," gold/amber for "neutral/curator/authority," blue for "protocol/system"
- **Flow direction:** Left-to-right for process flows, using arrow connectors in brand colors (cyan, green)
- **Cards/panels:** Rounded-corner rectangles with subtle borders, slightly lighter than background. Drop shadow or soft glow for depth
- **Typography on dark BG:** White for headings, light gray for body. Bold sans-serif for labels, uppercase for category headers
- **Icons:** Outlined/flat-fill style, using brand accent colors. Shield icons for security, gear icons for mechanics, chart icons for data, lock icons for on-chain enforcement

---

## Backgrounds & Textures

### Light (OGP images)

```
Background: #FFFFFF
Decorative vertical lines: thin bars (2-4px wide) in #8F68FC, #05D2DD, #FF961C, #7ECAF6, #FFD4A8
Lines are 40-80% opacity, random heights (30-90% of canvas height)
Positioned primarily on right half of image
```

### Dark (Inline diagrams)

```
Background gradient: linear-gradient(135deg, #0D1B2A 0%, #1B2838 50%, #243B55 100%)
Optional: faint concentric circles or radial glow from center in rgba(5, 210, 221, 0.05)
Optional: subtle dot grid at rgba(255, 255, 255, 0.03)
```

---

## Logo Usage

The DefiPrime logo is a geometric cross-mark composed of four quadrants:

| Quadrant | Color | Hex |
|----------|-------|-----|
| Top-left | Navy | `#292984` |
| Top-right | Purple | `#8F68FC` |
| Bottom-right | Cyan | `#05D2DD` |
| Bottom-left | Orange | `#FF961C` |

The wordmark "defiprime.com" uses:
- "defi" in navy `#292984`
- "prime.com" in purple `#8F68FC`
- Plus a period/dot after "prime" in navy

**Logo placement on OGP images:** Top-left corner, with approximately 40-60px padding from edges. Logo mark (~46px tall) followed by wordmark.

---

## Tone & Personality

- **Editorial and authoritative** — not playful or meme-driven
- **Data-informed** — charts, comparisons, and structured information
- **Clean and professional** — minimal visual clutter
- **DeFi-native** — comfortable with protocol names, TVL metrics, yield terminology
- **No stock photography** — all graphics are illustrations, diagrams, or data visualizations

---

## Reusable AI Prompt Templates

### Template 1: OGP / Social Share Image

```
Create a clean blog header image at 1200x630px for a DeFi finance website.

Background: Pure white (#FFFFFF).

Top-left corner: Place a small geometric cross logo made of four colored squares
(navy #292984, purple #8F68FC, cyan #05D2DD, orange #FF961C) followed by the
text "defiprime.com" in navy and purple.

Main text: "[YOUR TITLE HERE]" in large bold dark navy (#292984) sans-serif font,
left-aligned, positioned in the center-left area of the image.

Right side decoration: Scatter thin vertical bars/lines (2-4px wide, varying
heights from 30-90% of image height) in soft translucent brand colors: purple
(#8F68FC at 40% opacity), cyan (#05D2DD at 50% opacity), orange (#FF961C at 30%
opacity), light blue (#7ECAF6 at 40% opacity), and peach/light orange at 30%
opacity. Lines should be irregularly spaced across the right 40% of the image,
creating a subtle abstract data-visualization aesthetic.

Style: Minimal, professional, fintech editorial. No gradients, no photography,
no busy elements. Clean white space.
```

### Template 2: Inline Process Flow Diagram

```
Create a technical process flow diagram at 1024x576px for a DeFi blog article.

Background: Dark navy gradient from #0D1B2A to #1B2838, with a very subtle
radial glow in the center using rgba(5, 210, 221, 0.03).

Layout: Left-to-right horizontal flow with 3-5 stages connected by directional
arrows in cyan (#05D2DD).

Each stage is represented by a rounded-corner card/panel with:
- A subtle border in rgba(255, 255, 255, 0.1)
- Background slightly lighter than the main background
- A flat-style icon at the top in a brand accent color
- A bold white uppercase label
- 1-3 bullet points in light gray

Color coding:
- Green (#05D2DD) for positive/active elements
- Red/coral for negative/risk elements
- Gold/amber for authority/curator elements
- Blue (#7ECAF6) for system/protocol elements

Title: "[YOUR DIAGRAM TITLE]" centered at top in white bold sans-serif, with a
lighter subtitle beneath.

Style: Modern flat vector, semi-technical, clean and readable. DeFi/blockchain
infographic aesthetic. No photorealism.
```

### Template 3: Data Comparison / Stats Overview

```
Create a data comparison infographic at 1024x576px for a DeFi analytics blog.

Background: Deep blue gradient from #141E30 to #243B55, with subtle radial
light from center.

Central element: A large iconic illustration related to [YOUR TOPIC — e.g.,
vault door, blockchain, scale/balance] in a semi-flat style using muted blues
and cyans with subtle glow effects.

Surrounding the center: 4-6 floating data cards/browser-window-style panels,
each containing:
- A protocol/project name in bold white
- A key metric (e.g., "$5.8B") in large bold text
- Optional small bar chart or trend indicator
- Card background: subtle glass-morphism (semi-transparent with blur effect)

Title: "[YOUR TITLE — e.g., DeFi Lending TVL Leaders — March 2026]" in large
white bold sans-serif, centered at the top.

Accent colors: Use cyan (#05D2DD), purple (#8F68FC), and light blue (#7ECAF6)
for glows, borders, and highlights.

Style: Modern fintech dashboard aesthetic, dark theme, clean data presentation.
No clutter.
```

### Template 4: Conceptual / Ecosystem Illustration

```
Create a conceptual illustration at 1024x576px for a DeFi blog article about
[YOUR TOPIC].

Background: Dark navy (#0D1B2A) with subtle geometric patterns (thin lines or
dot grid at very low opacity).

Main illustration: A central metaphorical visual representing [YOUR CONCEPT]
using flat/semi-flat vector art. Use the brand palette:
- Navy (#292984) and dark blue for foundations
- Cyan (#05D2DD) for connectivity and flow
- Purple (#8F68FC) for governance/protocol elements
- Orange (#FF961C) for user/human elements
- Green for positive outcomes, red for risks

Supporting elements: Small icons scattered around (shields, gears, coins, charts,
locks) in outlined style with brand accent fills.

Text labels: Short uppercase labels in white next to key elements, using a clean
sans-serif font.

Style: Modern blockchain/DeFi editorial illustration. Technical but accessible.
Professional, not cartoonish. Dark theme with vibrant accent colors.
```

---

## File Organization

```
images/blog/
├── {topic}-ogp.png          # OGP / social share header (1200x630)
├── {topic}-{concept}.png    # Inline diagram or illustration (1024x576)
└── post.png                 # Fallback/default OGP image
```

### Frontmatter Reference

```yaml
---
layout: blog
title: "Your Blog Post Title"
permalink: your-post-slug
h1title: "Your Blog Post Title"
pagetitle: "Your Blog Post Title"
featured-image: /images/blog/{slug}-ogp.png
tags: ["DeFi"]
author: Your Name
date: 2026-03-04
---
```

---

## Do's and Don'ts

### Do

- Use the navy + purple + cyan + orange palette consistently
- Keep OGP images clean, minimal, with plenty of white space
- Use dark backgrounds for inline technical diagrams
- Apply consistent color coding (green = positive, red = negative, gold = authority)
- Include the defiprime.com logo on OGP images
- Use flat/semi-flat vector illustration style
- Keep text large and readable at small sizes (social previews render at ~600px wide)

### Don't

- Use stock photography or photorealistic renders
- Use colors outside the brand palette for primary elements
- Add heavy drop shadows, bevels, or skeuomorphic effects
- Use light backgrounds for inline diagrams (these should be dark)
- Make OGP images dark-themed (these should be white/light)
- Include more than 2-3 lines of text on an OGP image
- Use memes, emojis, or overly casual visual elements
