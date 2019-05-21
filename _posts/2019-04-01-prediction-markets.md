---
layout: page
title:  "Prediction markets"
permalink: decentralized_prediction_markets
h1title: Prediction markets
pagetitle: Best prediction markets on crypto blockchains  
metadescription: Prediction markets are exchange-traded markets created for the purpose of trading the outcome of events.
category: products
---

Prediction markets are exchange-traded markets created to trade the outcome of events. The market prices can indicate what the crowd thinks the probability of the event is.

{% for prediction_markets in site.prediction_markets %}
### <a href="{{ prediction_markets.product-url }}">{{ prediction_markets.product-title }}</a>{% if prediction_markets.ecosystem contains 'ethereum' %} ![](images/ether.png "Built on Ethereum or related to Ethereum ecosystem"){% endif %} {% if prediction_markets.ecosystem contains 'bitcoin' %} ![](/images/btc.png "Using Bitcoin ecosystem"){% endif %} {% if prediction_markets.ecosystem contains 'eos' %} ![](/images/eos.png "Built on EOS or related to EOS ecosystem"){% endif %}{% if prediction_markets.ecosystem contains 'tron' %} ![](/images/tron.png "Built on Tron or related to Tron ecosystem"){% endif %}{% if prediction_markets.ecosystem contains 'stellar' %} ![](/images/stellar.png "Built on Stellar or related to Stellar ecosystem"){% endif %}

![]({{ prediction_markets.image }})

{{ prediction_markets.product-description }}

{% endfor %}
