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
    <p class="fs-20 fs-sm-16 lh-180 color-primary mb-40 mb-sm-25 mw-730 mx-auto">Lending stablecoins could be an alternative to high yield CDs, ETFs, and savings accounts, with relatively higher risk.</p>
    <p class="fs-15 fs-sm-14 lh-160 color-primary-light mb-25"></p>
</section>
<section class="text-center">
    <div class="wrapper-buttons">
        <button class="period-button" data-period="0">1d</button>
        <button class="period-button" data-period="1">7d</button>
        <button class="period-button active" data-period="2">1m</button>
        <button class="period-button" data-period="3">3m</button>
        <button class="period-button" data-period="4">1y</button>
        <button class="period-button" data-period="5">All</button>
    </div>
    <div class="wrapper-graphs">
        <canvas id="rate_graphs"></canvas>
    </div>
    <div class="flex jc-sb wrapper-mark">
        {% assign descriptions = "SAI Lending|USDC Lending|DAI Lending|Interest Rate On Balances|Vanguard CDs|Vanguard Real Estate ETF|SPDR Bloomberg Barclays High Yield Bond ETF" | split: "|" %}
        {% assign icons = "sai_lending|usdc_lending|dai_lending|interest_rate_on_balances|vanguard_cds|vanguard_real_estate|sdpr_bloomberg" | split: "|" %}
        {% for description in descriptions %}
        <div class="flex item-mark">
            <img class="lazyload" data-src="/images/{{icons[forloop.index0]}}.svg">
            <span class="fs-16 lh-180 fw-400">{{description}}</span>
        </div>
        {% endfor %}
    </div>
</section>

<section class="pt-225 pb-135 pt-xl-90 pb-xl-90 pt-md-45 pb-md-45">
    <div class="text-center">
        <h2 class="mb-25 mb-sm-0">DeFi Lending Rates</h2>
        <p class="fs-20 fs-sm-16 lh-180 color-primary mb-50 mb-sm-25">What can you earn lending your stablecoins?</p>
    </div>
    <div class="flex fd-md-c">
        <div class="flex d-column col-4 col-md-6 col-sm-12 lending-wrapper" data-token="dai">
            <div class="provider-crypto">
                <div class="icon-provider flex">
                    {% include icons/dai.html %}
                </div>
                <div class="data-provider">
                    <div class="name-provider">DAI</div>
                    <div class="value-provider"><span class="lending-mean">11</span><span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <a href="https://trade.dydx.exchange/balances" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="dydx">DyDx</span>
                        </a>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://compound.finance/" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="compound_v2">Compound</span>
                        </a>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://fulcrum.trade/" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="fulcrum">Fulcrum</span>
                        </a>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="flex d-column col-4 col-md-6 col-sm-12 lending-wrapper" data-token="usdc">
            <div class="provider-crypto">
                <div class="icon-provider flex">
                    {% include icons/usdc.html %}
                </div>
                <div class="data-provider">
                    <div class="name-provider">USDC</div>
                    <div class="value-provider"><span class="lending-mean">11</span><span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <ul class="list-crypto">
                    <li class="item-crypto">                        
                        <a href="https://trade.dydx.exchange/balances" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="dydx">DyDx</span>
                        </a>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://compound.finance/" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="compound_v2">Compound</span>
                        </a>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://fulcrum.trade/" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="fulcrum">Fulcrum</span>
                        </a>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="flex d-column col-4 col-md-6 col-sm-12 lending-wrapper" data-token="sai">
            <div class="provider-crypto">
                <div class="icon-provider flex">
                    {% include icons/sai.html %}
                </div>
                <div class="data-provider">
                    <div class="name-provider">SAI</div>
                    <div class="value-provider"><span class="lending-mean">11</span><span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <ul class="list-crypto">
                    <!-- <li class="item-crypto">
                        <span class="inline-flex list-crypto-name" data-market="dydx">DyDx</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li> -->
                    <li class="item-crypto">
                        <a href="https://compound.finance/" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="compound_v2">Compound</span>
                        </a>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://fulcrum.trade/" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="fulcrum">Fulcrum</span>
                        </a>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</section>

