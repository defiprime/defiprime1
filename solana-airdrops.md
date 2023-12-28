---
git-date: 2019-05-20T22:02:39-07:00
layout: default
title: Solana Airdrops
metadescription: List of the best Solana DeFi Projects, that leverages decentralized networks to transform old financial products into trustless and transparent protocols.
permalink: solana-airdrops
h1title: Solana DeFi Ecosystem
pagetitle: Solana DeFi Ecosystem - List of the Best Solana Projects
featured-image: /images/og-solana.png
---

<section class="section-tickers">
  <p>intro</p>
  <div class="container-tickers">
    <table class="table-tickers">
      <thead>
        <tr>
          <th>Proejct</th>
          <th>Category</th>
          <th>Venture Funding</th>
          <th>URL</th>
          <th>Twitter</th>
          <th>What to do?</th>
        </tr>
      </thead>
      <tbody>

      {% assign solana_airdrops = site.airdrops | where_exp:"item", "item.ecosystem contains 'solana'" %}
      {% for solana_airdrops in solana_airdrops %}
        <tr class="ticker-row">
          <td > {{ solana_airdrops.title }} </td>
          <td > {{ solana_airdrops.category }}  </td>
          <td > {{solana_airdrops.raised}} from {{solana_airdrops.investors}} </td>
          <td > <a href="{{ solana_airdrops.proejct_url }}">{{ solana_airdrops.proejct_url }}</a> </td>
          <td > <a href="https://twitter.com/{{ solana_airdrops.twitter_handle }}">@{{ solana_airdrops.twitter_handle }}</a> </td>
          <td > <p>{{ solana_airdrops.todo }} </p> </td>
        </tr>
      {% endfor %}
      </tbody>
    </table>

  </div>
</section>
