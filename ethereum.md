---
layout: ecosystem
title: Ethereum DeFi
metadescription: List of the best Decentralized Finance Products. Decentralized Finance (DeFi) is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols that run without intermediaries.

---

# Lending

{% for lending in site.lending %}
{% if lending.ecosystem contains 'ethereum' %}
### <a href="{{ lending.product-url }}">{{ lending.product-title }}</a>{% if lending.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem") {% endif %} {% if lending.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if lending.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if lending.type == 'non-custodial' %}<i class="fas fa-user-lock" title="Non-custodial"></i>{% endif %}

![]({{ lending.image }})

{{ lending.product-description }}
{% endif %}
{% endfor %}

# Assets Management Tools
{% assign assets-managament-tools = site.assets-managament-tools %}
{% for assets-managament-tool in assets-managament-tools %}
{% if lending.ecosystem contains 'ethereum' %}

### <a href="{{ assets-managament-tools.product-url }}">{{ assets-managament-tools.product-title }}</a>{% if assets-managament-tools.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if assets-managament-tools.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if assets-managament-tools.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}

![]({{ assets-managament-tools.image }})

{{ assets-managament-tools.product-description }}
{% endif %}

{% endfor %}

# Derivatives

{% for derivatives in site.derivatives %}
{% if lending.ecosystem contains 'ethereum' %}

### <a href="{{ derivatives.product-url }}">{{ derivatives.product-title }}</a>{% if derivatives.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if derivatives.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if derivatives.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}

![]({{ derivatives.image }})

{{ derivatives.product-description }}
{% endif %}

{% endfor %}

# Exchanges

{% for exchanges in site.exchanges %}
{% if lending.ecosystem contains 'ethereum' %}

### <a href="{{ exchanges.product-url }}">{{ exchanges.product-title }}</a>{% if exchanges.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if exchanges.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if exchanges.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if exchanges.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if exchanges.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}{% if exchanges.type == 'non-custodial' %}<i class="fas fa-user-lock" title="Non-custodial"></i>{% endif %}

![]({{ exchanges.image }})

{{ exchanges.product-description }}
{% endif %}

{% endfor %}

# Infrastructure


{% for infrastructure in site.infrastructure %}
{% if lending.ecosystem contains 'ethereum' %}

### <a href="{{ infrastructure.product-url }}">{{ infrastructure.product-title }}</a>{% if infrastructure.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if infrastructure.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if infrastructure.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if infrastructure.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if infrastructure.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}

![]({{ infrastructure.image }})

{{ infrastructure.product-description }}
{% endif %}

{% endfor %}
