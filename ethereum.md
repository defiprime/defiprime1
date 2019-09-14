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

{% assign counter = 0 %}
{% assign counter_eth = 0 %}
{% assign counter_btc = 0 %}
{% assign counter_eos = 0 %}
{% assign counter_tron = 0 %}
{% assign counter_stellar = 0 %}

{% for assets-management-tools in site.assets-management-tools  %}
{% if assets-management-tools.ecosystem contains 'ethereum' %}  {% assign counter_eth = counter_eth | plus: 1 %}
 {% endif %}
{% if assets-management-tools.ecosystem contains 'bitcoin' %} {% endif %}
{% if assets-management-tools.ecosystem contains 'eos' %}  {% endif %}

{% assign counter = counter | plus: 1 %}


{% endfor %}


{% for derivatives in site.derivatives %}
{% if derivatives.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if derivatives.ecosystem contains 'bitcoin' %} {% endif %}
{% if derivatives.ecosystem contains 'eos' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}


{% for exchanges in site.exchanges %}
{% if exchanges.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if exchanges.ecosystem contains 'bitcoin' %} {% endif %}
{% if exchanges.ecosystem contains 'eos' %} {% endif %}
{% if exchanges.ecosystem contains 'tron' %} {% endif %}
{% if exchanges.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}

{% for margin-trading in site.margin-trading %}
{% if margin-trading.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if margin-trading.ecosystem contains 'bitcoin' %} {% endif %}
{% if margin-trading.ecosystem contains 'eos' %} {% endif %}
{% if margin-trading.ecosystem contains 'tron' %} {% endif %}
{% if margin-trading.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}


{% for infrastructure in site.infrastructure %}
{% if infrastructure.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if infrastructure.ecosystem contains 'bitcoin' %} {% endif %}
{% if infrastructure.ecosystem contains 'eos' %} {% endif %}
{% if infrastructure.ecosystem contains 'tron' %} {% endif %}
{% if infrastructure.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}


{% for insurance in site.insurance %}
{% if insurance.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if insurance.ecosystem contains 'bitcoin' %} {% endif %}
{% if insurance.ecosystem contains 'eos' %} {% endif %}
{% if insurance.ecosystem contains 'tron' %} {% endif %}
{% if insurance.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}


{% for assets-tokenization in site.assets-tokenization %}
{% if assets-tokenization.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if assets-tokenization.ecosystem contains 'bitcoin' %} {% endif %}
{% if assets-tokenization.ecosystem contains 'eos' %} {% endif %}
{% if assets-tokenization.ecosystem contains 'tron' %} {% endif %}
{% if assets-tokenization.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}

{% for payments in site.payments %}
{% if payments.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if payments.ecosystem contains 'bitcoin' %} {% endif %}
{% if payments.ecosystem contains 'eos' %} {% endif %}
{% if payments.ecosystem contains 'tron' %} {% endif %}
{% if payments.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}

{% for kyc_identity in site.kyc_identity %}
{% if kyc_identity.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if kyc_identity.ecosystem contains 'bitcoin' %} {% endif %}
{% if kyc_identity.ecosystem contains 'eos' %} {% endif %}
{% if kyc_identity.ecosystem contains 'tron' %} {% endif %}
{% if kyc_identity.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}



{% for lending in site.lending %}
{% if lending.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if lending.ecosystem contains 'bitcoin' %} {% endif %}
{% if lending.ecosystem contains 'eos' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}


{% for marketplaces in site.marketplaces %}
{% if marketplaces.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if marketplaces.ecosystem contains 'bitcoin' %} {% endif %}
{% if marketplaces.ecosystem contains 'eos' %} {% endif %}
{% if marketplaces.ecosystem contains 'tron' %} {% endif %}
{% if marketplaces.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}


{% for prediction_markets in site.prediction_markets %}
{% if prediction_markets.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if prediction_markets.ecosystem contains 'bitcoin' %} {% endif %}
{% if prediction_markets.ecosystem contains 'eos' %} {% endif %}
{% if prediction_markets.ecosystem contains 'tron' %} {% endif %}
{% if prediction_markets.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}


{% for stablecoins in site.stablecoins %}
{% if stablecoins.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if stablecoins.ecosystem contains 'bitcoin' %} {% endif %}
{% if stablecoins.ecosystem contains 'eos' %} {% endif %}
{% if stablecoins.ecosystem contains 'tron' %} {% endif %}
{% if stablecoins.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}


