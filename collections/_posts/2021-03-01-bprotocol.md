---
git-date:
layout: [blog]
title:  "B.Protocol"
permalink: bprotocol
h1title: "B.Protocol Explained"
pagetitle: "B.Protocol Explained - Interview with Founder"
metadescription: "Yaron told us how B.Protocol eliminating the gas wars and shifting the miner’s profit to the protocol users"
category: blog
featured-image: /images/blog/bprotocol-og.png
intro: "Yaron told us how B.Protocol eliminating the gas wars and shifting the miner’s profit to the protocol users"
author: Defiprime
tags: ['Interview']
---
Yaron told us how B.Protocol makes DeFi lending protocols more stable by incentivizing liquidity providers to commit to liquidation and shift the miners' proceeds back to the users.

_Disclosure: This article was sponsored by B.Protocol._

### Hello! What's your background, and what are you working on?

Hi. My name is Yaron Velner and I’m the founder and CEO of [B.Protocol](https://www.bprotocol.org/). B.Protocol is a backstop liquidity protocol for decentralized lending platforms. A new DeFi lego primitive, bringing traditional finance systems best practices into DeFi, aiming to stabilize the rapidly growing market of DeFi assets which are crucially dependent on adequate liquidation processes, which were missing till now in this young ecosystem.

Before B.Protocol I was the CTO of Kyber Network since it was founded in 2017. I met Lui Loo, Kyber’s CEO, while we were both working on our PhDs in Computer Science.Together with Victor Tran (currently Kyber’s CTO), we built SmartPool in 2016, which was the first decentralized mining pool on Ethereum, as a semi-academic project. Then, in late 2017, Kyber was born and I was the CTO till early 2020. Before diving into crypto I was working for over 10 years as a software engineer.

While in Kyber, as its CTO, I was also involved as a co-designer of the architecture and smart contracts of the WBTC protocol, together with the BitGo team. During that time I had the opportunity to dive deep into the development of some of the more complex on-chain market-making tools we have created for decentralized finance before the term DeFi was coined.  

After I left Kyber I was consulting a few private companies in building liquidation bots for DeFi and CeFi, bringing my experience and knowledge in the cross-section of trading and Solidity smart contracts. It was then when I realized that liquidations on the DeFi ecosystem are broken in so many ways, when compared to regular non-crypto trading systems, as well as to the crypto centralized ecosystem.

And then Black Thursday arrived and I had my theoretical expectations verified in (unfortunate)  real-time events. **Liquidations on DeFi were just not working when they were most needed.**

So I have decided to take B.Protocol from an idea to practice, and started developing the concept into a product - **building a permissionless backstop liquidity protocol for DeFi lending platforms.** I believe this to be one of the backbones of the DeFi ecosystem, and we target a long-term move here, making B.Protocol a standard lego piece among DeFi’s primitives used by existing platforms as well as with those yet to come.   


### What's B.Protocol backstory?

So as I mentioned, after Black Thursday, when the market crashed on March 12th,  I realized that the expectations DeFi lending platforms were building around - meaning that letting everyone participate in the liquidation process can perform well in every condition - would not work in severe market conditions. As there is no commitment from the liquidators, everyone will liquidate only if and when it is convenient for them. **And this makes DeFi fragile and unscalable compared to CeFi.** And as any system is being tested on its rainy day - DeFi failed this specific test.

Moreover, due to the uncertainty in the current situation, where each liquidation is open for everyone on the Ethereum network to compete on, most of the liquidators’ efforts are going for gas optimization and building front-running bots. This warns off the big algo traders from making the effort to build robust trading and hedging systems optimized for the DeFi ecosystem as it’s tough to predict the outcomes and the profitability of such efforts.

With B.Protocol we incentivize liquidity providers (Keepers) to share their proceeds with the platform users in return for a priority in the liquidation process. By that, users get more with the same funds they are using on the lending platforms, while the platforms get committed liquidators that shift back miners extracted profits (aka MEV) to the users.

![](/images/blog/bprotocol/image1.webp)
_[The B.Protocol app](https://bprotocol.org/app/)_

B.Protocol got a seed investment from Kyber Network, and launched its first integration on top of MakerDAO at the end of Oct 2020. We currently have over $30m TVL (of users deposits in ETH) and over 11m Dai that was borrowed through our platform.

Our Compound integration has just launched (Feb. 2021) so now also Compound users can opt-in into B.Protocol, either by migrating their existing funds or open a new account to be managed via B.Protocol.

We have also presented both the [MakerDAO](https://forum.makerdao.com/t/discussion-wbtc-b-collateral-type-backed-by-b-protocol-with-x10-leverage/5409) community as well as the [Aave](https://governance.aave.com/t/discussion-usdc-collateral-type-backed-by-b-protocol-with-90-liquidation-threshold/2005) community with a proposal for what we term “Native Integrations” to enable a new collateral that will let users get higher leverage on their funds. The terms are still not final but we are currently offering a 110% collateralized ratio (aka 90% collateral factor), which means x10 on users’ funds for the first time in DeFi - something that is possible due to the backstop making liquidations in a committed way with pre-deposited funds. We hope this will prove a successful experiment and that it will lead to more collaterals and better terms for both the platforms, their users, and the backstop liquidators as well as for the general DeFi ecosystem.


### What went into building the B.Protocol?

When we [started building B.Protocol](https://medium.com/b-protocol/b-protocol-b6dd4e3bf9c0) in May 2020, the all DeFi ecosystem had roughly $1b in TVL. The exponential growth DeFi saw in the past 8 months or so, growing roughly 30x-40x (depends on the day…), is very exciting but also quite risky - as no fundamental upgrades have been made to the liquidation systems of any of the platforms.  Having a Black Thursday-like event with current volumes can result in fatal outcomes for the entire ecosystem.

It might worth a (very) short explanation as to what liquidations are, and why they are so crucial for the stability, security, and scalability of DeFi (we even made [a short whiteboard explanatory video on that](https://www.youtube.com/watch?v=ieQwjhIm4Lk&ab_channel=B.Protocol)). The Dai ecosystem, lending platforms like Compound and Aave, synthetic asset platforms, and margin trading platforms, all rely on liquidations to remain solvent. Whenever a user’s debt is about to exceed its collateral, a liquidation process is triggered, in which a liquidator pays the user’s debt in return for a part of their collateral which he gets for a discount. Without such a mechanism, **Dai will lose its peg, Compound, Aave, CREAM and all the lending platforms will become insolvent**, as well as any margin or leveraged trading systems.

![](/images/blog/bprotocol/image2.webp)
_A simplified diagram of B.Protocol architecture_

As I have mentioned, all major DeFi platforms currently outsource their liquidations service to the entire Ethereum community, by allowing every Ethereum account to participate in the liquidation process, and offer a discount of 3–8% on the liquidated collateral in order to incentivize the liquidators to participate. This approach fosters fairness in a way but is causing gas wars between liquidators, which conclude in having more and more of the discount being shared with miners, in an endless trial to get your transaction first in line.  

B.Protocol is using a [technical “trick”](https://medium.com/b-protocol/liquidations-in-the-dark-forest-the-b-protocol-and-gnosis-protocol-approaches-eeb897086b17) to bypass the gas war by providing a temporary cushion to a user’s debt when he is getting close to liquidation. This way B.Protocol liquidators get a chance to liquidate the debt while the rest of the keepers of the platform see the funds as still safe.

In return for giving the committed backstop liquidators a priority in the liquidation process, the liquidators are sharing their profits with the users of B.Protocol, instead of spending it on miners’ fees. This results in a win-win situation for all parties involved - a) the platform is getting committed liquidators that enhance its stability; b) liquidators get better certainty and better prediction capabilities and are incentivise to build robust trading and hedging systems fit to DeFi liquidations requirements; c) users get a share of the liquidation proceeds while helping to secure the platforms they use.

As B.Protocol is a thin layer on top of the lending platform we are building on, we are working hard to keep it fully compatible with the platforms on the smart contract level - something that makes it quite easy for 3rd party services that are already integrated with MakerDAO and Compound to integrate B.Protocol as well. That helped us to integrate very quickly with [DeFi Pulse](https://defipulse.com/b.protocol), [DeFi Llama](https://defillama.com/protocol/b.protocol), [DeBank](https://debank.com/projects/bprotocol), and [Zapper](https://zapper.fi/dashboard). We have recently even announced our integration with [DeFi Saver](https://twitter.com/DeFiSaver/status/1352288189180948480?s=20) so now our MakerDAO users can manage their Vaults with DeFi Saver (automation will be added soon as well).

The hardest part of building anything in this ecosystem is getting trusted by the community so users feel safe to use your product. B.Protocol on that aspect is doing all it can to provide 100% transparency - the team is non-anon and in fact, is well known among the crypto community. Besides myself, Jitendra Chittoda who leads our smart contracts is a very experienced developer, who worked for Aave and mStable, as well as being a blockchain security researcher at Chain Security before joining B.Protocol. The project had gone through a full audit with [Solidified](https://twitter.com/SolidifiedHQ/status/1313158774815817728?s=20) for each of the releases (MakerDAO and Compound), with both audits coming out with no major issues.


### What's your business model?

Currently, B.Protocol users are getting bScores according to their usage of the protocol. On MakerDAO for example, for every 1000 Dai borrowed for 24h a user gets 1 bScore. This score is registered on the blockchain but is not transferable, and the liquidation proceeds, as well as the future governance votes, will be made according to the user’s bScore.

We have already coded into the smart contract that 100% of the governance on the protocol will be handed over to the users’ community 6 months after launch (e.g. April 2021 for the MakerDAO integration). During this first epoch, the liquidation proceeds are being divided 50-50 between the users and B.Protocol’s [genesis liquidators](https://medium.com/b-protocol/the-genesis-backstop-b-protocol-brings-new-players-to-defi-liquidations-74619b11486e).




It will be up to the new governance to vote about who will be entitled to take part as a liquidator in the backstop, and what would be the conditions and mechanism to distribute the liquidation proceeds in future epochs.

We are still checking the different monetization possibilities of B.Protocol which are quite broad. As we grow and offer more platforms to get the benefits of the backstop protocol, the question of how this interoperability is translated into revenue sharing will be an issue to be discussed by the protocol governance among other issues.

One of our main goals at the moment is to create what we call “Native Integrations” with platforms, such as the one we have proposed to [MakerDAO](https://forum.makerdao.com/t/discussion-wbtc-b-collateral-type-backed-by-b-protocol-with-x10-leverage/5409) and [Aave](https://governance.aave.com/t/discussion-usdc-collateral-type-backed-by-b-protocol-with-90-liquidation-threshold/2005) as well as to other platforms (still not finalized so I rather not share more details at the moment). In these native integrations, the backstop is getting a priority to liquidate within the platform (at first for a selected pair(s) of tokens), rather for the users needing to opt-in to B.Protocol service by using our own [UI and website](https://www.bprotocol.org/app/).


### What’s your position on the regulatory landscape today?

I believe Stani Kulechov, Aave founder and CEO, has captured most of this in one of his latest tweets
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">&quot;The Party&quot; <a href="https://t.co/8RgXwVdkw1">pic.twitter.com/8RgXwVdkw1</a></p>&mdash; stani.eth 👻 =(⬤_⬤)= 👻 (@StaniKulechov) <a href="https://twitter.com/StaniKulechov/status/1344409239058579461?ref_src=twsrc%5Etfw">December 30, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

### What are your goals for the future?

We have just launched our Compound integration that will enable Compound users to make better use of their funds - getting their slice of the liquidation proceeds while keep on doing the exact same thing with their funds on the platform. We believe that this integration will increase B.Protocol usage in a very significant way. Compound users, after connecting their MetaMask, can use the Import button on the [B.Protocol app page](https://bprotocol.org/app/) to migrate their funds from Compound to be managed via B.Protocol. They will gain bScore - which will let them also vote on the next protocol update, on top of getting their liquidations profits according to their bScore.

Besides of that another big step coming soon is handing over the governance to the community so we are preparing to that as well. And as I mentioned getting more platforms to integrate natively with B.Protocol to enable higher leverage to their users. We currently offer to platforms to have up to x20 leverage, with a collateral factor of 95%, something which was just not possible till now for platforms to offer without being at risk of becoming insolvent.

From someone who’s been in key positions in the crypto ecosystem, having developed Kyber which was way ahead of its time back in 2017, I believe 2021 to become the year DeFi will do the same Ethereum did in 2017 - the development pace will be so rapid that many projects will be left behind eventually but the fundamentals will get their core positioning. I believe B.Protocol will be among these fundamental primitives that will enable DeFi to scale.

We are excited about what 2021 will bring to B.Protocol and to the all DeFi ecosystem.

### Where can we go to learn more?

- Website - [https://www.bprotocol.org/](https://www.bprotocol.org/)
- Twitter - [https://twitter.com/bprotocoleth/](https://twitter.com/bprotocoleth/)
- Discord - [https://discord.gg/bJ4guuw](https://discord.gg/bJ4guuw)
- Medium - [https://medium.com/b-protocol](https://medium.com/b-protocol)
- GitHub - [https://github.com/backstop-protocol](https://github.com/backstop-protocol)
