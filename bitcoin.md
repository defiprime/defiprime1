---
git-date:
layout: ecosystem
title: Bitcoin DeFi ecosystem
metadescription: List of the best Bitcoin Defi Products. DeFi is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols that run without intermediaries.
permalink: bitcoin
h1title: Bitcoin DeFi ecosystem
pagetitle: Bitcoin DeFi ecosystem - List of the best Bitcoin Defi Projects
featured-image: /images/og-bitcoin.png
---

{% assign all_projects = site.alternative-savings
| concat: site.analytics
| concat: site.assets-management-tools 
| concat: site.assets-tokenization 
| concat: site.dao
| concat: site.derivatives
| concat: site.exchanges
| concat: site.infrastructure
| concat: site.insurance
| concat: site.kyc_identity
| concat: site.lending
| concat: site.margin-trading
| concat: site.marketplaces
| concat: site.payments
| concat: site.prediction_markets
| concat: site.stablecoins
 %}
 
{% assign counter = all_projects.size %}

{% assign btc_projects = all_projects | where_exp:"item", "item.ecosystem contains 'bitcoin'"%}

{% assign counter_btc = btc_projects.size %}


DeFi is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols that run without intermediaries. We have {{ counter }} DeFi projects listed and {{ counter_btc }} of them using Bitcoin.


{% for collection in site.collections %}

{% assign collection_name = collection.label %}
{% assign collection_display_name = collection.display_name %}

{% assign btc_projects =  site[collection_name] | where_exp:"item", "item.ecosystem contains 'bitcoin'"%}

{% if btc_projects.size > 0 and collection_display_name %}

# {{collection_display_name}}
{% for btc_project in btc_projects %}
### <a href="{{ btc_project.product-url }}">{{ btc_project.product-title }}</a>
{% include ecosystem-icons.html project = btc_project %}
{{ btc_project.product-description }}
{% endfor %}

{% endif %}

{% endfor %}