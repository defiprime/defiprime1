# Plans — Jekyll → Hugo Migration

> **Branch:** `hugo`
> **Goal:** Migrate defiprime.com from Jekyll 4.3 to Hugo while preserving 100% of design, URLs, functionality, and front matter.

---

## Phase 0: Setup & Baseline Test Suite

- [ ] `cc:TODO` **P0.1** Create `hugo` branch from `master`
- [ ] `cc:TODO` **P0.2** Build Jekyll site, capture full output for baseline comparison (`_site/`)
- [ ] `cc:TODO` **P0.3** Create test infrastructure: `tests/` directory with test runner (shell/Node)
- [ ] `cc:TODO` **P0.4** Write URL inventory test — crawl Jekyll `_site/`, extract all output URLs (~600+ pages), save as `tests/fixtures/url-inventory.txt`
- [ ] `cc:TODO` **P0.5** Write front matter parity tests — for each content type, validate all 47 front matter fields are preserved in Hugo output
- [ ] `cc:TODO` **P0.6** Write HTML structure comparison tests — extract key DOM elements (titles, meta tags, OG tags, canonical URLs, JSON-LD, nav, footer) from Jekyll output as golden fixtures

---

## Phase 1: Hugo Project Scaffolding

- [ ] `cc:TODO` **P1.1** Initialize Hugo project structure at repo root (hugo.toml, content/, layouts/, static/, assets/, data/)
- [ ] `cc:TODO` **P1.2** Configure `hugo.toml` with site metadata (title, baseURL, description, params matching _config.yml)
- [ ] `cc:TODO` **P1.3** Configure permalink patterns to match Jekyll URLs exactly:
  - Blog posts: `/:slug` (root-level, custom permalink per post)
  - Products: `/product/:filename` (all 18 product collections)
  - Airdrops: `/airdrop/:title` (preserving title case)
  - Tag pages: `/t/:slug.html`
  - Blog pagination: `/blog/`, `/blog/2/`, `/blog/3/`
- [ ] `cc:TODO` **P1.4** Configure Hugo taxonomies for tags (`tag_page_dir: t`, `.html` suffix)
- [ ] `cc:TODO` **P1.5** Configure Hugo outputs: HTML, RSS (`feed.xml` at root, 5 posts), sitemap.xml
- [ ] `cc:TODO` **P1.6** Set up aliases (redirects) in hugo.toml or per-page front matter:
  - `/product` → `/`
  - `/decentralized_lending` → `/decentralized-lending`
  - `/analytics` → `/defi-analytics`
  - `/decentralized_prediction_markets` → `/prediction-markets`
  - `/custodian_services` → `/assets-management-tools`
  - `/assets-managament-tools` → `/assets-management-tools`
  - `/posbakerz` → `/stakin`
  - `/sdpsaver` → `/cdpsaver`
- [ ] `cc:TODO` **P1.7** Enable `enableGitInfo: true` for git-date equivalent
- [ ] `cc:TODO` **P1.8** Set up `data/authors.yaml` from `_data/authors.yml`

---

## Phase 2: Content Migration

### 2.1 Blog Posts (409 files)
- [ ] `cc:TODO` **P2.1** Write migration script: `scripts/migrate-posts.sh`
  - Move `collections/_posts/*.md` → `content/blog/`
  - Convert front matter: `layout: [blog]` → `layout: blog`, preserve all 13 blog fields
  - Convert `redirect_from` → Hugo `aliases`
  - Preserve `permalink` as `url` in Hugo front matter
  - Handle `quote` field (optional, ~97 posts)
  - Normalize `tags` quoting (single→double quotes)
- [ ] `cc:TODO` **P2.2** Migrate "category: products" posts (18 listing pages) separately → `content/` root as standalone pages with `layout: page`

