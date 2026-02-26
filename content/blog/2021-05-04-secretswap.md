---
git-date: 2021-05-02T09:35:24-07:00
layout: blog
title:  "SecretSwap"
url: secretswap
h1title: "SecretSwap: Cross-Chain Dex With Front-Running Protection"
pagetitle: "SecretSwap Cross-Chain Dex Dex With Front-Running Protection"
metadescription: "What are privacy-preserving smart contracts? Find it out in our interview with Secret Network co-founder"
category: blog
featured-image: /images/blog/secretswap-og.png
intro: "What are privacy-preserving smart contracts? Find it out in our interview with Secret Network co-founder"
author: Defiprime
tags: ['Interview', 'DEXs']
---
What are privacy-preserving smart contracts? Find it out in our interview with Secret Network co-founder.

_Disclosure: This article was sponsored by SecretSwap_

### Hello! What's your background, and what are you working on?

Greetings, My name is Can Kisagun. I am one of the co-founders and the product lead at Enigma. Enigma is the main development company behind [Secret Network](https://scrt.network/). As a result, I also contribute to a lot of product efforts within the Secret Network ecosystem, such as SecretSwap and SecretNFTs.

I got into Bitcoin in 2014. Like many others, I had my eureka moment after I read the Bitcoin whitepaper. This was the time when I was starting my graduate degree at MIT and I decided to immerse myself in the MIT Bitcoin ecosystem. I started to get involved in MIT Bitcoin club, where people like Dan Elitzer (Nascent Capital) and David Vorick (Sia Network) were actively evangelizing blockchain and running the famous MIT Bitcoin experiment. Then I met Guy Zyskind, who was doing his research at MIT Media Lab on privacy for blockchains using Multiparty Computation (MPC), which eventually turned into the Enigma whitepaper and Enigma the company :)

Built on Secret Network, SecretSwap is the first front-running resistant, privacy-first, cross-chain Automated Market Maker (AMM) protocol. Secret Network introduces the concept of secret contracts, which are similar to smart contracts but operate with encrypted inputs, encrypted state, and encrypted outputs. Leveraging secret contracts, SecretSwap is able to achieve the following:

1. Front-running prevention: inputs in the mempool are encrypted, which means miners can’t extract value by reordering or frontrunning your transactions
2. Privacy: because inputs to a swap contract are encrypted, users get privacy assuming more than a single user swaps a given pair in any given block of transactions

SecretSwap also provides access to cross-chain liquidity, and reduces transaction fees relative to other protocols such as Ethereum.

All of these features provide an improved user experience compared to other AMMs and attract users to SecretSwap. As in the case of SecretSwap, our goal with DeFi products built on Secret Network is to improve usability and bring this new open finance paradigm to the masses.


### What's the SecretSwap backstory?

Decentralized exchanges and AMMs have always struggled with front-running. Front-running is an arbitrage strategy to make profit at someone else’s expense based on an information advantage. Front-running issues are not limited to DeFi. However, the scale of the problem is amplified given the public nature of blockchains.

Miners and arbitrage bots can see an order in the mempool before the order makes its way into the ledger. Front-runners then insert their orders with higher gas fees to be processed first. This means that the miner or the arbitrage bot can profit at the expense of a regular user. Furthermore, this arbitrage opportunity increases the gas fees of the underlying network - hurting users even more. Front-running problems on Ethereum DeFi costs users ~$1bn per year and millions of dollars in lost gas fees.


