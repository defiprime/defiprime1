---
git-date: 2020-12-18T17:10:02+02:00
layout: blog
title:  "Mirror Protocol"
url: mirror-protocol
h1title: "Mirror Protocol"
pagetitle: "Mirror Protocol - Synthetic Assets on Chain"
metadescription: "Do Kwon talks about Terra blockchain and a new Mirror Protocol that lives on Terra and Ethereum and enables access to global financial markets"
category: blog
featured-image: /images/blog/mirror-og.png
intro: "Do Kwon talks about Terra blockchain and a new Mirror Protocol that lives on Terra and Ethereum and enables access to global financial markets"
author: Defiprime
tags: ['Interview']
---
Do Kwon talks about Terra blockchain and a new Mirror Protocol that lives on Terra and Ethereum and enables access to global financial markets.

### Hello! What's your background, and what are you working on?

My name is Do Kwon, and I’m the co-founder and CEO of Terraform Labs (TFL), the group behind [Terra](https://terra.money/#3)—a stable, programmable currency for the internet.

Daniel Shin and I co-founded Terra back in January 2018 with the support of the Terra Alliance, a collective of 15 major e-commerce companies in Asia with more than 45 million combined users. Daniel’s prominent e-commerce experience in SE Asia and my previous founder’s role at mesh network-based P2P communication company, Anyfi, provided both of us with the perspective that traditional payments infrastructure needed to be replaced from the ground-up.

We soon began working on Terra to revamp the complicated and expensive traditional payments value chain, initially raising $32 million from household names in crypto like Binance, Arrington XRP, and Polychain Capital to build a cheaper, faster, distributed, and transparent technology ecosystem for payments, savings, and more.

Terra has gone on to achieve some amazing things since then, including our partner payments app, CHAI, surpassing 2 million users, and recently raising a [$70 million Series B](https://techcrunch.com/2020/12/09/seoul-based-payment-tech-startup-chai-gets-60-million-from-hanhwa-softbank-ventures-asia/). More recently, we’re proud to announce the rollout of Mirror Protocol, a synthetic asset platform for granting exposure to mAssets, which reflect traditional assets like equities, such as the US stock market.

The idea for Mirror is to grant intuitive access to global financial markets for disenfranchised users around that world that are precluded from specific international markets for various reasons. Eventually, we anticipate the community to propose and approve other traditional assets based on organic community demand, whether those assets are equities, commodities, crypto assets, ETFs, or others.

Mirror is currently available on Terra and Ethereum, with the latter via the Shuttle bridge.  

![](/images/blog/mirror-protocol/image1.jpg)

### What's Mirror Protocol backstory?


We initially started thinking about the framework of Mirror Protocol by examining the demand side for synthetics, primarily driven by individuals disenfranchised from some of the world’s largest financial markets. Given that there was, and remains, a strong trend for decentralization within the crypto space, we wanted to develop a system where any user could utilize his/her cryptocurrency assets to gain exposure to assets typically difficult for them to access at home.

We also wanted to take advantage of some of the newest technologies, such as AMMs, and incorporate them into the trading mechanism while retaining some of the legacy infrastructure characteristic of traditional markets. Synthetic assets may seem complex at first to many non-crypto users, but we think Mirror can help break down many of those barriers (e.g., prohibitive costs) as we move into 2021 and crypto awareness progresses.

As for Mirror’s technical ideation and specification, we’re lucky to have such a talented team. The majority of the Terra team comes from extensive backgrounds working in the crypto space, especially after building the Terra network from the ground up. In addition, our team consists of members who have significant experience in traditional finance and research. We combined these experiences to form a unique derivative product, which serves as one of Terra’s newest flagship applications.  


### What went into building the Mirror Protocol?

The project was originally conceived in early 2020 as an avenue for users to gain access and exposure to traditional financial assets and instruments via Terra’s blockchain.

In the spirit of the decentralization of finance, we wanted to ensure from the very beginning that there would be no initial allocation of native tokens to our team members or any other special party. This also included fetching the market prices that are used for minting new assets on the Mirror Protocol. We decided to [work with Band Protocol](https://www.google.com/url?q=https://medium.com/bandprotocol/mirror-protocol-integrates-band-protocol-oracles-to-secure-over-50m-in-synthetic-stocks-and-etfs-3a5b83ef77d5&sa=D&ust=1608000379406000&usg=AOvVaw0vtcd4Kz4J4KwSVX3t7Due) instead of providing our own price feeds in order to provide a more accurate and fair oracle. Before launch we asked CyberUnit to audit our smart contracts, and we have open bug bounties for any discoveries about potential weaknesses in the protocol.

In the few weeks before the official launch, we had QA testers run through potential weaknesses on the front-end, back-end, and the core smart contracts. We also ran through potential attack vectors from a trader’s point of view, such as economic exploits of oracles that are becoming so prevalent in the DeFi market. Band’s low-latency oracles update every 15 seconds, and are continually updated via multiple premium data providers. This helps to reduce the attack surface of oracles, by removing the dependency on single price feeds that can be manipulated. Band Protocol is currently overseeing [$66 million UST](https://terra.mirror.finance/) in locked assets on Mirror.

We originally had only planned Mirror for the Terra blockchain, but given the active DeFi community on Ethereum, we added further interfaces for Ethereum fans. This not only helped provide deeper liquidity to the Mirror Protocol itself, but also has helped the Mirror Protocol receive more attention in the larger DeFi community.


### What's your business model?

Mirror does not have a business model, and comes without a token premine or owner keys, meaning that financial upside for the project lay only with the community -- not TFL. We fulfill our mandate by making our stablecoins more useful if Mirror does well. This means working to facilitate the growth of UST, which mAssets trade against, and UST is required for minting mAssets (synths) on Mirror. By design, Mirror’s growth helps expand the scope, use, and adoption of UST, which is our goal in fulfilling our mandate.

Mirror’s design is predicated on the notion of appealing to open-source altruism, which can help community-governed projects grow more rapidly as benefits are shared mutually between the various participants rather than directly extracted by the company behind the product. The incentives for traders, liquidity providers, stakers, and minters are aligned in a way that is conducive to the adoption of UST. A larger profile of UST users subsequently extends positive effects into the broader Terra ecosystem.

We anticipate the MIR token’s fair launch design to encourage community collaboration on par with highly successful community-bootstrapped projects like Yearn Finance (YFI), where early participants are rewarded for their actions and contributions. Users have shown a preference for such open-source project designs. In addition, we will be working with ATQ Capital, the creator of the open-source Mirror Wallet, to propose a “[user farming framework](https://twitter.com/d0h0k1/status/1339750247912730624),” where developers can fork Mirror wallet, and are rewarded in MIR tokens by the community for attracting users and liquidity to Mirror Protocol.

We want to attract users of all backgrounds to Mirror, particularly financially disenfranchised users, with the goal of sharing in Mirror’s long-term value creation as the transformative power of decentralized synthetic assets is realized.  

![](/images/blog/mirror-protocol/image2.jpg)


### What’s your position on the regulatory landscape today?

The regulatory environment remains fragmented in different regions of the world, with some upcoming legislative proposals in countries like the US gaining mainstream attention. However, we firmly believe in the decentralization of financial infrastructure as a tool for empowering people, where there should be no legal risk transferred to entities like TFL, node operators of networks like Terra or Ethereum, or any individual user of DeFi products like Mirror.

With Mirror, we built everything through the prism of decentralization. We hold no tokens, retain no owner keys, the price feed is via a decentralized oracle, and the base of users minting mAssets are located around the world, with no restrictions on who can access or participate in the protocol.

Ultimately, the censorship-resistance of decentralized blockchain networks is a core ethos that both teams building products and the users of those products firmly believe in. That concept is fused into Mirror from its very conceptualization, and is something we think provides a net benefit for the broader DeFi ecosystem.


### What are your goals for the future?

Our immediate goals are to improve usability for users both on the Terra and Ethereum blockchains, so we have been very active with our community to reflect suggested features. This includes incorporating dashboard metrics for Mirror-based statistics that the community can view, as well as understanding some of the initial points of friction and how to attract more liquidity.

Also in the short term, we would like to improve and simplify the existing process for adding new assets on the protocol. Many of our current users have suggested recently IPO’d assets like ABNB and DASH, and we are looking to continuously engage with the community to start new asset whitelisting proposals. We would love for the community to take the reins in Mirror’s governance, proposing and voting on the listing of new synthetic assets based on organic demand from users.

Beyond Mirror, we’re currently working on [Anchor](https://anchorprotocol.com/), the low-volatility benchmark rate savings protocol on Terra that will launch in Q1 2021. Anchor addresses many of the problems currently facing the DeFi market, particularly variable-rate yields derived from speculatory [yield farming](/defi-yield-farming) and improving liquidation models to protect borrower collateral in periods of significant market volatility. Look for more details about the Anchor rollout to follow in the coming weeks.


### What are your future thoughts for the DeFi market?

One of the distinct ongoing trends is the transition of more sophisticated financial contracts and tooling to blockchains. These can range from porting popular TradFi instruments like structured risk products on-chain to building out novel synthetic protocols like Mirror. With more capital inflows, expect insurance and other risk-hedging derivatives to play a significant role as well in attracting larger institutional players, especially considering the current headache of exploits facing DeFi.

The goal? Bring more users to the ecosystem and democratize access to financial services. Whether the incoming users are institutions, retail investors, or disenfranchised people in financially repressed regions of the world, DeFi represents the inclusive financial system of the future.

Blockchain networks also reduce many of the inefficiencies of TradFi markets, including custody, settlement, escrow, etc., which makes them green pastures for financial innovation. Eventually, we may see clever financial instruments and engineering not possible with TradFi infrastructure (e.g., synthetic assets on Mirror) thriving across networks like Terra, Ethereum, Polkadot, and others.

More to that point, interchain DeFi is particularly intriguing.

Whereas interchain protocols were more of a concept only a few years ago, we’re beginning to see the rollout of useful interchain products, bridges (e.g., Mirror’s Shuttle to Ethereum), and other technology to connect different standalone blockchains in recent months. This is important for many reasons, including unlocking [superfluid collateral](https://tokeneconomy.co/superfluid-collateral-in-open-finance-8c3db15efac) and setting the stage for a thriving, diverse ecosystem of open-source communities working together for their mutual benefit.

Eventually, interchain progress may even help to break down maximalist barriers and improve collaboration on altruistic, open-source projects that are so representative of what crypto participants stand for.  


### Where can we go to learn more?

- **Terra Website** -- [https://terra.money/#1](https://terra.money/)
- **Mirror Website** -- [https://mirror.finance/](https://mirror.finance/)
- **Twitter** -- [https://twitter.com/terra_money](https://twitter.com/terra_money)
- **Medium** -- [https://medium.com/terra-money](https://medium.com/terra-money)
- **Discord** -- [https://discord.gg/bYfyhUT](https://discord.gg/bYfyhUT)
- **GitHub** -- [https://github.com/terra-project](https://github.com/terra-project) (Terra), [https://github.com/mirror-protocol](https://github.com/mirror-protocol) (Mirror)
