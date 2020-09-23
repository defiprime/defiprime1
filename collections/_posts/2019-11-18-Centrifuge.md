---
git-date:
layout: [blog, blog-amp]
title:  Centrifuge
permalink: centrifuge
h1title: "Centrifuge - bridging the gap between traditional finance and web3"
pagetitle: "Centrifuge - bridging the gap between traditional finance and web3"
metadescription: "Centrifuge is a network to exchange business documents (think invoices and similar items) privately and securely while relying on a public blockchain for proof of authenticity and the tokenization of these documents."
category: blog
featured-image: /images/blog/centrifuge-og.png
quote: /images/blog/centrifuge-quote.png
intro: "Philip on real-world assets tokenization, bridging the gap between traditional finance and web3, and the promise of DeFi"
author: Defiprime
tags: ['Interview', 'VC-founded']
---
Philip on real-world assets tokenization, bridging the gap between traditional finance and web3, and the promise of DeFi.  

### Hello! What’s your background, and what are you working on?

Hey there, my name is Philip Stehlik, one of the co-founders and the CTO of [Centrifuge](https://centrifuge.io). We enable our users to bring off-chain, real-world assets into the Blockchain universe, tokenize them, use them as collateral for lending, and include them in other DeFi use-cases. Originally from Germany,  I lived in San Francisco for 12 years, started and built a couple of projects and Fintech companies over the years (including the FinTech pioneer and leader Taulia) from the first lines of code to achieving product-market fit. Now I am spending most of my time in Berlin, Germany, working with our team at Centrifuge.

I started exploring Bitcoin in 2013 while I was still CTO at [Taulia](https://taulia.com). Taulia is one of the largest business networks and providers of financing services for the Fortune 500 and, even more importantly, their suppliers. The platform is transacting many billions of USD worth of payments and transactions every month. I was fascinated about what a new trustless, decentralized currency could do for the world of enterprise financial services and how we could leverage it. We didn’t end up building anything on Bitcoin but in 2017 (I had left Taulia at that point) some of my previous co-founders and I started working with Ethereum to experiment what the possibilities are beyond simple value exchange and encode business logic, exchange business data on a trustless, decentralized, censorship-resistant platform, tokenize them, and build a whole new set of apps.

Centrifuge is a network to exchange business documents (think invoices and similar items) privately and securely while relying on a public blockchain for proof of authenticity and the tokenization of these documents.

Today, our users utilize Centrifuge for the tokenization, underwriting, and securitization of all kinds of documents (invoices, mortgages, other “contracts”, etc) to exchange their data in a provable, unalterable way, and finally provide financing. Examples for this are real estate loans, future streaming royalties for music, or again different kinds of invoices.

### What’s Centrifuge backstory?

My co-founders and I have been working in the space of the financial supply chain for many years — some of us at SAP in the ’90s. Then founding [Ebydos](https://www.crunchbase.com/organization/ebydos), working at [ReadSoft](https://en.wikipedia.org/wiki/ReadSoft) after the acquisition, last founding [Taulia](https://www.crunchbase.com/organization/taulia) and supporting other fintechs as advisors along the way where we could. We built, implemented, launched, supported, and sold financial software to the largest companies of the world many times over. When we came together in 2017 and envisioned “what’s next?”, the one thing that really excited us was the question: “Which platform would WE like to build our next products on? What would this platform look like in the future?”.

Over the years we often dealt with questions of “Who owns the data?”, “Can a user give us access to their financial data without paying licenses?”, “How can we provide service to smaller/marginalized businesses to support their growth, regardless of location or size?”. All backed by the most important question: “How can any business on this planet get their money faster, at fairer terms?”. Because “Cash is King”.

We wanted a platform where the users have agency over their own information but are unable to tamper with the data, once deposited or exchanged with others. We wanted a system where it becomes possible to prove document ownership and business relationships through a network of connected enterprises (we call it the “business graph” at Centrifuge). We wanted a way to make these documents assignable, tradeable, and, in the end, allow anyone to provide financing or other kinds of services for them.

In 2017 the ICO-hype was reaching its peak, but we decided to go the “old fashioned route” of raising venture capital and have sufficient time to build the “right product”. We raised a seed round of $3.5m in early 2018 from [Mosaic](https://www.mosaicventures.com/), [BlueYard](http://blueyard.com), and [Semantic](https://www.crunchbase.com/organization/semantic-ventures) (the folks who also write [Token Economy](https://tokeneconomy.co). This gave us a great basis to iterate on our idea and approach.

### What went into building the Centrifuge?

We started with the idea and first prototype in mid-2017 and decided on raising outside funding towards the end of the year. Having closed our funding in early 2018, we focused on building the initial version and growing our team. Along the way, we validated the first versions with large corporates like [BASF](https://www.icis.com/explore/resources/news/2019/04/25/10353437/insight-chemical-producers-and-their-customers-seek-smarter-network-connectivity-look-to-blockchain) and financial service providers like [Elemica](https://elemica.com/). We started the collaborations with the [Maker Foundation](https://medium.com/centrifuge/centrifuges-tinlake-goes-live-with-the-financing-of-more-than-usd180k-2cc6ce176a1b), and other crypto and DeFi projects. The integration into DeFi is a key component for us. Our first testnet was live in October 2018, and we launched on Ethereum mainnet in April 2019.

We pushed through “crypto winter” (or are we still in it right now?) and continued building and shipping. I think that was an important chapter for us. Having sufficient patience to focus on what’s most important - create a good, useful product.

Centrifuge is built with a [two-layer approach](https://medium.com/centrifuge/the-centrifuge-protocol-the-inner-workings-4fcbc9f7aa2f): There is the Centrifuge peer-to-peer network for private, secure data exchange. Then there are the contracts deployed on Ethereum that represent business identities, document hashes from our [precise proofs](https://medium.com/centrifuge/introducing-precise-proofs-create-validate-field-level-merkle-proofs-a31af9220df0), and most importantly the “Business NFTs” to represent documents and make them financeable via MakerDAO, Compound, or others. We also launched [Tinlake](https://medium.com/centrifuge/tinlake-bringing-individual-non-fungible-assets-to-defi-f5ff0c77cadd) recently, which allows the tokenization and pooling of those NFTs in an easy, standardized way.

![](/images/blog/centrifuge/image3.png)

The protocol and the smart contracts were audited earlier in 2019 by the great folks at Trail of Bits, and we do internal audits of our new code before publishing it widely. We do our best we can to create a safe and sound system.

Centrifuge bridges the gap between ”traditional finance” and “web3”. This is exciting - because we unlock previously inaccessible value and bring it to DeFi.

On/off-ramps are crucial for our users. However, this is still an area where it is not easy for an SMB (Small Medium Business) to quickly transfer tens of thousands of Euros into a stable coin and back with very low fees. We are working on ways around those current limitations, but this is not a solved problem. Fees are high - when financing an invoice, even half a percent-point in fees for on/off-ramp can kill a business case.

Onboarding is slow - when a business needs financing, they don’t want to go through a 5-day KYC process to then figure out how to connect their bank account and move money in/out within another two days.

To counter those slow processing times, there are currently some centralized portions of our products that we hope to decentralize more in the future to create a level playing field for everyone in our ecosystem.

### What’s your business model?

The main goal of Centrifuge is to make financial services, like access to financing, insurance, and others, accessible for businesses all around the world. We set out to create a financial system that is inclusive and has a lower barrier to entry than the existing one. The Centrifuge network is the entry point for all off-chain, real-world assets into the Blockchain universe. While we are currently live on Ethereum, we are also launching a purpose-built blockchain, Centrifuge Chain, in early 2020. This chain is incentivizing participants to secure the network through a token-model similar to other POS chains.

Centrifuge Network Foundation holds a number of tokens that it can use to further the development of the network. Centrifuge “the company” will then apply for grants to finance the development just like any other contributor. Currently, we are well funded by private and [public](https://medium.com/centrifuge/berlin-and-the-eu-support-building-the-centrifuge-chain-with-1-4-million-18636a81975c) investors to finalize the chain to launch and expand the network.

We also developed [Tinlake](https://tinlake.com/), a set of contracts and tools to tokenize real-world assets, bundle, underwrite, and bring them into the broader DeFi ecosystem. Our team works with a number of asset originators as well as underwriters who use Tinlake. When collaborating with them, we take an as neutral stance as possible, to assure the best level playing field as possible for all our users while at the same time financially align the incentives for the projects.

![](/images/blog/centrifuge/image2.jpg)

### What’s your position on the regulatory landscape today?

We are at the intersection of the real-world and on-chain DeFi products. This area is ripe for innovation while also dealing with lots of existing regulation of financial products. Together with our partners, like Maker Foundation and others, we are devising legal frameworks that allow us to operate adequately while also pushing forward to continue delivering new products and supporting new use-cases. It is not always a simple task to get legal clarity. However, we believe that operating within the law is the best way to guarantee the success of our network and our user’s projects.

On the other hand, some DeFi proponents are holding the opinion that real-world assets are not suited well for DeFi. We think they are, even if they might not be 100% trustless. You can read more about that in a [recent post]((https://medium.com/centrifuge/defi-and-the-real-world-a-trust-issue-46f105eebe92?source=collection_home---4------3-----------------------)) of my co-founder Lucas Vogelsang

### What are your goals for the future?

The main focus for us is to further the footprint of Tinlake. This means we work with asset originators like e-invoicing networks, real-estate lenders, and other online platforms whose users are looking for access to capital. We are close to ten different asset types being financed through Tinlake today with a few hundred thousands of value. We are aiming to bring that to a steady state of millions of USD being financed in the coming months. Eventually, getting to a scale that is mirroring our success at Taulia, the previous company we created, financing billions of USD each month to achieve that, we are working with DeFi projects as well as traditional lenders who want to tap into the new asset pools that open up and enter the blockchain lending space. Currently relevant is the launch of Multi Collateral DAI (MCD) - we are aiming to bring [real-world assets to MCD](https://medium.com/centrifuge/centrifuge-tinlake-adding-real-world-assets-to-mcd-68cbcb67e9a4) shortly after launch

The other focus area is to set up Centrifuge Chain for a smooth and successful launch in the coming months. There we work with firms who run validators on other networks as well as our existing partners who use Centrifuge on Ethereum today to tokenize assets. We received grants from the European Union, the city of Berlin, as well as Web3 Foundation to support our work there. The team is focused on launching our public beta network before the end of the year.

### What are your future thoughts for the DeFi market?

Our founding team worked in Fintech (of CeFi as some call it now) for many years. Our previous companies and products finance billions of USD worth of transactions every quarter for the largest companies on this planet. We built products for the financial supply chain that have never existed before. Yet, all the data, transaction history, and network information are locked into single vendors and platforms. Nobody can innovate on this information or offer new services freely - not even the users themselves. We also fell short on providing accessible financial services to smaller firms around the globe. The overhead was too significant. There are too many incompatible platforms, silos, and stakeholders holding their users and data hostage.

DeFi is not the silver bullet for all problems in the financial world or the financial supply chain as it has evolved over many years. However, the promise of composability, choice, and open systems of DeFi is a reality today already. We strongly believe this openness and composability will accelerate the pace of innovation in the coming years. This will allow DeFi to outpace, replace, and out-innovate the incumbent players and platforms. There is lots of work to be done in regards to legislation, privacy, and scalability, but the first steps are done, and there is no way to put the cat back into the bag. An unstoppable wave is building and swelling. The question for us is who has the strength, adaptability, and longevity to be around when we can ride that wave together.

### Where can we go to learn more?

- [Twitter](https://twitter.com/centrifuge)
- [Centrifuge.io](https://centrifuge.io)
- [Tinlake.com](https://tinlake.com)
- [Tinlake public demo](https://kovan.demo.tinlake.centrifuge.io)
- [Medium](https://medium.com/centrifuge)
