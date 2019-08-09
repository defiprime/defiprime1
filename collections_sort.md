---
layout: default
title: Sorted Collections | DefiPrime.com
metadescription: Sorted colletions

---

<section>
    {% for collection in site.collections %}
        <h2>{{ collection.label }}</h2>
        {% assign documents = collection.docs | sort: 'last-modified-date' %}
        <ol>
        {% for document in documents limit: 5 %}
            <li>{{ document.title }}</li>
        {% endfor %}
        </ol>
    {% endfor %}
</section>