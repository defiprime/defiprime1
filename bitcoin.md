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


# Assets Management Tools

{% assign assets-management-tools = site.assets-management-tools | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% for assets-management-tool in assets-management-tools %}
### <a href="{{ assets-management-tool.product-url }}">{{ assets-management-tool.product-title }}</a>
{% include ecosystem-icons.html project = assets-management-tool %}
{{ assets-management-tool.product-description }}
{% endfor %}


# BTC Decentralized Exchanges


{% assign exchanges = site.exchanges | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% for exchange in exchanges %}
### <a href="{{ exchange.product-url }}">{{ exchange.product-title }}</a>
{% include ecosystem-icons.html project = exchange %}
{{ exchange.product-description }}
{% endfor %}

# Bitcoin Crypto Lending

{% assign lendings = site.lending | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% for lending in lendings %}
### <a href="{{ lending.product-url }}">{{ lending.product-title }}</a>
{% include ecosystem-icons.html project = lending %}
{{ lending.product-description }}
{% endfor %}

# DeFi Infrastructure & Dev Tooling

{% assign infrastructures = site.infrastructure | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% for infrastructure in infrastructures %}
### <a href="{{ infrastructure.product-url }}">{{ infrastructure.product-title }}</a>
{% include ecosystem-icons.html project = infrastructure %}
{{ infrastructure.product-description }}
{% endfor %}

# BTC Payments Solutions and Service Providers

{% assign payments = site.payments | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% for payment in payments %}
### <a href="{{ payment.product-url }}">{{ payment.product-title }}</a>
{% include ecosystem-icons.html project = payment %}
{{ payment.product-description }}
{% endfor %}

# Marketplaces

{% assign marketplaces = site.marketplaces | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% for marketplace in marketplaces %}
### <a href="{{ marketplace.product-url }}">{{ marketplace.product-title }}</a>
{% include ecosystem-icons.html project = marketplace %}
{{ marketplace.product-description }}
{% endfor %}

# Stablecoins

{% assign stablecoins = site.stablecoins | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% for stablecoin in stablecoins %}
### <a href="{{ stablecoin.product-url }}">{{ stablecoin.product-title }}</a>
{% include ecosystem-icons.html project = stablecoin %}
{{ stablecoin.product-description }}
{% endfor %}