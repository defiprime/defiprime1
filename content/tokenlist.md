---
git-date: 2020-07-05T13:31:59-07:00
layout: default
pagetitle: DeFi Tokens List
metadescription: We are participating in Token Lists initiative, providing and maintaining a list of reputable DeFi tokens tied to the products listed at Defiprime
featured-image: /images/blog/tokenlist-og.png
url: tokenlist
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
| concat: site.perps
| concat: site.marketplaces
| concat: site.payments
| concat: site.prediction_markets
| concat: site.stablecoins
 %}

<section class="sectoin-tickers">
  <p>We are participating in <a href="https://tokenlists.org/">Token Lists</a> initiative, providing and maintaining a <a href="https://tokenlists.org/token-list?url=https://defiprime.com/defiprime.tokenlist.json">list of reputable DeFi tokens tied to the products listed at Defiprime.</a> Visual representation of the Defiprime token list could be found below with a market stats.</p>
  <div class="container-tickers">
    <table class="table-tickers">
      <thead>
        <tr>
          <th class="ticker-product-title">Product</th>
          <th class="ticker-address-title">Address</th>
         <th class="ticker-address-copy"></th>
          <th class="ticker-price-title">Price, $</th>
          <th class="ticker-change-title">24h Change</th>
          <th class="ticker-vol-title">24h Volume, $</th>
          <th class="ticker-market-cap-title">Market Capitalization, $</th>
        </tr>
      </thead>
      <tbody>
      {% for all_project in all_projects %}
        {% if all_project.ticker  %}
        <tr class="ticker-row">
          <td class="ticker-product"><span class="name">{{ all_project.product-title }}</span> <span class="ticker">${{ all_project.ticker }}</span> <span class="coltitle">({{ all_project.coltitle }})</span></td>
          <td title="{{all_project.contract}}" class="ticker-address">
          <a href="https://etherscan.io/address/{{all_project.contract}}" target="_blank" rel="noopener noreferrer" class="link-address">{{all_project.contract}}</a>
          </td>
          <td class="btncopy"><span class="tooltip default-hover" title="Copied">
                      {% include icons/copy.svg %}
                    </span></td>
          <td class="ticker-price loading">
            <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
            <span class="sign">$</span><span class="ticker-price-value"></span>
          </td>
          <td class="ticker-change loading">
            <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
            <span class="ticker-change-plus">+</span><span class="ticker-change-value"></span><span class="precent">%</span>
            </td>
          <td class="ticker-vol loading">
            <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>  
            <span class="sign">$</span><span class="ticker-vol-value"></span>
          </td>
          <td class="ticker-market-cap loading">
            <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
            <span class="sign">$</span><span class="ticker-market-cap-value"></span>
          </td>
          <td class="ticker-link"><a href="https://dex.guru/token/eth/{{all_project.contract}}" target="_blank" class="button-trade">Analytics</a> </td>
        </tr>
        {% endif %}
      {% endfor %}
      </tbody>
    </table>
  </div>
  <p>Market data provided by <a href="https://www.coingecko.com/">Coingecko API</a>.</p>
</section>

<script defer src="/assets/js/defi_tickers.js"></script>
