---
git-date: 2019-05-16T11:43:26-07:00
layout: blog-list
title: DeFi Blog - What is DeFi? Interviews with DeFi projects, analytics, and important news
metadescription: We want to shed some light on how DeFi products build and how the ecosystem evolves over time. Our blog features interviews with DeFi projects, analytics, and important news.
permalink: /blog/
pagination:
  enabled: true
  category: blog
  permalink: /:num/  
---
<header class="blog-page-header">
	<h1>DeFi <span>Blog</span></h1>
	<p>Interviews with DeFi projects, analytics, and important news about decentralized finance.</p>
</header>

<section class="blog-articles-grid">
	{% for post in paginator.posts %}
    {% unless post.url contains "/amp" %}
    {% assign link_colors = 'violet|cyan|orange|muted' | split: '|' %}
    {% assign border_color = forloop.index | random_item: link_colors %}
		<article class="blog-card">
			<a href="{{ post.url }}">
				<div class="blog-card-inner border-{{ border_color }}">
					{% if post.tags.size != 0 %}
					<div class="blog-card-meta">
						{% for tag in post.tags limit:2 %}
						<span class="tag-pill tag-{{ border_color }}">{{ tag }}</span>
						{% endfor %}
						<span class="blog-card-date">{{ post.date | date_to_string }}</span>
					</div>
					{% endif %}
					<h3>{{ post.h1title }}</h3>
					<p>{{ post.intro | strip_html | strip_newlines | truncatewords: 30 }}</p>
					<div class="blog-card-author">
						{% assign author = site.data.authors[post.author] %}
						{% if author.image %}
						<img class="lazyload" data-src="{{ author.image }}">
						{% endif %}
						{% if author.name %}
						<span>{{ author.name }}</span>
						{% endif %}
					</div>
				</div>
			</a>
		</article>
    {% endunless %}
	{% endfor %}
</section>

<section class="pagination">
	{% if paginator.next_page %}
		<a class="pagination-btn" href="{{ paginator.next_page_path | prepend: site.baseurl }}">Older Posts</a>
	{% endif %}
	{% if paginator.previous_page %}
		<a class="pagination-btn" href="{{ paginator.previous_page_path | prepend: site.baseurl }}">Newer Posts</a>
	{% endif %}
</section>
