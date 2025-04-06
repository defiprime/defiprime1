---
git-date: 2019-05-20T22:02:39-07:00
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
  | concat: site.staking
  | concat: site.prediction_markets
  | concat: site.stablecoins
%}

{% assign counter = all_projects.size %}

{% assign eos_projects = all_projects | where_exp:"item", "item.ecosystem contains 'eos'" %}
{% assign counter_eos = eos_projects.size %}

{% assign btc_projects = all_projects | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% assign counter_btc = btc_projects.size %}

{% assign eth_projects = all_projects | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% assign counter_eth = eth_projects.size %}

DeFi is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols that run without intermediaries. We have {{ counter }} DeFi projects listed and {{ counter_btc }} of them using Bitcoin.

| Ethereum <br /> DeFi | {{ counter_eth }} |
| EOS <br /> DeFi | {{ counter_eos }} |
| Bitcoin <br /> DeFi | {{ counter_btc }} |

{% assign assets_management_tools = site.assets-management-tools | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if assets_management_tools.size > 0 %}

# Asset Management Tools

{% for tool in assets_management_tools %}

### <a href="/product/{{ tool.product-title | slugify }}">{{ tool.product-title }}</a>

{% include ecosystem-icons.html project = tool %}
{{ tool.product-description }}
{% endfor %}
{% endif %}

{% assign exchanges = site.exchanges | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if exchanges.size > 0 %}

# Bitcoin Decentralized Exchanges

{% for exchange in exchanges %}

### <a href="/product/{{ exchange.product-title | slugify }}">{{ exchange.product-title }}</a>

{% include ecosystem-icons.html project = exchange %}
{{ exchange.product-description }}
{% endfor %}
{% endif %}

{% assign stakings = site.staking | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if stakings.size > 0 %}

# Bitcoin Staking and Restaking

{% for staking in stakings %}

### <a href="/product/{{ staking.product-title | slugify }}">{{ staking.product-title }}</a>

{% include ecosystem-icons.html project = staking %}
{{ staking.product-description }}
{% endfor %}
{% endif %}

{% assign lendings = site.lending | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if lendings.size > 0 %}

# Bitcoin Crypto Lending

{% for lending in lendings %}

### <a href="/product/{{ lending.product-title | slugify }}">{{ lending.product-title }}</a>

{% include ecosystem-icons.html project = lending %}
{{ lending.product-description }}
{% endfor %}
{% endif %}

{% assign margin_tradings = site.margin-trading | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if margin_tradings.size > 0 %}

# Margin Trading

{% for margin_trading in margin_tradings %}

### <a href="/product/{{ margin_trading.product-title | slugify }}">{{ margin_trading.product-title }}</a>

{% include ecosystem-icons.html project = margin_trading %}
{{ margin_trading.product-description }}
{% endfor %}
{% endif %}

{% assign infrastructures = site.infrastructure | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if infrastructures.size > 0 %}

# DeFi Infrastructure & Dev Tooling

{% for infrastructure in infrastructures %}

### <a href="/product/{{ infrastructure.product-title | slugify }}">{{ infrastructure.product-title }}</a>

{% include ecosystem-icons.html project = infrastructure %}
{{ infrastructure.product-description }}
{% endfor %}
{% endif %}

{% assign payments = site.payments | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if payments.size > 0 %}

# BTC Payments Solutions and Service Providers

{% for payment in payments %}

### <a href="/product/{{ payment.product-title | slugify }}">{{ payment.product-title }}</a>

{% include ecosystem-icons.html project = payment %}
{{ payment.product-description }}
{% endfor %}
{% endif %}

{% assign marketplaces = site.marketplaces | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if marketplaces.size > 0 %}

# Marketplaces

{% for marketplace in marketplaces %}

### <a href="/product/{{ marketplace.product-title | slugify }}">{{ marketplace.product-title }}</a>

{% include ecosystem-icons.html project = marketplace %}
{{ marketplace.product-description }}
{% endfor %}
{% endif %}

{% assign stablecoins = site.stablecoins | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if stablecoins.size > 0 %}

# Stablecoins

{% for stablecoin in stablecoins %}

### <a href="/product/{{ stablecoin.product-title | slugify }}">{{ stablecoin.product-title }}</a>

{% include ecosystem-icons.html project = stablecoin %}
{{ stablecoin.product-description }}
{% endfor %}
{% endif %}

{% assign alternative_savings = site.alternative-savings | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if alternative_savings.size > 0 %}

# Alternative Savings Apps

{% for saving in alternative_savings %}

### <a href="/product/{{ saving.product-title | slugify }}">{{ saving.product-title }}</a>

{% include ecosystem-icons.html project = saving %}
{{ saving.product-description }}
{% endfor %}
{% endif %}

{% assign analytics = site.analytics | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if analytics.size > 0 %}

# Analytics

{% for analytic in analytics %}

### <a href="/product/{{ analytic.product-title | slugify }}">{{ analytic.product-title }}</a>

{% include ecosystem-icons.html project = analytic %}
{{ analytic.product-description }}
{% endfor %}
{% endif %}

{% assign assets_tokenizations = site.assets-tokenization | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if assets_tokenizations.size > 0 %}

# Asset Tokenization

{% for tokenization in assets_tokenizations %}

### <a href="/product/{{ tokenization.product-title | slugify }}">{{ tokenization.product-title }}</a>

{% include ecosystem-icons.html project = tokenization %}
{{ tokenization.product-description }}
{% endfor %}
{% endif %}

{% assign daos = site.dao | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if daos.size > 0 %}

# Bitcoin-based DAO Platforms

{% for dao in daos %}

### <a href="/product/{{ dao.product-title | slugify }}">{{ dao.product-title }}</a>

{% include ecosystem-icons.html project = dao %}
{{ dao.product-description }}
{% endfor %}
{% endif %}

{% assign derivatives = site.derivatives | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if derivatives.size > 0 %}

# Derivatives

{% for derivative in derivatives %}

### <a href="/product/{{ derivative.product-title | slugify }}">{{ derivative.product-title }}</a>

{% include ecosystem-icons.html project = derivative %}
{{ derivative.product-description }}
{% endfor %}
{% endif %}

{% assign insurances = site.insurance | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if insurances.size > 0 %}

# Decentralized Insurance Platforms

{% for insurance in insurances %}

### <a href="/product/{{ insurance.product-title | slugify }}">{{ insurance.product-title }}</a>

{% include ecosystem-icons.html project = insurance %}
{{ insurance.product-description }}
{% endfor %}
{% endif %}

{% assign kyc_identities = site.kyc_identity | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if kyc_identities.size > 0 %}

# KYC & Identity

{% for kyc_identity in kyc_identities %}

### <a href="/product/{{ kyc_identity.product-title | slugify }}">{{ kyc_identity.product-title }}</a>

{% include ecosystem-icons.html project = kyc_identity %}
{{ kyc_identity.product-description }}
{% endfor %}
{% endif %}

{% assign prediction_markets = site.prediction_markets | where_exp:"item", "item.ecosystem contains 'bitcoin'" %}
{% if prediction_markets.size > 0 %}

# Prediction Markets

{% for prediction_market in prediction_markets %}

### <a href="/product/{{ prediction_market.product-title | slugify }}">{{ prediction_market.product-title }}</a>

{% include ecosystem-icons.html project = prediction_market %}
{{ prediction_market.product-description }}
{% endfor %}
{% endif %}