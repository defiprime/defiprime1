---
git-date:
layout: ecosystem
title: EOS DeFi ecosystem
metadescription: List of the best EOS DeFi Projects. EOS DeFi dApps leverages decentralized networks to transform old financial products into trustless and transparent protocols.
permalink: eos
h1title: EOS DeFi Ecosystem
pagetitle: EOS DeFi Ecosystem - List of the best EOS DeFi Projects
featured-image: /images/og-eos.png

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

{% assign eos_projects = all_projects | where_exp:"item", "item.ecosystem contains 'eos'"%}

{% assign counter_eos = eos_projects.size %}

{% assign btc_projects = all_projects | where_exp:"item", "item.ecosystem contains 'bitcoin'"%}

{% assign counter_btc = btc_projects.size %}

{% assign eth_projects = all_projects | where_exp:"item", "item.ecosystem contains 'ethereum'"%}

{% assign counter_eth = eth_projects.size %}

DeFi is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols that run without intermediaries. We have {{ counter }} DeFi projects listed and {{ counter_eos }} of them using EOS.

| Ethereum <br /> DeFi | {{counter_eth}} |
| EOS <br /> DeFi | {{ counter_eos }} |
| Bitcoin <br /> DeFi | {{counter_btc}} |

# Assets Management Tools

{% assign assets-management-tools = site.assets-management-tools | where_exp:"item", "item.ecosystem contains 'eos'" %}
{% for assets-management-tool in assets-management-tools %}
### <a href="{{ assets-management-tool.product-url }}">{{ assets-management-tool.product-title }}</a>
{% include ecosystem-icons.html project = assets-management-tool %}
{{ assets-management-tool.product-description }}
{% endfor %}

# Decentralized exchanges on EOS


{% assign exchanges = site.exchanges | where_exp:"item", "item.ecosystem contains 'eos'" %}
{% for exchange in exchanges %}
### <a href="{{ exchange.product-url }}">{{ exchange.product-title }}</a>
{% include ecosystem-icons.html project = exchange %}
{{ exchange.product-description }}
{% endfor %}


# DeFi Infrastructure & Dev Tooling

{% assign infrastructures = site.infrastructure | where_exp:"item", "item.ecosystem contains 'eos'" %}
{% for infrastructure in infrastructures %}
### <a href="{{ infrastructure.product-url }}">{{ infrastructure.product-title }}</a>
{% include ecosystem-icons.html project = infrastructure %}
{{ infrastructure.product-description }}
{% endfor %}


# Decentralized Lending on EOS

{% assign lendings = site.lending | where_exp:"item", "item.ecosystem contains 'eos'" %}
{% for lending in lendings %}
### <a href="{{ lending.product-url }}">{{ lending.product-title }}</a>
{% include ecosystem-icons.html project = lending %}
{{ lending.product-description }}
{% endfor %}

# EOS Stablecoins

{% assign stablecoins = site.stablecoins | where_exp:"item", "item.ecosystem contains 'eos'" %}
{% for stablecoin in stablecoins %}
### <a href="{{ stablecoin.product-url }}">{{ stablecoin.product-title }}</a>
{% include ecosystem-icons.html project = stablecoin %}
{{ stablecoin.product-description }}
{% endfor %}