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
<!-- <section class="text-center">
    <div class="wrapper-buttons">
        <button class="period-button" data-period="0">1d</button>
        <button class="period-button" data-period="1">7d</button>
        <button class="period-button active" data-period="2">1M</button>
        <button class="period-button" data-period="3">3M</button>
        <button class="period-button" data-period="4">YTD</button>
        <button class="period-button" data-period="5">All-Time</button>
    </div>
    <div class="wrapper-graphs">
        <div id="tv-chart-container"></div>
    </div>
    <div class="flex jc-c wrapper-mark">
        {% assign descriptions = "DAI Lending, market avg.|USDC Lending, market avg." | split: "|" %}
        {% assign icons = "dai_lending|usdc_lending" | split: "|" %}
        {% for description in descriptions %}
        <div class="flex item-mark">
            <img class="lazyload" data-src="/images/{{icons[forloop.index0]}}.svg">
            <span>{{description}}</span>
        </div>
        {% endfor %}
    </div>
</section> -->

<section class="pt-120 pb-20 pt-xl-90 pb-xl-0 pt-md-45">
    <div class="text-center">
        <h2 class="mb-25 mb-sm-0">DeFi Lending Rates</h2>
        <p class="fs-20 fs-sm-16 lh-180 color-primary mb-50 mb-sm-25">What can you earn lending your stablecoins?</p>
    </div>
    <div class="flex fd-md-c jc-sa">
        <div class="flex d-column col-4 col-md-6 col-sm-12 lending-wrapper" data-token="dai">
            <div class="provider-crypto">
                <div class="icon-provider flex">
                    {% include icons/dai.html %}
                </div>
                <div class="data-provider">
                    <div class="name-provider">DAI</div>
                    <div class="value-provider"><span class="lending-mean" title="Market average today">0.00</span><span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <a href="https://app.aave.com/?referral=28" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="aave">Aave</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://compound.finance/" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="compound_v2">Compound</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://trade.dydx.exchange/balances" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="dydx">dYdX</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://fulcrum.trade/" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="fulcrum">Fulcrum</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                    <!-- <li class="item-crypto">
                        <a href="https://oasis.app/save" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="dsr">MakerDAO DSR</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li> -->
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
                    <div class="value-provider"><span class="lending-mean" title="Market average today">0.00</span><span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <a href="https://app.aave.com/?referral=28" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="aave">Aave</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://compound.finance/" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="compound_v2">Compound</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                    <li class="item-crypto">                        
                        <a href="https://trade.dydx.exchange/balances" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="dydx">dYdX</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://fulcrum.trade/" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="fulcrum">Fulcrum</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</section>

<section class="pt-120 pt-md-45 pb-45">
    <div class="text-center">
        <h2 class="mb-25">DeFi Borrowing Rates</h2>
        <p class="fs-20 lh-180 color-primary mb-50">Compare Decentralized Finance (DeFi) cryptocurrency borrowing platform interest rates</p>
    </div>
    <div class="flex fd-md-c jc-sa">
        <div class="flex d-column col-4 col-md-6 col-sm-12 borrowing-wrapper" data-token="dai">
            <div class="provider-crypto">
                <div class="icon-provider flex">
                    {% include icons/dai.html %}
                </div>
                <div class="data-provider">
                    <div class="name-provider">DAI</div>
                    <div class="value-provider"><span class="borrowing-mean">0.00</span><span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <a href="https://app.aave.com/?referral=28" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="aave">Aave</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://app.aave.com/?referral=28" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value"  data-market="aave_fixed">Aave fixed*</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://compound.finance/" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="compound_v2">Compound</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://trade.dydx.exchange/balances" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="dydx">dYdX</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                    <!-- <li class="item-crypto">
                        <a href="https://fulcrum.trade/" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="fulcrum">Fulcrum**</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li> -->
                    <!-- <li class="item-crypto">
                        <a href="https://torque.loans/" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="torque">Torque*</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li> -->
                </ul>
            </div>
        </div>
        <div class="flex d-column col-4 col-md-6 col-sm-12 borrowing-wrapper" data-token="usdc">
            <div class="provider-crypto">
                <div class="icon-provider flex">
                    {% include icons/usdc.html %}
                </div>
                <div class="data-provider">
                    <div class="name-provider">USDC</div>
                    <div class="value-provider"><span class="borrowing-mean">0.00</span><span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <a href="https://app.aave.com/?referral=28" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="aave">Aave</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://app.aave.com/?referral=28" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value"  data-market="aave_fixed">Aave fixed*</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://compound.finance/" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="compound_v2">Compound</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://trade.dydx.exchange/balances" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="dydx">dYdX</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                    <!-- <li class="item-crypto">
                        <a href="https://fulcrum.trade/" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="fulcrum">Fulcrum**</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li>
                    <li class="item-crypto">
                        <a href="https://torque.loans/" class="inline-flex list-crypto-name list-liquidity-name">
                            <span class="value" data-market="torque">Torque*</span>
                        </a>
                        <span class="list-crypto-today"></span>
                        <span class="list-crypto-month"></span>
                    </li> -->
                </ul>
            </div>
        </div>
    </div>
    <div class="description">*Loans with a fixed interest</div>
    <div class="description">**Loans as a part of margin trading platform</div>

</section>




<div id="overlay">
<div class="spinner"></div>
</div>

<script src="https://unpkg.com/array-flat-polyfill"></script>
<script src="https://unpkg.com/lightweight-charts@1.0.0/dist/lightweight-charts.standalone.production.js"></script>
<!-- <script src="//cdn.jsdelivr.net/npm/graphql.js@0.6.6/graphql.min.js"></script> -->
<script src="https://cdn.jsdelivr.net/npm/web3@latest/dist/web3.min.js"></script>
<script src="/assets/js/defi_rates.js"></script>
