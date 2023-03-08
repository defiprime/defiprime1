---
git-date:
layout: [blog]
title:  Liquality
permalink: liquality
h1title: "Liquality - cross-chain atomic swaps"
pagetitle: "Liquality - cross-chain atomic swaps"
metadescription: "Simon told us Liquality backstory, and shared his thoughts on complexities of a cross-chain swap for end users"
category: blog
featured-image: /images/blog/liquality-quote.png
quote: /images/blog/liquality-quote.png
intro: "Simon told us Liquality backstory, and shared his thoughts on complexities of a cross-chain swap for end users"
author: Defiprime
tags: ['Interview', 'DEXs', 'Cross-chain']
---
Simon told us Liquality backstory and shared his thoughts on the complexities of a cross-chain swap for end users.   

### Hello! What’s your background, and what are you working on?

My name is Simon Lapscher, and I am the Co-Founder of [Liquality](https://liquality.io/).  I have an educational background in engineering, and my professional background is in management and technology consulting focused on payments systems and financial infrastructure. I was born and raised in Venezuela. As the economic situation in Venezuela continued to quickly and consistently worsen and hyperinflation set in, I came across Bitcoin as a potential alternative for cross-border remittances that avoided government censorship. I attended the Bitcoin conference in Miami in 2013, fell into the crypto rabbit hole, and never looked back.

I and a few other colleagues started and ran Deloitte’s Blockchain Practice for close to two years. I then moved to ConsenSys, where I helped various governments think about their blockchain strategy, while meeting Alex and Thessy (Liquality co-founders) to talk about the problems we were seeing in the way the world exchanged value. That’s where Liquality started.

Liquality is a truly peer to peer exchange network. We enable two people that might not know or trust each other to exchange value in a simple, easy, free, non-custodial, and completely trustless way. Users can exchange value across multiple chains, without any counterparty risk using software that is entirely open source. What Bitcoin did for money - remove intermediaries out of the transfer of money - Liquality is doing for exchange. Through Liquality, we are able to bring Bitcoin’s 65% market dominance into DeFi’s explosive innovation, and we can bring DeFi’s capabilities to Bitcoin.

Liquality is currently comprised of 4 different parts:

1. The [standards](https://liquality.io/blog/hash-time-locked-contracts-htlcs-explained/) we’ve developed and improved for cross-chain atomic swaps ([ERC1630](https://github.com/ethereum/EIPs/pull/1630) and [BIP199]( https://github.com/bitcoin/bips/blob/master/bip-0199.mediawiki))
2. The [Chain Abstraction Layer](https://github.com/liquality/chainabstractionlayer), an open-source library that simplifies cross-chain development for financial applications, which projects like [Atomic Loans](https://atomic.loans/) are using to expand the cross-chain ecosystem.
3. The swap interface ([https://liquality.io/swap/](https://liquality.io/swap/)) that enables users to swap trustlessly across chains (e.g. BTC&lt;>ETH, BTC&lt;>DAI, BTC&lt;>USDC)
4. [Market Maker bots](https://liquality.io/atomic-swap-bot.html) that provide liquidity into the network and are available to trade with users 24/7

![](/images/blog/liquality_alpha_mainnet.png)

### What’s Liquality backstory?

We initially came together for a research project focused on use cases for 'global money’, on/off ramps and crypto adoption.

The more we discussed, we got obsessed about solving the problem of trust, security and accessibility in value exchange and to extend the principles of Bitcoin, to exchanging value across chains, unlock cross-chain liquidity and build unintermediation into the core protocol to make it easy to build accessible products that will drive equality and inclusion.

At that point we started Liquality, the name originating in ‘Liquidity' and ‘Equality’.  Following a strict review process we received funding from ConsenSys to grow a team and build Liquality.

We aligned on core principles because the 3 co-founders, as well as the diverse team we hired later, has been especially affected by system failure, access restrictions and other frictions.

Alex, our South African co-founder, exited the financial system a few years back and has been living entirely off of bitcoin since. In order to spend his bitcoin, he relied on a few top-up prepaid cards that were later shut down due to their dependence on a centralized provider. He was looking for a way to exchange his bitcoin for anything else that respected the essence of bitcoin (open, borderless, censorship resistant, based on it being disintermediated) and couldn’t find any.

Thessy had experienced the global financial crisis building collateral optimization and trading products in JPMorgan's Investment Bank, surprised at unnecessary complexity and the trend towards more risk based on ‘too-big-to fail’. She became active in Occupy’s Alternative Banking group with the goal to help financial inclusion. Also, as half-Iranian she knows how hyper- inflation and sanctions hit the most vulnerable of society.

I was thinking about how to enable a censorship resistant way for users to be able to send remittances, seeing how the Venezuelan government was shutting down most centralized remittance providers.

We quickly realized that for any interoperability and open access financial infrastructure you can’t build liquidity in isolation. We needed to build a way for anyone to be able to exchange any type of value with anyone else, without relying on a third party, with multiple interfaces speaking the same language. We needed to leave ourselves out of the trade so that liquidity could flow freely in a network without a centralized bottleneck.

Through extensive user and technical research, we understood that, in order to eventually compete with centralized exchanges, we needed to build something that was entirely disintermediated and blockchain agnostic from the start to prevent isolating liquidity in chains. This led us to start researching[ cross-chain atomic swaps](https://liquality.io/blog/atomic-swaps-explained/).


### What went into building the Liquality?

Liquality first started as a research project. For the first six months, we focused on talking to potential users to understand their pain points, and technical research to validate that peer-to-peer cross-chain swaps were possible and executable in a simple way via the browser. From there, we first worked on and released our [Chain Abstraction Layer](https://liquality.io/chain-abstraction-layer.html); we wanted to build standard communication tools for connected liquidity, as well as help other developers who were seeing the same frustrations of building across multiple blockchains we were seeing.   

It took a lot of work to release our first product; cross-chain swaps are hard, and we are building financial tools, so we had to make sure there was no possibility for loss of funds. Security is our first priority, and we require security audits for all our smart contracts. We released our first mainnet swap interface in June of 2019, which was purely for settlement - users needed to bring their counterparty to swap. Though we knew this MVP wasn’t enough to get significant adoption, it was a great starting point and allowed us to get input from users on what they needed.  

Around this time, we were starting to see decentralized exchanges (DEXs) gaining popularity and Uniswap getting great volumes. It was clear that the shift to DEXs had started, and that a majority (~70%) of the volume in DEXs was between ether and stablecoins, due to the rise of DeFi applications. We also knew that DEXs are built with a dependency on a single chain (i.e., Ethereum) and wouldn’t be able to offer their users access to Bitcoin and other chains, therefore validating our early architectural choice. Some of our other decisions have also been proven right since, such as having [single-use user-owned smart contracts](https://liquality.io/blog/the-0x-zrx-vulnerability-and-why-decentralized-exchanges-dexs-are-insecure/) as opposed to a central smart contract owned by Liquality. In essence, this helps preserve users’ privacy and makes our swaps more secure by not having a third party with the ability to stop trades (as we’ve seen with some DEXs). This approach not only preserves privacy and security, but also is more cost-efficient. When exchanging peer to peer, only the peers should be a part of the swap. There is no need for third parties.

Through our learnings from the MVP and the direction the market was moving, we decided to focus on providing liquidity to users. We recently launched the ability for users to create market maker bots, a way for users to offer their liquidity into the network and profit from idle assets across chains. This upgrade hides a lot of the complexities of a cross-chain swap for end-users, as they can swap with a bot 24/7 without the need to find a counterparty.


### What’s your business model?

Because we want to assure that liquidity flows freely through our network and not act as the regulatory or operational bottleneck, we do not monetize swaps through the introduction of fees or a token. Instead, we act as participants in our network and monetize in two main ways:

1. We are a liquidity provider and run a market maker bot ourselves. This way, we monetize through the spread in every transaction our bot is a part of.  
2. We build value-added services and products on top of the base layer that makes it easier to be a part of the network and provide more functionality to our users. For example, we are starting to provide infrastructure as a service for companies that want to run market makers, with more robust functionality.

Our competitors are mainly DEXs, other atomic swap providers, and instant exchanges (e.g., ShapeShift). Our main differentiators are we see them are:

*   **No Middlemen**: disintermediation minimizes the risk and cost associated with swapping cryptocurrencies, including unnecessary tokens, deposits, or withdrawals
*   **Cross-Chain**: there is no need for false representations of Bitcoin, like wBTC, as participants can swap cryptocurrencies across blockchains
*   **No Counterparty Risk**: atomic swaps are programmatically guaranteed to either happen securely or refund both parties
*   **Key Ownership**: the interface’s bring-your-own-wallet (BYOW) approach empowers users to retain control and custody over their funds
*   **Browser-based and Serverless**: removes barriers to entry such as downloading a desktop application or running nodes to participate
*   **Open Source**: all code is open source and promotes freedom

At the same time, we believe most of our competitors will become collaborators. As the trend towards interoperability through battle-tested standards continues to grow, everyone should be able to benefit from each others’ efforts.

### What’s your position on the regulatory landscape today?

There is no definite answer for how to view the regulatory landscape today, as each country will take their own perspective on the evolution of the crypto ecosystem. In some countries, the existing regulations might not be entirely applicable to the tools that are being developed. Regulations often require a central intermediary to govern and monitor a specific financial transaction. Still, if a user is interacting entirely peer to peer without intermediation through open source tools, that intermediary may not exist. This creates an opportunity to have conversations with regulators who are looking at the cutting-edge and develop new ways of making sure consumer protections and regulatory checks still take place.

For example, atomic swaps remove counterparty risk from the equation by making sure the exchange either happens for both parties or none, there is no scenario where one party can run away with the other’s fund. This creates a much safer foundation for exchange infrastructure and is, therefore, helping regulators keep users safe.  


### What are your goals for the future?

We want to create a more open and equitable future, where anyone can access the global digital economy freely, efficiently, and securely. As the world leaps into the digital realm, thanks in part to the current social distancing from coronavirus, commerce will need to evolve to meet the challenge. Our existing financial infrastructure is not built for this shift. Exchange of value will need to serve strangers who don’t trust each other, as there are no borders in the digital world. This will require a completely disintermediated trustless infrastructure that is not limited or dependent on any single system. We believe Liquality is perfectly suited to become the exchange layer of this new world.

Right now, developers are building new products in this disintermediated financial ecosystem, users are swapping cross-chain, and makers are creating liquidity provider bots. Our plan is to continue to make it easier and more valuable for each of these users to be a part of Liquality. In short to medium term, here are some of the things we are working or will be working on:

*   Add more pairs, more wallets, and more liquidity to the network
*   Improving the onboarding experience in a variety of ways
*   Researching how to overcome technical hurdles, such as implementing lightning network swaps to avoid long block times
*   Integrating with wallets and dapps, to provide their users with cross-chain exchange capabilities
*   On/off-ramp fiat to crypto integrations
*   Automating a lot of the current manual overhead with providing liquidity through a bot
*   Liquidity pools for retail users to earn trading fees from fractional pool ownership

### What are your future thoughts for the DeFi market?

The greatest benefit and curse of DeFi is permissionless innovation. The composability of smart contracts allows DeFi developers to develop new solutions and put together combinations of components incredibly quickly. We are seeing a pace of collaborative innovation that I have never experienced before. However, this is also leading to potentially catastrophic scenarios as solutions build on top of faulty solutions without understanding the consequences of a potential compounded downfall. The analogy often used in DeFi is money legos, but maybe in some scenarios, what is being built is money Jenga.

The space is now just getting into more complex financial instruments, and are seeing the power that automating these transaction types can have (e.g., flash loans). We should continue to remind ourselves that crypto was born in the midst of the Global Financial Crisis out of a deep need for a better system. Unless we build sound tools that can protect us against the very same flaws that created this crisis, we are doomed to relive it.

As infrastructure builders, we must create the right foundation, avoiding shortcuts such as centralization and intermediation that [recreate the existing problems we have in our legacy financial systems](https://medium.com/liquality/decentralization-disintermediation-208000413b82). This is especially true for tokens that add unnecessary friction; for representations of native assets that remove their main benefit in favor of convenience and leading to IOUs (e.g., tokenized bitcoin) and for platforms that have admin or control capabilities over their users and act as intermediaries.

My hope is that through open trial and error, we will be able to build an open, censorship-resistant, resilient, borderless, independent financial system that will be useful to those who need it the most, those living under censorship and without access to the digital economy.

### Where can we go to learn more?

You can learn more about Liquality by going to the following:

*   Swap: [https://liquality.io/swap/](https://liquality.io/swap/)
*   Website: [https://liquality.io/](https://liquality.io/)
*   Twitter: [https://twitter.com/Liquality_io](https://twitter.com/Liquality_io/status/1245475811248963584)
*   Telegram: [https://t.me/liquality](https://t.me/liquality)
*   Blog: [https://liquality.io/blog/](https://liquality.io/blog/)
