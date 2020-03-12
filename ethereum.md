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

{% assign eth_projects = all_projects | where_exp:"item", "item.ecosystem contains 'ethereum'"%}

{% assign counter_eth = eth_projects.size %}

DeFi is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols that run without intermediaries. We have {{ counter }} DeFi projects listed and {{ counter_eth }} of them built on Ethereum.


# Assets Management Tools

{% for assets-management-tools in site.assets-management-tools  %}
{% if assets-management-tools.ecosystem contains 'ethereum' %}
### <a href="{{ assets-management-tools.product-url }}">{{ assets-management-tools.product-title }}</a>
<span>
{% if assets-management-tools.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if assets-management-tools.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if assets-management-tools.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %} {% if  assets-management-tools.platform contains 'ios' %}    <i class="fab fa-app-store-ios" title="Mobile wallet for iOS"></i> {% endif %}  {% if  assets-management-tools.platform contains 'android' %}    <i class="fab fa-android" title="Mobile wallet for Android"></i> {% endif %} {% if  assets-management-tools.platform contains 'web' %}    <i class="fab fa-chrome" title="Browser based wallet"></i> {% endif %} {% if  assets-management-tools.platform contains 'win' %}    <i class="fab fa-windows" title="Desktop wallet for windows"></i> {% endif %} {% if  assets-management-tools.platform contains 'mac' %}    <i class="fab fa-apple" title="Desktop wallet for osx"></i> {% endif %}
</span>


{{ assets-management-tools.product-description }}
{% endif %}
{% endfor %}

# Alternative Savings Apps

{% for alternative-savings in site.alternative-savings %}
{% if alternative-savings.ecosystem contains 'ethereum' %}
### <a href="{{ alternative-savings.product-url }}">{{ alternative-savings.product-title }}</a>
<span>
{% if alternative-savings.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if alternative-savings.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if alternative-savings.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}
</span>

{{ alternative-savings.product-description }}
{% endif %}
{% endfor %}

# Derivatives

{% for derivatives in site.derivatives %}
{% if derivatives.ecosystem contains 'ethereum' %}
### <a href="{{ derivatives.product-url }}">{{ derivatives.product-title }}</a>
<span>
{% if derivatives.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if derivatives.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if derivatives.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}
</span>


{{ derivatives.product-description }}
{% endif %}
{% endfor %}


# Decentralized exchanges on Ethereum

{% for exchanges in site.exchanges %}
{% if exchanges.ecosystem contains 'ethereum' %}
### <a href="{{ exchanges.product-url }}">{{ exchanges.product-title }}</a>
<span>
{% if exchanges.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if exchanges.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if exchanges.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if exchanges.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if exchanges.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}{% if exchanges.type == 'non-custodial' %}<i class="fas fa-user-lock" title="Non-custodial"></i>{% endif %}
</span>


{{ exchanges.product-description }}
{% endif %}
{% endfor %}

# Margin Trading on Ethereum

{% for margin-trading in site.margin-trading %}
### <a href="{{ margin-trading.product-url }}">{{ margin-trading.product-title }}</a>
<span>
{% if margin-trading.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if margin-trading.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if margin-trading.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}
</span>

{{ margin-trading.product-description }}

{% endfor %}

# DeFi Infrastructure & Dev Tooling

{% for infrastructure in site.infrastructure %}
{% if infrastructure.ecosystem contains 'ethereum' %}
### <a href="{{ infrastructure.product-url }}">{{ infrastructure.product-title }}</a>
<span>
{% if infrastructure.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if infrastructure.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if infrastructure.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if infrastructure.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if infrastructure.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}
</span>


{{ infrastructure.product-description }}
{% endif %}
{% endfor %}

# Ethereum-based DAO Platforms

{% for dao in site.dao %}
{% if dao.ecosystem contains 'ethereum' %}
### <a href="{{ dao.product-url }}">{{ dao.product-title }}</a>
<span>
{% if dao.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if dao.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if dao.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if dao.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if dao.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}
</span>


{{ dao.product-description }}
{% endif %}
{% endfor %}

