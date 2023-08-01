---
git-date: 2019-09-13T07:06:04+00:00
layout: [blog]
title:  0x Protocol
permalink: 0x-protocol
h1title: '0x: Decentralized Exchange Protocol'
pagetitle: '0x: Decentralized Exchange Protocol'
metadescription: 'Matt Taylor from the 0x Core Team told us how they built a decentralized exchange protocol, and what comes next for DeFi dApps.'
category: blog
featured-image: /images/blog/0x-og.png
quote: /images/blog/0x-quote.png
intro: 'Matt Taylor from the 0x Core Team told us how they built a decentralized exchange protocol, and what comes next for DeFi dApps.'
author: Defiprime
tags: ['Interview', 'DEXs']

---
Matt Taylor from the 0x Core Team told us how they built a decentralized exchange protocol, and what comes next for DeFi dApps.

### Hello! What's your background, and what are you working on?

Hey DeFi Prime, thanks for reaching out! My name is [Matt Taylor](https://twitter.com/mattytay), and I'm currently the Marketing Lead for [0x](https://0x.org/), a decentralized exchange protocol that many crypto projects use to facilitate the p2p exchange of Ethereum-based assets. I joined the 0x Core Team about a year ago, and I'm responsible for our external communications, marketing strategy, product marketing, etc. Before 0x, I worked for [Abra](https://www.abra.com/) and [Square](https://squareup.com/us/en). I've been pretty obsessed with cryptocurrency for a while and went down the rabbit hole when writing my undergraduate thesis on the economic incentives in Bitcoin's proof-of-work consensus mechanism.

A bit about 0x just to frame the conversation: 0x is [a pipeline of open-source smart contracts](https://www.youtube.com/playlist?list=PLN51Tjs40v5PIm4avEo1m2Uz08qj0YWPa) that serve as foundational exchange infrastructure and the networked liquidity layer for several crypto verticals including DeFi and blockchain gaming. We are building 0x protocol to be the standard for trading crypto tokens and connecting complementary protocols to bring both existing and completely new financial markets to people around the world.

DeFi projects ranging from lending services to atomic trading bots can tap into [0x's networked liquidity pool](https://0x.org/asset-swapper) to give users the ability to trade a large number of tokens at competitive prices. 0x's liquidity and DEX infrastructure can be accessed by anyone, making it easy to add peer-to-peer exchange functionality in really any application. We are very excited about what we’ve seen so far from the DeFi businesses integrated with 0x, especially from those leveraging [contract-fillable liquidity (CFL)](https://blog.0xproject.com/contract-fillable-liquidity-made-simple-8b9cf1b2f2f2). The rate of experimentation and innovation in financial markets has already increased dramatically now that capital can now flow freely through peer-to-peer networks, at a much lower cost.

To give your readers a sense of our progress so far, over a billion dollars in trades have flowed through the 0x protocol, 100+ projects have utilized 0x to enable p2p exchange functionality in their apps, and 0x’s networked liquidity pool often has the lowest slippage on the most popular trading pairs in the DeFi space, including ETH/DAI, ETH/USDC, DAI/USDC, and more.

{% youtube "https://youtu.be/c04eIt3FQ5I" %}

### What's 0x's backstory?

Our co-founders Will Warren and Amir Bandealli started working on 0x in 2016. They initially attempted to build a tokenized derivatives exchange, but quickly realized they needed to create a protocol that enabled these tokenized positions to be traded peer-to-peer. From there, they found that many of the projects in the space needed a standard set of smart contracts that coordinated and executed the exchange of tokens for their products to function properly. They also foresaw that all forms of value were going to be tokenized and traded on public blockchains. I think we've seen this vision playing out with the explosion of new tokens being minted on Ethereum; NFTs for games, tokenized derivatives, prediction market shares, security tokens, tokenized digital art, etc. From there, they started building 0x with the[mission](https://blog.0xproject.com/the-0x-mission-and-values-181a58706f9f) of creating a tokenized world where all value can flow freely.

Will and Amir then hired a few more members to the 0x Core Team (the organization that develops and evangelizes 0x) to help build the protocol and the necessary developer tools that would enable crypto projects to integrate with the technology. In 2017, they conducted a ZRX token sale that emphasized distribution, with an individual purchase cap per user. I'll explain the mechanics and purpose of the token in sections below, but in short, ZRX is the protocol's native governance token.

Right after the launch of the network in mid-2017, several crypto projects started integrating with the protocol. I think this was a big point of validation for the team. Now, the 0x Core Team employs around 40 people working in San Francisco and abroad. We have a really talented team that is working on all areas of 0x development and plan to expand over the coming months to meet integration demands and continue building out the protocol. If you're interested in joining us, take a look at the open positions on [our job board](https://0x.org/about/jobs).

### What went into building 0x?

When Will and Amir started building 0x, they evaluated many different models of decentralized exchange, including automated market makers (as implemented by Uniswap and Bancor), on-chain orderbooks, and state channel-based approaches. They found that the current orderbook model, which combines off-chain relay of orders and on-chain settlement, would offer the highest flexibility by combining the best parts of some of these different models. The chosen model was highly efficient and also allowed many different modes of exchange to be utilized within the protocol, including open orderbooks, matching systems, and contract-fillable liquidity (CFL). I'll discuss these forms of exchange in detail in the sections below.

In the early days, people often mistook 0x for a single decentralized exchange. This is a common misconception - 0x is a *protocol* that powers decentralized exchange in various forms. It was primarily created for developers to integrate exchange functionality into their protocols and applications. End-users may never know that they are interacting with the 0x protocol, similar to how most people who use the internet do not know that they are interacting with TCP. As a result, the 0x Core Team spends a significant amount of resources and dev time improving the protocol, building tooling, and writing documentation that makes building on 0x easy for different developer segments.

Will and Amir also knew that the space was still nascent and would drastically change over time, so upgradability and governance were core areas of research even before the protocol launched. At the same time, they knew that the utility of the protocol would increase with adoption - it was important that all of its stakeholders use the canonical set of smart contracts in order to capitalize on network effects. As such, it was very important that a decentralized set of stakeholders could upgrade the protocol in a way that would prevent the ecosystem from becoming fractured. From the early days, it was understood that ZRX would play a critical role in the governance of the protocol.

To learn more about how 0x works under the hood, check out our smart contract pipeline video series:

{% youtube "https://youtu.be/WSxphhWcLxk" %}
[YouTube playlist](https://www.youtube.com/playlist?list=PLN51Tjs40v5PIm4avEo1m2Uz08qj0YWPa)

### What's your business model?

0x does not have a business model in the traditional sense. We view 0x as public infrastructure that anyone in the world can plug into. In order for 0x to be sustainable long-term and owned by its community of stakeholders, ZRX is needed to coordinate upgrades and eventually route protocol fees to liquidity providers via a token holder-controlled treasury.

[The idea](https://blog.0xproject.com/0x-roadmap-2019-part-4-proposal-for-stake-based-liquidity-incentive-52c16558df29) is that protocol fees from each 0x trade will be passed onto to market makers in the form of liquidity rewards for providing trade volume and staking ZRX over specific periods of times (called epochs). Market makers who do not have sufficient ZRX can form staking pools. Any ZRX token holder will be able to delegate their tokens to market makers to receive an allocation of these liquidity rewards. As more volume and liquidity flows into the 0x Network, the fees and rewards will grow proportionally. This, in turn, will incentivize ecosystem stakeholders to hold ZRX for staking and voting on changes to the protocol that affect their usage of the network. We are hoping to implement these token mechanisms through a community vote at the beginning of Q4 2019.

In the future, we may launch revenue-generating business lines to grow the 0x ecosystem further. We don't have any concrete plans at this time, but there are a variety of services we could provide that would accelerate adoption of the protocol, including market making and staking ZRX. We want to keep our options open on this front.


### Who is your target market?

Generally, 0x's target market is anyone that wants to exchange digital assets directly, without any entity in the middle. This is an extensive set of potential users, so we find it helpful to segment the market. 0x is unique in that there are a variety of protocol stakeholders we are attracting. We bucket them into several groups: makers, takers, relayers, and ZRX token holders. There is obviously a lot of overlap between these participants, but I can briefly discuss how we are working to grow each segment.

For makers, the token sellers that originate orders, we are working to increase the number of standing orders in the network primarily through our [Market Maker Program](https://0x.org/market-maker). These makers are algo-traders that create bots to execute specific trading strategies. We are providing monetary incentives and education on how to trade via decentralized exchanges. On the taker side, we have focused in on DeFi projects that need to fill those open orders by leveraging contract-fillable liquidity (CFL), which describes the ability for smart contracts to programmatically swap tokens via DEX networks to fulfill a specific function. Our dev team released a new tool called Asset Swapper that will make it simple to leverage 0x's CFL. Our go-to-market team is spending a lot of time pitching DeFi projects on this type of integration and letting the broader cryptosphere know that 0x currently has the deepest liquidity compared to other DEX networks. I'll discuss this more in the section below, but as more makers and takers trade with each other, liquidity in the network grows. Liquidity begets more liquidity, and the flywheel spins faster and faster.

![](/images/blog/0x-wooow.png)

In addition to these more automated approaches to making and taking orders, there are retail traders that use 0x relayers like [Radar Relay](https://radarrelay.com/), [Paradex](https://paradex.io/), [Tokenlon](https://tokenlon.im/), and [Deversify](https://www.ethfinex.com/) (formerly Ethfinex). However, we are seeing a lot more demand from the smart contract-based trading segment vs. retail. I think automated trading will continue to dominate DEX usage as it takes advantage of the unique benefits provided by decentralized crypto exchange.

Another key participant in the 0x Network are relayers, which are simply user-facing applications that surface 0x orders. There are two primary approaches relayers take, matching, and open orderbook. Matching relayers only accept orders where the taker is an address controlled by the relayer. When the relayer receives two orders on opposite sides of the market with overlapping prices, they automatically match both orders together. Traders can benefit from this approach as they cannot accidentally or intentionally attempt to fill the same order since only the relayer is allowed to fill each order. The relayer also knows when orders are matched before anyone else and can update the orderbook as soon as the transaction is submitted, allowing for a more real-time trading experience. This strategy also moves all gas costs to the relayer, which can provide a better UX for traders.

Unlike matchers, open orderbook relayers accept and broadcast orders that allow anyone to make or take orders. Traders can share orders across relayers, which enables external smart contracts to fill these orders via networked liquidity. However, as trading throughput increases, it becomes increasingly likely that multiple traders will attempt to fill the same order (either intentionally or accidentally). We are very excited about a new relayer model that combines the best characteristics of these two approaches by utilizing [Coordinators](https://blog.0xproject.com/0x-roadmap-2019-part-5-introducing-coordinators-1406365ecbd). More on that in the section below.

We've worked hard to make launching a relayer extremely easy. [0x Launch Kit](https://0x.org/launch-kit) is a simple, extensible relayer codebase that can be forked or used as reference material to create an exchange in minutes. It also comes with a pair of off-the-shelf react UIs that developers can use to launch their marketplace in just 1 line of code! There are dozens of projects that have utilized Launch Kit, and we continue to add features to the product to make sure all exchange needs are met.

And finally, there are ZRX token holders. These are stakeholders in the protocol that have governance rights to vote on [ZEIPs (0x Improvement Proposals)](https://github.com/0xProject/ZEIPs). We've conducted a few successful votes so far, where token holders have approved ZEIPs to add support for [ERC-1155](https://blog.0xproject.com/vote-with-zrx-to-add-support-for-erc-1155-and-the-staticcallassetproxy-49a855807bcd) tokens and[mult-asset bundle trading](https://blog.0xproject.com/zeip-23-vote-post-mortem-311c9323e228). As mentioned above, we introduced a new token economics proposal that will further empower ZRX holders by offering stake-based liquidity rewards. We are excited about these new mechanisms and are working on a few different initiatives that will help token holders put their ZRX to work!

### What's your position on the regulatory landscape today?

The current landscape consists of legacy financial regulations that don't easily map onto what we (and the rest of DeFi) are trying to build. However, we are working on several fronts to make sure 0x complies with existing laws and create legal resources for the ecosystem of businesses built on the protocol. First, we have an in-house legal team consisting of Jason Somensatto and Rui Zhang that help the 0x Core Team navigate the regulatory landscape.

Second, we are active members in the [Blockchain Association](https://theblockchainassociation.org/), which is a group of leading crypto organizations that collaborate with and educate regulatory bodies in the U.S. on the innovation happening in DeFi. Again, our mission is to create a world in which all value is tokenized and exchanged freely, which includes regulated stocks and derivative products. So, we work with the Blockchain Association to figure out the best path forward in compliantly bringing these markets to the 0x Network.

And third, we provide essential legal resources to projects as part of our [Ecosystem Acceleration Program](https://0x.org/eap). We recognize the difficulty for independent teams trying to build businesses on 0x in light of the current regulatory landscape, so we give legal support where we can. In general, 0x is open-source so anyone can build on our technology, and we cannot control if someone makes a product that does not comply with existing regulations. Having said that, we are working to ensure that 0x and projects in our ecosystem will continue the operate legally within their jurisdictions.
We look forward to educating regulators around the world on decentralized exchange and the innovative services developing in the DeFi space.

Check out our Decrypting the Law video series to get our take on current regulatory issues:

{% youtube "https://youtu.be/dID-wn2dSwk" %}
[YouTube playlist](https://www.youtube.com/playlist?list=PLN51Tjs40v5PQ5p4TbkQcF7iVtVGR5PGy)

### What are your goals for the future?

The 0x Core Team is working on a variety of [roadmap objectives for the rest of 2019](https://blog.0xproject.com/tagged/0xroadmap). We feel all these initiatives will significantly benefit the DeFi ecosystem and help push it forward towards mainstream adoption. First, as mentioned above, we are working on our ZRX token economics proposal that will be voted on later this year with the 0x v3.0 upgrade. We hope this provides clarity around the purpose of ZRX and how it drives governance and community-ownership in the protocol in the long run.

Second, we are working on improving networked liquidity by building out 0x Mesh, which is a p2p network for propagating orders off-chain throughout the ecosystem. You can think of it as BitTorrent for crypto exchange. Mesh will further decentralize the 0x stack and make it much easier to tap into 0x's networked liquidity by simply spinning up a node. We released the Mesh beta last month on mainnet and plan to continue iterating on it until the full production launch near the end of Q3 2019.

Third, we are improving the trader user experience through [Coordinators](https://blog.0xproject.com/0x-roadmap-2019-part-5-introducing-coordinators-1406365ecbd), which are opt-in contracts that enforce rules over trade execution. The first Coordinator demo implementation is live on[](https://bamboorelay.com/trade/WBTC-DAI)[Bamboo Relay](https://bamboorelay.com/), where market makers can cancel orders for free, and traders can find the best prices for DAI + wBTC. Future iterations on Coordinators could provide protection against front-running and trade collisions.

Overall, we feel that Coordinators combine the best characteristics of Order Matching and Open Orderbook relayer models: market makers can perform free, instant order cancellations and users/devs can leverage contract-fillable liquidity to power decentralized applications.

![](/images/blog/0x-hellos.png)

Fourth, we are researching zero-knowledge proofs to scale decentralized exchange. In collaboration with [StarkWare](https://starkware.co/), we released a demo of [StarkDEX](https://blog.0xproject.com/starkdex-bringing-starks-to-ethereum-6a03fffc0eb7), which is PoC infrastructure that utilizes STARKs to remove the glass ceiling on non-custodial trading and allows crypto exchanges to offer their customers trading at scale, without counter-party risk. Today, the system at max capacity can batch 8,000 transactions per block, which is over 550 transactions per second and 200x cheaper in terms of gas costs. Ethereum at max capacity can only verify roughly three transactions per second. You can view the [demo here](https://www.starkdex.io/) to see the system in action. We have a team dedicated to further researching zero-knowledge proofs and plan to announce some exciting updates on this front in the coming months.

And fifth, and most importantly, we are working to provide additional DeFi liquidity to the 0x network. We are trying to bring on more external liquidity providers through our Market Maker Program. We have seen a significant increase in liquidity over the past few months, and we plan to continue pushing forward on this front so DeFi projects can allow their users to exchange tokens at the best prices. This is what the market demands, so we've made it our primary objective for the year.

### What are your future thoughts for the DeFi market?

DeFi has started to take off in the past six months or so, especially in the lending/borrowing market. We’ve seen several businesses, including 0x integrators like [dYdX](https://dydx.exchange/) and [Radar Relay](https://radarrelay.com/), gain significant traction. One aspect of DeFi we are excited about is what we are calling [contract-fillable liquidity](https://blog.0xproject.com/dydx-and-contract-fillable-liquidity-cb965fc6f7e9), as mentioned above.

DeFi projects consume liquidity from DEX networks for specific functions related to token exchange in products ranging from decentralized lending services to leverage trading platforms. Even atomic arbitrage bots need consumable liquidity to trade effectively across exchange venues. There are a variety of projects using this automated token swap functionality including dYdX for increasing/decreasing margin positions, Set for rebalancing token index funds, and DeFi Saver for avoiding Maker CDP liquidations. I think contract-fillable liquidity is the bedrock of the Open Finance space and is one of the most critical functions enabled by smart contracts on permissionless blockchains. It opens the door for capital to frictionlessly flow between crypto protocols and services to allow for the creation of markets that couldn't exist in the traditional financial system.

![](/images/blog/0x-dydxcontract.png)

We have been working hard to increase the amount of liquidity in our network so that DeFi projects can swap tokens at the best prices, and have been building tools like [Asset Swapper](https://0x.org/asset-swapper) which make it easy to leverage contract-fillable liquidity through 0x. We are just starting to see 0x's flywheel spin and look forward to supporting the massive amount of volume that will flow through the protocol over the coming months and years.

### Where can we go to learn more?

We try to distribute info about 0x where ever the crypto community hangs out. However, we use [Twitter](https://twitter.com/0xProject) and [our blog](https://blog.0xproject.com/) as our primary communication channels. If you’re interested in trading or developing on 0x, check out the following resources:

* [0x Website](https://0x.org/)
* [0x Asset Swapper](https://0x.org/asset-swapper) for DeFi projects needing to source liquidity
* [0x Launch Kit](https://0x.org/launch-kit) for developers looking to launch a DEX
* [0x Explore](https://0x.org/explore) to trade in the 0x ecosystem
* [Official Discord Chat](https://discord.gg/d3FTX3M?source=post_page---------------------------)
* [0x Documentation](https://0x.org/docs)
* [0x Github](https://github.com/0xProject?source=post_page---------------------------)
* [0x Monthly Newsletter](https://0xprotocol.substack.com/)
* [0x YouTube channel](https://www.youtube.com/channel/UCFrSpPi9WUW9wYTa0Q1sdnA)
* [0x Subreddit](https://www.reddit.com/r/0xProject/?source=post_page---------------------------)
* [0x Research Forum](https://forum.0x.org/)
