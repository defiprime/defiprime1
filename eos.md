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
{% if assets-management-tools.ecosystem contains 'eos' %} {% assign counter_eos = counter_eos | plus: 1 %} {% endif %}

{% assign counter = counter | plus: 1 %}


{% endfor %}


{% for derivatives in site.derivatives %}
{% if derivatives.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if derivatives.ecosystem contains 'bitcoin' %} {% endif %}
{% if derivatives.ecosystem contains 'eos' %} {% assign counter_eos = counter_eos | plus: 1 %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}


{% for exchanges in site.exchanges %}
{% if exchanges.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if exchanges.ecosystem contains 'bitcoin' %} {% endif %}
{% if exchanges.ecosystem contains 'eos' %} {% assign counter_eos = counter_eos | plus: 1 %} {% endif %}
{% if exchanges.ecosystem contains 'tron' %} {% endif %}
{% if exchanges.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}


{% for margin-trading in site.margin-trading %}
{% if margin-trading.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if margin-trading.ecosystem contains 'bitcoin' %} {% endif %}
{% if margin-trading.ecosystem contains 'eos' %} {% assign counter_eos = counter_eos | plus: 1 %} {% endif %}
{% if margin-trading.ecosystem contains 'tron' %} {% endif %}
{% if margin-trading.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}

{% for infrastructure in site.infrastructure %}
{% if infrastructure.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if infrastructure.ecosystem contains 'bitcoin' %} {% endif %}
{% if infrastructure.ecosystem contains 'eos' %} {% assign counter_eos = counter_eos | plus: 1 %} {% endif %}
{% if infrastructure.ecosystem contains 'tron' %} {% endif %}
{% if infrastructure.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}


{% for insurance in site.insurance %}
{% if insurance.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if insurance.ecosystem contains 'bitcoin' %} {% endif %}
{% if insurance.ecosystem contains 'eos' %} {% assign counter_eos = counter_eos | plus: 1 %} {% endif %}
{% if insurance.ecosystem contains 'tron' %} {% endif %}
{% if insurance.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}


{% for assets-tokenization in site.assets-tokenization %}
{% if assets-tokenization.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if assets-tokenization.ecosystem contains 'bitcoin' %} {% endif %}
{% if assets-tokenization.ecosystem contains 'eos' %} {% assign counter_eos = counter_eos | plus: 1 %} {% endif %}
{% if assets-tokenization.ecosystem contains 'tron' %} {% endif %}
{% if assets-tokenization.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}


{% for kyc_identity in site.kyc_identity %}
{% if kyc_identity.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if kyc_identity.ecosystem contains 'bitcoin' %} {% endif %}
{% if kyc_identity.ecosystem contains 'eos' %} {% assign counter_eos = counter_eos | plus: 1 %} {% endif %}
{% if kyc_identity.ecosystem contains 'tron' %} {% endif %}
{% if kyc_identity.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}



{% for lending in site.lending %}
{% if lending.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if lending.ecosystem contains 'bitcoin' %} {% endif %}
{% if lending.ecosystem contains 'eos' %} {% assign counter_eos = counter_eos | plus: 1 %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}

{% for payments in site.payments %}
{% if payments.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if payments.ecosystem contains 'bitcoin' %} {% assign counter_btc = counter_btc | plus: 1 %} {% endif %}
{% if payments.ecosystem contains 'eos' %} {% assign counter_eos = counter_eos | plus: 1 %}  {% endif %}
{% if payments.ecosystem contains 'tron' %} {% endif %}
{% if payments.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}

{% for marketplaces in site.marketplaces %}
{% if marketplaces.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if marketplaces.ecosystem contains 'bitcoin' %} {% endif %}
{% if marketplaces.ecosystem contains 'eos' %} {% assign counter_eos = counter_eos | plus: 1 %} {% endif %}
{% if marketplaces.ecosystem contains 'tron' %} {% endif %}
{% if marketplaces.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}


{% for prediction_markets in site.prediction_markets %}
{% if prediction_markets.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if prediction_markets.ecosystem contains 'bitcoin' %} {% endif %}
{% if prediction_markets.ecosystem contains 'eos' %} {% assign counter_eos = counter_eos | plus: 1 %} {% endif %}
{% if prediction_markets.ecosystem contains 'tron' %} {% endif %}
{% if prediction_markets.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}


