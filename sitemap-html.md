---
layout: basic
title: sitemap
h1title: sitemap
pagetitle: sitemap
permalink: sitemap-html
---

<ul>
{% for post in site.alternatives %}
   {% unless post.published == false %}    
   <li>{{ post.date | date_to_string }} - <a href="{{ site.url }}{{ post.url }}">{{ post.pagetitle }}</a>
   </li>
   {% endunless %}
 {% endfor %}
</ul>

<ul>
{% for post in site.posts %}
   {% unless post.published == false %}    
   <li>{{ post.date | date_to_string }} - <a href="{{ site.url }}{{ post.url }}">{{ post.pagetitle }}</a>
   </li>
   {% endunless %}
 {% endfor %}
</ul>
