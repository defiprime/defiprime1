---
layout: page
title: "Prediction markets"
permalink: prediction-markets
h1title: Decentralized Prediction Markets
pagetitle: Best Decentralized Prediction Markets on crypto blockchains  
metadescription: Decentralized Prediction Markets - what it is? DeFi Prediction markets are exchange-traded markets created for the purpose of trading the outcome of events.
category: products
redirect_from:
  - decentralized_prediction_markets
---

Prediction markets are exchange-traded markets created to trade the outcome of events. The market prices can indicate what the crowd thinks the probability of the event is.

{% for prediction_markets in site.prediction_markets %}
### <a href="{{ prediction_markets.product-url }}?utm_source=defiprime.com">{{ prediction_markets.product-title }}</a>{% if prediction_markets.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if prediction_markets.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if prediction_markets.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if prediction_markets.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if prediction_markets.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}

![]({{ prediction_markets.image }})

{{ prediction_markets.product-description }}

{% endfor %}
