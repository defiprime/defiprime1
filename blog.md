---
layout: blog-list
title: Defi Blog - What is DeFi? Interviews with DeFi projects, analytics, and important news
metadescription: We want to shed some light on how DeFi products build and how the ecosystem evolves over time. Our blog features interviews with DeFi projects, analytics, and important news.
permalink: /blog/
pagination:
  enabled: true
  category: blog
  permalink: /:num/  
---

<header>
<h1 class="align-center">De<span class="text-green">fi</span> <span class="text-orange">Blog</span></h1>
</header>
We want to shed some light on how DeFi products build and how the ecosystem evolves over time. Our blog features interviews with DeFi projects, analytics, and important news.

<section class="tiles">

{% for post in paginator.posts %}
	<article class="style{{ forloop.index | random_number: 0, 10 }}">



		<a href="{{ post.url }}">
			<h2>{{ post.title }}</h2>
			<div class="content">
				<p>{{ post.intro | strip_html | truncatewords:50 }}</p>
			</div>
		</a>
		<div class="article-image">
			<div class="image">
				<a href="{{ post.url }}">
					<img src="{{ post.quote }}" alt="" />
				</a>
			</div>
		</div>
	</article>
{% endfor %}

</section>

{% if paginator.next_page %}
  <a class="button" href="{{ paginator.next_page_path | prepend: site.baseurl }}">Next</a>
{% endif %}

  {% if paginator.previous_page %}
    <a class="button" href="{{ paginator.previous_page_path | prepend: site.baseurl }}">Previous</a>
  {% endif %}
