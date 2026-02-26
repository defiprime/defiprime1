---
git-date: 2019-08-27T21:50:05-07:00
layout: blog
title: LocalEthereum
url: localethereum
h1title: 'LocalEthereum: Decentralized P2P Fiat on-ramp for ETH'
pagetitle: 'LocalEthereum: decentralized P2P fiat on-ramp for ETH'
metadescription: 'Michael Foster, talks about building decentralized fiat on-ramp for ETH and the future of decentralized finances.'
category: blog
featured-image: /images/blog/localethereum-og.png
quote: /images/blog/localethereum-quote.png
intro: 'Michael Foster, talks about building decentralized fiat on-ramp for ETH and the future of decentralized finances.'
author: Defiprime
tags: ['Interview']

---
Michael Foster, talks about building decentralized fiat on-ramp for ETH and the future of decentralized finances.

### Hello! What's your background, and what are you working on?

My name is Michael Foster and I'm the CEO of [LocalEthereum](https://localethereum.com/). I first discovered Bitcoin in 2010 and have been obsessed with the idea of permissionless and programmable money ever since.

LocalEthereum is a non-custodial peer-to-peer marketplace. It’s a platform where anybody in the world can buy and sell ETH however they choose — whether that be via bank transfer in Venezuela, AliPay in China, a face-to-face cash exchange, or anything else. LocalEthereum provides an all-inclusive privacy-centric on-ramp from fiat currency to ETH free from the horrors of centralized exchanges.

![](/images/blog/localethereum1.png)

It works like this:

When somebody wants to buy or sell ETH, they come to LocalEthereum, enter their preferred payment method, the amount they’d like to exchange, which fiat currency they want to swap, and where in the world they’re located. They match themselves with another trader who fits those parameters, then conduct a peer-to-peer exchange.

A peer-to-peer exchange is a different experience to using a traditional centralized exchange. To complete a peer-to-peer exchange, the seller first puts the ETH side into an escrow account. Once the ETH is in escrow, the pair discusses payment details over end-to-end encrypted chat. The buyer then pays the seller through the agreed-upon means, and afterwards the seller releases the ETH from escrow.

![](/images/blog/localethereum3.gif)

It’s as simple as that for approximately 98% of trades. However, when there is a payment dispute (i.e. somebody claims to have paid and the seller hasn’t received anything), there is a further step: arbitration. When either party calls for help with a payment dispute, a moderator is given limited privileges to do three things: (a) read the encrypted conversation between the two users, (b) talk to each party privately to request further evidence, and (c) make a resolution, directing the ETH to the rightful owner.

### What's LocalEthereum’s backstory?

There are enormous privacy issues, risks and obstacles associated with trading cryptocurrency. These issues have nothing to do with crypto itself, and everything to do with profiteers replicating the vulnerable systems of Wall Street stock exchanges and banks (which motivated the invention of crypto in the first place).

