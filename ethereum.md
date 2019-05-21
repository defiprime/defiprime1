---
layout: ecosystem
title: Ethereum DeFi ecosystem
metadescription: List of the best Ethereum Defi Products. Decentralized Finance (DeFi) is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols that run without intermediaries.
permalink: ethereum
h1title: Ethereum DeFi ecosystem
pagetitle: Ethereum DeFi ecosystem
featured-image: /images/og-ethereum.png
toc: true
---

# Assets Management Tools

{% for assets-managament-tools in site.assets-managament-tools  %}
{% if assets-managament-tools.ecosystem contains 'ethereum' %}
### <a href="{{ assets-managament-tools.product-url }}?ref=defiprime.com">{{ assets-managament-tools.product-title }}</a>{% if assets-managament-tools.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if assets-managament-tools.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if assets-managament-tools.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}


{{ assets-managament-tools.product-description }}
{% endif %}
{% endfor %}

# Derivatives

{% for derivatives in site.derivatives %}
{% if derivatives.ecosystem contains 'ethereum' %}
### <a href="{{ derivatives.product-url }}?ref=defiprime.com">{{ derivatives.product-title }}</a>{% if derivatives.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if derivatives.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if derivatives.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}


{{ derivatives.product-description }}
{% endif %}
{% endfor %}

# Decentralized exchanges on Ethereum

{% for exchanges in site.exchanges %}
{% if exchanges.ecosystem contains 'ethereum' %}
### <a href="{{ exchanges.product-url }}?ref=defiprime.com">{{ exchanges.product-title }}</a>{% if exchanges.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if exchanges.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if exchanges.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if exchanges.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if exchanges.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}{% if exchanges.type == 'non-custodial' %}<i class="fas fa-user-lock" title="Non-custodial"></i>{% endif %}


{{ exchanges.product-description }}
{% endif %}
{% endfor %}


# DeFi Infrastructure

{% for infrastructure in site.infrastructure %}
{% if infrastructure.ecosystem contains 'ethereum' %}
### <a href="{{ infrastructure.product-url }}?ref=defiprime.com">{{ infrastructure.product-title }}</a>{% if infrastructure.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if infrastructure.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if infrastructure.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if infrastructure.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if infrastructure.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}


{{ infrastructure.product-description }}
{% endif %}
{% endfor %}

# Decentralized Insurance Platforms

{% for insurance in site.insurance %}
{% if insurance.ecosystem contains 'ethereum' %}
### <a href="{{ insurance.product-url }}?ref=defiprime.com">{{ insurance.product-title }}</a>{% if insurance.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if insurance.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if insurance.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if insurance.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if insurance.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}


{{ insurance.product-description }}
{% endif %}
{% endfor %}

# Assets Tokenization

{% for assets-tokenization in site.assets-tokenization %}
{% if assets-tokenization.ecosystem contains 'ethereum' %}
### <a href="{{ assets-tokenization.product-url }}?ref=defiprime.com">{{ assets-tokenization.product-title }}</a>{% if assets-tokenization.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if assets-tokenization.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if assets-tokenization.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if assets-tokenization.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if assets-tokenization.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}


{{ assets-tokenization.product-description }}
{% endif %}
{% endfor %}

# KYC & Identity

{% for kyc_identity in site.kyc_identity %}
{% if kyc_identity.ecosystem contains 'ethereum' %}
### <a href="{{ kyc_identity.product-url }}?ref=defiprime.com">{{ kyc_identity.product-title }}</a>{% if kyc_identity.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if kyc_identity.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if kyc_identity.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if kyc_identity.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if kyc_identity.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}


{{ kyc_identity.product-description }}
{% endif %}
{% endfor %}


# Decentralized Lending on Ethereum

{% for lending in site.lending %}
{% if lending.ecosystem contains 'ethereum' %}
### <a href="{{ lending.product-url }}?ref=defiprime.com">{{ lending.product-title }}</a>{% if lending.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem") {% endif %} {% if lending.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if lending.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if lending.type == 'non-custodial' %}<i class="fas fa-user-lock" title="Non-custodial"></i>{% endif %}


{{ lending.product-description }}
{% endif %}
{% endfor %}

# Marketplaces

{% for marketplaces in site.marketplaces %}
{% if marketplaces.ecosystem contains 'ethereum' %}
### <a href="{{ marketplaces.product-url }}?ref=defiprime.com">{{ marketplaces.product-title }}</a>{% if marketplaces.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if marketplaces.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if marketplaces.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if marketplaces.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if marketplaces.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}


{{ marketplaces.product-description }}
{% endif %}
{% endfor %}

# Prediction Markets

{% for prediction_markets in site.prediction_markets %}
{% if prediction_markets.ecosystem contains 'ethereum' %}
### <a href="{{ prediction_markets.product-url }}?ref=defiprime.com">{{ prediction_markets.product-title }}</a>{% if prediction_markets.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if prediction_markets.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if prediction_markets.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if prediction_markets.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if prediction_markets.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}


{{ prediction_markets.product-description }}
{% endif %}
{% endfor %}

# Stablecoins

{% for stablecoins in site.stablecoins %}
{% if stablecoins.ecosystem contains 'ethereum' %}
### <a href="{{ stablecoins.product-url }}?ref=defiprime.com">{{ stablecoins.product-title }}</a>{% if stablecoins.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if stablecoins.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if stablecoins.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if stablecoins.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if stablecoins.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}


{{ stablecoins.product-description }}
{% endif %}
{% endfor %}

# Analytics

{% for analytics in site.analytics %}
{% if analytics.ecosystem contains 'ethereum' %}
### <a href="{{ analytics.product-url }}?ref=defiprime.com">{{ analytics.product-title }}</a>{% if analytics.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if analytics.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if analytics.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}


{{ analytics.product-description }}
{% endif %}
{% endfor %}
