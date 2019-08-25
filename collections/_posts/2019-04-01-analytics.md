---
layout: page
title:  "Analytics"
permalink: defi-analytics
h1title: Analytics
pagetitle: DeFi Analytics - Best Tools to keep track of DeFi ecosystem    
metadescription: DeFi Analytics is the discovery, interpretation, and communication of meaningful patterns in data; and the process of applying those patterns towards effective decision making.
category: products
og: /images/og-analytics.png
redirect_from:
  - analytics
---
Analytics is the discovery, interpretation, and communication of meaningful patterns in data; and the process of applying those patterns towards effective decision making.

{% for analytics in site.analytics %}
### <a href="{{ analytics.product-url }}">{{ analytics.product-title }}</a>{% if analytics.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if analytics.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if analytics.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}  <a href="/product/{{ analytics.product-title | slugify: "latin"}}"><i title="Would you recommend this product?" class="far fa-comments"></i></a>


![]({{ analytics.image }})

{{ analytics.product-description }}


{% endfor %}
