---
git-date: 2019-04-13T21:06:27-07:00
layout: default
title: DeFi - Best Decentralized Finance(DeFi) Projects | What is DeFi in Crypto
metadescription: Decentralized Finance(DeFi) is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols.
redirect_from:
  - product
---
<header class='main-page-header'>
	<h1>DeFi and Open Finance</h1>
	<span>
	Decentralized Finance (DeFi) is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols that run without intermediaries.
	</span>
</header>

<h2 class='defi_projects_annotation'>DeFi projects</h2>

<section class="tiles floating">
{% assign sorted_categories_products = site.categories.products | sort: 'title', 'last' %}

{% for post in sorted_categories_products %}
	{% for collection in site.collections %}
		{% if post.cards == collection.label %}
			<article class="style{{ forloop.index | random_number: 0, 10 }}">
				<a href="{{ post.url }}">
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
    {% assign docArray = "" | split: "" %}
	{% assign collections = site.collections | where_exp: "coll", "coll.label != 'events'" | where_exp: "coll", "coll.label != 'posts'"  %}
    {% for collection in collections %}
        {% assign docArray = collection.docs | concat: docArray %}
    {% endfor %}
    {% assign documents = docArray | sort: 'git-date' | reverse %}
	{% comment %} The most recently __changed__ is last-modified-date. Temporarily swithing to __date__ {% endcomment %}
    {% for document in documents limit: 6 %}
		<article>
			<a class='recent_blog_link' href="/product/{{ document.product-title | slugify: 'latin'}}">
				<img src="{{ document.image }}">
				<h2>{{ document.product-title }}</h2>
			</a>
		</article>
    {% endfor %}
</section>
<h2 class='recently_added_annotation'>Latest from defi<span>blog</span></h2>
<section class='latest_blog_sneak_peak'>
	{% assign posts = site.categories.blog | sort: "date" | reverse  %}
	{% for blog_post in posts limit:6 %}
	{% assign link_colors = 'violet|cyan|orange|violetgray' | split: '|' %}
		<article class='latest_blog_link recent-blog-color_{{ forloop.index | random_item: link_colors }}'>
			<a  href="{{ blog_post.permalink | prepend: '/' }}">
				<h2>{{ blog_post.title }}</h2>
				<p>{{ blog_post.intro | strip_html | strip_newlines }}</p>
			</a>
		</article>
	{% endfor %}
</section>
<h2 class='recently_added_annotation'>Upcoming DeFi events</h2>
<section class='upcoming_events_cards'>
{% assign events = site.events | sort: "date" | reverse %}
{% for event in events limit: 3 %}
<article>
	<a href='{{event.product-url}}'>
		<img src='{{event.image}}'>
		<div class='event_card_info_part'>
			<h4>{{ event.product-title }}</h4>
			<div class='event_card_details'>
				<date>
					{{ event.date | date_to_string }}
				</date>
				<span> {{ event.location | truncate: 31 }} </span>
			</div>
		</div>
	</a>
</article>
{% endfor%}
</section>
