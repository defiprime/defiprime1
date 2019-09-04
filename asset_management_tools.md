---
layout: default
pagetitle: 'Asset management tools | DeFiprime.com'
metadescription: 'Asset management tools.'
permalink: asset-management-tools
---

<h1>Asset Management Tools</h1>
<div class="custodian_description">
Custodian it is a specialized financial institution responsible for safeguarding a firm’s or individual’s financial assets and is not engaged in “traditional” commercial or consumer/retail banking.Custodian services in DeFi it is wallets, apps, and dashboards for managing your cryptocurrencies and assets.
</div>
<section id='assets_cards'>
    {% for asset_tool in site["assets-managament-tools"] %}
        <article class="asset_tool_card">
            <img src="{{ asset_tool['image'] }}">
            <h4><a href="{{ asset_tool['product-url']}} ">{{ asset_tool["product-title"] }}</a></h4>
            <div class="asset-tool-tags">
                {% assign market_tags = asset_tool["ecosystem"] | split: ", " %}
                {% for market_tag in market_tags %}
                    {% case market_tag %}
                        {% when "ethereum" %}
                            <img title="Built on Ethereum or related to Ethereum ecosystem" src="images/eth.svg" />
                        {% when "bitcoin" %}
                            <img title="Using Bitcoin ecosystem" src="images/btc.svg" />
                        {% when "tron" %}
                            <img title="Built on Tron or related to Tron ecosystem" src="images/tron.svg" />
                        {% when "stellar" %}
                            <img title="Built on Stellar or related to Stellar ecosystem" src="images/stellar.svg" />
                        {% when "eos" %}
                            <img title="Built on EOS or related to EOS ecosystem" src="images/eos.svg" />
                    {% endcase %}
                {% endfor %}
                <div class="tags_separator"></div>
                {% assign platform_tags = asset_tool["platform"] | split: ", " %}
                {% for platform_tag in platform_tags %}
                    {% case platform_tag %}
                        {% when "android" %}
                            <img src="/images/android.svg" title="Mobile wallet for Android">
                        {% when "web" %}
                            <img src="/images/web.svg" title="Browser based wallet">
                        {% when "ios" %}
                            <img src="/images/ios.svg" title="Mobile wallet for iOS">
                    {% endcase %}
                {% endfor %}
            </div>
            <p>{{ asset_tool["product-description"] }}</p>
            <div title="Would you recommend this product?" class="comments">
                <a href="/product/{{ asset_tool.product-title | slugify: 'latin'}}">
                    <img src="/images/no_comment.svg">
                    <span>0</span>
                </a>
            </div>
        </article>
    {% endfor %}
</section>
<section class="read_next">
    <h3>Next</h3>
    <div class='reading_next_links'>
        {% assign collections = site.collections | where_exp:"post", "post.section_url != page.url" %}
        {% for collection in collections %}
            <a href="{{ collection.section_url }}">
                {{ collection.label | capitalize | replace: "-", " " | replace: "_", " " }}
                <span class="articles_count">{{ collection.docs | size }}</span>
            </a>
        {% endfor %}
    </div>
</section>