# Decentralized Insurance Platforms

{% for insurance in site.insurance %}
{% if insurance.ecosystem contains 'ethereum' %}
### <a href="{{ insurance.product-url }}">{{ insurance.product-title }}</a>
<span>
{% if insurance.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if insurance.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if insurance.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if insurance.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if insurance.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}
</span>


{{ insurance.product-description }}
{% endif %}
{% endfor %}

# Asset Tokenization

{% for assets-tokenization in site.assets-tokenization %}
{% if assets-tokenization.ecosystem contains 'ethereum' %}
### <a href="{{ assets-tokenization.product-url }}">{{ assets-tokenization.product-title }}</a>
<span>
{% if assets-tokenization.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if assets-tokenization.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if assets-tokenization.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if assets-tokenization.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if assets-tokenization.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}
</span>


{{ assets-tokenization.product-description }}
{% endif %}
{% endfor %}

# KYC & Identity

{% for kyc_identity in site.kyc_identity %}
{% if kyc_identity.ecosystem contains 'ethereum' %}
### <a href="{{ kyc_identity.product-url }}">{{ kyc_identity.product-title }}</a>
<span>
{% if kyc_identity.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if kyc_identity.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if kyc_identity.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if kyc_identity.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if kyc_identity.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}
</span>


{{ kyc_identity.product-description }}
{% endif %}
{% endfor %}


# Decentralized Lending on Ethereum

{% for lending in site.lending %}
{% if lending.ecosystem contains 'ethereum' %}
### <a href="{{ lending.product-url }}">{{ lending.product-title }}</a>
<span>
{% if lending.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem") {% endif %} {% if lending.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if lending.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if lending.type == 'non-custodial' %}<i class="fas fa-user-lock" title="Non-custodial"></i>{% endif %} {% if lending.type contains 'cefi' %}<i class="fas fa-bullseye" title="CeFi product. CeFi products are custodial, use centralized price feeds, initiate margin calls centrally, centrally determine interest rates, and centrally provide liquidity for their margin calls."></i>{% endif %}
</span>


{{ lending.product-description }}
{% endif %}
{% endfor %}

# Payments

{% for payments in site.payments %}
### <a href="{{ payments.product-url }}">{{ payments.product-title }}</a>
<span>
{% if payments.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if payments.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if payments.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}
</span>

{{ payments.product-description }}

{% endfor %}

# Marketplaces

{% for marketplaces in site.marketplaces %}
{% if marketplaces.ecosystem contains 'ethereum' %}
### <a href="{{ marketplaces.product-url }}">{{ marketplaces.product-title }}</a>
<span>
{% if marketplaces.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if marketplaces.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if marketplaces.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if marketplaces.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if marketplaces.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}
</span>


{{ marketplaces.product-description }}
{% endif %}
{% endfor %}

# Prediction Markets

{% for prediction_markets in site.prediction_markets %}
{% if prediction_markets.ecosystem contains 'ethereum' %}
### <a href="{{ prediction_markets.product-url }}">{{ prediction_markets.product-title }}</a>
<span>
{% if prediction_markets.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if prediction_markets.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if prediction_markets.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if prediction_markets.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if prediction_markets.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}
</span>


{{ prediction_markets.product-description }}
{% endif %}
{% endfor %}

# Stablecoins

{% for stablecoins in site.stablecoins %}
{% if stablecoins.ecosystem contains 'ethereum' %}
### <a href="{{ stablecoins.product-url }}">{{ stablecoins.product-title }}</a>
<span>
{% if stablecoins.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if stablecoins.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if stablecoins.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if stablecoins.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if stablecoins.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}
</span>


{{ stablecoins.product-description }}
{% endif %}
{% endfor %}

# Analytics

{% for analytics in site.analytics %}
{% if analytics.ecosystem contains 'ethereum' %}
### <a href="{{ analytics.product-url }}">{{ analytics.product-title }}</a>
<span>
{% if analytics.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if analytics.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if analytics.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}
</span>


{{ analytics.product-description }}
{% endif %}
{% endfor %}
