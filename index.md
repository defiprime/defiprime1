---
git-date: 2019-04-13T21:06:27-07:00
layout: default
pagetitle: DeFi - Best Decentralized Finance Projects | What is DeFi in Crypto
metadescription: DeFi(Decentralized Finance) is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols.
redirect_from:
  - product
---

<aside id='defi-search-fullpage'></aside>

<header class='main-page-header'>
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

<section class="banner">
    <a class="banner-link" target="_blank" href="https://1inch.exchange/#/r/0xEbDb626C95a25f4e304336b1adcAd0521a1Bdca1">
      <div class="banner-content">
        <div class="banner-icon">{% include icons/1inch.svg %}</div>
        <div class="banner-description"><span class="fw-800">1inch</span> gives you the best <span class="separator"></span> DEX prices for {% include icons/fire.svg %}  DeFi Tokens</div>
      </div>
    </a>
    <div class="circle circle-1"><span class="background"></span><span class="dot"></span></div>
    <div class="circle circle-2"><span class="background"></span><span class="dot"></span></div>
    <div class="circle circle-3"><span class="background"></span><span class="dot"></span></div>
    <div class="circle circle-4"><span class="background"></span><span class="dot"></span></div>
    <div class="circle circle-5"><span class="background"></span><span class="dot"></span></div>
</section>

<section>
  <h2 id="defi_projects" class='recently_added_annotation'>DeFi projects</h2>
  <div class="tiles floating grid">
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
  </div>
</section>

<section>
  <h2 class='recently_added_annotation'>Recently added</h2>
  <div class="tiles grid" id='recently_added_section'>
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
          <img class="lazyload" data-src="{{ document.image }}">
          <h2>{{ document.product-title }}</h2>
        </a>
      </article>
    {% endfor %}
  </div>
</section>

<section>
  <h2 class='recently_added_annotation'>Latest from DeFi <span>blog</span></h2>
  <div class='latest_blog_sneak_peak'>
    {% assign posts = site.categories.blog | sort: "date" | reverse  %}
    {% assign nonAmpPosts = ""  | split: ','%}
    
    {% for post in posts %}
      {% unless  post.url contains "/amp" %}
        {% assign nonAmpPosts = nonAmpPosts | push: post %}
      {% endunless  %}
    {% endfor %}
      
    {% for blog_post in nonAmpPosts limit:12 %}
    {% assign link_colors = 'violet|cyan|orange|violetgray' | split: '|' %}
      <article class='latest_blog_link recent-blog-color_{{ forloop.index | random_item: link_colors }}'>
        <a  href="{{ blog_post.permalink | prepend: '/' }}">
          <h2>{{ blog_post.title }}</h2>
          <p>{{ blog_post.intro | strip_html | strip_newlines }}</p>
        </a>
      </article>

    {% endfor %}
  </div>
</section>

<section>
  <h2 class='recently_added_annotation'>Upcoming DeFi events</h2>
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
  <h2 class='recently_added_annotation'>Recent Topics at <a href="https://alpha.defiprime.com/">Alpha</a></h2>
  <div class='latest_alpha'></div>
</section>


{% include algolia.html %}
