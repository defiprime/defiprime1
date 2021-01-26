---
git-date:
layout: [blog, blog-amp]
title:  "The Current State of Ethereum L2"
permalink: ethereum-l2
h1title: "The Current State of Ethereum L2"
pagetitle: "The Current State of Ethereum L2 - Ethereum Layer 2 Projects"
metadescription: "In today’s post let’s examine how some of Ethereum’s most promising L2 projects are looking in the here and now"
category: blog
featured-image: /images/blog/l2-og.png
intro: "In today’s post let’s examine how some of Ethereum’s most promising L2 projects are looking in the here and now"
author: Peaster
tags: ['DeFi List']
---
Demand to use Ethereum blockspace has exploded over the last year. The recent traction has led to Ethereum’s transaction fees, i.e. ETH gas prices, rising to painful levels at times.

On the bright side, this shows that Ethereum’s young base layer is extremely useful and that many people are bidding over each other to get their transactions processed in a timely fashion.

Conversely, for Ethereum to keep making advances toward the mainstream, it’ll need to scale up so it can offer instant and cheap transactions and meet the demand of _billions_ of users, not just thousands.

The good news, then, is that an ecosystem of layer-two (L2) scaling solutions has already bloomed around Ethereum and is offering multiple different avenues to scale Ethereum for the masses. “Layer-two,” we say, because these innovations work by being appended to Ethereum from the blockchain’s _periphery_ rather than via making modifications to the reigning smart contract platform’s base layer.

As such, we’re now staring down a future where Ethereum will serve the masses with the help of a range of different L2 solutions. In today’s post, then, let’s survey the various L2 styles that have come to the fore to date and examine how some of Ethereum’s most promising L2 projects are looking in the here and now.


### Understanding L2

In the years ahead, Ethereum will eventually embrace L1, i.e. base layer, scaling via sharding, which will split Ethereum’s activity across 64 main chains rather than one.

Yet it will be some time before sharding is implemented. The innovation’s scaling benefits can work collaboratively with L2 tools, so we’ve seen the L2 arena really blossom in recent months as projects have raced to help Ethereum scale amid this critical transitionary period for the network.

So far, the three main L2 models we’ve seen are as follows:



*   **_State channels_**
*   **_Sidechains_**
*   **_Rollups_**
    *   _optimistic rollups (ORUs)_
    *   _zkRollups (ZRUs)_
    *   _Plasma_
    *   _Validium_



![](/images/blog/the-current-state-of-ethereum-l2/image1.png)


_**Source:** Token Terminal_


#### <span style="text-decoration:underline;">State Channels</span>

State channels take the burden off the Ethereum base layer by facilitating transactions off-chain. State channels require a user to deposit a snapshot of Ethereum’s state into a multi-sig contract (not dissimilar to how users deposit bitcoin into the Lightning Network’s payments channels). This state will harbor key data, like an address’s ETH holdings at a given time. Such a system allows for free off-chain transactions with instant finality and superior privacy.


#### <span style="text-decoration:underline;">Sidechains</span>

Sidechains are independent blockchains with their own independent consensus rules where Ethereum transactions can be moved to in a custodial manner in order to decrease the burden on the Ethereum mainnet.


#### <span style="text-decoration:underline;">Rollups</span>

