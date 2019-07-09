---
layout: page
title:  "Decentralized exchanges"
permalink: exchanges
h1title: Decentralized exchanges
pagetitle: List of decentralized exchanges - best dex Decentralized exchanges    
metadescription: A decentralized exchange (DEX) is a cryptocurrency exchange which operates in a decentralized way, without a central authority.
category: products
og: /images/og-decentralized-exchanges.png
---
A decentralized exchange (DEX) is a cryptocurrency exchange which operates in a decentralized way, without a central authority.

{% for exchanges in site.exchanges %}
### <a href="{{ exchanges.product-url }}">{{ exchanges.product-title }}</a>{% if exchanges.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if exchanges.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if exchanges.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if exchanges.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if exchanges.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}{% if exchanges.type == 'non-custodial' %}<i class="fas fa-user-lock" title="Non-custodial"></i>{% endif %}

![]({{ exchanges.image }})

{{ exchanges.product-description }}

{% endfor %}
