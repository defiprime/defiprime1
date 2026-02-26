# DeFiPrime Project Memory

## Project: Jekyll to Hugo Migration

### Key Conversion Patterns (Jekyll Liquid -> Hugo Go Templates)

- `{% unless page.name == "index.md" %}` -> `{{ if ne .Page.File.LogicalName "_index.md" }}`
- `{% include foo.html %}` -> `{{ partial "foo.html" . }}`
- `{% include_cached icons/foo.svg %}` -> `{{ partialCached "icons/foo.svg" . }}`
- `{{ site.baseurl }}` -> empty string (Hugo handles base URLs automatically)
- `{{ site.url }}{{ site.baseurl }}` -> `{{ .Site.BaseURL }}`
- `{{ site.algolia.application_id }}` -> `{{ .Site.Params.algolia.applicationId }}`
- `{{ site.algolia.index_name }}` -> `{{ .Site.Params.algolia.indexName }}`
- `{% assign author = site.data.authors[page.author] %}` -> `{{ $author := index site.Data.authors .Params.author }}`
- `{% assign posts = site.categories.blog | sample:4 %}` -> `{{ $posts := where site.RegularPages "Section" "blog" | shuffle | first 4 }}`
- Jekyll `include.param` in shortcodes -> Hugo `{{ .Get "param" }}`
- Jekyll `{% if x contains 'y' %}` -> Hugo `{{ if in x "y" }}`

### Directory Structure
- Jekyll `_includes/*.html` -> Hugo `layouts/partials/*.html`
- Jekyll `_includes/icons/*.svg` -> Hugo `layouts/partials/icons/*.svg`
- Jekyll `_includes/figure.html` (shortcode) -> Hugo `layouts/shortcodes/figure.html`
- CSS files in `_includes/` are copied as-is to `layouts/partials/`

### also.html Note
The Jekyll `also.html` used `site.collections` with Jekyll-specific `section_url` and `label` fields.
Hugo equivalent uses `site.Sections` with `.Section`, `.RelPermalink`, `.Title`, and `len .RegularPages`.
Exclude sections: blog, events, alternatives, posts.

### Layouts Conversion (Completed)
All 13 Jekyll `_layouts/*.html` converted to Hugo `layouts/`:
- `_layouts/default.html` → `layouts/_default/baseof.html` + `layouts/index.html`
- `_layouts/blog.html` → `layouts/blog/single.html`
- `_layouts/product.html` → `layouts/product/single.html`
- `_layouts/page.html` → `layouts/_default/page.html` (product listing page)
- `_layouts/ecosystem.html` → `layouts/ecosystem/single.html`
- `_layouts/blog-list.html` → `layouts/blog/list.html`
- `_layouts/tag_page.html` → `layouts/taxonomy/tag.html`
- `_layouts/airdrop.html` → `layouts/airdrop/single.html`
- `_layouts/alternatives.html` → `layouts/alternatives/single.html`
- `_layouts/events.html` → `layouts/events/single.html`
- `_layouts/static.html` → `layouts/static/single.html`
- `_layouts/stats.html` → `layouts/stats/single.html`
- `_layouts/basic.html` → `layouts/basic/single.html`

Key tricky conversions:
- Hyphenated params: `page.product-title` → `index .Params "product-title"`
- Dynamic collection: `site[page.collection]` → `where site.RegularPages "Section" .Params.cards`
- Jekyll `| sample:N` → Hugo `| shuffle | first N`
- Jekyll `| remove: '<p>'` → Hugo `| replaceRE "</?p>" ""`
- Filter buttons from grouped data: must manually range+append+uniq (no group_by in Hugo)
- `{{ content | toc }}` → `{{ .TableOfContents }}{{ .Content }}`
- Events future filter: `{% unless event.date < site.time %}` → `{{ if not .Date.Before now }}`
- Alternatives layout: concatenate collections with multiple `| append` calls