![](/images/blog/secretswap/image1.webp)
_MEV = Maximum Extractable Value. Chart via [explore.flashbots.net](https://explore.flashbots.net/)_

When you see a billion dollar problem, why not solve it? That’s why we started building SecretSwap.


![](/images/blog/secretswap/image2.webp)


SecretSwap leverages programmable privacy with secret contracts on Secret Network. Using an encrypted mem pool via a secret contract, SecretSwap empowers users with a seamless experience where front-running is nullified. Even better is that transactions are encrypted - giving users default privacy and anonymity with each of their transactions. Like in other AMMs, in order to calculate prices on SecretSwap, pool balances must be public. When there’s more than one user swapping a pair in a given block, those users enjoy anonymity. If there’s only one user, it’s possible to identify the swap details due to the change in the publicly visible pool balances. Secret Network, which is a layer-1 blockchain based on Cosmos SDK, also allows fees on SecretSwap to be extremely competitive. Each swap costs less than $1.

You might ask, “Why an AMM as one of the first major application layer projects on Secret Network?”

In addition to solving a real pain-point, SecretSwap is the foundation for other DeFi products (such as staking derivatives, synthetic assets, lending protocols) to be built on Secret Network. If we look into the growth of DeFi in Ethereum, Uniswap plays a foundational role. We expect SecretSwap to have equal importance for Secret Network.

Finally, we are firm believers that usability improvements that are made possible by the privacy features of Secret Network is an essential step towards mass adoption of DeFi. Today, the major players in DeFi struggle with the fact that their wallets and their transactions are being constantly monitored. This is a problem we need to solve if we want to attract more money to DeFi. We need to provide users the ability to preserve their privacy if we expect the masses to use DeFi.

That is precisely what Secret Network provides.


### What went into building the SecretSwap?

SecretSwap was launched on the Secret Network mainnet March 31, 2021 after three months of development. The idea of a front-running resistant, privacy preserving cross-chain DEX has been on our minds for many years. I actually presented and wrote about [front-running prevention using Secret Contracts back in 2019.](https://blog.enigma.co/preventing-dex-front-running-with-enigma-df3f0b5b9e78)

SecretSwap was made possible by three key Secret Network milestones - the implementation of secret contracts which enabled programmable privacy, the creation of the SNIP-20 secret token standard, and the launch of the Secret Ethereum Bridge.

The first milestone was the implementation of secret contracts on the Secret Network mainnet in September of 2020. This made Secret Network the first layer-one blockchain to enable general purpose private computations. Secret contracts facilitate arbitrarily complex data privacy controls to be implemented inside applications - exactly the type of flexibility needed to make SecretSwap possible.

The second milestone occurred in November of 2020 with the creation of the SNIP-20 specification for private fungible tokens (based upon CosmWasm on Secret Network). SNIP-20 outlined the creation of Secret Tokens which mimic the ERC-20 standard, but with the added privacy-preserving benefits of:

1. All balances are encrypted
2. Transfer operation arguments are encrypted

These properties of Secret Tokens ensure that any transaction and all rolling balances are forever kept encrypted. Each person can still query their own (and only their own) balance, as well as send tokens to others privately. Additionally, Secret Network can take a normal implementation of a token standard such as an ERC-20 and wrap it into the Secret Token equivalent. The SNIP-20 specification was critical for SecretSwap as all tokens exchanged on SecretSwap are Secret Tokens.

The final key milestone was the launch of the Secret Ethereum Bridge in December of 2020 - empowering users to create the secret synthetic (wrapped) ETH and ERC-20 tokens which have all of the benefits of the SNIP-20 standard. The Secret Ethereum Bridge was the final component that was needed for SecretSwap to be successful as these wrapped privacy-preserving tokens (sETH, sDAI, sUNI, sSCRT, etc.) could then be swapped on SecretSwap at launch.  


### What's your business model?

Fundamentally, SecretSwap is governed and controlled by $SEFI -  the governance token for SecretSwap and the Secret DeFi ecosystem. Users of SecretSwap can earn SEFI to participate in shaping the future of the first front-running resistant, privacy-first open financial system. SEFI is a SNIP-20 or Secret Token, which means all SEFI transactions and contract interactions are private.

Total supply of SEFI is set at 1,000,000,000. This amount is a non-inflationary fixed supply set at launch. 10% of the SEFI supply was distributed at the genesis event to SecretSwap liquidity providers and stakers. The remaining 90% is distributed over the course of four years.

Currently 0.3% trading fees are reinvested back in the liquidity pools providing income for LPs in addition to LP rewards. We are looking to use a portion of trading fees for SEFI buyback. This would be a feature upgrade that SEFI holders would vote on.

A unique feature of SecretSwap is the SEFI governance token which enables changes to SecretSwap protocol code via proposals. Approximately 25% of SEFI distribution over the next four years will be allocated to a development pool which will fund future product development, marketing, rewards, and liquidity provider acquisition. In the spirit of decentralization, we want SEFI stakeholders to play an integral role in the direction of SecretSwap.


### What are your goals for the future?

SecretSwap aims to be the foundation of SecretDeFi, the only front-running resistant, privacy first cross-chain open finance ecosystem. We expect SecretDeFi ecosystem to introduce lending protocols, synthetic assets, derivatives minting and trading protocols and eventually dark pools.

Our goals with SecretSwap are $500mn TLV and $300mn daily trading volume by the end of 2021.

The increase in TVL is primarily expected to come from i) bridges to new ecosystems and ii) increased value of assets on Secret Network. The Secret Network community is currently building a bridge to Binance Smart Chain and have a testnet bridge to Plasm, an EVM-based parachain, which will allow Secret Network to tap into the Polkadot ecosystem. In addition there are new assets being created on Secret Network. One example is DeFi focused Sienna Network, another is gaming focused ZeroSum Network and there’s also staking derivatives are under development which will allow 90mn staked SCRT to be used in SecretDeFi ecosystem.

