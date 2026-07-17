# Generates author profile pages at /authors/<slug>/ and an all-authors index
# at /authors/. Posts are grouped by a slug derived from each author's
# _data/authors.yml entry: the entry's `slug` field if present, else the author
# key downcased. That mapping lets several keys collapse into one profile (e.g.
# `Defiprime` and `sawinyh`, which are the same person, both map to `sawinyh`).
module Jekyll
  class AuthorPagesGenerator < Generator
    safe true
    priority :low

    def generate(site)
      authors = site.data['authors'] || {}

      # author key (as written in post front matter) -> profile slug
      key_to_slug = {}
      authors.each do |key, data|
        data ||= {}
        key_to_slug[key] = (data['slug'] || key).to_s.downcase
      end

      # profile slug -> canonical key + data. Prefer the entry whose own key
      # downcases to the slug; otherwise the first entry that maps to it.
      slug_to_key = {}
      slug_to_data = {}
      authors.each do |key, data|
        data ||= {}
        slug = (data['slug'] || key).to_s.downcase
        if key.to_s.downcase == slug || !slug_to_key.key?(slug)
          slug_to_key[slug] = key
          slug_to_data[slug] = data
        end
      end

      # group posts by slug
      posts_by_slug = Hash.new { |h, k| h[k] = [] }
      site.posts.docs.each do |post|
        key = post.data['author']
        next if key.nil? || key.to_s.empty?
        slug = key_to_slug[key]
        if slug.nil?
          Jekyll.logger.warn "AuthorPages:",
            "No _data/authors.yml entry for author '#{key}' (#{post.relative_path}); skipped."
          next
        end
        posts_by_slug[slug] << post
      end

      authors_list = []
      posts_by_slug.each do |slug, posts|
        sorted = posts.sort_by { |p| p.data['date'] }.reverse
        data = slug_to_data[slug] || {}
        key = slug_to_key[slug] || slug
        site.pages << AuthorPage.new(site, slug, key, data, sorted)
        authors_list << { 'slug' => slug, 'data' => data, 'count' => sorted.size }
      end

      authors_list.sort_by! { |a| -a['count'] }
      site.pages << AuthorsIndexPage.new(site, authors_list)
    end
  end

  # /authors/<slug>/
  class AuthorPage < PageWithoutAFile
    def initialize(site, slug, key, data, posts)
      @site = site
      @base = site.source
      @dir  = File.join('authors', slug)
      @name = 'index.html'
      process(@name)

      name = data['name'] || slug
      self.data = {
        'layout'       => 'author_page',
        'author'       => key,          # lets author_bio.html resolve this author
        'author_slug'  => slug,
        'author_data'  => data,
        'author_posts' => posts,
        'post_count'   => posts.size,
        'title'        => name,
        'pagetitle'    => "#{name} | DeFiprime",
      }
    end
  end

  # /authors/
  class AuthorsIndexPage < PageWithoutAFile
    def initialize(site, authors_list)
      @site = site
      @base = site.source
      @dir  = 'authors'
      @name = 'index.html'
      process(@name)

      self.data = {
        'layout'       => 'authors_index',
        'authors_list' => authors_list,
        'title'        => 'Authors',
        'pagetitle'    => 'Authors | DeFiprime',
      }
    end
  end
end
