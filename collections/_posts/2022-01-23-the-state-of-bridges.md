---
git-date:
layout: [blog, blog-amp]
title: "The State of Bridges"
permalink: the-state-of-bridges
h1title: "The State of Bridges"
pagetitle: "The State of Bridges"
metadescription: "Bridges are in their infancy. In 2016, most people were skeptical about anything other than Bitcoin. In 2018, most people were skeptical about smart contract platforms which were not Ethereum…"
category: blog
featured-image: /images/blog/bridges-og.png
intro: "Bridges are in their infancy. In 2016, most people were skeptical about anything other than Bitcoin. In 2018, most people were skeptical about smart contract platforms which were not Ethereum…"
author: Ashdown
tags: ["Cross-chain"]
---

On January 7th, Ethereum founder Vitalik Buterin made a bold statement in regards to how the future will be multi-chain but will _not_ be cross-chain.

I had some comments on his statement which were picked up in [CoinTelegraph](https://cointelegraph.com/news/industry-players-respond-to-vitalik-buterin-s-thoughts-on-cross-chain-ecosystems). Shortly after this was published people reached out to me asking for more detail as to why I felt this way. A longer post was clearly required so here we are.

In Vitalik's post he goes on to describe the state of the union of bridge technology in its current incarnation, addressing a multitude of issues all concluding with the statement that bridges are bad, and we shouldn’t use them.

![](/images/blog/the-state-of-bridges/image1.webp)


You can find the link to the original tweet [here](https://twitter.com/VitalikButerin/status/1479501366192132099).

As someone who has worked in the crypto space for a number of years, and as a general participant I wanted to shed more light in a simplified version as to what Vitalik is in fact referring to. So let’s explore where he is wrong, where is right, while backing the whole thing up with facts.

We’re going to break this down into three different topics, then delve in a little further, and simplify why they are all important.

* Why use a bridge
* Cost of bridges
* Contract composability
* Decentralization

Once we have gone through this we’ll explain where Vitalik is very wrong.

As an FYI - This is a brief overview, and there is so much more. That is not being said. I am not endorsing any one bridge, nor am I condemning any of them. I have personally used most of the ones in production. As such, opinions should be formed for yourself. If you are looking for a more technical in depth explanation on bridges, please refer to [1KX’s Dmitry Berenzon’s post](https://medium.com/1kxnetwork/blockchain-bridges-5db6afac44f8) which provided inspiration for this.


### Bridges are airlines, Blockchains are countries.

For the sake of this article lets oversimplify some of the lingo and bring it back to things that are easy to understand for those who are relatively new to bridges.

**Bridges are airlines:** They will bring people from point A -> point B. They do not all go to the same locations, cost the same, and will likely gauge you at the last minute in regards to fees.

**Blockchains are countries:** They are independent nations who operate with their own rules, and native currency (the network token)


### Why Would I Want to Use a Bridge?

The primary use case to bridge from one chain to another **today** is arguably to get away from high gas fees as Ethereum has become a very costly place to live in the cryptoverse.


![](/images/blog/the-state-of-bridges/image2.webp)


See full report here ([https://coinmetrics.io/the-ethereum-gas-report/](https://coinmetrics.io/the-ethereum-gas-report/))

For this reason, people are looking to either move their assets from Ethereum to other chains or move entirely to new chains altogether.

A simple analogy would be moving from Russia (Ethereum) to Norway (Moonbeam), and wanting to take all of your stuff with you. It makes perfect sense.


![](/images/blog/the-state-of-bridges/image3.webp)


Moonbeam is a country on its own that is still in Europe, which is beautiful, cheaper to live, and has many things that Ethereum does not have. But has a lot to offer on its own which people from Ethereum might appreciate.

The only caveat is that instead of taking a plane to move your assets from one chain to another you are simply using a bridge.

As per Vitalik’s post, if I told you that you are moving from Country A - Country B and had to sell everything you own, how would you feel? If this was the 1700’s and you had to move everything cross country in a wagon, then I get where he is coming from… But the reality is that’s not the case.


#### Cost of Bridges

We have now established what bridges do, and why they are necessary. Now let’s provide some comparisons to the real world.

Bridges are like airlines. They will get you where you want to go, at different rates, offering different perks, and different travel destinations.

Let’s look further and compare Celer Network to Optics.


![](/images/blog/the-state-of-bridges/image4.webp)


As you can see below there is an example of the cost of **Celer VS Optics** when bridging $500 USDC from ETH -> Polygon. The cost from one bridge to another is drastically different but they will both get you from point A-B.


![](/images/blog/the-state-of-bridges/image5.webp)


Another thing to note is that Celer will bridge you to more chains than Optics, but Optics is the main bridge that goes from Celo -> ETH/Polygon.


### Contract Composability

Now that you have a better understanding of bridges, this is the meat as to where Vitalik is right and wrong at the same time.

As things work today, if you have a token minted on ETH, and send it across Bridge A it will arrive differently if you send it across bridge B, this is subject to how the token was originally created.

Let’s look at this again from the airline example. You are examining two airlines (Celer & Optics) to transport your CQT from ETH -> Polygon.


![](/images/blog/the-state-of-bridges/image6.webp)


The problem is when you show up there are two separate people stepping off the plane that are both claiming they are the original.


![](/images/blog/the-state-of-bridges/image7.webp)


This is because there is a single verified smart contract on ETH, but when the CQT crosses each bridge, the contract is different based on the bridge that it crosses.

This is something that most bridges don’t actually care about since it provides moats. This means that dApps will push traffic to a single bridge to ensure contract composability on its destination chain.

As you can see this is a pretty big issue. Not to mention that if you ever want to go back to ETH from the destination bridge the problem might repeat itself.

At a high level this doesn’t sound like a huge deal, but imagine you send your NFT across a bridge, and when you send it back it is no longer part of the original collection so you are excluded from all air drops, or additional utility that might come along with it. The same also applies to farming on multi-chain defi protocols.


#### Decentralization

The other issue with this is that it leaves bridges permissioned as individuals have to whitelist specific assets to ensure that it is the official token that is crossing the bridge. This exploits further human error, and potential issues where projects crossing bridges might not be the right origin contract address on the Ethereum network.

There are also separate issues with bridges requiring a certain amount of liquidity which is similar to funding an LP pool on a DEX, but you need to fund a multi-chain bridge / DEX which is WAY more complicated and is why most bridges also operate as a DEX.

This makes those operating bridges look like airport security since they need to manually do due diligence before letting assets pass through. If they don't do the due diligence, bad actors can happen, and false multi-chain claims can be made. So for now it’s pretty essential.

![](/images/blog/the-state-of-bridges/image8.webp)


There is also the issue of the 51% attack, but we won’t get into that since it’s been played out multiple times ([see quick explainer here](https://www.coindesk.com/learn/what-is-a-51-attack/#:~:text=A%2051%25%20attack%2C%20also%20known,power%20from%20a%20third%20party.))).

To summarize, and where I agree with Vitalik is that in their current incarnation bridges need to be centralized to work, and need human intervention which is contrary to the decentralized world we are trending towards.


### Conclusion

Bridges are in their infancy. In 2016, most people were skeptical about anything other than Bitcoin. In 2018, most people were skeptical about smart contract platforms which were not Ethereum… ßWe have now witnessed the rise of multiple L1’s which have found their place in the world and all have drastically different approaches, all of which are starting to find their place. You are seeing this with EVM chains (Fantom, Avalanche C-Chain, Binance Smart Chain, Harmony), ETH scaling solutions (Arbitrum, Optimism, Polygon, ZkSync), as well as, more novel approaches like Solana, NEAR, Elrond or various substrate chains on Polkadot (Moonbeam, Acala, Astar, etc…) and of course the numbers chains in the Cosmos Ecosystem (Pokt, Terra, Kava, Evmos etc…).

All of these were designed with some sort of interoperability in mind, and the numbers today are speaking to it.

As seen below you can see the TVL by bridges by chain as well as the TVL of bridges over Ethereum L2’s over the last 30 days ([see data for yourself here](https://bi.etherscan.io/public/dashboards/Z6PuB2HTLK4tGOCtrYvP65seYXGWfLea76mknRu6?org_slug=default)):


![](/images/blog/the-state-of-bridges/image9.webp)


![](/images/blog/the-state-of-bridges/image10.webp)


Bridges are here, and Vitaliks points on security, trust, and composability are 100% valid in the way we use bridges today. But much like the rest of the crypto ecosystem, bridges are maturing at a rapid pace and to say that the future is multi-chain but not cross chain is made by looking at the Web3 space today, but not where it is headed.

You are seeing the launch of newer bridges which solve the consensus problem like Axelar, and the composability problems such as Layer 0 & Nomad. You are seeing existing bridges like Synaps launch their own chain which will address many of the same underlying issues.

Much like it took blockchains some trial & error to find their stride. I believe the same is true for bridges.