### 2.2 Product Collections (18 collections, ~300+ files)
- [ ] `cc:TODO` **P2.3** Write migration script: `scripts/migrate-products.sh`
  - Map each Jekyll collection to Hugo section: `collections/_lending/` → `content/product/lending/`
  - All product pages output at `/product/:filename`
  - Preserve all 20 product front matter fields exactly
  - Handle `GitHub` vs `github` casing inconsistency
  - Handle `alternative-to` as both string and array
  - Handle `platform` field (assets-management-tools only)
  - Handle `long-description` field (LooksRare only)
  - Set `type: product` layout via section defaults in hugo.toml

### 2.3 Airdrops (7 files)
- [ ] `cc:TODO` **P2.4** Migrate `collections/_airdrops/` → `content/airdrop/`
  - Preserve all 15 airdrop-specific fields
  - Map `permalink: "/airdrop/:title"` → Hugo `url` with title case

### 2.4 Alternatives (15 files)
- [ ] `cc:TODO` **P2.5** Migrate `collections/_alternatives/` → `content/alternatives/`
  - Each file has custom permalink override (e.g., `1inch-alternatives`)
  - Preserve `alternative-to`, `filter-by`, `og` fields

### 2.5 Events (5 files)
- [ ] `cc:TODO` **P2.6** Migrate `collections/_events/` → `content/events/`
  - Events do NOT output individual pages (headless bundle in Hugo: `_index.md` with `render: never`)
  - Preserve `date`, `location` fields

### 2.6 Top-level Pages (25+ files)
- [ ] `cc:TODO` **P2.7** Migrate ecosystem pages (12 files) → `content/` with `layout: ecosystem`
- [ ] `cc:TODO` **P2.8** Migrate static/utility pages (about, 404, tokenlist, etc.) → `content/` with appropriate layouts
- [ ] `cc:TODO` **P2.9** Migrate blog.md with pagination config → `content/blog/_index.md`

---

## Phase 3: Layout & Template Conversion (Liquid → Go Templates)

### 3.1 Base Layouts
- [ ] `cc:TODO` **P3.1** Convert `_layouts/default.html` → `layouts/_default/baseof.html` + `layouts/index.html`
  - `{% include_cached %}` → `{{ partialCached }}`
  - `{{ page.x }}` → `{{ .Params.x }}`
  - Organization JSON-LD schema
- [ ] `cc:TODO` **P3.2** Convert `_layouts/blog.html` → `layouts/blog/single.html`
  - Author data lookup: `site.data.authors[page.author]` → `index site.Data.authors .Params.author`
  - `{{ content | toc }}` → `{{ .TableOfContents }}` + `{{ .Content }}`
  - `| sample:4` → custom shuffle+first template function
  - `| date_to_xmlschema` → `.Date.Format "2006-01-02T15:04:05-07:00"`
  - AMP URL filtering logic
  - BlogPosting JSON-LD schema
- [ ] `cc:TODO` **P3.3** Convert `_layouts/product.html` → `layouts/product/single.html`
  - Dynamic collection access `site[page.collection]` → Hugo section-based lookup
  - Conditional fields (analytics, twitter, github, ticker, contract, alternative-to)
  - `| markdownify`, `| textilize`, `| slugify: 'latin'` conversions
  - BreadcrumbList + Product JSON-LD schemas
- [ ] `cc:TODO` **P3.4** Convert `_layouts/page.html` → `layouts/_default/page.html`
  - **Most complex layout** — product card grid with dynamic filtering
  - `site[page.cards]` → parameterized section lookup
  - Filter button generation from `filter-by` field
  - Ecosystem/platform/type icon case-when logic
  - Critical CSS inlining + async CSS loading JS
  - Client-side filtering (page.js integration)
- [ ] `cc:TODO` **P3.5** Convert `_layouts/ecosystem.html` → `layouts/ecosystem/single.html`
  - Sidepanel ToC + jekyll-toc → Hugo `.TableOfContents`
- [ ] `cc:TODO` **P3.6** Convert `_layouts/blog-list.html` → `layouts/blog/list.html`
  - Pagination: `paginator.posts` → `.Paginator.Pages`
- [ ] `cc:TODO` **P3.7** Convert `_layouts/tag_page.html` → `layouts/taxonomy/tag.html`
  - `page.posts` → `.Pages`
  - Author lookups, tag links, AMP filtering
