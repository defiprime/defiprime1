---
git-date:
layout: [blog]
title: "Crypto Debit Cards in 2026: The Real Numbers, the Real Risks, and What a $607M Month Actually Means"
permalink: crypto-debit-cards-2026
h1title: "Crypto Debit Cards in 2026: The Real Numbers and the Real Risks"
pagetitle: "Crypto Debit Cards in 2026: The Real Numbers, the Real Risks, and What a $607M Month Actually Means"
metadescription: "Crypto card volume hit $607M in March 2026. A deep look at how it's measured, who actually uses these cards, the regulatory walls closing in, and which programs are living on borrowed time."
category: blog
featured-image: /images/blog/crypto-debit-cards-2026-ogp.png
intro: "Crypto card volume hit $607M in March 2026. A deep look at how it's measured, who actually uses these cards, the regulatory walls closing in, and which programs are living on borrowed time."
author: sawinyh
tags: ["Analysis", "Payments", "Stablecoins"]
---

The crypto card market hit [$607 million in monthly volume](https://www.coingabbar.com/en/crypto-currency-news/crypto-card-usage-hits-record-607-million-in-march-2026) for March 2026, according to Paymentscan data. A year prior, that number was $187 million. Eighteen months before that, roughly $100 million. We're looking at 6x growth in a year and a half, with $6.5 billion in cumulative spending across more than 21 million transactions.

Those are the headline numbers. They're real. But they also obscure as much as they reveal, and this article is about what's actually happening underneath them.

I've been using the March 2026 leaderboard from Obchakevich Research as a starting point, the most granular on-chain dataset we have for this market. But the dataset itself has limitations that change how you should interpret almost every number I'm about to cite. So let's start there.

## How volume is measured (and why it matters more than you think)

Obchakevich Research runs a [public Dune Analytics dashboard](https://dune.com/obchakevich/crypto-cards-all-chains) tracking on-chain activity for 14 crypto card programs. The data splits into two categories depending on card architecture, and this distinction is more important than the rankings themselves.

For non-custodial cards (ether.fi Cash, Cypher, MetaMask, Avici, ExaApp, Moonwell, kardpay), the dashboard tracks **spend volume**: actual card payment transactions visible on-chain. For custodial cards (RedotPay, Kolo), it tracks **deposits flow volume**: crypto moving into the card provider's wallets. Those are fundamentally different things.

When RedotPay shows $283.9M in monthly volume, that's stablecoins deposited into their app. Not all of it gets spent in the same month. Some sits idle. Some gets withdrawn. Some funds future purchases. When ether.fi Cash shows $47.8M, that's closer to actual card-level spending because vault-to-card transactions settle through observable smart contracts. Obchakevich is upfront about this, noting the analysis "does not show the full status and volume of crypto cards on the market."

There's also a $230M gap between the $607M Paymentscan total and the $377M tracked across Obchakevich's 14 cards. Where does it go? Mostly to programs that don't produce on-chain footprints: Crypto.com, Binance, Coinbase, Bybit, Wirex, and other CEX-issued cards that process everything off-chain. Those programs likely represent a significant share of actual global card spend, but they're invisible to on-chain analytics.

Bottom line: the leaderboard is the best data we have, but it's comparing deposit flows against spend volumes, and it's missing the largest card programs entirely. Treat the rankings as directional, not definitive.

## Who actually uses crypto cards (and why it matters for picking winners)

Before the card-by-card breakdown, it's worth mapping out who these products are actually for. The "crypto card user" is not one person. There are at least four distinct segments, and each one gravitates toward a different product model.

**Stablecoin pragmatists** are the largest group by volume. They hold USDT or USDC, often as a primary savings vehicle in regions with weak local currencies, and they want a simple way to spend it. They don't care about self-custody, DeFi composability, or governance tokens. They want a card that works at the grocery store and the airport. RedotPay and Kolo own this segment.

**DeFi-native holders** have significant ETH, staked ETH, or DeFi positions, and they don't want to sell to spend. They want yield until the moment of purchase, tax-efficient spending structures, and cashback that compounds on-chain. ether.fi Cash and, to a lesser extent, Avici and ExaApp serve this group.

**Exchange-first traders** already live inside a CEX app. The card is a feature, not a product. When Bitget or MetaMask adds a card, it's a zero-friction extension of an existing relationship. Convenience and ecosystem lock-in drive adoption, not card-specific features.

**Privacy-conscious spenders** want virtual prepaid cards, minimal KYC, and no connection between their on-chain identity and their spending. kardpay targets this group directly. It's small but growing at 208% YoY.

These segments have different risk tolerances, different geographic distributions, and different feature priorities. A card optimized for Telegram-heavy emerging markets (Kolo) isn't competing with a DeFi credit card (ether.fi). Treating them as a single market produces misleading comparisons.

But there's a fifth segment that no crypto card company will acknowledge publicly, and it may be the single biggest reason this market is growing as fast as it is.

## The demand driver nobody will say out loud

Let's be direct: a significant share of crypto card volume exists because these cards make it easy to spend money without generating the tax reporting trail that a traditional bank card produces. That's not a bug. For many users, it's the feature.

The IRS treats every crypto-to-fiat conversion as a taxable disposition. When you swipe a crypto card at a coffee shop, you've technically realized a gain or loss on the stablecoins you spent. If those stablecoins had any cost basis difference from the fiat amount, which they almost always do when FX movements and conversion spreads are factored in, you owe taxes on the difference. Every single transaction. Now multiply that by the 21.4 million transactions processed across this market.

How many of those are being reported? We have some data. An IRS internal review from 2023 found the potential for only about [25% voluntary compliance](https://www.cnn.com/2025/11/14/business/taxes-crypto-irs-form-1099-da) among crypto investors. Awaken Tax founder Andrew Duca put it more bluntly in a [February 2026 CoinDesk interview](https://www.coindesk.com/business/2026/02/18/american-crypto-holders-are-scared-and-confused-about-this-year-s-new-irs-tax-rules): under 20% of crypto holders report what they ought to. A [CoinTracker/Coinbase survey](https://www.cointracker.io/2026-crypto-tax-report) of 3,000 US crypto users published in April 2026 found 65% had previously reported crypto on their taxes, but that's a self-selected population of Coinbase users who opted into a tax compliance survey, about as representative as asking gym members whether they exercise.

And those numbers cover crypto broadly, meaning mainly exchange-based trading where there's at least some paper trail. Crypto card spending is structurally harder to track. Transactions happen at the point of sale through offshore issuers that don't file 1099-DAs with the IRS. Individual stablecoin-to-fiat conversions generate tiny gains or losses that are tedious to calculate per swipe. And a large share of users are in jurisdictions that either don't tax crypto-to-fiat spending or don't have the infrastructure to enforce it. If general crypto compliance sits at 20-25%, card-specific compliance is almost certainly lower.

For the stablecoin pragmatist segment, especially in emerging markets, the appeal isn't just "spend USDT at a store." It's "spend USDT at a store and none of this shows up on a bank statement, a 1099, or a tax authority's radar." In jurisdictions with capital controls, unstable currencies, or aggressive tax regimes, a card that converts stablecoins to local fiat at the point of sale is effectively an unregulated off-ramp. RedotPay's 6 million users across 100+ countries aren't all crypto enthusiasts. Many of them are people who found a way to move dollars around without going through their local banking system.

In the US, the same dynamic plays out differently. Form 1099-DA, the IRS's new digital asset reporting form, became mandatory for brokers starting January 1, 2025, with cost basis reporting phasing in for 2026 transactions. Custodial exchanges now report gross proceeds to the IRS. But here's the gap: crypto card issuers that operate offshore and don't qualify as US brokers may not file 1099-DAs at all. A RedotPay card funded by USDT from a non-custodial wallet, used to buy groceries in Miami, currently sits in a reporting gray zone. The user owes taxes. The IRS just has limited visibility into the transaction.

DeFi-native cards add another layer. Congress repealed the DeFi broker reporting rule, meaning non-custodial protocols aren't required to file 1099-DAs. When you spend through ether.fi's Borrow Mode, you're technically not even disposing of crypto. You're borrowing against it. That's not a taxable event under current IRS guidance. The tax efficiency of "spend without selling" isn't just a convenience for ETH maximalists. It's a structural tax arbitrage that saves real money for anyone with appreciated crypto holdings.

None of this is illegal per se. Tax obligations exist whether or not a form is filed. But the enforcement gap between "you owe this" and "the IRS can see this" is wide, and crypto cards live right inside it.

The global picture complicates the story, though. The US and EU are tightening fast, but most of RedotPay's 6 million users aren't in the US or EU. They're in Southeast Asia, LATAM, Africa, and the CIS, and the tax enforcement reality in those regions looks nothing like the US or EU.

Vietnam, ranked among the world's highest in crypto adoption, had no specific crypto tax law until its Law on Digital Technology Industry took effect January 2026. Even now, enforcement infrastructure barely exists. The Philippines taxes crypto gains under general income tax rules, but the Bureau of Internal Revenue only introduced crypto-specific reporting forms in 2026 and won't join the OECD's cross-border CARF data exchange until 2028. Thailand approved a five-year capital gains tax exemption for crypto sold through licensed platforms, running through 2029, effectively making compliant crypto spending tax-free. Nigeria enacted new crypto tax law in mid-2025 with rates up to 25% on digital asset gains, but stablecoins function as the primary savings vehicle for millions of Nigerians escaping naira inflation, and P2P habits built during the 2021-2023 banking ban still dominate over formal exchange use. Brazil requires reporting on crypto sales above BRL 30,000/month and is phasing in a VASP authorization regime through 2026, but 90% of its crypto activity is stablecoin-related according to the central bank, much of it in cross-border corridors that remain hard to trace.

The pattern across these markets: the laws are formalizing, but enforcement lags years behind legislation, and stablecoin spending at the point of sale through an offshore card sits in a gray zone that most tax authorities don't yet have the tools or mandate to monitor. CARF will eventually create cross-border information sharing, but the first wave of 48 countries only started in January 2026, and the markets where crypto card adoption is highest (Philippines, Vietnam, Nigeria) are in the second wave, scheduled for 2027-2028.

This changes the answer to "how much volume disappears when rules are enforced." In the US and EU, the impact is likely real and near-term: 1099-DA reporting, MiCA enforcement, and GENIUS Act compliance will close the gap within 12-18 months. In the emerging markets where most stablecoin card spending actually happens, the gap will persist for years. The regulatory tightening is global in direction but deeply uneven in timing. That unevenness is where the volume lives.

The GENIUS Act requires permitted stablecoin issuers to comply with Bank Secrecy Act obligations and maintain AML/sanctions programs. The OECD's CARF and the EU's DAC8 both went into operational implementation on January 1, 2026, creating the first cross-border information-sharing frameworks for crypto transactions. The IRS is receiving 1099-DAs from custodial brokers for the first time. These are real developments. But they primarily affect the US and EU, which are probably not where most of the $607M in monthly volume originates.

What happens to crypto card volumes as enforcement spreads? In the US and EU, some volume shifts to more compliant channels or disappears. In emerging markets, the cards keep working as they do today, probably for years. The net effect on global volume may be smaller than the regulatory headlines suggest, at least in the medium term.

This doesn't make crypto cards a fraud. Stablecoin spending has real utility independent of tax avoidance. But pretending that tax opacity isn't a demand driver is like reviewing a privacy coin and never mentioning why people want privacy. The honest analysis has to account for it.

## How these cards are actually built (and why some limits are red flags)

Most crypto card analysis focuses on the consumer-facing product: cashback rates, supported tokens, Apple Pay. Almost nobody asks how the card program itself was set up, what type of card it actually is, or why a card marketed to individuals has limits that no individual card should have.

There are two supply-side tricks worth understanding because they explain a lot of what you see on the leaderboard. (This framework draws on [a detailed breakdown by Wirex CEO Pavel Matveev](https://x.com/matveevp/status/2020779293513502816), who has built crypto card infrastructure since 2014. He has a competitive interest in calling out non-compliant programs, but the structural observations are independently verifiable.)

**The gift card repackage.** Visa and Mastercard both offer [single-load prepaid gift cards](https://www.visa.com/en-us/personal/cards/prepaid), mostly US-issued. Load once, spend until the balance runs out, done. The user experience is bad: most merchants won't accept them, you can rarely spend the full balance, and whatever's left gets eaten by inactivity fees. But distributors figured out that if you accept crypto and stablecoins as the funding method and market the product as a "privacy-focused no-KYC card," you can charge 3-7% on the top-up. The issuing bank collects another 3-5% on unspent balances through breakage and inactivity fees. That leftover balance isn't a bug. It's the business model. When you see a "virtual prepaid card" with sky-high cashback rates and minimal identity requirements, this is often what's underneath.

**The corporate card disguised as a consumer card.** This one is more sophisticated and more relevant to the leaderboard. Corporate card programs are built differently from consumer programs: higher interchange rates (the highest possible on credit), flexible global distribution designed for traveling employees, and limits sized for companies, not people.

The scheme works like this: an issuer obtains a corporate card program in an offshore jurisdiction, Puerto Rico, Hong Kong, or similar. Intermediaries then repackage those corporate cards as low-KYC consumer products. Users get cards with no travel rule checks, no proof of address, no enhanced due diligence, and limits that make no sense for a retail cardholder. Visa does not approve $1M monthly limits for individual consumers. If a crypto card is advertising that kind of limit to retail users, it's almost certainly running a corporate program underneath.

The revenue model is stacking: card issuance fees paid by users happy to get low-friction access, elevated interchange from the corporate classification, and 2-4% FX conversion on every non-dollar transaction because these programs typically settle only in USD.

These programs have a consistent lifecycle. They launch fast, grow fast, and die fast. Card networks and regulators eventually catch up. The shutdown is always abrupt, often with balances frozen mid-spend. If you're using a card, or building on top of one, and you can't answer the question "what type of card program is this actually running?", you're accepting a risk you can't size.

## RedotPay: dominant, custodial, and facing fee pressure

RedotPay posted $283.9M in monthly volume (deposits flow) for March, representing 75.26% of the tracked leaderboard. The Hong Kong-based company [raised $107M in its Series B](https://www.redotpay.com/news/redotpay-raises-us107m-in-series-b-to-drive-stablecoin-payments-adoption-globally) in December 2025, led by Goodwater Capital with participation from Pantera, Blockchain Capital, and Circle Ventures. By late 2025 they reported 6 million registered users and a $10B annualized payment volume. They also recently launched a Solana card in February 2026 to capture SOL-ecosystem spending.

Behind the scenes, Singapore-based StraitsX acts as RedotPay's Visa BIN sponsor. StraitsX saw card transaction volume [surge 40x between Q4 2024 and Q4 2025](https://www.coindesk.com/business/2026/03/29/stablecoin-payments-go-invisible-in-southeast-asia-as-crypto-card-business-surges), with card issuance growing 83x. The infrastructure is scaling fast. But it's worth understanding what "BIN sponsor" means here: RedotPay doesn't have its own direct relationship with Visa. StraitsX sits in between, issuing cards on RedotPay's behalf. That adds a dependency layer and a potential point of failure.

The alternative model is full-stack issuance, and the biggest player there is Rain. Rain holds direct Visa principal membership, meaning it settles directly to the network without needing a BIN sponsor. It [raised $250M in a January 2026 Series C](https://insights4vc.substack.com/p/the-state-of-stablecoin-cards) led by ICONIQ at a $1.95B valuation, on top of a $58M Series B in August 2025. It powers cards for 200+ partners across 150+ jurisdictions, with Visa itself as a strategic investor and design partner for stablecoin settlement pilots. Rain doesn't appear on the Obchakevich leaderboard because it's infrastructure, not a consumer card. But it processed over $3B in annualized volume by late 2025, reportedly scaling 38x during the year.

The distinction matters because it defines who controls the economics. In the StraitsX model, RedotPay captures the consumer relationship but depends on StraitsX for card issuance, settlement, and compliance. If StraitsX tightens terms or loses its Visa relationship, RedotPay has a problem. In Rain's model, the infrastructure provider owns the full stack, capturing interchange, FX spread, and reserve yield directly, then letting partners (wallets, fintechs, exchanges) white-label on top. GnosisPay takes yet another approach, building self-custodial card infrastructure on Gnosis Chain for partners to deploy.

Wirex BaaS represents a fourth model worth watching. Wirex claims $105M in on-chain card volume for March 2026 alone, with 2.4M on-chain transactions since launching to production in November 2025 and 300 partners building on its API. The data is publicly verifiable at [paymentscan.xyz](https://paymentscan.xyz/issuers/wirex). What distinguishes Wirex's pitch from Rain's is multi-currency stablecoin settlement: Wirex settles in both USDC and EURC with Visa, which it says is unique in the market. For European partners, that eliminates the 2-3% FX conversion cost that USD-only settlement programs pass to users on every euro transaction. The claimed average time from signing to live is 44 days, compared to the 6-12 month timelines partners report from other providers. If those numbers hold, Wirex is competing on speed-to-market and European economics rather than pure scale.

Four competing infrastructure theses, each with different economics and different regulatory exposure. The consumer cards on leaderboards are the visible layer. The infrastructure underneath is where the real market is being decided.

The product model is simple: load stablecoins, spend via Visa at 130M+ merchants, auto-convert at the point of sale. But the fee structure tells a more nuanced story. RedotPay charges 1% on every crypto-to-fiat conversion, 1.2% FX markup on non-USD transactions, $100 for a physical card ($10 virtual), and 2-3% on ATM withdrawals. Those stack. A foreign ATM withdrawal can cost 3.2% total. And the custodial model means your stablecoins sit in their app, not your wallet.

For someone spending $2,000/month in USD-denominated transactions, the 1% conversion is $20, roughly comparable to what a traditional debit card costs in hidden interchange. But scale that to $10,000/month with some international travel, and you're looking at $150-200/month in fees, before counting ATM withdrawals.

RedotPay's dominance confirms a thesis that should be obvious but often gets lost in DeFi discourse: most of the world's stablecoin users don't care about self-custody. They want reliability, reach, and simplicity. RedotPay delivers that. But as the market matures, fee competition will intensify. When someone builds a comparable product at 0.5% conversion and 0% FX, RedotPay's stickiness will be tested.

The bigger question is regulatory. Hong Kong passed its Stablecoins Ordinance in May 2025, with the first licenses expected around March 2026. RedotPay's positioning in that jurisdiction gives it a compliance runway, but access to the US market under GENIUS Act rules and the EU under MiCA is far from guaranteed.

And then there's the limits question, which connects directly to the supply-side analysis above. [RedotPay's own help center](https://redotpay.zendesk.com/hc/en-us/articles/9720619307663-Rules-for-physical-cards-and-virtual-cards) confirms: the USD BIN allows up to $100,000 per transaction, with no stated daily spending cap ([multiple](https://sweepbase.net/cards/redotpay-card) [sources](https://www.bleap.finance/en-us/blog/bleap-vs-redotpay-full-crypto-cards-comparison) cite $1,000,000/day). The HKD BIN allows up to 800,000 HKD per transaction. Physical cards support $50,000/month in ATM withdrawals. Compare that to the standard retail prepaid Visa market: [NetSpend's prepaid Visa](https://www.cardrates.com/advice/best-no-limit-high-limit-prepaid-debit-cards/), one of the largest US consumer programs, caps daily spending at $4,999 with a $15,000 maximum balance. Typical bank-issued prepaid cards in the US sit at $2,500/day. That's a 200x gap between what a normal retail prepaid card allows and what RedotPay offers to individual users who completed basic KYC.

Visa does not approve $100,000 per-transaction limits for standard retail prepaid programs. That limit structure, combined with the HK-issued BIN, the minimal onboarding requirements [reported by multiple reviewers](https://cryptoslate.com/crypto-cards/redotpay-card-review/) (proof of identity only, no proof of address, no enhanced due diligence), and the absence of travel rule checks, looks structurally consistent with a corporate or commercial card program repackaged for individual consumers. I can't confirm that definitively from public sources, but the numbers don't fit any retail prepaid framework I'm aware of. If you're using RedotPay, it's worth understanding that the limits you're enjoying may be the same feature that eventually draws regulatory attention.

## ether.fi Cash: the DeFi card, risks first

ether.fi Cash sits at $47.8M monthly spend volume, 12.67% share, with 42.7% YoY growth. The product has two modes: Direct Pay (draw from USDC/eETH in your vault, earn staking yield until the moment of purchase) and Borrow Mode (stake ETH as collateral, ether.fi borrows USDC on your behalf, your ETH never moves). Cashback is paid in wETH at 2-3% depending on tier. For US holders, Borrow Mode avoids triggering a taxable sale, which is a real structural advantage.

That's the pitch. Here's what can go wrong.

**Liquidation risk.** In Borrow Mode, if ETH drops hard enough that your collateral ratio breaches the threshold, your position gets liquidated. Forced sale, worst possible time. The card is built on lending mechanics, and lending mechanics have teeth.

**Smart contract risk.** The architecture runs on Gnosis Safe smart contracts settling on Scroll L2. The ByBit breach in 2025, a $1.5 billion loss, was executed through a Safe{Wallet} compromise, the same framework ether.fi relies on. Different implementation, same attack surface category.

**The 0% borrow rate is a promotion, not a feature.** Expected to expire Q2 2026, reverting to the floating Aave market rate. If the promo is what's driving the 42.7% growth, the numbers may look very different by Q3.

**Transparency concerns.** ether.fi started as a liquid staking protocol and pivoted aggressively into payments. The Cash card is technically issued by a separate entity from the protocol, but the branding conflates them. The team has leaned heavily on promotional cashback campaigns and referral bonuses to drive adoption, which raises the question of how much of the current volume is organic versus subsidized. When the subsidies stop, we'll find out.

## The mid-tier: real signals in small numbers

The middle of the leaderboard is where things get analytically thin. Volumes are small enough that a single whale or promotional campaign can swing percentages dramatically. But there are real signals in the noise.

**Cypher** ($13.3M monthly, -41.9% growth) runs a multi-chain wallet with a zero-fee USDC Visa card supporting EVM and Cosmos chains. The non-custodial design and free virtual cards positioned it well early on, but the negative growth rate demands an explanation nobody's providing publicly. Is this product-market fit failure, or is ether.fi eating the non-custodial card segment? The feature set looks fine on paper: Apple/Google Pay, cross-chain top-ups, 100M+ merchant acceptance. But features without distribution lose to distribution without features. Cypher doesn't have an exchange behind it, a major protocol driving traffic, or a Telegram bot onboarding users in emerging markets. That may be the whole problem.

**GnosisPay** ($6.8M monthly, -37.2% growth) is the odd card on this list because it's really infrastructure, not a consumer product. Wallets and apps use it to issue branded self-custodial Visa cards on Gnosis Chain. The declining volume might not reflect user demand at all; it could reflect the timing of partner launches or the loss of a B2B client. The 1-4% cashback in GNO ties rewards to a relatively illiquid governance token, a drawback for anyone who doesn't want more GNO exposure. Worth watching for the white-label model, not for the consumer metrics.

**Ready** (formerly Argent, $6.0M monthly, +82.2% growth) is the most interesting mid-tier card because of what it's not. It's not DeFi-native. It's not non-custodial. It's a Mastercard with fiat deposits, USDC spending, no FX fees, and 3% cashback. In other words, it's a neobank that happens to run on stablecoin rails. The 82.2% growth suggests there's a meaningful user segment that wants crypto-rail economics (lower fees, faster settlement) without any of the crypto UX. If Ready maintains this trajectory, it may prove that the winning crypto card for mass adoption is the one that doesn't feel like crypto at all.

**Kolo** ($5.7M monthly, +44.6% MoM) is one of only two cards on the leaderboard showing positive month-over-month growth. USDT funding, BTC cashback (2-5%), Telegram integration. That combination is almost perfectly optimized for Southeast Asian and CIS markets where Telegram is the default messaging layer and USDT is the default dollar substitute. The positive MoM in a month where nearly every other card declined says something real about geographic-specific product-market fit.

**MetaMask Card** ($4.8M monthly, -21.7% growth) launched with MetaMask's tens of millions of installed wallets as a built-in distribution channel. It hasn't translated. The virtual card starts at 1% cashback, the $199/year Metal tier offers 3%. But MetaMask's "sell to spend" model requires converting crypto at the point of sale, which is both a taxable event and a less attractive proposition now that collateral-backed alternatives exist. Brand alone isn't enough when the underlying mechanics are commoditized.

## Fast risers from small bases

**Avici** (+575.8% YoY, $3.4M monthly) offers a crypto-collateralized Visa credit card with category-specific cashback. The growth rate grabs attention, but at $3.4M monthly, a single promotional partnership could explain most of the move. The collateral-backed model (spend without selling, similar to ether.fi) is clearly resonating as a category, even if Avici's individual traction is still early.

**Bitget Wallet Card** (+233.9%, $3.0M monthly) confirms that exchange-wallet integration is a real distribution channel. When the card lives inside the app where you already trade and hold assets, activation friction drops to near zero.

**kardpay** (+208%, $193K monthly) is the privacy play: virtual prepaid cards with up to 8% cashback and minimal identity footprint. The volume is negligible, but the growth rate signals unmet demand for card products that don't require full KYC. It's also worth asking where that 8% cashback comes from. If kardpay is running a single-load gift card model, the real revenue is breakage: users rarely spend their full balance, and the issuer collects the remainder through inactivity fees. The cashback is funded by the money you're going to lose anyway. As regulations tighten globally, this niche either gets squeezed out or becomes more valuable. Probably both, depending on jurisdiction.

The bottom of the leaderboard rounds out with four cards too small to analyze individually but worth noting for what they represent. **Exodus** ($1.3M monthly, +0.9% growth) is a wallet-native Mastercard that extends spending to Exodus's large self-custody user base, functional but flat. **ExaApp** ($706K monthly, -25.1% growth) offers a Visa Signature card linked to Exactly Protocol where users borrow against crypto collateral for BNPL-style installments, interesting mechanics but declining traction. **Moonwell** ($280K monthly, -66.3% growth) partners with Cypher to let users borrow against DeFi lending positions to load a card, the steepest decline on the board. And **Sonic** ($56K monthly, -78.6% growth) appears tied to the Sonic Labs L1 blockchain, likely in very early stages. Together these four account for less than 1% of tracked volume. Their main contribution to the analysis is confirming that the long tail of this market is thin and struggling, while the top two players control nearly 88% of tracked volume between them.

## Comparing fees across the top cards

Most comparison articles list features. Here's what actually matters: what you pay to use the card.

RedotPay charges 1% conversion on every transaction, plus 1.2% FX on non-USD spending, plus 2-3% on ATM withdrawals. A $5,000/month international spender pays roughly $110/month in fees. ether.fi Cash charges 0% on USD transactions, 1% FX on foreign currency, 2% on ATM withdrawals, and 0% annual fee. That same $5,000/month international spender pays roughly $50/month, but earns 2-3% cashback in wETH, potentially netting positive. Cypher charges zero fees on USDC loading and competitive conversion rates, but lower cashback. GnosisPay's fees vary by white-label partner. MetaMask's Metal card charges $199/year but offers 3% cashback and zero foreign fees, which at $5,000/month spending easily offsets the annual cost.

Now flip the profile. A stablecoin pragmatist spending $1,500/month, mostly domestic USD purchases, no international travel. RedotPay's cost: 1% conversion on $1,500 = $15/month, no FX markup, no annual fee. Simple. ether.fi Cash: $0 in fees on USD transactions, plus 2-3% cashback ($30-45/month back in wETH). On raw economics, ether.fi still wins. But the stablecoin pragmatist now has to set up an on-chain vault, manage collateral ratios or USDC deposits, understand Scroll L2 settlement, and accept smart contract risk, all to save $15/month and earn $30 in wETH. For most people at this spend level, that complexity isn't worth it. RedotPay wins by being the card you don't have to think about.

The real comparison isn't just fee vs. fee. It's total cost of ownership (fees + card costs + opportunity cost of locked/idle capital) versus total return (cashback + yield on deposits + tax efficiency). ether.fi wins that calculation for ETH holders spending at scale. RedotPay wins for stablecoin spenders who value simplicity. The cheapest card on a fee schedule isn't always the cheapest card in practice, because complexity has a cost too.

## Two regulatory walls closing in at once

Most crypto card coverage treats regulation as a footnote. That's a mistake. Two major frameworks are converging in 2026, and they'll reshape which cards can operate where.

**In the US: the GENIUS Act.** Signed into law in July 2025, this is the first federal stablecoin legislation. The OCC published proposed implementation rules in February 2026. The FDIC approved its framework in April. Treasury proposed rules for state-level regime equivalency. FinCEN and OFAC issued joint AML/sanctions compliance rules. Final regulations are due by July 2026, with enforcement beginning January 2027.

The Act requires one-to-one reserve backing for payment stablecoins, audited regularly, held in high-quality liquid assets. It explicitly says permitted payment stablecoins are not securities. And it prohibits anyone other than a permitted issuer from issuing stablecoins in the US.

For crypto cards, this means the stablecoins underneath (USDC, USDT) face a clear compliance path, which should reduce counterparty risk. But it also means cards operating from non-US jurisdictions face barriers to the American market.

**In Europe: MiCA.** The Markets in Crypto-Assets Regulation is now fully operational, with the grandfathering deadline for existing crypto service providers hitting July 1, 2026. MiCA requires CASP licensing with EU-wide passporting, strict reserve requirements for stablecoin issuers, and transaction caps on non-EU-currency stablecoins (1 million transactions daily or €200M in value).

The effects have been blunt. Coinbase Europe delisted USDT in December 2024. Crypto.com followed in January 2025. Binance removed USDT from EEA spot trading in March 2025. Meanwhile, Circle achieved MiCA compliance in July 2024, and USDC transaction volume in Europe jumped 337% in the first half of 2025. Tether has no plans to seek MiCA authorization.

For European crypto card users, this is already reshaping the market. Cards that depend on USDT funding face a narrower path in EU markets. Cards built on USDC or MiCA-compliant stablecoins have a structural advantage. GnosisPay, with European roots and self-custodial architecture, may benefit from MiCA filtering out competitors. And the dual-licensing requirement introduced in March 2026, where EMT custody may need both MiCA authorization and PSD2 payment services licenses, adds compliance cost that favors well-capitalized players.

The two frameworks converge on one principle: regulated stablecoins backed by real reserves. They diverge on almost everything else. How each card navigates both simultaneously will be a defining competitive factor over the next 12 months.

## The risk layer most articles skip

Every crypto card article covers cashback rates and fee schedules. Almost none discuss what happens when things go wrong.

**Custodial risk (RedotPay, Kolo):** your stablecoins sit in the provider's wallet. If the company faces a regulatory freeze, gets hacked, or becomes insolvent, your funds are at risk. There's no FDIC insurance on crypto card balances.

**Smart contract risk (ether.fi, Cypher, GnosisPay, Avici, ExaApp, Moonwell):** your assets sit in smart contracts. The industry lost [$2.87 billion to hacks in 2025](https://www.trmlabs.com/reports-and-whitepapers/2026-crypto-crime-report). The ByBit breach ($1.5B) was executed through a Safe{Wallet} compromise. Security experts say on-chain code is getting harder to exploit directly, but the attack surface has shifted toward operational infrastructure: compromised signers, social engineering, supply-chain attacks. An audit is necessary, not sufficient.

**Liquidation risk (ether.fi Borrow Mode, Avici, ExaApp):** a sharp ETH drawdown triggers forced sales of your collateral. If you're using Borrow Mode without understanding the liquidation threshold, you're taking leveraged exposure to ETH volatility through your grocery spending.

**Network risk (all cards):** Visa and Mastercard are the settlement rails for every card on this list. If either network tightens policies around crypto-funded programs, it disrupts the entire market simultaneously. This has happened before and could happen again.

**Program shutdown risk (especially smaller/no-KYC cards):** This may be the most underappreciated risk on the list. Crypto card programs built on gift card schemes or repackaged corporate programs have a consistent lifecycle: launch fast, grow fast, get flagged by the card network or a regulator, shut down abruptly. The shutdown doesn't come with a 90-day wind-down notice. It comes with frozen balances and a dead card in your wallet. If your card offers corporate-grade limits with consumer-grade KYC, if it launched recently from an offshore jurisdiction, if it can't clearly explain what type of program it's running, the question isn't whether the cashback rate is good. It's whether the card will exist in 18 months.

## What I'm watching

The GENIUS Act enforcement window (January 2027) and MiCA grandfathering deadline (July 2026) will force real compliance decisions. Cards that thread both frameworks access the two largest regulated consumer markets. Cards that don't get confined to smaller jurisdictions.

The ether.fi 0% borrow rate expiration is the next big test for the DeFi card category. If spending volume holds through Q3 at market-rate borrowing costs, the collateral-backed model works without subsidies. If it drops, the Q1-Q2 numbers were promotional noise, and the category's growth story needs recalibrating.

Kolo's Telegram model in emerging markets has breakout potential if it scales beyond early adopters.

And I'm watching for the first bank-issued stablecoin card. The GENIUS Act opens the door. The economics work (interchange revenue, conversion spreads, reserve yield). A bank-issued stablecoin Visa could reshape the competitive picture overnight.

## The honest takeaway

Strip away the leaderboard rankings and the cashback comparisons, and the March 2026 data tells a specific story.

A meaningful share of this market's growth is built on compliance arbitrage. Tax opacity, offshore issuance, corporate card programs repackaged for retail users, gift card breakage models, minimal KYC in jurisdictions that require more. In the US and EU, that's not sustainable. The GENIUS Act enforcement window opens in January 2027. MiCA's grandfathering deadline hits July 2026. CARF and DAC8 are already live. The IRS is receiving 1099-DAs for the first time. Every quarter that passes, the regulatory surface area in these markets expands.

But most of the volume doesn't live in the US and EU. It lives in Southeast Asia, LATAM, and Africa, where stablecoins function as savings accounts, remittance rails, and inflation hedges, and where enforcement infrastructure is years behind legislation. The compliance arbitrage that drives growth in those regions isn't going away in 18 months. It's going away in 5-10 years, maybe longer.

The cards that survive the next 18 months will be the ones that didn't need the gray zone to grow. ether.fi's value proposition works whether or not the IRS can see the transaction, because the product advantage is yield and tax-deferred spending through borrowing, not reporting avoidance. Ready's neobank model works under full compliance because it's designed like a bank. GnosisPay's infrastructure play gets stronger as regulation filters out less compliant competitors. Even RedotPay, for all the questions about its limit structure, has real utility for stablecoin spenders in 100+ countries that isn't going away.

The cards that won't survive are the ones where, if you removed the tax opacity and the low-KYC onboarding, there's no product left. If the only reason someone uses a card is that it doesn't ask questions, that card has an expiration date. The market just doesn't know the exact month yet.

$607 million in monthly volume is real. In the US and EU, a meaningful chunk of it is living on borrowed time. In the markets where most of the spending actually happens, the runway is longer than Western regulators assume. The cards that win long-term are the ones that work in both worlds.
