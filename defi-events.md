---
layout: ecosystem
title: events
metadescription: List of the best Defi events. Calendar with the best DeFi meetups and conferences around the world.
permalink: events
h1title: DeFi Meetups and Conferences
pagetitle: DeFi Events. Defi meetups and conferences
featured-image: /images/og-events.png

---
Upcoming events related to the DeFi ecosystem. Do you want to add your event here? Fill [this form](https://sneg55.typeform.com/to/SPrjTk) and we'll get in touch.


{% for events in site.events %}

{% unless events.date < site.time %}

### <a href="{{ events.product-url }}">{{ events.product-title }}</a>{% if events.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if events.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if events.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}

{{ events.date | date_to_string }} - {{ events.location }}

![]({{ events.image }})

{{ events.product-description }}
{% endunless %}

{% endfor %}
