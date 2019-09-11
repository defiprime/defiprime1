---
layout: default
title: DeFi - Best Decentralized Finance(DeFi) Products | What is DeFi in Crypto
metadescription: Decentralized Finance(DeFi) is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols.
redirect_from:
  - product
---
<header class='main-page-header'>
	<h1>List of the best Decentralized Finance Products</h1>
	<span>
	Decentralized Finance (DeFi) is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols that run without intermediaries.
	</span>
</header>

<h2 class='defi_projects_annotation'>DeFi projects</h2>

<section class="tiles">
{% assign sorted_categories_products = site.categories.products | sort: 'title', 'last' %}

{% for post in sorted_categories_products %}
	{% for collection in site.collections %}
		{% if post.cards == collection.label %}
			<article class="style{{ forloop.index | random_number: 0, 10 }}">
				<a href="{{ post.url | prepend:site.baseurl | prepend:site.url }}">
					<h2>{{ post.title }}</h2>
					<span>{{ collection.docs | size }}</span>
				</a>
			</article>
		{% endif %}
	{% endfor %}
{% endfor %}
</section>
<h2 class='recently_added_annotation'>Recently added</h2>
<section class="tiles" id='recently_added_section'>
	{% assign posts = site.categories.blog | sort: "date"  %}
	{% for blog_post in posts limit:6 %}
		{% capture blog_image %}
			{{ blog_post.featured-image }}
		{% endcapture %}
		{% for collection in site.collections %}
			{% if collection.label != 'events' and collection.label != 'posts' %}
				{% for document in collection.docs %}
					{% assign doc_title = document.title | upcase %}
					{% assign blog_title = blog_post.title | upcase %}
					{% assign doc_prod_title = document.product-title | upcase %}
					{% if document.image and blog_title contains doc_title or blog_title contains doc_prod_title %}
						{% capture blog_image %}
							{{ document.image }}
						{% endcapture %}
					{% endif %}
				{% endfor %}
			{% endif %}
		{% endfor %}
		<article>
			<a class='recent_blog_link' href="{{ blog_post.permalink | prepend:site.baseurl | prepend:site.url }}">
				<img src="{{ blog_image }}">
				<h2>{{ blog_post.title }}</h2>
			</a>
		</article>
	{% endfor %}
</section>