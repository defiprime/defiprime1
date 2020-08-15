---
git-date:
layout: default
pagetitle: DeFi Tokens List
metadescription: Decentralized Exchanges Trading Volume Tracker for Ethereum-based trading platforms. DEXs ranked by volume along with historic volume and daily market share
featured-image: /images/og-dexs.png
permalink: tickers
---
# DeFi Tokens List

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
<section class="sectoin-tickers">
  <p>Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. </p>
  <div class="container-tickers">
    <table class="table-tickers">
      <thead>
        <tr>
          <th class="ticker-product-title">Product</th>
          <th class="ticker-address-title">Address</th>
          <th class="ticker-price-title">Price </th>
          <th class="ticker-change-title">24hr_change </th>
          <th class="ticker-vol-title">24hr_vol </th>
          <th class="ticker-market-cap-title">Market Cap</th>
        </tr>
      </thead>
      <tbody>
      {% for all_project in all_projects %}
        {% if all_project.ticker  %}
        <tr class="ticker-row">
          <td class="ticker-product"><span class="name">{{ all_project.product-title }}</span> <span class="ticker">${{ all_project.ticker }}</span> <span class="coltitle">({{ all_project.coltitle }})</span></td>
          <td class="ticker-address">{{ all_project.contract }}</td>
          <td class="ticker-price"><span class="sign">$</span><span class="ticker-price-value">100</span></td>
          <td class="ticker-change"> 100 </td>
          <td class="ticker-vol"> 100 </td>
          <td class="ticker-market-cap"> 100 </td>
          <td class="ticker-link"><a href="https://1inch.exchange/#/r/0xEbDb626C95a25f4e304336b1adcAd0521a1Bdca1/ETH/{{ all_project.ticker }}" class="button-trade">Trade</a> </td>
        </tr>
        {% endif %}
      {% endfor %}
      </tbody>
    </table>
  </div>
  <p>Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. </p>
</section>



<script src="/assets/js/defi_tickers.js"></script>