- [ ] `cc:TODO` **P3.8** Convert `_layouts/airdrop.html` → `layouts/airdrop/single.html`
  - `| capitalize`, conditional reflink logic
- [ ] `cc:TODO` **P3.9** Convert `_layouts/alternatives.html` → `layouts/alternatives/single.html`
  - **Mega-concat of all product collections** → `site.GetPage` / `where` across sections
  - Client-side JS for alternatives loading/filtering
- [ ] `cc:TODO` **P3.10** Convert `_layouts/events.html` → `layouts/events/single.html`
  - Future event filtering: `event.date < site.time` → date comparison in Go templates
- [ ] `cc:TODO` **P3.11** Convert `_layouts/static.html` → `layouts/static/single.html`
- [ ] `cc:TODO` **P3.12** Convert `_layouts/stats.html` → `layouts/stats/single.html`
- [ ] `cc:TODO` **P3.13** Convert `_layouts/basic.html` → `layouts/basic/single.html`

### 3.2 Partials (Includes)
- [ ] `cc:TODO` **P3.14** Convert `_includes/header.html` → `layouts/partials/header.html`
  - Conditional Algolia search loading
- [ ] `cc:TODO` **P3.15** Convert `_includes/footer.html` → `layouts/partials/footer.html`
  - SVG icon includes, script loading
- [ ] `cc:TODO` **P3.16** Convert `_includes/head.html` → `layouts/partials/head.html`
- [ ] `cc:TODO` **P3.17** Convert `_includes/sidepanel.html` → `layouts/partials/sidepanel.html`
  - tocbot.js integration
- [ ] `cc:TODO` **P3.18** Convert `_includes/algolia.html` → `layouts/partials/algolia.html`
  - Site config variable access for Algolia credentials
- [ ] `cc:TODO` **P3.19** Convert `_includes/also.html` → `layouts/partials/also.html`
  - `site.collections` iteration → Hugo sections with doc counts
- [ ] `cc:TODO` **P3.20** Convert `_includes/author_bio.html` → `layouts/partials/author_bio.html`
- [ ] `cc:TODO` **P3.21** Convert `_includes/blog-readmore.html` → `layouts/partials/blog-readmore.html`
  - Random post sampling
- [ ] `cc:TODO` **P3.22** Convert `_includes/figure.html` → `layouts/shortcodes/figure.html`
- [ ] `cc:TODO` **P3.23** Convert `_includes/critical.css` → `layouts/partials/critical.css`
- [ ] `cc:TODO` **P3.24** Convert `_includes/ecosystem-icons.html` → `layouts/partials/ecosystem-icons.html`
- [ ] `cc:TODO` **P3.25** Convert `_includes/folowus.html` → `layouts/partials/folowus.html`
- [ ] `cc:TODO` **P3.26** Migrate all 34 SVG icons → `layouts/partials/icons/`
- [ ] `cc:TODO` **P3.27** Convert `_includes/tooltipster.bundle.min.css` → inline partial

### 3.3 Custom Plugin Equivalents
- [ ] `cc:TODO` **P3.28** Replace `multipost.rb` — use Hugo output formats for `layout: [blog]` array handling
- [ ] `cc:TODO` **P3.29** Replace `sidepanel_toc_generator.rb` → Hugo built-in `.TableOfContents`
- [ ] `cc:TODO` **P3.30** Replace `hook-add-last-modified-date.rb` → `enableGitInfo: true` + `.GitInfo.AuthorDate`
- [ ] `cc:TODO` **P3.31** Implement `jekyll-random` equivalents — custom template functions for `sample:N`, `random_number`, `random_item`
- [ ] `cc:TODO` **P3.32** Configure Hugo image render hook for lazy loading (replaces `jekyll-lazy-load-image`)

---

## Phase 4: Assets Migration

