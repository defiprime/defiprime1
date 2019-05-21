---
layout: page
title:  "Insurance"
permalink: insurance
h1title: Decentralized Insurance Platforms
pagetitle: Best Decentralized Insurance Platforms - Crowdsurance Platforms
metadescription: Decentralized Insurance Platforms. Insurance is a practice or arrangement by which a company provides a guarantee of compensation for specified loss, damage, illness, or death in return for payment of a premium.
category: products
---

Insurance is a practice or arrangement by which a company provides a guarantee of compensation for specified loss, damage, illness, or death in return for payment of a premium.

{% for insurance in site.insurance %}
### <a href="{{ insurance.product-url }}">{{ insurance.product-title }}</a>{% if insurance.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if insurance.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if insurance.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if insurance.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if insurance.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}

![]({{ insurance.image }})

{{ insurance.product-description }}

{% endfor %}
