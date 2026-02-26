# DeFiPrime.com - Project Context

## Overview
DeFiPrime is a Jekyll 4.3 static site covering DeFi products, blog posts, and educational content. Deployed on Netlify at https://defiprime.com.

## Tech Stack
- **Framework**: Jekyll 4.3 (Ruby 3.1)
- **Hosting**: Netlify
- **Search**: Algolia
- **CSS**: Sass (compressed)
- **Plugins**: jekyll-paginate-v2, jekyll-sitemap, jekyll-feed, jekyll-toc, jekyll-algolia, jekyll-lazy-load-image, jekyll-tagging

## Project Structure
```
_config.yml          # Jekyll configuration
_layouts/            # Page layouts (blog.html, product.html, ecosystem.html, etc.)
_includes/           # Partials (header, footer, head, sidepanel, etc.)
_sass/               # Stylesheets
_data/authors.yml    # Author data
_plugins/            # Custom Jekyll plugins
collections/         # All content collections:
  _posts/            # Blog posts (~409 articles)
  _lending/          # DeFi lending products
  _exchanges/        # DEX products
  _derivatives/      # Derivatives products
  _stablecoins/      # Stablecoins
  _insurance/        # DeFi insurance
  _infrastructure/   # Infrastructure projects
  _analytics/        # Analytics tools
  _airdrops/         # Airdrop listings
  ... (20+ collections)
images/              # All images
assets/              # JS/CSS assets
```

## Content Conventions

### Blog Posts
- Location: `collections/_posts/`
- Filename: `YYYY-MM-DD-slug.md`
- Front matter:
  ```yaml
  ---
  git-date:
  layout: [blog]
  title: "Post Title"
  permalink: slug-here
  h1title: "Post Title"
  pagetitle: "Post Title"
  metadescription: "SEO description"
  category: blog
  featured-image: /images/blog/image.png
  intro: "First paragraph / summary"
  author: sawinyh
  tags: ["Tag1", "Tag2"]
  ---
  ```

### Product Listings
- Location: `collections/_<category>/`
- Front matter:
  ```yaml
  ---
  git-date: YYYY-MM-DDTHH:MM:SS-TZ
  product-title: Product Name
  product-url: https://...
  image: /images/output_md/domain.png
  ecosystem: ethereum, polygon, ...
  product-description: "Description with [links](/path)"
  type: non-custodial
  filter: Category1, Category2
  coltitle: "Collection Title"
  colpermalink: url-slug
  twitter: https://twitter.com/handle
  github: https://github.com/org/repo
  ticker: TOKEN
  contract: "0x..."
  decimals: 18
  ---
  ```

## Commands
- `bundle exec jekyll serve` — Local dev server
- `bundle exec jekyll build` — Build site
- `bundle exec jekyll algolia` — Update Algolia search index

## Rules
- Always preserve existing front matter fields when editing content
- Image paths use `/images/` prefix
- Blog permalinks should be short, lowercase, hyphenated slugs (no trailing slash in front matter)
- Product images follow pattern: `/images/output_md/domain.png`
- Keep blog intro concise (1-2 sentences)
- Tags use title case inside arrays: `["DeFi Guides", "Governance"]`
