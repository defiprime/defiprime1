---
git-date:
layout: rates
pagetitle: DeFi Yields Rates | DeFi Lending Interest Rates | DeFiprime.com
metadescription: 'Compare DeFi crypto lending products with traditional financial system offerings.
Lending stablecoins could be an alternative to high yield CDs, ETFs, and savings accounts, with relatively higher risk.
Crypto lending rates comparison.'
h1title: DeFi Rates
permalink: defi-rates
featured-image: /images/og-rates.png
---

<section class="text-center">
    <p class="fs-20 lh-180 color-primary mb-40 mw-730 mx-auto">Decentralized Finance (DeFi) is the movement that leverages decentralized networks to transform old financial products into trustless</p>
    <p class="fs-15 lh-160 color-primary-light mb-25">Lending stablecoins could be an alternative to high yield CDs, ETFs, and savings accounts, with relatively higher risk.</p>
</section>

<section class="text-center">
    <div class="inline-flex wrapper-buttons">
        <button class="period-button active" data-period="7d">7d</button>
        <button class="period-button" data-period="1m">1m</button>
        <button class="period-button" data-period="3m">3m</button>
        <button class="period-button" data-period="1y">1y</button>
        <button class="period-button" data-period="all">All</button>
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
            <span class="fs-16 lh-180 fw-400">{{description}}</span>
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
        <div class="flex d-column col-4">
            <div class="provider-crypto">
                <div class="icon-provider flex">
                    {% include icons/dai.html %}
                </div>
                <div class="data-provider">
                    <div class="name-provider">DAI</div>
                    <div class="value-provider">11<span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">DyDx</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">12<span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">Compound</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">12<span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">Fulcrum</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">12<span class="fw-300">%</span></span>
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
                    <div class="value-provider">11<span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">DyDx</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">12<span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">Compound</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">12<span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">Fulcrum</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">12<span class="fw-300">%</span></span>
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
                    <div class="value-provider">11<span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">DyDx</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">12<span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">Compound</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">12<span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">Fulcrum</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">12<span class="fw-300">%</span></span>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</section>

<section class="pt-120 pb-135">
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
                    <div class="value-provider">11<span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">DyDx</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">12<span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">Compound</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">12<span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">Fulcrum</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">12<span class="fw-300">%</span></span>
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
                    <div class="value-provider">11<span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">DyDx</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">8<span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">Compound</span>
                        <span class="list-crypto-today">9<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">85<span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">Fulcrum</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">61<span class="fw-300">%</span></span>
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
                    <div class="data-provider">SAI</div>
                    <div class="value-provider">11<span class="fw-300">%</span></div>
                </div>
            </div>
            <div class="data-crypto">
                <ul class="list-crypto">
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">DyDx</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">12<span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">Compound</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">12<span class="fw-300">%</span></span>
                    </li>
                    <li class="item-crypto">
                        <span class="inline-flex list-crypto-name">Fulcrum</span>
                        <span class="list-crypto-today">12<span class="fw-300">%</span></span>
                        <span class="list-crypto-month">12<span class="fw-300">%</span></span>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</section>

<section class="section-portfolio">
    <div class="flex ai-c">
        <div class="mr-55 flex jc-c ai-c">
            {% include icons/portfolio.html %}
        </div>
        <div class="mr-30">
            <p class="fs-26 lh-140 color-white mb-0">Check complete protocols stats and APR performance history at DeFi <span class="color-orange">Portfolio</span></p>
        </div>
        <a class="button-portfolio flex jc-c ai-c" href="https://portfolio.defiprime.com/opportunities">Go to</a>
    </div>
</section>

<section class="section-liquidity pt-95 pb-50">
    <div class="text-center">
        <h2 class="mb-75">Best liquidity pools Yields</h2>
    </div>
    <div class="flex jc-sb col-10 mx-auto">
        <div class="flex d-column col-5">
            <div class="flex mb-35">
                <div class="icon-provider-liquidity flex">
                    {% include icons/dai-eth.html %}
                </div>
                <div class="name-provider-liquidity lh-180">DAI/ETH</div>
            </div>
            <div class="wrap-list-liquidity">
                <ul class="list-liquidity">
                    <li class="item-liquidity lh-180 flex jc-sb">
                        <a class="list-liquidity-name" href="#" target="_blank">Uniswap</a>
                        <span class="list-liquidity-value"><span class="value">12</span>%</span>
                    </li>
                    <li class="item-liquidity lh-180 flex jc-sb">
                        <a class="list-liquidity-name" href="#" target="_blank">Bancor</a>
                        <span class="list-liquidity-value"><span class="value">6</span>%</span>
                    </li>
                    <li class="item-liquidity lh-180 flex jc-sb">
                        <a class="list-liquidity-name" href="#" target="_blank">Kyber</a>
                        <span class="list-liquidity-value"><span class="value">9</span>%</span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="flex d-column col-5">
            <div class="flex mb-35">
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
                    <li class="item-liquidity lh-180 flex jc-sb">
                        <a class="list-liquidity-name" href="#" target="_blank">Bancor</a>
                        <span class="list-liquidity-value"><span class="value">6</span>%</span>
                    </li>
                    <li class="item-liquidity lh-180 flex jc-sb">
                        <a class="list-liquidity-name" href="#" target="_blank">Kyber</a>
                        <span class="list-liquidity-value"><span class="value">9</span>%</span>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</section>

<script>
    window.requestURL = "https://api-rates.defiprime.com";
</script>
<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/knockout/3.5.0/knockout-min.js"></script>
<script src="/assets/js/defi_rates.js"></script>