{% for stablecoins in site.stablecoins %}
{% if stablecoins.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if stablecoins.ecosystem contains 'bitcoin' %} {% endif %}
{% if stablecoins.ecosystem contains 'eos' %} {% assign counter_eos = counter_eos | plus: 1 %} {% endif %}
{% if stablecoins.ecosystem contains 'tron' %} {% endif %}
{% if stablecoins.ecosystem contains 'stellar' %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}


{% for analytics in site.analytics %}
{% if analytics.ecosystem contains 'ethereum' %} {% assign counter_eth = counter_eth | plus: 1 %} {% endif %}
{% if analytics.ecosystem contains 'bitcoin' %} {% endif %}
{% if analytics.ecosystem contains 'eos' %} {% assign counter_eos = counter_eos | plus: 1 %} {% endif %}

{% assign counter = counter | plus: 1 %}

{% endfor %}

DeFi is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols that run without intermediaries. We have {{ counter }} DeFi projects listed and {{ counter_eos }} of them using EOS.


# Assets Management Tools

{% for assets-management-tools in site.assets-management-tools  %}
{% if assets-management-tools.ecosystem contains 'eos' %}
### <a href="{{ assets-management-tools.product-url }}">{{ assets-management-tools.product-title }}</a>
<span>
{% if assets-management-tools.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if assets-management-tools.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if assets-management-tools.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %} {% if  assets-management-tools.platform contains 'ios' %}    <i class="fab fa-app-store-ios" title="Mobile wallet for iOS"></i> {% endif %}  {% if  assets-management-tools.platform contains 'android' %}    <i class="fab fa-android" title="Mobile wallet for Android"></i> {% endif %} {% if  assets-management-tools.platform contains 'web' %}    <i class="fab fa-chrome" title="Browser based wallet"></i> {% endif %} {% if  assets-management-tools.platform contains 'win' %}    <i class="fab fa-windows" title="Desktop wallet for windows"></i> {% endif %} {% if  assets-management-tools.platform contains 'mac' %}    <i class="fab fa-apple" title="Desktop wallet for osx"></i> {% endif %}
</span>


{{ assets-management-tools.product-description }}
{% endif %}
{% endfor %}

# Decentralized exchanges on EOS

{% for exchanges in site.exchanges %}
{% if exchanges.ecosystem contains 'eos' %}
### <a href="{{ exchanges.product-url }}">{{ exchanges.product-title }}</a>
<span>
{% if exchanges.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if exchanges.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if exchanges.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if exchanges.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if exchanges.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}{% if exchanges.type == 'non-custodial' %}<i class="fas fa-user-lock" title="Non-custodial"></i>{% endif %}
</span>


{{ exchanges.product-description }}
{% endif %}
{% endfor %}


# DeFi Infrastructure & Dev Tooling

{% for infrastructure in site.infrastructure %}
{% if infrastructure.ecosystem contains 'eos' %}
### <a href="{{ infrastructure.product-url }}">{{ infrastructure.product-title }}</a>
<span>
{% if infrastructure.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if infrastructure.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if infrastructure.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if infrastructure.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if infrastructure.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}
</span>


{{ infrastructure.product-description }}
{% endif %}
{% endfor %}


# Decentralized Lending on EOS

{% for lending in site.lending %}
{% if lending.ecosystem contains 'eos' %}
### <a href="{{ lending.product-url }}">{{ lending.product-title }}</a>
<span>
{% if lending.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem") {% endif %} {% if lending.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if lending.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if lending.type == 'non-custodial' %}<i class="fas fa-user-lock" title="Non-custodial"></i>{% endif %} {% if lending.type contains 'cefi' %}<i class="fas fa-bullseye" title="CeFi product. CeFi products are custodial, use centralized price feeds, initiate margin calls centrally, centrally determine interest rates, and centrally provide liquidity for their margin calls."></i>{% endif %}
</span>


{{ lending.product-description }}
{% endif %}
{% endfor %}

# EOS Stablecoins

{% for stablecoins in site.stablecoins %}
{% if stablecoins.ecosystem contains 'eos' %}
### <a href="{{ stablecoins.product-url }}">{{ stablecoins.product-title }}</a>
<span>
{% if stablecoins.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if stablecoins.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if stablecoins.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if stablecoins.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if stablecoins.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}
</span>


{{ stablecoins.product-description }}
{% endif %}
{% endfor %}
