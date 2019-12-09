---
git-date:
layout: rates
pagetitle: DeFi Yields Rates | DeFi Lending Interest Rates | DeFiprime.com
metadescription: 'Compare DeFi crypto lending products with traditional financial system offerings.
Lending stablecoins could be an alternative to high yield CDs, ETFs, and savings accounts, with relatively higher risk. Crypto lending rates comparison.'
h1title: DeFi Rates
permalink: defi-rates
featured-image: /images/og-rates.png
---

<section class="text-center">
    <p class="fs-20 lh-180 color-primary mb-40 mw-730 mx-auto">Decentralized Finance (DeFi) is the movement that leverages decentralized networks to transform old financial products into trustless</p>
    <p class="fs-15 lh-160 color-primary-light mb-25">Lending stablecoins could be an alternative to high yield CDs, ETFs, and savings accounts, with relatively higher risk.</p>
</section>
<section>
    <div class="wrapper-buttons">
        <button class="period-button active" data-period="0">7d</button>
        <button class="period-button" data-period="1">1m</button>
        <button class="period-button" data-period="2">3m</button>
        <button class="period-button" data-period="3">1y</button>
        <button class="period-button" data-period="4">All</button>
    </div>
    <div class="wrapper-graphs">
        <canvas id="rate_graphs"></canvas>
    </div>
    <div class="wrapper-mark">
        {% assign descriptions = "DeFi lending|Liquidity pools|Staking|Vanguard Brokerage CDs|Interest rate on balances" | split: "|" %}
        {% assign icons = "defi_lending|sdpr_bloomberg|vanguard_real_estate|vanguard_cds|interest_rate_on_balances" | split: "|" %}
        {% for description in descriptions %}
        <div class="item-mark">
            <img class="lazyload" data-src="/images/{{icons[forloop.index0]}}.svg">
            <span>{{description}}</span>
        </div>
        {% endfor %}
    </div>
</section>

<section class="pt-225">
    <div class="text-center">
        <h2 class="mb-25">DeFi Lending Rates</h2>
        <p class="fs-20 lh-180 color-primary mb-50">Avg. interest rates</p>
    </div>
    <div class="flex">
        <div class="flex d-column col-4 lending-wrapper" data-token="dai">
            <div class="provider-crypto">
                <div class="icon-provider">
                    {% include icons/dai.html %}
                </div>
                <div class="name-provider">
                    <div class="color-primary">DAI</div>
                    <div class="color-secondary"><span class="lending-mean">11</span><span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <div class="mark-crypto">
                    <div class="mark-crypto-name">APR</div>
                    <div class="mark-crypto-today">Today</div>
                    <div class="mark-crypto-month">30-days</div>
                </div>
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <span class="list-crypto-name" data-market="dydx">DyDx</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="list-crypto-name"  data-market="compound_v2">Compound</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="list-crypto-name"  data-market="fulcrum">Fulcrum</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="flex d-column col-4 lending-wrapper" data-token="usdc">
            <div class="provider-crypto">
                <div class="icon-provider">
                    {% include icons/usdc.html %}
                </div>
                <div class="name-provider">
                    <div class="color-primary">USDC</div>
                    <div class="color-secondary"><span class="lending-mean">11</span><span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <div class="mark-crypto">
                    <div class="mark-crypto-name">APR</div>
                    <div class="mark-crypto-today">Today</div>
                    <div class="mark-crypto-month">30-days</div>
                </div>
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <span class="list-crypto-name" data-market="dydx">DyDx</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="list-crypto-name"  data-market="compound_v2">Compound</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="list-crypto-name"  data-market="fulcrum">Fulcrum</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="flex d-column col-4 lending-wrapper" data-token="sai">
            <div class="provider-crypto">
                <div class="icon-provider">
                    {% include icons/sai.html %}
                </div>
                <div class="name-provider">
                    <div class="color-primary">SAI</div>
                    <div class="color-secondary"><span class="lending-mean">11</span><span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <div class="mark-crypto">
                    <div class="mark-crypto-name">APR</div>
                    <div class="mark-crypto-today">Today</div>
                    <div class="mark-crypto-month">30-days</div>
                </div>
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <span class="list-crypto-name" data-market="dydx">DyDx</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="list-crypto-name"  data-market="compound_v2">Compound</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="list-crypto-name"  data-market="fulcrum">Fulcrum</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</section>

