---
git-date: 2019-05-20T22:02:39-07:00
layout: ecosystem
title: Arbitrum DeFi Ecosystem
metadescription: List of the best Arbitrum DeFi Projects, that leverages decentralized networks to transform old financial products into trustless and transparent protocols.
permalink: arbitrum
h1title: Arbitrum DeFi Ecosystem
pagetitle: Arbitrum DeFi Ecosystem - List of the Best Arbitrum Projects
featured-image: /images/blog/arbitrum.png
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
| concat: site.yield-aggregators
 %}

{% assign counter = all_projects.size %}

{% assign bsc_projects = all_projects | where_exp:"item", "item.ecosystem contains 'bsc'"%}

{% assign counter_bsc = bsc_projects.size %}

{% assign eos_projects = all_projects | where_exp:"item", "item.ecosystem contains 'eos'"%}

{% assign counter_eos = eos_projects.size %}

{% assign btc_projects = all_projects | where_exp:"item", "item.ecosystem contains 'bitcoin'"%}

{% assign counter_btc = btc_projects.size %}

{% assign eth_projects = all_projects | where_exp:"item", "item.ecosystem contains 'ethereum'"%}

{% assign counter_eth = eth_projects.size %}

{% assign arbitrum_projects = all_projects | where_exp:"item", "item.ecosystem contains 'arbitrum'"%}

{% assign counter_arbitrum = arbitrum_projects.size %}

{% assign polygon_projects = all_projects | where_exp:"item", "item.ecosystem contains 'polygon'"%}

{% assign counter_polygon = polygon_projects.size %}

DeFi is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols that run without intermediaries. We have {{ counter }} DeFi projects listed and {{ counter_arbitrum }} of them built on Arbitrum.

| Ethereum <br /> DeFi | {{counter_eth}} |
| BNB <br /> DeFi | {{ counter_bsc }} |
| Arbitrum <br /> DeFi | {{counter_arbitrum}} |

{% assign assets-management-tools = site.assets-management-tools | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if assets-management-tools.size > 0 %}

# Asset Management Tools

{% for assets-management-tool in assets-management-tools %}

### <a href="/product/{{ assets-management-tool.product-title | slugify }}">{{ assets-management-tool.product-title }}</a>

{% include ecosystem-icons.html project = assets-management-tool %}
{{ assets-management-tool.product-description }}
{% endfor %}
{% endif %}

{% assign alternative-savings = site.alternative-savings | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if alternative-savings.size > 0 %}

# Alternative Savings Apps

{% for alternative-saving in alternative-savings %}

### <a href="/product/{{ alternative-saving.product-title | slugify }}">{{ alternative-saving.product-title }}</a>

{% include ecosystem-icons.html project = alternative-saving %}
{{ alternative-saving.product-description }}
{% endfor %}
{% endif %}

{% assign derivatives = site.derivatives | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if derivatives.size > 0 %}

# Derivatives

{% for derivative in derivatives %}

### <a href="/product/{{ derivative.product-title | slugify }}">{{ derivative.product-title }}</a>

{% include ecosystem-icons.html project = derivative %}
{{ derivative.product-description }}
{% endfor %}
{% endif %}

{% assign yield-aggregators = site.yield-aggregators | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if yield-aggregators.size > 0 %}

# Yield Aggregators on Arbitrum

{% for yield-aggregator in yield-aggregators %}

### <a href="/product/{{ yield-aggregator.product-title | slugify }}">{{ yield-aggregator.product-title }}</a>

{% include ecosystem-icons.html project = yield-aggregator %}
{{ yield-aggregator.product-description }}
{% endfor %}
{% endif %}

{% assign exchanges = site.exchanges | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if exchanges.size > 0 %}

# Decentralized exchanges on Arbitrum

{% for exchange in exchanges %}

### <a href="/product/{{ exchange.product-title | slugify }}">{{ exchange.product-title }}</a>

{% include ecosystem-icons.html project = exchange %}
{{ exchange.product-description }}
{% endfor %}
{% endif %}

{% assign margin-tradings = site.margin-trading | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if margin-tradings.size > 0 %}

# Margin Trading on Arbitrum

{% for margin-trading in margin-tradings %}

### <a href="/product/{{ margin-trading.product-title | slugify }}">{{ margin-trading.product-title }}</a>

{% include ecosystem-icons.html project = margin-trading %}
{{ margin-trading.product-description }}
{% endfor %}
{% endif %}

