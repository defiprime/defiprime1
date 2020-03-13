---
git-date:
layout: ecosystem
title: Ethereum DeFi Ecosystem
metadescription: List of the best Ethereum Defi Projects, that leverages decentralized networks to transform old financial products into trustless and transparent protocols.
permalink: ethereum
h1title: Ethereum DeFi Ecosystem
pagetitle: Ethereum DeFi Ecosystem - List of the Best Ethereum DeFi dApps Projects
featured-image: /images/og-ethereum.png

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

{% assign counter = all_projects.size %}

{% assign eos_projects = all_projects | where_exp:"item", "item.ecosystem contains 'eos'"%}

{% assign counter_eos = eos_projects.size %}

{% assign btc_projects = all_projects | where_exp:"item", "item.ecosystem contains 'bitcoin'"%}

{% assign counter_btc = btc_projects.size %}

{% assign eth_projects = all_projects | where_exp:"item", "item.ecosystem contains 'ethereum'"%}

{% assign counter_eth = eth_projects.size %}

DeFi is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols that run without intermediaries. We have {{ counter }} DeFi projects listed and {{ counter_eth }} of them built on Ethereum.

| Ethereum <br /> DeFi | {{counter_eth}} |
| EOS <br /> DeFi | {{ counter_eos }} |
| Bitcoin <br /> DeFi | {{counter_btc}} |

# Assets Management Tools

{% assign assets-management-tools = site.assets-management-tools | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% for assets-management-tool in assets-management-tools %}
### <a href="{{ assets-management-tool.product-url }}">{{ assets-management-tool.product-title }}</a>
{% include ecosystem-icons.html project = assets-management-tool %}
{{ assets-management-tool.product-description }}
{% endfor %}

# Alternative Savings Apps

{% assign alternative-savings = site.alternative-savings | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% for alternative-saving in alternative-savings %}
### <a href="{{ alternative-saving.product-url }}">{{ alternative-saving.product-title }}</a>
{% include ecosystem-icons.html project = alternative-saving %}
{{ alternative-saving.product-description }}
{% endfor %}

# Derivatives

{% assign derivatives = site.derivatives | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% for derivative in derivatives %}
### <a href="{{ derivative.product-url }}">{{ derivative.product-title }}</a>
{% include ecosystem-icons.html project = derivative %}
{{ derivative.product-description }}
{% endfor %}

# Decentralized exchanges on Ethereum

{% assign exchanges = site.exchanges | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% for exchange in exchanges %}
### <a href="{{ exchange.product-url }}">{{ exchange.product-title }}</a>
{% include ecosystem-icons.html project = exchange %}
{{ exchange.product-description }}
{% endfor %}

# Margin Trading on Ethereum

{% assign margin-tradings = site.margin-trading | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% for margin-trading in margin-tradings %}
### <a href="{{ margin-trading.product-url }}">{{ margin-trading.product-title }}</a>
{% include ecosystem-icons.html project = margin-trading %}
{{ margin-trading.product-description }}
{% endfor %}

# DeFi Infrastructure & Dev Tooling

{% assign infrastructures = site.infrastructure | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% for infrastructure in infrastructures %}
### <a href="{{ infrastructure.product-url }}">{{ infrastructure.product-title }}</a>
{% include ecosystem-icons.html project = infrastructure %}
{{ infrastructure.product-description }}
{% endfor %}

# Ethereum-based DAO Platforms

{% assign daos = site.dao | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% for dao in daos %}
### <a href="{{ dao.product-url }}">{{ dao.product-title }}</a>
{% include ecosystem-icons.html project = dao %}
{{ dao.product-description }}
{% endfor %}

# Decentralized Insurance Platforms

{% assign insurances = site.insurance | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% for insurance in insurances %}
### <a href="{{ insurance.product-url }}">{{ insurance.product-title }}</a>
{% include ecosystem-icons.html project = insurance %}
{{ insurance.product-description }}
{% endfor %}

# Asset Tokenization

{% assign assets-tokenizations = site.assets-tokenization | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% for assets-tokenization in assets-tokenizations %}
### <a href="{{ assets-tokenization.product-url }}">{{ assets-tokenization.product-title }}</a>
{% include ecosystem-icons.html project = assets-tokenization %}
{{ assets-tokenization.product-description }}
{% endfor %}

# KYC & Identity

{% assign kyc_identities = site.kyc_identity | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% for kyc_identity in kyc_identities %}
### <a href="{{ kyc_identity.product-url }}">{{ kyc_identity.product-title }}</a>
{% include ecosystem-icons.html project = kyc_identity %}
{{ kyc_identity.product-description }}
{% endfor %}

# Decentralized Lending on Ethereum

{% assign lendings = site.lending | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% for lending in lendings %}
### <a href="{{ lending.product-url }}">{{ lending.product-title }}</a>
{% include ecosystem-icons.html project = lending %}
{{ lending.product-description }}
{% endfor %}

# Payments

{% assign payments = site.payments | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% for payment in payments %}
### <a href="{{ payment.product-url }}">{{ payment.product-title }}</a>
{% include ecosystem-icons.html project = payment %}
{{ payment.product-description }}
{% endfor %}

# Marketplaces

{% assign marketplaces = site.marketplaces | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% for marketplace in marketplaces %}
### <a href="{{ marketplace.product-url }}">{{ marketplace.product-title }}</a>
{% include ecosystem-icons.html project = marketplace %}
{{ marketplace.product-description }}
{% endfor %}

# Prediction Markets

{% assign prediction_markets = site.prediction_markets | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% for prediction_market in prediction_markets %}
### <a href="{{ prediction_market.product-url }}">{{ prediction_market.product-title }}</a>
{% include ecosystem-icons.html project = prediction_market %}
{{ prediction_market.product-description }}
{% endfor %}

# Stablecoins

{% assign stablecoins = site.stablecoins | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% for stablecoin in stablecoins %}
### <a href="{{ stablecoin.product-url }}">{{ stablecoin.product-title }}</a>
{% include ecosystem-icons.html project = stablecoin %}
{{ stablecoin.product-description }}
{% endfor %}

# Analytics

{% assign analytics = site.analytics | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
{% for analytic in analytics %}
### <a href="{{ analytic.product-url }}">{{ analytic.product-title }}</a>
{% include ecosystem-icons.html project = analytic %}
{{ analytic.product-description }}
{% endfor %}