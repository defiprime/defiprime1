---
git-date: 2021-03-14T10:57:05-07:00
layout: [blog]
title:  "Indexed Finance"
permalink: indexed-finance
h1title: "Indexed Finance Explained"
pagetitle: "Indexed Finance - Capitalization-weighted Index Pools"
metadescription: "Dillion shared Indexed Finance backstory, explained DeFi index investing niche and capitalization-weighted index pools"
category: blog
featured-image: /images/blog/indexed-og.png
intro: "Dillion shared Indexed Finance backstory, explained DeFi index investing niche and capitalization-weighted index pools"
author: Defiprime
tags: ['Interview', 'Derivatives']
---
Dillion shared Indexed Finance backstory, explained DeFi index investing niche and capitalization-weighted index pools.    

### Hello! What's your background, and what are you working on?

My name is Dillion Kellar, and I am the founder of [Indexed Finance](http://indexed.finance/). I have been tinkering with Solidity for the past three years and did monstly contract work for various crypto projects. My last gig before building Indexed was at Dharma, where I was hired to build a Layer-2 EVM to scale their wallet transactions. Unfortunately, it never made it to production :-)

After working on infra/l2 stuff for a couple of years I increasingly felt the urge to do something in the DeFi space. I have always been quite interested in finance and had all these ideas of stuff to build, but the traditional financial system doesn’t allow that. On Ethereum on the other hand, anyone can build whatever financial primitive they like and in many ways improve it to the way it works in traditional finance.

For me the primitive that seemed really interesting and underexplored in DeFi was index investing. Needless to stress how big ETFs are in traditional finance because most people don’t have the time or the expertise to manage their investments.

Crypto needed something similar in my opinion. In short, Indexed is a protocol focused on the development of passive portfolio management strategies for the Ethereum network. Users can invest into a basket of tokens like DEFI5, CC10 or DEGEN by doing just one trade. The basket will automatically track the best tokens within a specific market sector. I guess what is really worth highlighting is that once an index is deployed, this all happens without human intervention. The entire operational overhead is managed by smart contracts.



### What's Indexed Finance backstory?

I launched a beta version of Indexed in December 2020. At that point I had been working on the code for about 4-5 months just by myself and frankly had no idea what to expect once I would deploy the code on the mainnet.

After a relatively calm first week things started really taking off though as some relatively known figures in the space found the project and grew an interest. One such figure was Molly Wintermute from Hegic. She invested 100,000 DAI at the very beginning. I guess that was the turning point.

![](/images/blog/indexed-finance/image1.webp)

### What went into building Indexed Finance?

A lot of hard work. You would think the hardest part is building the initial contracts and deploying them. But the real work only starts after that’s done. Building a community and continuing to ship features that differentiate the project is infinitely harder.

One of the core concepts of Indexed is that the tokens of each index sit in an AMM liquidity pool. Anyone can trade with these liquidity pools and that’s actually how the pools change their weights ([re-weighting](https://cryptotesters.com/review/comparing-defi-index-projects)). In a nutshell, when the market caps of the tokens change significantly, a Controller contract submits new target weights to the AMM. The purpose is to create small arbitrage opportunities to reduce or increase exposure of a specific token and let external traders profit from them. So these liquidity pools are brought to their target weights by market forces and **generate yield** for the index token holders by earning swap fees.

This is unlike DPI from Indexcoop for example, where the tokens are static and don’t generate yield beyond the simple price appreciation of the tokens. To build the contracts for these AMM pools we forked Balancer pools, which are multi-token AMMs and made some important modifications to them. As to security audits, we got two independent auditors to review the core contracts and will continue to do more audits in the future.



### What's your business model?
Right now we don’t charge any fees. Some competitors charge streaming fees which are paid annually on the TVL managed by the protocol. We haven’t decided which route we’re going to take but would ideally like to stay away from charging users directly.

We think that DeFi should do better than traditional ETFs since we have smart contracts that can replace fund managers. However, we want to earn revenue and are looking into different ways to utilize the assets in the pools in a more capital efficient manner.

If we would use some of the assets to yield farm in the wider DeFi space we could charge a spread on the additional revenue that is generated for instance.

![](/images/blog/indexed-finance/image2.webp)

Right now we only have one index charging an exit fee, namely the DEGEN index. This fee is paid by DEGEN holders who decide to burn (instead of selling) their index token to redeem it against the underlying 10 tokens. This is mostly done for arbitrage reasons when DEGEN trades at a discount relative to the net asset value of the 10 tokens it represents. In this case we think it’s justified to charge a fee and we’re curious to see how much revenue this will generate.


### What’s your position on the regulatory landscape today?

We’re not experts in this domain but it seems like regulators are taking a wait and see approach. They also seem to prefer truly decentralized protocols over centralized ones which they view as money grabs. This is why we diluted the core team as fast as possible by having a quite aggressive emission schedule in the first liquidity mining program. A total of 25% of the token supply was distributed to early adopters within two months so at this point we’re not majority stakeholders anymore. Our stake in the protocol will only become smaller over time.

### What are your goals for the future?

In the short term we want to build a couple of new indices. Our goal is to always develop indices for new market sectors users want to get exposure to. We’ve received a lot of requests for an NFT index for instance because many people have no idea of that sector but understand its growth potential and want to participate. We’re also working on developing a long-term (a.k.a sustainable) liquidity mining strategy and improving our tokenomics.

Another goal is to make it as easy as possible for end-users to acquire our indices. We’re working on a revamp of the website and trying to get more integrations in wallets. Right now we’re already integrated in Zerion, Zapper and a range of other wallets and frankly speaking they are doing a better job at nailing the user experience than we are so why not try to develop more of these partnerships? Having liquidity on L2 exchanges like Quickswap on Matic or Uniswap on Optimism in the future would also help us distribute our indices to smaller investors who can’t afford the high gas prices of Ethereum mainnet. Ultimately it would also be nice to be listed on a prominent centralized exchange like FTX or Coinbase.

### What are your future thoughts for the DeFi market?

I think the governance discussion is super important for the future of DeFi. How can we involve more people into the governance of a protocol? What’s the role of the core team? How will protocols be governed in 2-5 years from now? In a world where every multi-billion dollar application is governed by a protocol, your protocol must be set up in a way that it can survive in the long-term.


### Where can we go to learn more?

- [https://indexed.finance/](https://indexed.finance/)
- [https://twitter.com/ndxfi](https://twitter.com/ndxfi)
- [https://ndxfi.medium.com/](https://ndxfi.medium.com/)
- [https://discord.gg/jaeSTNPNt9](https://discord.gg/jaeSTNPNt9)