{% assign infrastructures = site.infrastructure | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if infrastructures.size > 0 %}

# DeFi Infrastructure & Dev Tooling

{% for infrastructure in infrastructures %}

### <a href="/product/{{ infrastructure.product-title | slugify }}">{{ infrastructure.product-title }}</a>

{% include ecosystem-icons.html project = infrastructure %}
{{ infrastructure.product-description }}
{% endfor %}
{% endif %}

{% assign daos = site.dao | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if daos.size > 0 %}

# Arbitrum-based DAO Platforms

{% for dao in daos %}

### <a href="{{ dao.product-url }}">{{ dao.product-title | slugify }}</a>

{% include ecosystem-icons.html project = dao %}
{{ dao.product-description }}
{% endfor %}
{% endif %}

{% assign insurances = site.insurance | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if insurances.size > 0 %}

# Decentralized Insurance Platforms

{% for insurance in insurances %}

### <a href="/product/{{ insurance.product-title | slugify }}">{{ insurance.product-title }}</a>

{% include ecosystem-icons.html project = insurance %}
{{ insurance.product-description }}
{% endfor %}
{% endif %}

{% assign assets-tokenizations = site.assets-tokenization | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if assets-tokenizations.size > 0 %}

# Asset Tokenization

{% for assets-tokenization in assets-tokenizations %}

### <a href="/product/{{ assets-tokenization.product-title | slugify }}">{{ assets-tokenization.product-title }}</a>

{% include ecosystem-icons.html project = assets-tokenization %}
{{ assets-tokenization.product-description }}
{% endfor %}
{% endif %}

{% assign kyc_identities = site.kyc_identity | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if kyc_identities.size > 0 %}

# KYC & Identity

{% for kyc_identity in kyc_identities %}

### <a href="/product/{{ kyc_identity.product-title | slugify }}">{{ kyc_identity.product-title }}</a>

{% include ecosystem-icons.html project = kyc_identity %}
{{ kyc_identity.product-description }}
{% endfor %}
{% endif %}

{% assign lendings = site.lending | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if lendings.size > 0 %}

# Decentralized Lending on Arbitrum

{% for lending in lendings %}

### <a href="/product/{{ lending.product-title | slugify }}">{{ lending.product-title }}</a>

{% include ecosystem-icons.html project = lending %}
{{ lending.product-description }}
{% endfor %}
{% endif %}

{% assign payments = site.payments | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if payments.size > 0 %}

# Payments Solutions and Service Providers

{% for payment in payments %}

### <a href="/product/{{ payment.product-title | slugify }}">{{ payment.product-title }}</a>

{% include ecosystem-icons.html project = payment %}
{{ payment.product-description }}
{% endfor %}
{% endif %}

{% assign marketplaces = site.marketplaces | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if marketplaces.size > 0 %}

# Marketplaces

{% for marketplace in marketplaces %}

### <a href="/product/{{ marketplace.product-title | slugify }}">{{ marketplace.product-title }}</a>

{% include ecosystem-icons.html project = marketplace %}
{{ marketplace.product-description }}
{% endfor %}
{% endif %}

{% assign prediction_markets = site.prediction_markets | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if prediction_markets.size > 0 %}

# Prediction Markets

{% for prediction_market in prediction_markets %}

### <a href="/product/{{ prediction_market.product-title | slugify }}">{{ prediction_market.product-title }}</a>

{% include ecosystem-icons.html project = prediction_market %}
{{ prediction_market.product-description }}
{% endfor %}
{% endif %}

{% assign stablecoins = site.stablecoins | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if stablecoins.size > 0 %}

# Stablecoins

{% for stablecoin in stablecoins %}

### <a href="/product/{{ stablecoin.product-title | slugify }}">{{ stablecoin.product-title }}</a>

{% include ecosystem-icons.html project = stablecoin %}
{{ stablecoin.product-description }}
{% endfor %}
{% endif %}

{% assign analytics = site.analytics | where_exp:"item", "item.ecosystem contains 'arbitrum'" %}
{% if analytics.size > 0 %}

# Analytics

{% for analytic in analytics %}

### <a href="/product/{{ analytic.product-title | slugify }}">{{ analytic.product-title }}</a>

{% include ecosystem-icons.html project = analytic %}
{{ analytic.product-description }}
{% endfor %}
{% endif %}
