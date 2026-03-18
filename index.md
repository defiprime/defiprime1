---
git-date: 2019-04-13T21:06:27-07:00
layout: default
pagetitle: DeFi - Best Decentralized Finance Projects | What is DeFi in Crypto
metadescription: DeFi(Decentralized Finance) is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols.
featured-image: /images/og.png
redirect_from:
  - product
---

<aside id='defi-search-fullpage'></aside>

<header class='main-page-header compact'>
	<h1>DeFi and Open Finance</h1>
	<span>
	Decentralized Finance (DeFi) is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols that run without intermediaries.
	</span>
	<div id='defi-search'>
		<div id="search-searchbar"></div>
		<div id='search-powered-by'></div>
		<div id='search-container'>
    	<div class="post-list" id="search-hits">
    	</div>
    	<div class="post-list" id="search-hits-defiprime">
    	</div>
    </div>
    </div>
</header>

<section>
  <div class='section-heading-row'>
    <h2 class='section-heading'>Latest from DeFi <span>blog</span></h2>
    <a href='/blog' class='view-all'>View all posts &rarr;</a>
  </div>

  {% assign posts = site.categories.blog | sort: "date" | reverse %}
  {% assign nonAmpPosts = "" | split: ',' %}
  {% for post in posts %}
    {% unless post.url contains "/amp" %}
      {% assign nonAmpPosts = nonAmpPosts | push: post %}
    {% endunless %}
  {% endfor %}

  {% assign featured = nonAmpPosts | first %}
  <a href="{{ featured.permalink | prepend: '/' }}" class='featured-post'>
    <div class='featured-post-content'>
      <div class='featured-tag'>Latest Post</div>
      <h2>{{ featured.h1title }}</h2>
      <p class='intro'>{{ featured.intro | strip_html | strip_newlines }}</p>
      <span class='read-more'>Read article &rarr;</span>
    </div>
    <div class='featured-post-visual'>
      <div class='decorative-bars'>
        <span style="left:15%; top:10%; height:60%; background:rgba(143,104,252,0.2)"></span>
        <span style="left:25%; top:25%; height:50%; background:rgba(5,210,221,0.25)"></span>
        <span style="left:38%; top:5%; height:70%; background:rgba(126,202,246,0.2)"></span>
        <span style="left:50%; top:30%; height:55%; background:rgba(255,150,28,0.15)"></span>
        <span style="left:62%; top:15%; height:45%; background:rgba(174,133,202,0.18)"></span>
        <span style="left:72%; top:20%; height:60%; background:rgba(5,210,221,0.2)"></span>
        <span style="left:85%; top:8%; height:50%; background:rgba(143,104,252,0.15)"></span>
      </div>
      {% if featured.tags.first %}
      <div class='topic-label'>{{ featured.tags | first }}</div>
      {% endif %}
    </div>
  </a>

  <div class='blog-grid'>
    {% for blog_post in nonAmpPosts limit:6 offset:1 %}
    {% assign link_colors = 'violet|cyan|orange|muted' | split: '|' %}
    {% assign border_color = forloop.index | random_item: link_colors %}
      <article class='blog-card'>
        <a href="{{ blog_post.permalink | prepend: '/' }}">
          <div class='blog-card-inner border-{{ border_color }}'>
            {% if blog_post.tags.first %}
            <span class='tag-pill tag-{{ border_color }}'>{{ blog_post.tags | first }}</span>
            {% endif %}
            <h3>{{ blog_post.h1title }}</h3>
            <p>{{ blog_post.intro | strip_html | strip_newlines | truncate: 120 }}</p>
          </div>
        </a>
      </article>
    {% endfor %}
  </div>
</section>

<section>
  <div class='section-heading-row'>
    <h2 class='section-heading' id="defi_projects">DeFi <span>projects</span></h2>
  </div>
  <div class="projects-grid">
    {% assign sorted_categories_products = site.categories.products | sort: 'title', 'last' %}
    {% for post in sorted_categories_products %}
      {% for collection in site.collections %}
        {% if post.cards == collection.label %}
          <a class="project-tile" href="{{ post.url }}">
            <span class='tile-name'>{{ post.title }}</span>
            <div class='tile-count'>{{ collection.docs | size }} projects</div>
          </a>
        {% endif %}
      {% endfor %}
    {% endfor %}
  </div>
</section>

<section>
  <div class='section-heading-row'>
    <h2 class='section-heading'>Recently <span>added</span></h2>
  </div>
  <div class="tiles grid" id='recently_added_section'>
    {% assign docArray = "" | split: "" %}
    {% assign collections = site.collections | where_exp: "coll", "coll.label != 'events'" | where_exp: "coll", "coll.label != 'posts'" | where_exp: "coll", "coll.label != 'alternatives'" %}
      {% for collection in collections %}
          {% assign docArray = collection.docs | concat: docArray %}
      {% endfor %}
      {% assign documents = docArray | sort: 'git-date' | reverse %}
    {% for document in documents limit: 6 %}
      <article>
        <a class='recent_blog_link' href="/product/{{ document.product-title | slugify: 'latin'}}">
          <img class="lazyload" data-src="{{ document.image }}">
          <h2>{{ document.product-title }}</h2>
        </a>
      </article>
    {% endfor %}
  </div>
</section>

<section>
  <div class='section-heading-row'>
    <h2 class='section-heading'>Upcoming <span>events</span></h2>
    <a href='/events' class='view-all'>All events &rarr;</a>
  </div>
  <div class='upcoming_events_cards'>
  {% assign today_date = 'now' | date: '%s' %}
  {% assign events = site.events | sort: "date" %}
  {% assign counter = 0 %}
  {% for event in events %}
    {% assign event_date = event.date | date: '%s' %}
    {% if counter > 2 %}
      {% break %}
    {% endif %}
    {% if event_date > today_date %}
      {% assign counter = counter | plus:1 %}
      <article>
        <a href='{{event.product-url}}'>
          <img class="lazyload" data-src='{{event.image}}'>
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
    {% endif %}
  {% endfor%}
  </div>
</section>

<section>

</section>

{% include algolia.html %}
