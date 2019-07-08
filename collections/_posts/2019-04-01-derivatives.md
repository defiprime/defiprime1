---
layout: page
title:  "Derivatives"
permalink: derivatives
h1title: Derivatives
pagetitle: Decentralized Crypto Derivatives. Crypto derivatives exchanges and platforms.   
metadescription: What is Cryptocurrency Derivatives? In finance, a derivative is a contract that derives its value from the performance of an underlying entity. This underlying entity can be an asset, index, or interest rate, and is often simply called the underlying.
category: products
---
In finance, a derivative is a contract that derives its value from the performance of an underlying entity. This underlying entity can be an asset, index, or interest rate, and is often simply called the "underlying."

{% for derivatives in site.derivatives %}
### <a href="{{ derivatives.product-url }}?utm_source=defiprime.com">{{ derivatives.product-title }}</a>{% if derivatives.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if derivatives.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if derivatives.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}

![]({{ derivatives.image }})

{{ derivatives.product-description }}

{% endfor %}
