---
git-date: 2019-05-20T22:02:39-07:00
layout: default
title: "Crypto Airdrops: The Most Comprehensive List for 2024 Bull Market"
metadescription: 101 Guide to Crypto Airdrops - This is the most comprehensive list that covers upcoming significant airdrops. Our approach is simple and straightforward; we don't list any bogus airdrops that waste your time or ours. We only feature high-quality Ethereum and L2 ecosystem projects where tokens are relevant, and meaningful airdrops are highly probable.
permalink: crypto-airdrops
h1title: Crypto Airdrops
pagetitle: "Crypto Airdrops: The Most Comprehensive List"
featured-image: /images/blog/2024-airdrops.png
---

<h1>{{ page.h1title }}</h1>

<section class="section-tickers">
  <p>Our approach is simple and straightforward; we don't list any bogus airdrops that waste your time or ours. We only feature high-quality Ethereum and L2 ecosystem projects where tokens are relevant, and meaningful airdrops are highly probable.</p>
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

      {% assign solana_airdrops = site.airdrops | where_exp:"item", "item.ecosystem contains 'ethereum'" %}
      {% for solana_airdrops in solana_airdrops %}
        <tr class="ticker-row">
          <td > {{ solana_airdrops.title }} </td>
          <td > {{ solana_airdrops.category }}  </td>
          <td > {{solana_airdrops.raised}} from {{solana_airdrops.investors }} </td>
          <td > <a href="{% if solana_airdrops.reflink %} {{solana_airdrops.reflink}} {% else %}
{{solana_airdrops.project_url}} {% endif %}">{{solana_airdrops.project_url | remove: 'https://'}}</a> </td>
          <td > <a href="https://twitter.com/{{ solana_airdrops.twitter_handle }}">@{{ solana_airdrops.twitter_handle }}</a> </td>
          <td > {{ solana_airdrops.todo | markdownify }} Read more: <a href="/airdrop/{{ solana_airdrops.title | remove:  ' ' | capitalize }}">{{ solana_airdrops.h1title}}</a></td>
        </tr>
      {% endfor %}
      </tbody>
    </table>

  </div>
</section>
