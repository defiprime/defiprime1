---
git-date: 2019-08-25T14:05:50-07:00
layout: blog
title:  Nexus Mutual
url: nexus-mutual
h1title: Nexus Mutual - Smart Contract Insurance. Interview with founder.   
pagetitle: Nexus Mutual - Smart Contract Insurance. Interview with Hugh Karp, founder of Nexus Mutual.   
metadescription: Nexus Mutual - Smart Contract Insurance. Hugh Karp talks about Nexus as a part of the best practice standard for smart contract security.
category: blog
featured-image: /images/blog/nexus-og.png
quote: /images/blog/nexus-quote.png
intro: Hugh Karp talks about Nexus as a part of the best practice standard for smart contract security.
author: Defiprime
tags: ['Interview', 'Insurance']
---
Hugh Karp talks about Nexus as a part of the best practice standard for smart contract security.

### Hello! What's your background, and what are you working on?

Hi, my name is Hugh Karp, Founder of [Nexus Mutual](https://nexusmutual.io/).

Prior to working on Nexus full time, I've been in the corporate world of insurance as an actuary for over 15 years. I started in Australia, where I'm from, working for a life insurance company before moving to the UK in 2012 to work for Munich Re, one of the two largest global reinsurance companies in the world. I was most recently the CFO for Munich Re's UK and Ireland Life operations before leaving to work on Nexus.

In terms of crypto, I stumbled across bitcoin on some internet forum quite a while ago and found the whole idea fascinating. I have to admit I didn't really understand how it all worked, but I was intrigued by the idea you could send money to someone else without involving a bank. In retrospect, one of my most memorable experiences was buying a couple of bitcoin by sending premium text messages! I then actually put bitcoin aside for a few years because I couldn't immediately see what I could do with it. My background and expertise is in insurance, and payments didn't interest me that much.

Then I heard about Ethereum, and my mind started whirring again with the possibilities. Conditional payments are essentially insurance contracts, and that's when I recognised the opportunity to apply my corporate experience with a passion for this new technology, and Nexus started coming together.

At its most basic Nexus Mutual is a DAO, though we prefer the term digital cooperative. Members join together and contribute funds and/or expertise to the mutual and share risk with each other. Specifically, you can get protection against hacks or bugs in Ethereum smart contracts by purchasing Smart Contract Cover, and you can also participate in other aspects of running the mutual if you like.

![](/images/blog/nexus2.png)

### What's Nexus Mutual's backstory?

Nexus Mutual goes back to the roots of the insurance industry, and it's essentially a way for a community to come together and share risk without the need for an insurance company. The members of the mutual own the funds and decide how they are used. This is the way insurance started thousands of years ago. It's just now we have a new technology that can scale the old way of doing things and ideally compete with the large insurance companies of the world.

One of the key attractions of the mutual model is the significantly reduced conflicts of interest, as you no longer have a shareholder that directly makes more money when claims are denied. Once I recognised that we could use Ethereum to build a scalable mutual, I started iterating on different designs and also focused heavily on regulatory and legal research. The insurance industry is one of the most heavily regulated in the world, and I knew that if we didn't find a viable route to market, we wouldn't get very far.

Specifically, on regulation, there is a whole raft of complex regulations and laws surrounding appropriately managing an insurance company's assets, and this is because insurers are essentially caretakers of their customers money until claim obligations have ended. If smart contracts control the rules of how funds can be used, then we can achieve the same aims of those laws and regulations in a more efficient manner. This is the aspect I like most about what we've built, the non-custodial pool of funds.

On the product side, one interesting aspect is that we started with earthquake cover as there are many communities that can't access basic coverage. However, we very quickly realised our early adopters would be crypto natives, and the number of crypto natives wanting earthquake cover was approximately 2. So we switched pretty early on to crypto native risks, and in particular Smart Contract Cover after observing The DAO hack and the first Parity multi-sig issue. Watching The DAO get drained live was something I won't forget anytime soon. These events highlighted a clear risk that needed covering.

![](/images/blog/nexus1.png)

### What went into building the Nexus Mutual?

Overall it would have taken us about three years to get to main-net launch from the earliest point. There was a lot of time doing legal and regulatory research, discussing with UK regulators as well as mutual experts and what could work and what wouldn't. We went down a lot of dead ends, but we're confident this time and money will be well worth it in the long run. We also made a decision early on that we couldn't possibly build a fully decentralised network on day-1, it was just too complex, that meant we needed to comply with regulations fully.

In terms of building, aside from the direct coding, there have been a lot of economic modelling, simulations, and testing. We've used all of our actuarial skills to replicate the economic nature of an insurance company but on? An open crypto network instead. Once we had the core of the model bedded down, we started building it, with many tweaks and updates along the way. We also knew we had to focus heavily on security as we were building a relatively complex dApp. Our approach was to test everything we could think of, then do the usual security audits but also release the code with an emergency pause functionality that any Board Member can initiate. This allows contracts to be fixed should an error occur, but only after the members agree to the update.

This actually highlights an interesting aspect to what we're doing in terms of the spectrum of decentralisation. The mutual, or DAO, is actually linked to a legal entity in the UK which means we have a Board and while the Board's powers are extremely limited compared to regular company boards, they do have some additional powers like the emergency pause functionality. We've specifically decided to take this approach but also counteract their power by allowing the members to replace the Board members at any time, and the Board can't stop it. Our goal is to have a governance model that allows relatively quick progress, but also has the appropriate controls on power.

### What's your business model?

Very simply, the members of the mutual, NXM token holders, own all the surplus that is generated from cover purchases. We've priced smart contract cover with an expected surplus margin that will eventuate provided claims costs are within reasonable bounds. That surplus will remain in the mutual and is collectively owned by all members of the mutual.

When the mutual has excess funds, the NXM price increases, and members may redeem their NXM for ETH. When the mutual needs more funds, the price of NXM decreases to encourage funds to be provided. Overall the process dynamically ensures the capitalisation levels of the mutual are both adequate and not excessive.

Regarding our product, as far as I'm aware we're the only ones offering Smart Contract Cover, so we don't have any direct competitors right now. Our goal is to become the best practice standard for projects developing smart contracts. So in a similar way to getting a security audit, we believe projects should also consider buying smart contract cover to protect their early users. This will give their users more confidence in using the new platform, knowing that they'll be reimbursed if something were to go wrong. It's a common worry from many users, so we think it will help spur adoption of new platforms.

### What's your position on the regulatory landscape today?

The most challenging aspect as a project is dealing with a regulatory landscape that it is very unclear. It stifles innovation and wastes a lot of time and effort. The clarity is coming piece by piece, so I think that is a positive, but it could be moving faster.

I'd encourage any project operating in the DeFi space to thoroughly understand their regulatory position and risks they are taking, even understanding exactly where the unknowns are is a huge benefit as small tweaks to product design can reduce the risk substantially. Also, I think we should all understand that regulation comes from good intentions to protect consumers and often what we're doing in DeFi is trying to achieve the same objectives; for example, to remove or reduce custodial risks. If we can get to market safely with alternative models that are actually better from a consumer protection standpoint that has to be a win for everyone. The wider crypto ecosystem has a long way to go on showing regulators the benefits of these new approaches, and we've been considering them the enemy for a while now, but hopefully, that will change.

### What are your goals for the future?

Our main goal is to establish Nexus as part of the best practice standard for smart contract security. We see ourselves as an enabler. All economies have insurance to protect against risks, and it's how new businesses and progress is made. We see Ethereum as building a new financial economy, and we aim to be the insurance-alternative for that economy. In that regard, we're looking to expand the reach and traction of Smart Contract Cover in many different ways, but we're also assessing other crypto native risks as potential future products.

### What are your future thoughts for the DeFi market?

DeFi is still in its infancy, but it's growing rapidly, and I see it as a method for onboarding many users into the Ethereum ecosystem. The on-ramp issue is one of the biggest barriers remaining, but lots of people are actively working on that, so I'm sure we'll see some tangible progress within the next year. In particular, If I can easily upload my assets to Ethereum and earn returns much higher than my bank account, that could be a trigger for many more regular users to enter the ecosystem.

More generally, DeFi really shines when users can't trust the regular financial system or are excluded for some reason. Once we've built a reliable alternative financial ecosystem, we'll be able to provide options for these individuals, and for me, that's what we should be aiming for in the longer term.

### Where can we go to learn more?

- [Website](https://nexusmutual.io/)
- [Get a quote](https://app.nexusmutual.io/#/SmartContractCover)
- [Twitter](https://twitter.com/NexusMutual)
- [Discord](https://discord.gg/DwtQuSD)
- [Medium](https://medium.com/nexus-mutual)