[Rollups](https://vitalik.ca/general/2021/01/05/rollup.html) are akin to advanced, non-custodial sidechains that can extensively extend the throughput capabilities of the Ethereum mainnet. So far, rollups have come in four main varieties: optimistic rollups (ORUs), zkRollups (ZRUs), Plasma chains, and Validium chains.


![](/images/blog/the-current-state-of-ethereum-l2/image2.png)


_**Source:** [buildblockchain.tech](https://www.buildblockchain.tech/newsletter/issues/no-99-validium-and-the-layer-2-two-by-two)_

You can contrast these four rollup styles depending on whether they handle data storage on-chain (ZRUs, ORUs) or off-chain (Plasma, Validium) and whether they handle computation via zero-knowledge validity proofs (ZRUs, Validium) or via deposit-slashing fraud proofs (ORUs, Plasma).


### Surveying Ethereum’s Top Layer 2 Projects


#### <span style="text-decoration:underline;">Connext</span>

**Style**: State channels \
**TPS**: ∞

Connext is a state channels project that is striving to be an L2 solution not only for Ethereum but also a [cross-chain routing hub](https://medium.com/connext/instant-cross-l2-transfers-are-now-on-testnet-2f1295530c22) for Ethereum’s many L2 solutions. One of the concerns in the early L2 arena has been that these projects will be too siloed from each other. Connext’s new cross-L2 transfer system can prove pivotal in making sure that won’t be a serious problem going forward.


#### <span style="text-decoration:underline;">xDai Chain</span>

**Style**: Sidechain \
**TPS**: 70 txs

[xDai Chain](https://www.xdaichain.com/#:~:text=The%20xDai%20Chain%20is%20a,Proof%2Dof%2DStake%20consensus.) is an EVM-based sidechain that’s been designed to facilitate transactions in an extremely rapid and stable manner. The project is underpinned by its STAKE token, which consensus providers stake in order to secure the sidechain. Because of its efficiency, xDai Chain has been growing in popularity in recent weeks.


#### <span style="text-decoration:underline;">POA Network</span>

**Style**: Sidechain \
**TPS**: 70 txs

Like xDai Chain, [POA Network](https://www.poa.network/) is an EVM-based sidechain that relies on a set of trusted validators to power quick and cheap transactions. The solution is viable for backing anything from blockchain games to community currencies.


#### <span style="text-decoration:underline;">Optimism</span>

**Style**: ORU \
**TPS**: +20,000 txs

[Optimism](https://optimism.io/) is an ORU implementation that is gaining early traction among some big DeFi players, like Synthetix. Optimism has built the OVM, an L2-based EVM that makes it so projects can enjoy all the benefits of Ethereum’s L1 smart contracts while on L2. Moreover, Optimism is already in the process of facilitating its mainnet launch, so L2 benefits are no longer on the horizon.


#### <span style="text-decoration:underline;">Fuel</span>

**Style**: ORU \
**TPS**: +20,000 txs

[Fuel](https://fuel.sh/) was the first ORU implementation to hit the Ethereum mainnet, as Fuel’s first rendition went live on Dec. 31st, 2020. The great promise of this L2 solution is super fast and super efficient token payments. Indeed, the project’s aiming for nothing less than becoming “Earth’s value exchange layer.”


#### <span style="text-decoration:underline;">zkSync</span>

**Style**: ZRU \
**TPS**: +20,000 txs

Created by Matter Labs, [zkSync](https://medium.com/matter-labs/introducing-zk-sync-the-missing-link-to-mass-adoption-of-ethereum-14c9cea83f58) is a ZRU-based **L2 scaling** solution that uses zero-knowledge proofs to offer high throughput and high security. Ethereum projects that have already integrated with zkSync include Gitcoin and Golem.


#### <span style="text-decoration:underline;">Loopring</span>

**Style**: ZRU \
**TPS**: +16,000 txs

Loopring was the first rollup deployed to Ethereum, running on mainnet for over one year at this point. [Loopring’s ZRU-based tech](https://loopring.org/#/protocol) is currently focused on scaling decentralized exchanges (AMMs and orderbooks), and payments. The technology is already usable in the Loopring 3.6 release, on which the Loopring Exchange and Loopring Wallet are based.


#### <span style="text-decoration:underline;">StarkEx</span>

**Style**: Validum \
**TPS**: +20,000 txs

[StarkEx](https://starkware.co/product/starkex/) works somewhat similarly to zkRollups, with the main difference being that StarkEx’s Validium-based system handles data storage off-chain. This dynamic allows the project to have higher throughput capabilities compared to pure ZRU systems.

## Conclusion

There are a variety of L2 solutions that will be responsible for forming Ethereum’s scaling landscape in the future. These solutions are starting to take shape right in front of us, to the point that 2021 will likely see more scaling advances around Ethereum than we’ve ever seen before. These projects won’t be zero sum, but rather will work in tandem to make it so that Ethereum can handle millions of transactions per second, not just dozens. Accordingly, L2 solutions will be how Ethereum wins over mainstream users and becomes a popular international settlement system.
