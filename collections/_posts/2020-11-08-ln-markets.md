---
git-date: 2020-11-08T12:20:26-08:00
layout: [blog]
title:  "LN Markets"
permalink: lnmarkets
h1title: "LN Markets"
pagetitle: "LN Markets - Trading Platform Built on Lightning Network"
metadescription: "Romain talks about decentralization, derivatives trading and building product on Lightning Network"
category: blog
featured-image: /images/blog/ln-og.png
intro: "Romain talks about decentralization, derivatives trading and building product on Lightning Network"
author: Defiprime
tags: ['Interview', 'Derivatives']
---
Romain talks about decentralization, derivatives trading and building product on Lightning Network.

### Hello! What's your background, and what are you working on?

My name is Romain Rouphael, co-founder of [LN Markets](https://lnmarkets.com/).

After several years of working in financial markets, I found out about Bitcoin while I was living in Hong Kong in 2013. At that time, a Bitcoin ATM opened in my street, I purchased some, did my first Bitcoin transactions, and quickly realized how elegant and efficient Bitcoin was compared to my bank account. That’s how I got into Bitcoin and started to really want to understand it, along with my friend Côme, who was working as an FX trader there.

We came back to France at the same time during summer 2015, and since we shared this passion, we decided to go full time on it, and we set up a lab to explore Bitcoin and blockchain protocols. We were quickly joined by Victor, our CTO. Our quest to get a holistic view of how Bitcoin could reshape finance led us to the idea behind [LN Markets](https://lnmarkets.com/).

[LN Markets](https://lnmarkets.com/) is a new type of Bitcoin derivatives trading platform, one that can only be accessed via the Lightning Network.

Trading is done directly from any Lightning wallet and enables super fast access to derivatives markets. Open a position by making a Lightning transaction, close the position and receive the money directly in your wallet, it’s as easy as that!

The first product available is a Contract For Difference (CFD) derivative product tracking the BTC-USD price. Margin positions are funded using Lightning Network transactions.

Because the product is still in alpha, the maximum margin per position is limited to 0.01 BTC. Despite the small-trade size, [LN Markets](https://lnmarkets.com/) users have executed more than 35,000 trades, aggregating over $15 million of volume since last Spring.


![](/images/blog/ln-markets-1.jpg)


### What's LN Markets backstory?

We had the idea of [LN Markets](https://lnmarkets.com/) because of our own frustrations trading on crypto derivatives exchanges!

Indeed, the most convenient way for retail traders to enter a Bitcoin derivatives position is through crypto exchanges, which currently play two roles at the same time: trading venue and clearing house. To make sure that buyers and sellers honor their contractual obligations, these exchanges require traders to deposit and maintain an account funded with Bitcoin as collateral: this is called the margin.

By doing so, traders give the ownership of their asset to a third party: they take a counterparty risk. To mitigate that risk, traders could transfer their bitcoins out of the exchange whenever they are not in an active position and do the opposite when they want to enter into a position.

But this is painful, as it means navigating through various interfaces and wallets. This is a slow process, since Bitcoins transfers usually take around one hour to be confirmed. This is expensive, too, since each Bitcoin transaction incurs transaction costs in addition to exchange fees. On top of all this, these cumbersome processes mean traders may miss market opportunities.

This is why we built [LN Markets](https://lnmarkets.com/): with the Lightning Network, we can design a whole new trading experience where traders are much more in control of their funds.

[LN Markets](https://lnmarkets.com/) leverages the Lightning Network as a settlement layer to provide a completely new experience where trading and transfer of bitcoin funds are done at the very same time, in one click.

Bitcoin funds that are not used in a position never stay at risk on an exchange: traders minimize their risk. With [LN Markets](https://lnmarkets.com/), traders can instantly access Bitcoin markets, post margin and claim P&L instantly in a trust-minimized environment. Counterparty risk is reduced to a minimum.


### What went into building the LN Markets?

We started building [LN Markets](https://lnmarkets.com/) in September 2019, and we went live on Bitcoin Testnet in December 2019. Back then, you could only log in with your Lightning node using Joule, which reduced the scope of potential users. We learned a lot from this Testnet version and we made sure that before going Mainnet any user could log in and trade instantly in a very simple manner, straight from any mobile wallet.

We launched on mainnet on March 11th 2020, just before the day crypto markets broke down last. That “Black Thursday,” the BTC price fell down steeply from $8,000 to $5,000 and even lower. The Bitcoin blockchain quickly became saturated, some trading venues even halted their operations during this selloff and hence it became very complex for market participants to manage their risks. A few even had to shut down their activity because it became impossible for them to post margin in this high volatility context!

But in fact, these tough times for Bitcoin markets proved to be beneficial for LN Markets, because it highlighted our _raison d’être_!

When markets are crashing 20% in 10 minutes, and the blockchain is saturated and nobody can move their assets, being able to move your funds instantly and pay your margin calls in due time becomes a very high competitive advantage! That’s what we have built with [LN Markets](https://lnmarkets.com/).

We are very thankful to our users who have been extremely supportive since the very beginning, helping us find glitches, fixing bugs, and pushing us to develop new features!

Last July, we secured a pre-seed funding round with [Bitfinex](https://www.bitfinex.com/), [Arcane Crypto](https://www.arcane.no/) and [Fulgur Ventures](https://fulgur.ventures/), three investors who are strongly committed to the growth of the Lightning Network ecosystem and who will certainly help us accelerate our development and offer new trading experiences to our users.


### What's your business model?

Our business model is simple. We quote a bid-offer on our platform and charge 0.1% fee per trade. There is no funding rate, no maintenance margin, no complex fee structures.

[LN Markets](https://lnmarkets.com/) is a radical change in the way users interact with the market: using the Lightning Network as an authentication and settlement layer for margin payments allows heavy simplification of the trading process.

We place the personal wallet at the center, everything is done from there. We recently opened our API and access to trading is no longer limited to a closed interface and can be ported to any kind of platform: wallet, social media platform, chat room, etc. And we are indeed currently working with other Lightning wallets for trading account management integrations. Bitcoin is a financial asset and a very powerful infrastructure and we intend to develop toward both aspects of it.


### What’s your position on the regulatory landscape today?

Since we launched, we have decided to limit the maximum margin per position to 0.01 BTC.

Meanwhile, we are working on a regulatory framework that could enable us to raise these limits while maintaining the same trading experience for our users.


### What are your goals for the future?

In the next few months, we will continue the integration of [LN Markets](https://lnmarkets.com/) to various interfaces such as other Lightning wallets. We will also add more products for trading such as options.

We also closely follow the developments of the RGB protocol that will enable the instant trading of a stablecoin like Tether. We will certainly first use Tether on Lightning to list USD-denominated products.

Overall, we think that Bitcoin and the Lightning Network can deeply disrupt the logics in place in the legacy financial system. Programmable assets are very powerful tools that will reshape the standard for a better transparency and risk control.

Our main goal is to offer new types of trading experiences to our users based on the Bitcoin infrastructure. Our success will only be measured by the number of people to whom we manage to deliver these powerful services.


### What are your future thoughts for the DeFi market?

In our view, for a trading platform simplicity and speed are much stronger value propositions than decentralization for the sake of decentralization. LN Markets is trust-minimized, in the sense that users' funds are not at risk when traders are not in a position, yet the system is not fully decentralized.

Whether you use a centralized or decentralized service, there is trust involved, you either trust an entity or a smart contract. And we believe that for financial products, a centralised entity does a better job, at least for the moment.


### Where can we go to learn more?

- LN Markets: [https://lnmarkets.com/](https://lnmarkets.com/) \
- LN Markets API: [https://lnmarkets.github.io/docs/](https://lnmarkets.github.io/docs/) \
- LN Markets FAQ: [https://lnmarkets.com/faq](https://lnmarkets.com/faq)
- LN Markets Newsletter covers everything at the intersection of the Lightning Network and Finance: [https://lnmarkets.substack.com/](https://lnmarkets.substack.com/)

You can reach out directly to us on:
*   Twitter: [https://twitter.com/LNMarkets](https://twitter.com/LNMarkets)
*   Telegram: [https://www.t.me/lnmarkets](https://www.t.me/lnmarkets)
