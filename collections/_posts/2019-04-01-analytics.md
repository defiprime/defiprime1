---
layout: page
title:  "Analytics"
permalink: analytics
h1title: Analytics
pagetitle: DeFi Analytics - Best Tools to keep track of DeFi ecosystem    
metadescription: Analytics is the discovery, interpretation, and communication of meaningful patterns in data; and the process of applying those patterns towards effective decision making.
category: products
og: /images/og-analytics.png
---
Analytics is the discovery, interpretation, and communication of meaningful patterns in data; and the process of applying those patterns towards effective decision making.

{% for analytics in site.analytics %}
### <a href="{{ analytics.product-url }}?utm_source=defiprime.com">{{ analytics.product-title }}</a>{% if analytics.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if analytics.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if analytics.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}

![]({{ analytics.image }})

{{ analytics.product-description }}

{% endfor %}
