---
git-date:
layout: blog-list
title: DeFi Blog - What is DeFi? Interviews with DeFi projects, analytics, and important news
metadescription: We want to shed some light on how DeFi products build and how the ecosystem evolves over time. Our blog features interviews with DeFi projects, analytics, and important news.
permalink: /blog/
pagination:
  enabled: true
  category: blog
  permalink: /:num/  
---
<header>
	<h1>De<span class="text-green">fi</span> <span class="text-orange">Blog</span></h1>
	<p>We want to shed some light on how DeFi products build and how the ecosystem evolves over time. Our blog features interviews with DeFi projects, analytics, and important news.</p>
</header>
<section class="blog-articles">
	{% for post in paginator.posts %}
    {% unless  post.url contains "/amp" %}
		<article>
      {% if post.tags.size != 0 %}
        <div class="tags">
          {% for tag in post.tags %}
          <a href="/t/{{tag | downcase | replace: ' ', '-' }}.html" class="tag">{{ tag }}</a>
          {% endfor %}
        </div>
      {% endif %}
			<a href="{{ post.url }}">
				<div class="date">{{ post.date | date_to_string}}</div>
				<div class="header">
					<h2>{{ post.h1title }}</h2>
					<div class="author-item">
						{% assign author = site.data.authors[post.author] %}
						{% if author.image %}
							<img class="lazyload" data-src="{{ author.image }}">
						{% endif %}
						<div class="author-data">
							{% assign author = site.data.authors[post.author] %}								
							{% if author.image %}
								<span>Author</span>
								<span class="author">{{author.name}}</span>
							{% endif %}
						</div>
					</div>
				</div>
				<div class="content">
					<p>{{ post.intro | strip_html | truncatewords:50 }}</p>
				</div>    
			</a>
		</article>
    {% endunless  %}
	{% endfor %}
</section>

<section class="pagination">
	{% if paginator.next_page %}
		<a class="button" href="{{ paginator.next_page_path | prepend: site.baseurl }}">Older Posts</a>
	{% endif %}
	{% if paginator.previous_page %}
		<a class="button" href="{{ paginator.previous_page_path | prepend: site.baseurl }}">Newer Posts</a>
	{% endif %}
</section>
