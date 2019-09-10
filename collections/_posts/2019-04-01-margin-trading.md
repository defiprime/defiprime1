---
layout: page
title:  "Margin trading"
permalink: margin-trading
h1title: Margin trading
pagetitle: DeFi crypto margin trading - DeFi Short and Leveraged trading platforms    
metadescription: DeFi crypto margin trading refers to the practice of using borrowed funds from a broker to trade a financial asset, which forms the collateral for the loan from the broker.
category: products
og: /images/og-margin-trading.png
---
DeFi crypto margin trading refers to the practice of using borrowed funds from a broker to trade a financial asset, which forms the collateral for the loan from the broker. Usually broker in DeFi it's one of autonomous money markets.

{% for margin-trading in site.margin-trading %}
### <a href="{{ margin-trading.product-url }}">{{ margin-trading.product-title }}</a>{% if margin-trading.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if margin-trading.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if margin-trading.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %} <a href="/product/{{ margin-trading.product-title | slugify: "latin"}}"><i title="Would you recommend this product?" class="far fa-comments"></i></a>

![]({{ margin-trading.image }})

{{ margin-trading.product-description }}

{% endfor %}
