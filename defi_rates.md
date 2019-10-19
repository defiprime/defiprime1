---
git-date:
layout: rates
pagetitle: Defi Yields Rates | DeFi Lending Interest Rates | DeFiprime.com
metadescription: 'Compare DeFi crypto lending products with traditional financial system offerings.
Lending stablecoins could be an alternative to high yield CDs, ETFs, and savings accounts, with relatively higher risk. Crypto lending rates comparison.'
h1title: DeFi Yields
permalink: defi-rates
featured-image: /images/og-rates.png
---

<section id="defi_rates_section">
    <p>Lending stablecoins could be an alternative to high yield CDs, ETFs, and savings accounts, with relatively higher risk.</p>
    <canvas id="rate_graphs"></canvas>
    <div id="description">
        {% assign descriptions = "Defi lending|Interest rate on balances|Vanguard CDs|Vanguard Real Estate ETF|SPDR Bloomberg Barclays High Yield Bond ETF" | split: "|" %}
        {% assign icons = "defi_lending|interest_rate_on_balances|vanguard_cds|vanguard_real_estate|sdpr_bloomberg" | split: "|" %}
        {% for description in descriptions %}
        <div>
            <img src="/images/{{icons[forloop.index0]}}.svg">
            <span>{{description}}</span>
        </div>
        {% endfor %}
    </div>
</section>

<section>
    <h2 class="defi-rates-heading">DeFi Lending Rates</h2>
    <span class="rates_annotation">What you can earn lending your stablecoins?</span>
    <div id="avg_interest_rates_cryptos">
        <article class="providersDAI">
            <img src="/images/dai.svg">
            <span class="providerCryptoName">DAI</span>
            <span class="percentCrypto" data-bind="text: $root.averageDAI"></span> 7-days avg.
            <div class="listAnnotation">Best Yields DAI Today, APR</div>
            <ul data-bind="foreach: providersDAI">
                <li>
                    <a class="cryptoListName" target="_blank" data-bind="text: provider, attr: { href: providerLink }"></a>
                    <span class="cryptoListPercent" data-bind="text: window.getPercent(providerDAI)"></span>
                </li>
            </ul>
        </article>
        <article class="providersUSDC">
            <img src="/images/usdc.svg">
            <span class="providerCryptoName">USDC</span>
            <span class="percentCrypto"  data-bind="text: $root.averageUSDC"></span> 7-days avg.
            <div class="listAnnotation">Best Yields USDC Today, APR</div>
            <ul data-bind="foreach: providersUSDC">
                <li>
                    <a class="cryptoListName" target="_blank" data-bind="text: provider, attr: { href: providerLink }"></a>
                    <span class="cryptoListPercent" data-bind="text: window.getPercent(providerUSDC)"></span>
                </li>
            </ul>
        </article>
    </div>
</section>

<section id="liquidityPools">
    <h2 class="defi-rates-heading">Uniswap Liquidity Pools</h2>
    <span class="rates_annotation"><a href="/uniswap-liquidity-pools">How liquidity pools works?</a></span>
    <div id="avg_interest_rates_cryptos">
        <article class="providersDAI">
            <img src="/images/dai_eth.svg">
            <span class="providerCryptoName">DAI/ETH</span>
            <ul data-bind="foreach: providersETHDai">
                <li>
                    <a class="cryptoListName" target="_blank" data-bind="text: provider, attr: { href: providerLink }"></a>
                    <span class="cryptoListPercent" data-bind="text: providerDAI+'%'"></span>
                </li>
            </ul>
        </article>
        <article class="providersUSDC">
            <img src="/images/usdc_eth.svg">
            <span class="providerCryptoName">USDC/ETH</span>
            <ul data-bind="foreach: providersETHUsdc">
                <li>
                    <a class="cryptoListName" target="_blank" data-bind="text: provider, attr: { href: providerLink }"></a>
                    <span class="cryptoListPercent" data-bind="text: providerUSDC+'%'"></span>
                </li>
            </ul>
        </article>
    </div>
</section>

<div class="container">
<hr>

<p>DeFi lending rates pulled from on-chain data</p>

</div>
<script>
    window.requestURL = "https://api-rates.defiprime.com";
</script>
<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/knockout/3.5.0/knockout-min.js"></script>
<script src="/assets/js/defi_rates.js"></script>