<!-- <section class="pt-120 pb-135">
    <div class="text-center">
        <h2 class="mb-25">DeFi Borrowing Rates</h2>
        <p class="fs-20 lh-180 color-primary mb-50">Avg. interest rates</p>
    </div>
    <div class="flex">
        <div class="flex d-column col-4">
            <div class="provider-crypto">
                <div class="icon-provider flex">
                    {% include icons/dai.html %}
                </div>
                <div class="data-provider">
                    <div class="name-provider">DAI</div>
                    <div class="value-provider"><span class="lending-mean">11</span><span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name" data-market="dydx">DyDx</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name"  data-market="compound_v2">Compound</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name"  data-market="fulcrum">Fulcrum</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="flex d-column col-4">
            <div class="provider-crypto">
                <div class="icon-provider flex">
                    {% include icons/usdc.html %}
                </div>
                <div class="data-provider">
                    <div class="name-provider">USDC</div>
                    <div class="value-provider"><span class="lending-mean">11</span><span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name" data-market="dydx">DyDx</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name"  data-market="compound_v2">Compound</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name"  data-market="fulcrum">Fulcrum</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="flex d-column col-4">
            <div class="provider-crypto">
                <div class="icon-provider flex">
                    {% include icons/sai.html %}
                </div>
                <div class="data-provider">
                    <div class="name-provider">SAI</div>
                    <div class="value-provider"><span class="lending-mean">11</span><span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name" data-market="dydx">DyDx</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name"  data-market="compound_v2">Compound</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name"  data-market="fulcrum">Fulcrum</span>
                        <span class="list-crypto-today"><span class="value">12</span><span class="fw-300">%</span></span>
                        <span class="list-crypto-month"><span class="value">12</span><span class="fw-300">%</span></span>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</section> -->

<section class="section-portfolio">
    <div class="flex ai-c f-lg-wrap">
        <div class="icon-portfolio flex jc-c ai-c">
            {% include icons/portfolio.html %}
        </div>
        <div class="info-portfolio">
            <p class="lh-140 color-white">Check complete protocols stats and APR performance history at DeFi <span class="color-orange">Portfolio</span></p>
        </div>
        <a class="button-portfolio flex jc-c ai-c" href="https://portfolio.defiprime.com/opportunities">Go to</a>
    </div>
</section>

<section class="section-liquidity pt-95 pb-45 pt-md-45">
    <div class="text-center">
        <h2 class="mb-75">Best liquidity pools Yields</h2>
    </div>
    <div class="flex jc-sb col-10 col-lg-12 mx-auto f-md-wrap">
        <div class="flex d-column col-5 col-md-6 col-sm-12 sai-eth">
            <div class="flex mb-35 mb-xl-0 ai-c">
                <div class="icon-provider-liquidity flex">
                    {% include icons/dai-eth.html %}
                </div>
                <div class="name-provider-liquidity lh-180">SAI/ETH</div>
            </div>
            <div class="wrap-list-liquidity">
                <ul class="list-liquidity">
                    <li class="item-liquidity lh-180 flex jc-sb">
                        <a class="list-liquidity-name" href="#" target="_blank">Uniswap</a>
                        <span class="list-liquidity-value"><span class="value">12</span>%</span>
                    </li>
                    <!-- <li class="item-liquidity lh-180 flex jc-sb">
                        <a class="list-liquidity-name" href="#" target="_blank">Bancor</a>
                        <span class="list-liquidity-value"><span class="value">6</span>%</span>
                    </li>
                    <li class="item-liquidity lh-180 flex jc-sb">
                        <a class="list-liquidity-name" href="#" target="_blank">Kyber</a>
                        <span class="list-liquidity-value"><span class="value">9</span>%</span>
                    </li> -->
                </ul>
            </div>
        </div>
        <div class="flex d-column col-5 col-md-6 col-sm-12 usdc-eth">
            <div class="flex mb-35 mb-xl-0 ai-c">
                <div class="icon-provider-liquidity flex">
                    {% include icons/usdc-eth.html %}
                </div>
                <div class="name-provider-liquidity lh-180">USDC/ETH</div>
            </div>
            <div class="wrap-list-liquidity">
                <ul class="list-liquidity">
                    <li class="item-liquidity lh-180 flex jc-sb">
                        <a class="list-liquidity-name" href="#" target="_blank">Uniswap</a>
                        <span class="list-liquidity-value"><span class="value">12</span>%</span>
                    </li>
                    <!-- <li class="item-liquidity lh-180 flex jc-sb">
                        <a class="list-liquidity-name" href="#" target="_blank">Bancor</a>
                        <span class="list-liquidity-value"><span class="value">6</span>%</span>
                    </li>
                    <li class="item-liquidity lh-180 flex jc-sb">
                        <a class="list-liquidity-name" href="#" target="_blank">Kyber</a>
                        <span class="list-liquidity-value"><span class="value">9</span>%</span>
                    </li> -->
                </ul>
            </div>
        </div>
    </div>
</section>

<div id="overlay">
<div class="spinner"></div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.13.0/moment.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
<script src="https://unpkg.com/array-flat-polyfill"></script>
<script src="/assets/js/defi_rates.js"></script>
