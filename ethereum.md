---
layout: ecosystem
title: Ethereum DeFi
metadescription: List of the best Decentralized Finance Products. Decentralized Finance (DeFi) is the movement that leverages decentralized networks to transform old financial products into trustless and transparent protocols that run without intermediaries.

---

# Lending

{% for collection in site.collections %}
{% for collection in collections %}
### <a href="{{ collection.product-url }}">{{ items.product-title }}</a>{% if items.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem") {% endif %} {% if items.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if items.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if items.type == 'non-custodial' %}<i class="fas fa-user-lock" title="Non-custodial"></i>{% endif %}

{{ items.product-description }}

{% endfor %}
{% endfor %}
