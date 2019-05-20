---
layout: page
title:  "KYC & Identity"
permalink: decentralized_kyc_identity
h1title: Decentralized Identity
pagetitle: Decentralized Identity Systems
metadescription: KYC is an abbreviation for Know Your Customer and can refer to government regulations designed to prevent money laundering, financing terrorism and other crimes involving money.
category: products
---

KYC is an abbreviation for Know Your Customer refers to government regulations designed to prevent money laundering, financing terrorism and other crimes involving money. It also refers to the policies, procedures, and technology used by banks and financial services companies to comply with KYC regulations.

{% for kyc_identity in site.kyc_identity %}
### <a href="{{ kyc_identity.product-url }}">{{ kyc_identity.product-title }}</a>{% if kyc_identity.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if kyc_identity.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if kyc_identity.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if kyc_identity.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if kyc_identity.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}

![]({{ kyc_identity.image }})

{{ kyc_identity.product-description }}

{% endfor %}
