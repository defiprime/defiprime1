---
layout: ecosystem
title: events
metadescription: List of the best DeFi events. DeFi Calendar with the best meetups, conferences, and hackathons around the world.
permalink: events
h1title: DeFi Meetups and Conferences
pagetitle: DeFi Events Calendar. DeFi meetups, conferences and hackathons
featured-image: /images/og-events.png

---
Upcoming events related to the DeFi ecosystem. Do you want to add your event here? Fill [this form](https://sneg55.typeform.com/to/SPrjTk) and we'll get in touch.


{% for events in site.events %}

{% unless events.date < site.time %}

### <a href="{{ events.product-url }}">{{ events.product-title }}</a>{% if events.ecosystem contains 'ethereum' %} ![](images/ether.png "Ethereum ecosystem"){% endif %} {% if events.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Bitcoin ecosystem"){% endif %} {% if events.ecosystem contains 'eos' %} ![](/images/eos.png "EOS ecosystem"){% endif %}

{{ events.date | date_to_string }} - {{ events.location }}

![]({{ events.image }})

{{ events.product-description }}
{% endunless %}

{% endfor %}