[LocalEthereum](https://localethereum.com) is largely inspired by LocalBitcoins, the Bitcoin-flavoured marketplace with a similar name, which set out to solve many of these problems. We also draw inspiration from other peer-to-peer marketplaces such as PaxFul and LocalMonero.

I met my co-founder in 2012 through one of these marketplaces. Back then, it didn’t cross our minds to build a competitor, however the opportunities for enhancement were obvious: the platform was buggy, slow, unencrypted, and—most importantly—it was custodial, making it just as vulnerable to theft as a centralized exchange.

Five years later, in early 2017, we noticed there was no service enabling users to trade ETH peer-to-peer, yet plenty of platforms offering the same for BTC. It didn’t take long for us to validate the idea and discover that, yes, people want a LocalEthereum. So we set out to build it.

LocalEthereum launched without outside funding in late 2017, and it took off like a rocket. Our only significant pre-revenue cost was buying the LocalEthereum.com domain name from a squatter for around $3,000.

Today, LocalEthereum has more than 100,000 users from almost every country, and a new peer-to-peer transaction is created every 2-3 minutes. The platform is most popular in Venezuela, Russia, China, Kenya, Nigeria, and the U.S., however on an average day there are 1,000 active users in 70 countries.

### What went into building LocalEthereum?

We didn’t want to simply build a LocalBitcoins clone.

With the flexibility Ethereum provides, we quickly realized we could make LocalEthereum non-custodial by turning the escrow service into an Ethereum smart contract. What this means is that while an arbitrator has the capability to resolve payment disputes, they can only do so with explicit digital permission, and it’s impossible for them to direct ETH to anyone other than the buyer or seller.

We also decided early-on to go a step further and make messages between users end-to-end encrypted (using a forward secret protocol derived from OTR). Users are discussing sensitive details over chat, including bank account numbers and names — information they deserve to keep private.

![](/images/blog/localethereum4.gif)

To allow the platform to be newcomer-friendly, we decided that the MetaMask-only approach wasn’t a road we wanted to go down. The simple truth is that most people are not comfortable with installing a browser extension, and setting up a crypto wallet is a burden to entry-level users. To get around this, we built a simplistic non-custodial web wallet from the ground up and plugged it into LocalEthereum. We also built a gas relay service so new buyers can interact with LocalEthereum’s smart contract before owning any ETH.

The non-custodial and end-to-end encrypted nature of the platform makes it immune from the thefts and hacks plaguing the crypto community, which have stolen billions so far. LocalEthereum only ever holds a couple hundred dollars worth of ETH on its servers to allow the gas relay service to function.

From start to launch, LocalEthereum took around six months to develop and a further three months of rigorous testing and revision.

### What's your business model?

Every successful escrow has a transaction fee attached. We charge the same fee as competing platforms: 1% of the escrow amount (0.25% on one side, 0.75% on the other).

We considered eliminating the fee and raising money via an ICO, however a utility token is totally unnecessary for a product like ours. It would have been possible to over-complicate LocalEthereum to superimpose some kind of token function, but this would only make the platform harder to develop and significantly more difficult to use. Besides, we didn’t need a large budget to launch LocalEthereum.

Looking at the trend of similar P2P projects that did ICOs in 2017, I’m fairly certain that LocalEthereum wouldn’t have one tenth of the user count it has now if we had followed suit.

![](/images/blog/localethereum2.png)

### What are your goals for the future?

[LocalEthereum](https://localethereum.com) still is and always will be a work in progress. We’re always working on the next iteration.

In 2019, our top focus has been on preventing scammers from ripping off LocalEthereum users. We’ve spent a lot of time learning the different techniques fraudsters pull on peer-to-peer platforms (some are simple, others are more advanced). Currently we’re working on [an optional identity verification system](https://blog.localethereum.com/preventing-identity-theft-with-optional-id-verification/), which will allow users to optionally share their identity to other users while remaining pseudonymous to LocalEthereum and protected from identity theft.

We’re also looking at ways to further decentralize LocalEthereum. The ecosystem surrounding Ethereum has greatly improved since our launch in 2017, and we think now is the time to begin moving bits and pieces over to technologies like Swarm.

Besides these advances, there is something massive we’re brewing in secret. We’re excited to unveil it in a few months.

### What are your future thoughts for the DeFi market?

Right now, the DeFi craze is collateral loans and synthetic stablecoins. While I see the demand for stability and I’m excited about DAI’s potential to accelerate worldwide adoption, I’m personally waiting for the era when fiat-denominated stablecoins are no longer useful, and the world has transitioned to a cryptocurrency with an unchangeable, theft-resistant monetary policy reminiscent of Bitcoin.

The truth is that nobody knows where this is going. The only thing I know for sure is that in twenty years from now, the space is going to look entirely different and we’re going to be arguing about topics that nobody today could predict.

### Where can we go to learn more?

You can take a look at [LocalEthereum.com](https://localethereum.com). There are over 100,000 users right now and thousands of active listings.

If you want to read more about the background and technologies underpinning LocalEthereum, read our [technical whitepaper](https://whitepaper.localethereum.com/).

- Find us on Twitter: [@LocalEthereum](https://twitter.com/LocalEthereum).
- Telegram: [English](https://t.me/localethereumdotcom), [Spanish](https://t.me/es_localethereumdotcom), [Russian](https://t.me/ru_localethereumdotcom).
