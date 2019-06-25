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

<section id='coming_soon'>
	<h3>DeFi is coming. Don't get left behind</h3>
	<button>
		<svg width="22" height="14" viewBox="0 0 22 14" fill="none" xmlns="http://www.w3.org/2000/svg">
			<rect x="2" y="2" width="18" height="12" fill="white"/>
			<path d="M1 1L11 9.5L21 1" stroke="#8F68FC" stroke-width="2"/>
		</svg>
		Email Subscribe
	</button>
	<button>
		<svg width="21" height="18" viewBox="0 0 21 18" fill="none" xmlns="http://www.w3.org/2000/svg">
			<path fill-rule="evenodd" clip-rule="evenodd" d="M21 2.13078C20.2274 2.49219 19.397 2.73648 18.5255 2.84634C19.4149 2.28392 20.0982 1.39343 20.4199 0.332253C19.5873 0.853065 18.6653 1.23118 17.6839 1.43495C16.898 0.551806 15.7782 0 14.5391 0C12.1598 0 10.2307 2.03454 10.2307 4.54403C10.2307 4.90017 10.2688 5.24696 10.3422 5.57964C6.7616 5.39007 3.58695 3.58102 1.46198 0.831678C1.09104 1.50287 0.878597 2.28342 0.878597 3.11627C0.878597 4.69282 1.63925 6.08366 2.79532 6.89854C2.08901 6.8749 1.42475 6.67047 0.843824 6.33019C0.843428 6.34916 0.843428 6.36812 0.843428 6.38734C0.843428 8.58896 2.32862 10.4254 4.29952 10.8431C3.938 10.9469 3.5574 11.0025 3.16444 11.0025C2.88681 11.0025 2.61694 10.974 2.3538 10.921C2.9021 12.7262 4.49319 14.04 6.37854 14.0765C4.90397 15.2954 3.04634 16.0219 1.02767 16.0219C0.679939 16.0219 0.337039 16.0003 0 15.9584C1.90666 17.2477 4.17128 18 6.60437 18C14.5291 18 18.8627 11.0758 18.8627 5.07094C18.8627 4.87394 18.8585 4.67795 18.8502 4.48304C19.692 3.84234 20.4224 3.04199 21 2.13078Z" fill="white"></path>
		</svg>
		Twitter Channel
	</button>
</section>