SecretSwap is also introducing the concept of rewarding traders as well as LPs. Traders acquire cashback tokens (currently under development) for each trade they make on SecretSwap. The larger the trade the more cashback tokens. These cashback tokens will be redeemable for SEFI or in other words, users of SecretSwap will be able to burn cashback tokens to receive SEFI. We believe this will be a key mechanism to grow daily trading volume in SecretSwap

SecretSwap provides significant UX improvements and with growing TVL (lower slippage), adoption of SecretSwap will only increase. This is only the beginning!


### What are your future thoughts for the DeFi market?

Decentralized finance (DeFi) has enabled open access to a new financial ecosystem, which will eventually be superior compared to the traditional financial services both for users and innovators. Users can now opt-in to services they want to use at low cost, easily switch between services, and even become owners and earn voting rights for the products they use - all built on an interconnected system of blockchains. What have historically been passive assets now become productive assets. Creative minds can develop a practically unlimited list of financial instruments and services, all controlled by a series of smart contracts meant to ensure fair dealing and safety of funds. The ability for anyone around the world to gain access to US stocks through protocols like Mirror is truly exciting.

However, we should recognize that in order for DeFi to gain mass adoption, there are two major roadblocks we need to address as an industry

1. Privacy: I firmly believe DeFi cannot hope to eventually reach mass adoption as a complex and complete open financial system if financial privacy must be sacrificed. We cannot expect financial institutions to bring money into the DeFi ecosystem if every transaction they do can be observed and tagged in platforms like Nansen
2. Compliance: It’s very important that we work to create a compliant ecosystem for more money to flow into DeFi. Graysacle Bitcoin and Ethereum Trusts alone have over $43bn in assets, almost the entire DeFi ecosystem. Creating compliant structures will enable institutions to directly deposit assets to the DeFi ecosystem. Furthermore, in order for this new open finance paradigm to really reach masses we need to engage retail banks and financial institutions as well. I firmly believe that current yields on stable coins on DeFi would give significant advantage to many challenger banks. It’s our responsibility to create a compliant infrastructure that can attract retail money to DeFi.

I am personally very interested in the compliance aspect and collaborating with experts in AML / KYC space to come up with the design requirements of a compliant DeFi ecosystem. Privacy and compliance are the two factors that will propel DeFi to trillions of AUM and serve over 1.7 billion people who are unbanked globally.


### Where can we go to learn more?

- [Website](https://scrt.network/)
- [Telegram](https://t.me/SCRTCommunity)
- [Twitter](https://twitter.com/SecretNetwork)
- [Blog](https://scrt.network/media/blog)
- [YouTube](https://www.youtube.com/watch?v=c70BBVUCxxk&list=PLL1JDiTNCUAUZUyK3-uZfjM-AJFnFtLLo)
- [LinkedIn](https://www.linkedin.com/showcase/secretnetwork/)
- [Reddit](https://www.reddit.com/r/SecretNetwork/)
- [Discord](https://discord.gg/gfGUKPxC)
