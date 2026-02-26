---
git-date: 2020-01-08T10:06:04+00:00
layout: blog
title: Crypto Loans Without Collateral
url: crypto-loans-without-collateral
h1title: "Unsecured DeFi loans: an overview"
pagetitle: "Unsecured DeFi loans: an overview. Crypto Loans Without Collateral"
metadescription: "Ethereum ecosystem is already looking to build new financial services for as many people as possible — and in DeFi, that implies unsecured loans"
category: blog
featured-image: /images/blog/loans-without-collateral-og.png
quote: /images/blog/loans-without-collateral-quote.png
intro: "Ethereum ecosystem is already looking to build new financial services for as many people as possible — and in DeFi, that implies unsecured loans"
author: masmej
tags: ['DeFi Guides', 'Lending', 'NFTs']
---

In the past months, there’s been an uptick in interest for #DeFi beyond margin trading, popularized by Compound, Maker Vaults, and InstaDapp. To start 2020 with the same innovation speed, the Ethereum ecosystem is already looking to build new financial services for as many people as possible — and in DeFi, that implies unsecured loans.

Disclaimer: most of the feasible solutions in Under-collateralized DeFi are solutions for cryptonative users. The myth of “bank the unbanked as the first use case” will die off, as builders usually build products for their own (or a similar demographic). Plus, it is easy to comprehend that even in first world countries, there is a huge market for unsecured loans.

#### Learning from a small scale Crypto Twitter survey

Two weeks ago, I sent out [a tweet](https://twitter.com/AlexMasmej/status/1210252111373635584?s=20) asking to chat with people wanting a loan without collateral. I received 30 DMs, then my friend [Daniel](https://twitter.com/onggunhao) helped me out & we sent out a form, receiving 30 replies. Including overlap, I guess we gathered wisdom on around 50 cryptonatives, all wanting to experience an unsecured loan outside of traditional finance. Here are some findings from my survey:

*   The average loan asked is $4,000, loaned for a year at a 7.5% interest rate. A simple calculation indicates that in principle, people are ready “pay” on average $300 for such a service.
*   Reasons range from financing crypto projects (which makes sense, as most aren’t profitable enough and widely seen as “too early” by venture capitalists), to investing, car loans, repay Maker Vaults, repay a higher-interest-rate bank loan, and even completing a Master’s degree!
*   Half of the respondents claim to have not consulted a bank before, either because the amount is too low to both asking, or because the rate would be too high to even consider.
*   In terms of underwriting, there was many innovative, non-financial ways people found trying to convince to lend them some funds. We can categorize them in two types: the first was all sorts of NFTs, such as ENS domains, valuable crypto art or game collectibles, backed by value, and easy to put into an escrow account. The second one revolved around identity or what I call “proof of trustworthiness”: a 3Box profile, a grant from the Maker Foundation, DAO membership, a profitable Gitcoin developer account, book author account. All of those are subjective, but highly suggest that unless an unfortunate turn of events, that person is real and able to make enough money to repay.
*   People want loans in stablecoins, but that shouldn’t come as a surprise.

This was a neat way of gauging, and we hope to fund a few of those, although it would partly be based on web-of-trust rather than a cold genuine conviction about a candidate, because I have at least second-degree connections with some of the strongest candidates. The small sample size is also suspect of overfitting, as most cryptonatives probably do not have a valuable NFT to give out, for instance.

One big concern regarding this new unsecured loan market is that the [TAM](https://en.wikipedia.org/wiki/Total_addressable_market) for unsecured loans within #DeFi seems small beyond speculation for now. All loans are implicitly fiat loans, the only ones in crypto are to do investing, which margin trading already allows for the most part. Will the fiat offboard be OK for borrowers, even if it implies they are charged a fee for both receiving and paying back the money? (only 15% were paid in crypto, so this is a too small market, although [Sablier](https://www.sablier.finance/) could help).

### Crypto Loans Without Collateral

These uncertainties did not stop projects to launch, whether longtime in the making or newly arrived in the cryptosphere. Here are five that I’m interested in:

#### Union Protocol: a Credit DAO for cryptonatives

[Union](https://medium.com/primeradiant/a-credit-union-called-union-521358a995cc), a primitive built by seasoned DeFi founders including MetaMoneyMarket’s Jacob Shiach, aims to build a DAO-like credit union. Its goal is to have people pool DAI and lend it out to some configurable risk-profiles and collateralization ratio called “Credit Vehicles.” Sleeping DAI is lent on Compound, and _UnionTokens_ are distributed to stakers to share potential dividends.

This approach is great, and I’m curious to see it go live. Once the code is pushed to Ethereum, most of the work would be to convince lenders that this beats Compound rates, which can be a daunting task.

#### Centrifuge Tinlake: tokenize traditional assets as crypto collateral

[Centrifuge](https://centrifuge.io/) is an interesting project: on a mission to connect the global (traditional) financial supply chain to crypto, they’re partnering with the likes of Maker to tokenize existing assets into NFTs, guaranteeing authenticity then dividing them into fungible “Collateral Value Tokens,” then redeemable for stablecoins on Maker or Compound. [More on their website](https://tinlake.com/).

![](/images/blog/centrifuge/image3.png)
_Tinlake approach: making turning traditional assets, like business invoices, into NFTs._

#### Zero Collateral

Released out of nowhere in the past week, [this project](https://medium.com/fabrx-blockchain/meet-zero-collateral-dcfe27fb3a2d) aims to achieve Zero Collateral loans by gradually reducing the collateral amount proportionally to the borrower’s repaid interest rates. Put in simpler terms, every time you successfully repay a loan, the next loan will be more attractive. That way, running away with the money is never at a loss on the lenders’ side, since they got paid out via past interests regardless. And the defaulters will have to go back to the starting interest rates. This mechanism incentivizes repayments all the way until giving out fully undercollaterization. Bonus point to the team for thinking ahead and anticipating future Web 2 collaborations with credit scoring websites, such as Credit Karma, to further evaluate a borrower’s solvability.

To protect themselves from abusers, lending rates seem really high to start with, though. Let’s see if there’s demand. They’re currently [on testnet here](https://zerocollateral.com/).

#### The NFT Bank & the #UndercollaterizedDeFi experiments

As a first experiment, a team was gathered from the #UndercollaterizedDeFi Discord & Telegram channels I created three weeks ago. Details TBA, but we want to build a case-by-case basis escrow system that locks up any NFTs. DAI is then sent. It’s the MVP, fast experimentation approach that accelerates learnings and collects feedback based on as much data as we can. We are having weekly calls, and if you’re keen to code up some smart contracts, feel free to [DM](https://twitter.com/alexmasmej)!

#### The alternative: humans as collateral with social tokens

With the likes of [Pepo](https://pepo.com/) and [Roll](https://tryroll.com), creators are more and more susceptible of making money without intermediaries. Social tokens are interesting: people in crypto such as Camila Russo, DeFi Dude, and myself released their own personal token! For instance, you can buy $CAMI to both (1) get some pre-planned service or time slot, like a Twitter shoutout or office hours, or (2) speculate on Camila Russo future success on different #DeFi platform. A Uniswap frontend is coming soon for Roll!

In conclusion, it’s safe to say that this industry is extremely early and risky. As stablecoins have barely crossed the chasm, this time seems perfect to try out all sorts of experiments. Who knows, perhaps some of the learnings today will be key competitive advantages in the next few years.
