---
title: Stablecoins
layout: page
permalink: stablecoins
h1title: Stablecoins
pagetitle: Complete Stablecoins List - Decentralized Stablecoins  
metadescription: Stablecoins are cryptocurrencies designed to minimize the volatility of the price of the stablecoin, relative to some 'stable' asset or basket of assets.
category: products
og: /images/og-stablecoins.png
---
Stablecoins are cryptocurrencies created to decrease the volatility of the coin's price, relative to some "stable" asset or basket of assets. A stablecoin can be pegged to currency or exchange-traded commodities.


{% for stablecoins in site.stablecoins %}
### <a href="{{ stablecoins.product-url }}?utm_source=defiprime.com">{{ stablecoins.product-title }}</a>{% if stablecoins.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if stablecoins.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if stablecoins.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if stablecoins.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if stablecoins.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}

![]({{ stablecoins.image }})

{{ stablecoins.product-description }}

{% endfor %}
