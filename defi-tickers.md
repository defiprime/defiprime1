---
git-date:
layout: default
title: tickers
h1title: tickers
pagetitle: DeFi Tokens List
metadescription: Decentralized Exchanges Trading Volume Tracker for Ethereum-based trading platforms. DEXs ranked by volume along with historic volume and daily market share
featured-image: /images/og-dexs.png
permalink: tickers
author: sawinyh
date: 2020-06-25
---
# tickers

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

 <table style="width:100%">
   <tr>
     <th>Product</th>
     <th>Ticker</th>
   </tr>

{% for all_project in all_projects %}

{% if all_project.ticker  %}
<tr>
 <td> {{ all_project.product-title }}</td>
 <td>{{ all_project.ticker }} <a href="https://1inch.exchange/#/r/0xEbDb626C95a25f4e304336b1adcAd0521a1Bdca1/ETH/{{ all_project.ticker }}" class="button-trade">Trade ${{ all_project.ticker }} on 1inch.exchange</a> </td>
</tr>

{% endif %}
 {% endfor %}

 </table>
