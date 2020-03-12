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

{% for assets-management-tools in site.assets-management-tools  %}
{% if assets-management-tools.ecosystem contains 'bitcoin' %}
### <a href="{{ assets-management-tools.product-url }}">{{ assets-management-tools.product-title }}</a>
<span>
{% if assets-management-tools.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if assets-management-tools.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if assets-management-tools.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %} {% if  assets-management-tools.platform contains 'ios' %}    <i class="fab fa-app-store-ios" title="Mobile wallet for iOS"></i> {% endif %}  {% if  assets-management-tools.platform contains 'android' %}    <i class="fab fa-android" title="Mobile wallet for Android"></i> {% endif %} {% if  assets-management-tools.platform contains 'web' %}    <i class="fab fa-chrome" title="Browser based wallet"></i> {% endif %} {% if  assets-management-tools.platform contains 'win' %}    <i class="fab fa-windows" title="Desktop wallet for windows"></i> {% endif %} {% if  assets-management-tools.platform contains 'mac' %}    <i class="fab fa-apple" title="Desktop wallet for osx"></i> {% endif %}
</span>


{{ assets-management-tools.product-description }}
{% endif %}
{% endfor %}


# BTC Decentralized Exchanges

{% for exchanges in site.exchanges %}
{% if exchanges.ecosystem contains 'bitcoin' %}
### <a href="{{ exchanges.product-url }}">{{ exchanges.product-title }}</a>
<span>
{% if exchanges.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if exchanges.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if exchanges.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if exchanges.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if exchanges.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}{% if exchanges.type == 'non-custodial' %}<i class="fas fa-user-lock" title="Non-custodial"></i>{% endif %}
</span>


{{ exchanges.product-description }}
{% endif %}
{% endfor %}



# Bitcoin Crypto Lending

{% for lending in site.lending %}
{% if lending.ecosystem contains 'bitcoin' %}
### <a href="{{ lending.product-url }}">{{ lending.product-title }}</a>
<span>
{% if lending.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem") {% endif %} {% if lending.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if lending.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if lending.type == 'non-custodial' %}<i class="fas fa-user-lock" title="Non-custodial"></i>{% endif %} {% if lending.type contains 'cefi' %}<i class="fas fa-bullseye" title="CeFi product. CeFi products are custodial, use centralized price feeds, initiate margin calls centrally, centrally determine interest rates, and centrally provide liquidity for their margin calls."></i>{% endif %}
</span>

{{ lending.product-description }}
{% endif %}
{% endfor %}

# DeFi Infrastructure & Dev Tooling

{% for infrastructure in site.infrastructure %}
{% if infrastructure.ecosystem contains 'bitcoin' %}
### <a href="{{ infrastructure.product-url }}">{{ infrastructure.product-title }}</a>
<span>
{% if infrastructure.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if infrastructure.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if infrastructure.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if infrastructure.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if infrastructure.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}
</span>


{{ infrastructure.product-description }}
{% endif %}
{% endfor %}

# BTC Payments Solutions and Service Providers
{% for payments in site.payments %}
{% if payments.ecosystem contains 'bitcoin' %}
### <a href="{{ payments.product-url }}">{{ payments.product-title }}</a>
<span>
{% if payments.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if payments.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if payments.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}
</span>

{{ payments.product-description }}
{% endif %}

{% endfor %}

# Marketplaces

{% for marketplaces in site.marketplaces %}
{% if marketplaces.ecosystem contains 'bitcoin' %}
### <a href="{{ marketplaces.product-url }}">{{ marketplaces.product-title }}</a>
<span>
{% if marketplaces.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if marketplaces.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if marketplaces.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if marketplaces.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if marketplaces.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}
</span>


{{ marketplaces.product-description }}
{% endif %}
{% endfor %}
