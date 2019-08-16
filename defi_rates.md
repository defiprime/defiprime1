---
layout: rates
title: DeFi lending rates | DeFiprime.com
metadescription: Defi Rates
h1title: Defi Rates
permalink: defi-rates
featured-image: /images/og-rates.png
---

<section id="defi_rates_section">
    <p>Decentralized Finance (DeFi) is the movement that leverages decentralized networks to transform old financial products into trustless</p>
    <span>Compare DeFi products with traditional financial system offerings</span>
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
    <h1>DeFi Lending Rates</h1>
    <span class="rates_annotation">What you can earn?</span>
    <div id="avg_interest_rates_cryptos">
        <article class="providersDAI">
            <img src="/images/dai.svg">
            <span class="providerCryptoName">DAI</span>
            <span class="percentCrypto" data-bind="text: $root.averageDAI"></span> avg. today
            <div class="listAnnotation">Best Yields DAI</div>
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
            <span class="percentCrypto"  data-bind="text: $root.averageUSDC"></span> avg. today
            <div class="listAnnotation">Best Yields USDC</div>
            <ul data-bind="foreach: providersUSDC">
                <li>
                    <a class="cryptoListName" target="_blank" data-bind="text: provider, attr: { href: providerLink }"></a>
                    <span class="cryptoListPercent" data-bind="text: window.getPercent(providerUSDC)"></span>
                </li>
            </ul>
        </article>
    </div>
</section>

DeFi lending rates data provided by: [loanscan.io](https://loanscan.io/)  
<script>
    window.requestURL = "https://api-rates.defiprime.com";
</script>
<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/knockout/3.5.0/knockout-min.js"></script>
<script src="/assets/js/defi_rates.js"></script>