- [ ] `cc:TODO` **P4.1** Move `_sass/` → `assets/scss/` (Hugo Pipes Sass)
- [ ] `cc:TODO` **P4.2** Configure Hugo Pipes for Sass compilation (compressed output)
- [ ] `cc:TODO` **P4.3** Move `assets/js/` → `assets/js/` (preserve main.js, page.js, etc.)
- [ ] `cc:TODO` **P4.4** Move `images/` → `static/images/` (preserve all image paths)
- [ ] `cc:TODO` **P4.5** Move static files (favicon.ico, favicon.png, robots.txt) → `static/`
- [ ] `cc:TODO` **P4.6** Move `defiprime.tokenlist.json` → `static/`

---

## Phase 5: Deployment Configuration

- [ ] `cc:TODO` **P5.1** Update `netlify.toml` for Hugo build:
  - Build command: `hugo --minify`
  - Hugo version environment variable
  - Preserve CORS headers
- [ ] `cc:TODO` **P5.2** Update `vercel.json` if needed (cleanUrls equivalent)
- [ ] `cc:TODO` **P5.3** Configure Algolia indexing for Hugo output (manual script or hugo-algolia)

---

## Phase 6: Comprehensive Test Suite [feature:tdd]

### 6.1 URL Parity Tests
- [ ] `cc:TODO` **P6.1** Test: every URL from Jekyll `url-inventory.txt` exists in Hugo output
- [ ] `cc:TODO` **P6.2** Test: all 8 redirect URLs return 301 to correct destination
- [ ] `cc:TODO` **P6.3** Test: blog pagination URLs `/blog/`, `/blog/2/`...`/blog/N/` all exist with 16 posts per page
- [ ] `cc:TODO` **P6.4** Test: tag page URLs `/t/{tag}.html` all exist for all tags used in posts

### 6.2 Front Matter / Content Parity Tests
- [ ] `cc:TODO` **P6.5** Test: blog post front matter — all 13 fields preserved (git-date, layout, title, permalink, h1title, pagetitle, metadescription, category, featured-image, intro, author, tags, quote)
- [ ] `cc:TODO` **P6.6** Test: product front matter — all 20 fields preserved (including optional ticker, contract, decimals, analytics, alternative-to, featured, platform)
- [ ] `cc:TODO` **P6.7** Test: airdrop front matter — all 15 fields preserved (twitter_handle, raised, investors, todo, reflink, project_url)
- [ ] `cc:TODO` **P6.8** Test: alternatives front matter — all fields preserved (alternative-to, filter-by, og)
- [ ] `cc:TODO` **P6.9** Test: events front matter — date, location, product-title, image preserved
- [ ] `cc:TODO` **P6.10** Test: ecosystem page front matter — all 8 fields preserved

### 6.3 HTML Output Parity Tests
- [ ] `cc:TODO` **P6.11** Test: `<title>` tags match between Jekyll and Hugo output for all pages
- [ ] `cc:TODO` **P6.12** Test: `<meta name="description">` matches for all pages
- [ ] `cc:TODO` **P6.13** Test: OG meta tags (og:title, og:description, og:image, og:url) match
- [ ] `cc:TODO` **P6.14** Test: canonical URLs match
- [ ] `cc:TODO` **P6.15** Test: JSON-LD structured data (Organization, BlogPosting, Product, BreadcrumbList) present and valid
- [ ] `cc:TODO` **P6.16** Test: RSS feed at `/feed.xml` has correct structure and 5 most recent posts
- [ ] `cc:TODO` **P6.17** Test: sitemap.xml contains all URLs
- [ ] `cc:TODO` **P6.18** Test: 404 page renders at `/404.html`

### 6.4 Layout / Visual Parity Tests
- [ ] `cc:TODO` **P6.19** Test: blog post pages contain ToC, author bio, "read more" section, tag links
- [ ] `cc:TODO` **P6.20** Test: product pages contain all conditional sections (analytics embed, twitter/github links, token info, alternative links)
- [ ] `cc:TODO` **P6.21** Test: category listing pages render product cards with correct filter buttons and ecosystem icons
- [ ] `cc:TODO` **P6.22** Test: homepage sections present (DeFi Projects grid, Recently Added, Latest Blog, Upcoming Events)
- [ ] `cc:TODO` **P6.23** Test: Algolia search integration loads correctly
- [ ] `cc:TODO` **P6.24** Test: lazy loading attributes (`data-src`, `lazyload` class) present on images

