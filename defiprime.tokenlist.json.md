---
permalink: defiprime.tokenlist.json
layout: null
---
{% assign all_projects = site.alternative-savings
| concat: site.analytics
| concat: site.assets-management-tools
| concat: site.assets-tokenization
| concat: site.dao
| concat: site.derivatives
| concat: site.exchanges
| concat: site.infrastructure
| concat: site.insurance
| concat: site.kyc_identity
| concat: site.lending
| concat: site.margin-trading
| concat: site.marketplaces
| concat: site.payments
| concat: site.prediction_markets
| concat: site.stablecoins
 %}
     {% for all_project in all_projects %}
     {% if all_project.ticker  %}
     {
       "chainId": 1,
       "address": "{{ all_project.contract }}",
       "symbol": "{{ all_project.ticker }}",
       "name": "{{ all_project.product-title }}",
       "decimals": {{ all_project.decimals }},
       "tags": [
         "{{ all_project.coltitle }}"
       ]
     },
     {% endif %}
      {% endfor %}
