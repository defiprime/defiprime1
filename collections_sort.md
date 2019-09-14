---
git-date: 
layout: default
title: Sorted Collections | DefiPrime.com
metadescription: Sorted colletions

---

<section>
    {% assign docArray = "" | split: "" %}
    {% for collection in site.collections %}
        {% assign docArray = collection.docs | concat: docArray %}
    {% endfor %}
    {% assign documents = docArray | sort: 'last-modified-date' %}
    <h2>Newest 5 pages</h2>
    <ol>
    {% for document in documents limit: 5 %}
        <li>{{ document.title }}</li>
    {% endfor %}
    </ol>
</section>