{% for analytics in site.analytics %}
{% if analytics.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if analytics.ecosystem contains 'bitcoin' %} {% endif %}
{% if analytics.ecosystem contains 'eos' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}

DeFi is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols that run without intermediaries. We have {{ counter }} DeFi projects listed and {{ counter_eth }} of them built on Ethereum.


# Assets Management Tools

{% for assets-management-tools in site.assets-management-tools  %}
{% if assets-management-tools.ecosystem contains 'ethereum' %}
### <a href="{{ assets-management-tools.product-url }}">{{ assets-management-tools.product-title }}</a>



{{ assets-management-tools.product-description }}
{% endif %}
{% endfor %}

# Derivatives

{% for derivatives in site.derivatives %}
{% if derivatives.ecosystem contains 'ethereum' %}
### <a href="{{ derivatives.product-url }}">{{ derivatives.product-title }}</a>



{{ derivatives.product-description }}
{% endif %}
{% endfor %}

# Decentralized exchanges on Ethereum

{% for exchanges in site.exchanges %}
{% if exchanges.ecosystem contains 'ethereum' %}
### <a href="{{ exchanges.product-url }}">{{ exchanges.product-title }}</a>



{{ exchanges.product-description }}
{% endif %}
{% endfor %}

# Margin Trading on Ethereum

{% for margin-trading in site.margin-trading %}
### <a href="{{ margin-trading.product-url }}">{{ margin-trading.product-title }}</a>


{{ margin-trading.product-description }}

{% endfor %}

# DeFi Infrastructure & Dev Tooling

{% for infrastructure in site.infrastructure %}
{% if infrastructure.ecosystem contains 'ethereum' %}
### <a href="{{ infrastructure.product-url }}">{{ infrastructure.product-title }}</a>



{{ infrastructure.product-description }}
{% endif %}
{% endfor %}

# Decentralized Insurance Platforms

{% for insurance in site.insurance %}
{% if insurance.ecosystem contains 'ethereum' %}
### <a href="{{ insurance.product-url }}">{{ insurance.product-title }}</a>



{{ insurance.product-description }}
{% endif %}
{% endfor %}

# Asset Tokenization

{% for assets-tokenization in site.assets-tokenization %}
{% if assets-tokenization.ecosystem contains 'ethereum' %}
### <a href="{{ assets-tokenization.product-url }}">{{ assets-tokenization.product-title }}</a>



{{ assets-tokenization.product-description }}
{% endif %}
{% endfor %}

# KYC & Identity

{% for kyc_identity in site.kyc_identity %}
{% if kyc_identity.ecosystem contains 'ethereum' %}
### <a href="{{ kyc_identity.product-url }}">{{ kyc_identity.product-title }}</a>



{{ kyc_identity.product-description }}
{% endif %}
{% endfor %}


# Decentralized Lending on Ethereum

{% for lending in site.lending %}
{% if lending.ecosystem contains 'ethereum' %}
### <a href="{{ lending.product-url }}">{{ lending.product-title }}</a>



{{ lending.product-description }}
{% endif %}
{% endfor %}

# Payments

{% for payments in site.payments %}
### <a href="{{ payments.product-url }}">{{ payments.product-title }}</a>


{{ payments.product-description }}

{% endfor %}

# Marketplaces

{% for marketplaces in site.marketplaces %}
{% if marketplaces.ecosystem contains 'ethereum' %}
### <a href="{{ marketplaces.product-url }}">{{ marketplaces.product-title }}</a>



{{ marketplaces.product-description }}
{% endif %}
{% endfor %}

# Prediction Markets

{% for prediction_markets in site.prediction_markets %}
{% if prediction_markets.ecosystem contains 'ethereum' %}
### <a href="{{ prediction_markets.product-url }}">{{ prediction_markets.product-title }}</a>



{{ prediction_markets.product-description }}
{% endif %}
{% endfor %}

# Stablecoins

{% for stablecoins in site.stablecoins %}
{% if stablecoins.ecosystem contains 'ethereum' %}
### <a href="{{ stablecoins.product-url }}">{{ stablecoins.product-title }}</a>



{{ stablecoins.product-description }}
{% endif %}
{% endfor %}

# Analytics

{% for analytics in site.analytics %}
{% if analytics.ecosystem contains 'ethereum' %}
### <a href="{{ analytics.product-url }}">{{ analytics.product-title }}</a>


{{ analytics.product-description }}
{% endif %}
{% endfor %}