<section class="pt-120">
    <div class="text-center">
        <h2 class="mb-25">DeFi Borrowing Rates</h2>
        <p class="fs-20 lh-180 color-primary mb-50">Avg. interest rates</p>
    </div>
    <div class="flex">
        <div class="flex d-column col-4">
            <div class="provider-crypto">
                <div class="icon-provider">
                    {% include icons/dai.html %}
                </div>
                <div class="name-provider">
                    <div class="color-primary">DAI</div>
                    <div class="color-secondary"><span class="lending-mean">11</span><span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <div class="mark-crypto">
                    <div class="mark-crypto-name">APR</div>
                    <div class="mark-crypto-today">Today</div>
                    <div class="mark-crypto-month">30-days</div>
                </div>
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <span class="list-crypto-name" data-market="dydx">DyDx</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="list-crypto-name"  data-market="compound_v2">Compound</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="list-crypto-name"  data-market="fulcrum">Fulcrum</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="flex d-column col-4">
            <div class="provider-crypto">
                <div class="icon-provider">
                    {% include icons/usdc.html %}
                </div>
                <div class="name-provider">
                    <div class="color-primary">USDC</div>
                    <div class="color-secondary"><span class="lending-mean">11</span><span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <div class="mark-crypto">
                    <div class="mark-crypto-name">APR</div>
                    <div class="mark-crypto-today">Today</div>
                    <div class="mark-crypto-month">30-days</div>
                </div>
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <span class="list-crypto-name" data-market="dydx">DyDx</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="list-crypto-name"  data-market="compound_v2">Compound</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="list-crypto-name"  data-market="fulcrum">Fulcrum</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="flex d-column col-4">
            <div class="provider-crypto">
                <div class="icon-provider">
                    {% include icons/sai.html %}
                </div>
                <div class="name-provider">
                    <div class="color-primary">SAI</div>
                    <div class="color-secondary"><span class="lending-mean">11</span><span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <div class="mark-crypto">
                    <div class="mark-crypto-name">APR</div>
                    <div class="mark-crypto-today">Today</div>
                    <div class="mark-crypto-month">30-days</div>
                </div>
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <span class="list-crypto-name" data-market="dydx">DyDx</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="list-crypto-name"  data-market="compound_v2">Compound</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="list-crypto-name"  data-market="fulcrum">Fulcrum</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</section>


<div class="container">
    <hr>

    <p>DeFi lending rates pulled from on-chain data. Check complete protocols stats and APR performance history at <a
            href="https://portfolio.defiprime.com/opportunities">DeFi Portfolio</a>.</p>

</div>
<section id="liquidityPools">
    <h2 class="defi-rates-heading">Uniswap Liquidity Pools</h2>
    <span class="rates_annotation"><a href="/uniswap-liquidity-pools">How liquidity pools works?</a></span>
    <div id="avg_interest_rates_cryptos">
        <article class="providersDAI">
            <img class="lazyload" data-src="/images/dai_eth.svg">
            <span class="providerCryptoName">SAI/ETH</span>
            <ul data-bind="foreach: providersETHDai">
                <li>
                    <a class="cryptoListName" target="_blank"
                        data-bind="text: provider, attr: { href: providerLink }"></a>
                    <span class="cryptoListPercent" data-bind="text: providerDAI+'%'"></span>
                </li>
            </ul>
        </article>
        <article class="providersUSDC">
            <img class="lazyload" data-src="/images/usdc_eth.svg">
            <span class="providerCryptoName">USDC/ETH</span>
            <ul data-bind="foreach: providersETHUsdc">
                <li>
                    <a class="cryptoListName" target="_blank"
                        data-bind="text: provider, attr: { href: providerLink }"></a>
                    <span class="cryptoListPercent" data-bind="text: providerUSDC+'%'"></span>
                </li>
            </ul>
        </article>
    </div>
</section>


<script>
    window.requestURL = "https://api-rates.defiprime.com";
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.13.0/moment.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
<script src="https://unpkg.com/array-flat-polyfill"></script>
<script src="/assets/js/defi_rates.js"></script>