### 6.5 Build & Performance Tests
- [ ] `cc:TODO` **P6.25** Test: `hugo build` completes without errors or warnings
- [ ] `cc:TODO` **P6.26** Test: total page count matches Jekyll output (±0)
- [ ] `cc:TODO` **P6.27** Test: no broken internal links (run link checker on Hugo output)

---

## Phase 7: Final Validation & Cleanup

- [ ] `cc:TODO` **P7.1** Side-by-side visual comparison of 10 representative pages (homepage, blog post, product page, category listing, ecosystem, airdrop, alternatives, events, tag page, 404)
- [ ] `cc:TODO` **P7.2** Remove Jekyll-specific files from Hugo branch (Gemfile, Gemfile.lock, _plugins/, gems/)
- [ ] `cc:TODO` **P7.3** Update README.md with Hugo build/dev instructions
- [ ] `cc:TODO` **P7.4** Run full test suite — all green
- [ ] `cc:TODO` **P7.5** Document any known differences or trade-offs in migration notes

---

## Priority Matrix

| Priority | Tasks | Rationale |
|----------|-------|-----------|
| **Required** | P0 (all), P1 (all), P2 (all), P3.1-P3.13, P3.14-P3.27, P4 (all), P6.1-P6.4, P6.25-P6.27 | Core migration — site must build and all URLs must work |
| **Required** | P3.28-P3.32, P6.5-P6.18 | Plugin equivalents and content parity — nothing can be lost |
| **Recommended** | P5 (all), P6.19-P6.24, P7.1-P7.3 | Deploy config and visual verification |
| **Optional** | P7.4-P7.5 | Polish and documentation |

---

## Technical Notes

### Front Matter Field Count by Content Type
| Type | Fields | Count |
|------|--------|-------|
| Blog (article) | git-date, layout, title, permalink, h1title, pagetitle, metadescription, category, featured-image, intro, author, tags, quote | 13 |
| Blog (category listing) | git-date, layout, title, permalink, h1title, pagetitle, metadescription, category, cards, filter-by, og, redirect_from | 12 |
| Products | git-date, product-title, product-url, image, product-description, ecosystem, coltitle, colpermalink, twitter, github, filter, type, ticker, contract, decimals, analytics, alternative-to, featured, platform, long-description | 20 |
| Airdrops | git-date, layout, title, permalink, h1title, pagetitle, metadescription, og, ecosystem, category, twitter_handle, raised, investors, project_url, reflink, todo | 16 |
| Alternatives | git-date, layout, title, permalink, h1title, pagetitle, metadescription, og, filter-by, alternative-to | 10 |
| Events | git-date, product-title, product-url, image, product-description, date, location | 7 |
| Ecosystem | git-date, layout, title, metadescription, permalink, h1title, pagetitle, featured-image | 8 |

### Key Liquid → Go Template Conversions
| Jekyll | Hugo |
|--------|------|
| `{{ page.field }}` | `{{ .Params.field }}` |
| `{{ site.url }}` | `{{ .Site.BaseURL }}` |
| `{% include_cached x %}` | `{{ partialCached "x" . }}` |
| `{{ content \| toc }}` | `{{ .TableOfContents }}{{ .Content }}` |
| `site.data.authors[key]` | `{{ index site.Data.authors key }}` |
| `site[page.cards]` | `{{ where site.RegularPages "Section" .Params.cards }}` |
| `\| sample:4` | `{{ shuffle .Pages \| first 4 }}` (custom) |
| `\| date_to_xmlschema` | `{{ .Date.Format "2006-01-02T15:04:05-07:00" }}` |
| `redirect_from` | `aliases` in front matter |
| `\| markdownify` | `{{ .Params.x \| markdownify }}` |

### Total unique front matter fields across entire site: **47**
