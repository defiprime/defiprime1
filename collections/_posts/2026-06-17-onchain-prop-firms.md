---
git-date:
layout: [blog]
title: "Onchain Prop Firms: The House Edge Nobody Used to Admit Is Now a Published Feature"
permalink: onchain-prop-firms
h1title: "Onchain Prop Firms: The House Edge, On the Table"
pagetitle: "Onchain Prop Firms: The House Edge Nobody Used to Admit Is Now a Published Feature"
metadescription: "Funded-trader firms have always quietly bet against some of their own customers. Onchain prop firms on Hyperliquid are putting that conflict on the table."
category: blog
featured-image: /images/blog/onchain-prop-firms-ogp.png
intro: "Funded-trader firms have always quietly bet against some of their own customers. The onchain prop firms now launching on Hyperliquid are putting that conflict on the table, and turning it into a feature."
author: sawinyh
tags: ["Analysis", "Regulation"]
---

In August 2023 the CFTC froze the assets of MyForexFunds, a Toronto prop-trading firm that had collected more than $310 million in fees from over 135,000 customers. The complaint was not that prop firms are illegal. It was that this one had lied about what it was. MyForexFunds told customers they were trading against third-party liquidity providers. In reality the firm itself was the counterparty to substantially all of their trades, and, the CFTC alleged, it ran software that slipped customer fills to worse prices and closed winning accounts on technicalities. The firm was a bucket shop in prop-firm clothing.

That case is the right place to start a piece about onchain prop firms, because the thing MyForexFunds went to court for hiding, that it was the house betting against its own customers, is the thing the new onchain entrants now write into their documentation. The conflict has not gone away. The secrecy around it has, and the part MyForexFunds faked, an actual route to a real market, is now real for the traders who get it.

This piece reflects the landscape as of mid-June 2026. The onchain prop-firm category is roughly six months old, two of the three most credible players are in alpha or early launch, and tokens, fees, and funded-trader counts are all still moving. Treat the specifics as a snapshot, not a settled state.

## What a Prop Firm Actually Sells

Strip away the language about "funding the next generation of traders" and a modern prop firm sells one product: a paid exam with a payout attached. You pay a one-time fee, somewhere between $50 and a few thousand dollars depending on account size, for the right to trade a simulated account against a set of rules. Hit a profit target, usually around 10%, without breaching a drawdown limit, and you are declared "funded." From then on you keep a share of your profits, typically 80%, and the firm keeps the rest.

The fees are the visible business. [FTMO](https://ftmo.com/), the Prague-based market leader, ran $329 million in revenue in 2024 across 2.3 million open accounts, and has paid out more than $450 million to traders over its ten-year life. FundedNext, a UAE challenger, cleared an estimated $100 million-plus in 2024. The total addressable market for evaluation fees is somewhere in the low billions a year. This is a real industry, and most of it runs on the same funnel.

The funnel only works because almost nobody passes. Hard data is scarce, since almost no firm publishes audited numbers, but the credible estimates cluster low, and they answer two very different questions: how many pass the evaluation, and how many ever actually collect a payout.

![Funnel showing that of every 100 traders who buy a prop-firm challenge, roughly 10 pass the evaluation and roughly 6 ever collect a payout](/images/blog/onchain-prop-firms-funnel.png)

The per-firm numbers, where they exist, tell the same story from different angles:

| Firm / source | Pass the evaluation | Ever collect a payout | Basis |
|---|---|---|---|
| FTMO | ~8% (Phase 1) | ~7% of all entrants | community estimates |
| Topstep | 16.8% (2025 Combine) | 33% of funded traders | firm-published |
| FPFX Tech study | n/a | 7% of 300,000 accounts | third-party platform data |
| The Funded Trader | n/a | 1–2% of all clients | CEO statement |
| Industry composite | 5–10% (higher in futures) | ~5–7% of entrants | surveys plus the above |

The headline that "1 in 20 traders pass" is roughly right for the forex firms; futures, which is more rule-driven, runs a little kinder. Either way, the buyer's odds are the product.

So the economics are simple. Most customers fail, their fee is gross margin, and the small minority who pass are paid out of the much larger pool of fees from everyone who didn't. As long as fees from failures exceed payouts to winners, the firm prints money. That is the part everyone understands, and it is worth being clear that this fee funnel, not anything clever about trading, is the foundation of the business.

## The Part Everyone Doesn't: the B-Book

There is a second profit layer stacked on top of the fees, and the marketing leaves it out. The challenge phase is a simulation by design, an exam against a demo feed where no real order ever reaches a market. The interesting question is what happens after you pass. When you trade a "funded" account, your orders still frequently do not go to a real market at all. The firm internalizes them. If you lose, which is the base-rate outcome, the firm keeps your losses directly instead of just keeping your fee. This is the B-book, the same mechanic retail forex brokers have used for decades, and for a prop firm it is profitable precisely because most accounts lose. It is gravy on the fee funnel, not a substitute for it.

The opposite of a B-book is an A-book: the firm passes your order to a real venue and earns only a spread or commission. A firm A-books the traders it thinks will win, so it is not on the hook for their profits, and B-books the ones it thinks will lose, so it collects those losses. The decision of who goes in which book is the entire game. It is also where the conflict of interest lives, because a firm that B-books you has a direct financial incentive for you to lose, and the documented failure mode, the one the CFTC charged MyForexFunds over, is a firm that B-books a winning trader and then finds a rule to close the account before it has to pay.

For most of the industry's history this has been a secret. Firms either denied running a B-book or simply never mentioned it. The onchain entrants do the opposite. They describe the A/B engine in their docs, and in one case open-source the classifier that decides which book you land in. The conflict didn't go away. It got published.

## Why It's Moving Onchain, and Why Now

The substrate that made this possible is [Hyperliquid](/hyperliquid-chain-deep-dive). A prop firm needs deep liquidity across many markets, fast execution, and a way to settle and pay out programmatically. Hyperliquid supplies the first two through its onchain order book and its [perpetuals](/perps) markets, and its builder-deployed framework lets outside teams stand markets and tooling on top without renting infrastructure from anyone. A prop firm built on Hyperliquid gets deep liquidity, at least in crypto majors, without building a matching engine, and inherits the chain's transparency by default. Every trade, every rule, every payout can be a verifiable onchain event.

There is a defensive reason for the timing too. The legacy prop industry runs mostly on MetaTrader, and in 2024 and 2025 a licensing crackdown by MetaQuotes, the platform's vendor, helped push an estimated 80 to 100 firms out of business, on the order of an eighth of the global total. A business whose trading rail can be switched off by a software licensor has a structural fragility that an onchain venue, settling on a public chain nobody can revoke, is explicitly pitched against.

That last point is the actual pitch. The onchain version takes the three things prop firms have historically been able to fudge, the rulebook, the payouts, and the counterparty, and drags them into the open, though not all to the same degree:

- **The rulebook is a smart contract.** Drawdown limits, profit targets, and breach conditions are coded and immutable, not terms a support agent can reinterpret after you've made money.
- **Payouts are onchain and near-instant.** Where legacy firms are notorious for slow-walking withdrawals, the onchain firms settle in USDC in seconds, from a payout reserve whose balance anyone can check on a block explorer.
- **The counterparty is disclosed.** The firms admit in docs, and in Propr's case in code, that they internalize some flow, rather than denying a B-book exists at all.

Two caveats keep this honest. The reserve and the rulebook are genuinely verifiable onchain; the routing of any single trade is not. That a firm can A-book to Hyperliquid does not let you prove your own fill was mirrored there rather than booked against the house, and the classifier's promotion threshold is not public. So "disclosed" is the accurate word, not "verifiable," for the A/B decision specifically. Even so, disclosing the conflict is a genuinely different posture from MyForexFunds, and it is the thing worth thinking hardest about in this category.

## The Players

The field is young but already consolidating. The most significant move came from outside crypto-native circles entirely: in September 2025, [Kraken](https://blog.kraken.com/news/kraken-acquires-breakout) acquired Breakout, a Tampa-based crypto prop firm that had issued more than 20,000 funded accounts since 2023. It made Kraken the first major crypto exchange to step directly into funded trading, and signaled that prop trading is now a feature large exchanges want to own, not a fringe experiment. Two newer entrants, both building natively on Hyperliquid, are the clearest expressions of the onchain model.

Propr, built by XBorg and backed by SwissBorg, went live in early 2026. It funds traders up to $100K to trade perps across crypto, equities, and commodities, plus [prediction markets](/hyperliquid-hip4-vs-polymarket) and Solana memecoins, on an 80/20 split with onchain payouts. Its distinguishing move is transparency taken to its logical end: Propr [open-sources its A/B booking classifier](https://github.com/XBorgLabs/ab-booking), the actual code that decides which book you land in, and publishes its API docs in the open. It raised a $1.5M seed at a $17.5M FDV, and its $PROPR token is scheduled to unlock fully at a token generation event (TGE) in August 2026. XBorg has also started selling the underlying stack to other operators, a "license the prop firm OS" business that tells you where it thinks the margins are.

Hypernova launched a closed alpha on May 1, 2026 and raised $3M in a pre-seed led by Lemniscap, with CMS Holdings, Very Early Ventures, Pivot Global, and a roster of Hyperliquid-ecosystem angels. Its architecture splits the stack: smart contracts, accounts, and payouts live on [Arbitrum](/arbitrum) settling in USDC, while liquidity and pricing come from Hyperliquid's 110-plus perps spanning crypto, US equities, commodities, and indices. The team carries a RockawayX and Coinbase pedigree, and notably, CEO Anar Bayramov was an early backer of Breakout at RockawayX before it sold to Kraken. As of late May the alpha had onboarded around 250 traders, funded 20-plus, and paid out more than $30,000, against a $1M onchain payout reserve carved from the raise.

Behind those three sits a longer tail, names like HyperPnL, Upscale Trade, GT Funded, Solana Funded, and Carrot Funding, tracked by aggregators such as onchainprop.wtf. Treat the aggregators with caution; one of them lists Hypernova's profit split as 90% when Hypernova's own docs say up to 80%, so prefer primary sources. One of the builders selling this stack to other operators has predicted more than 100 onchain prop firms inside a year. Whether or not that number lands, the direction is clear: this is a category filling fast and drawing real institutional money, not a handful of clones.

| | Breakout (Kraken) | Propr | Hypernova |
|---|---|---|---|
| Stage | Live; acquired by Kraken Sept 2025 | Live since early 2026 | Closed alpha (launched May 1, 2026) |
| Venue | Kraken infrastructure | Hyperliquid | Arbitrum settlement + Hyperliquid liquidity |
| Instruments | Crypto | Perps (crypto, equities, commodities), prediction markets, memecoins | 110+ perps (crypto, US equities, commodities, indices) |
| Account size | Up to $200K | $10K–$100K | $5K–$200K |
| Profit split | Up to 90% | 80% | Up to 80% |
| Evaluation | Challenge → funded | 1-step or 2-step → funded | 1-step assessment, 10% target |
| A/B booking | Not disclosed | Open-sourced classifier (public repo) | Dynamic by trader quality; confirmed by CEO |
| Token | None | $PROPR, TGE Aug 2026 | Planned (raise had token warrants) |
| Funding | Acquired by Kraken | $1.5M seed @ $17.5M FDV | $3M pre-seed, led by Lemniscap |

Figures are drawn from each firm's docs and public coverage as of mid-June 2026; account sizes and fees vary by tier, and the alpha numbers in particular will move. Breakout, now Kraken-owned, is the centralized contrast here rather than an onchain peer; it is in the table for the consolidation picture, not as a like-for-like comparison.

## The B-Book, Now on the Record

The most telling shift in this category is not the technology. It is that the A/B conflict, the thing MyForexFunds was charged for concealing, is now a marketing point.

Hypernova's CEO, Anar Bayramov, described the mechanic to [The Block](https://www.theblock.co/post/402923/hyperliquid-prop-trading-platform-hypernova-crypto-funding) without euphemism. When a trader is A-booked, the firm takes their trades to the real market and loses money when they lose. When a trader is B-booked, because the firm lacks enough data on them or has judged them weak, it keeps the trades in-house and pockets the losses. Weak and unproven traders are internalized; strong traders get routed to the real market. He framed it as the fix for legacy firms that B-book everyone and then ban the ones who win, which is almost exactly the MyForexFunds fact pattern.

Propr goes a step further and open-sources the classifier, so the logic that sorts you is auditable rather than asserted. Either way, the bet is the same: that a conflict you can see, and in Propr's case inspect line by line, is safer than one you have to trust a support desk about. There is something to that. A B-book breach you can verify against an immutable rulebook is harder to manufacture than one adjudicated in a private dashboard. The firm still profits when a B-booked trader loses, but it can no longer quietly change the rules after the fact to make sure they do.

The honest read is that onchain prop firms have not solved the conflict of interest. They have made it legible, and they have made the A-book real, where MyForexFunds only claimed to have one. That is a genuine improvement over the MyForexFunds model on two counts, the disclosure and the actual routing, and neither is the same thing as alignment. A trader who is B-booked is still trading against the house, and the house still wants them to lose. The difference is that now you can find out which side of that you're on.

## What Onchain Genuinely Fixes, and What It Doesn't

Worth separating the parts that are structurally better from the parts that are still the same business with better optics.

Genuinely improved: payout reliability and rule integrity. The single most common complaint about legacy prop firms is that they don't pay, whether through slow withdrawals, manufactured rule breaches, or outright disappearance. An immutable onchain rulebook and a publicly auditable payout reserve attack exactly that. When Hypernova's reserve balance is queryable on a block explorer, "are they solvent enough to pay me" stops being a matter of faith. When the breach conditions are in a contract, "did I actually break a rule" stops being a judgment call. For a customer, this is the real value, and it is not trivial.

Not improved, and arguably sharpened: the base-rate economics. Onchain or off, the model still depends on most traders failing. The drawdown limits that make the firm solvent are the same limits that wash out most accounts, often on a single bad day. The funnel onchain is unlikely to be structurally different from the legacy one, where roughly 5–17% pass the evaluation and far fewer, on the order of 5–7%, ever collect a payout, because the same target-and-drawdown math drives both. The transparency improves trust; it does not improve your odds. A 10% profit target inside a 6% drawdown is a hard exam whether it's enforced by a contract or a compliance team.

And the same old risk, now in plain sight: payout-reserve solvency. A legacy firm pays winners out of a general corporate balance sheet, and when it ran short, plenty of them simply vanished owing traders money. An onchain firm pays from a named, finite reserve. Hypernova's is $1M, seeded from its raise and meant to be topped up from revenue. That is fine while the funded book is small, but a reserve is a hard ceiling in a way a balance sheet is not, and a cluster of simultaneous winners, or an A-booked cohort that does well, draws it down directly. The insolvency risk itself is not new; what is new is that you can watch the reserve drain in real time. The daily payout cap Hypernova runs in alpha, $10K of profit per user per day, is the visible pressure-release valve on exactly this constraint. Transparency cuts both ways here: when the reserve is public, a run on it is public too.

## The MyForexFunds Lesson Is Not the One You'd Think

It would be easy to read the MyForexFunds case as proof that the prop model is doomed and that going onchain is a way to dodge regulators offshore. That misreads both the case and the risk.

The CFTC's theory was specific. The killable conduct was the misrepresentation, telling customers they faced third-party liquidity when the firm was the counterparty; the deliberate execution-quality manipulation; and the pretextual closing of winning accounts. It was not "being the counterparty" as such, and it was not "running a challenge." A firm that discloses the counterparty accurately, routes verified flow to real venues, and enforces breaches through transparent onchain logic neutralizes most of that theory. In that narrow sense, the onchain design is a better answer to the CFTC's actual complaint than the offshore-and-hope posture most legacy firms took.

The case also has a tail worth knowing, because it cuts against easy conclusions. In May 2025 it collapsed. On the recommendation of a court-appointed Special Master who found the CFTC had taken "deliberate steps down a path of obfuscation and avoidance," a federal judge dismissed the case with prejudice, ordered the agency to pay the defendants' legal fees on the sanctions motion, and the CFTC placed four of its lawyers and an investigator on administrative leave. The enforcement action that defined this category's risk profile did not just stall; it was thrown out, with sanctions against the regulator. That does not make the underlying conduct fine. It does mean the regulatory line here is drawn around deception and execution abuse, not around the model itself, which is precisely the line an onchain firm is best positioned to stay behind, if it chooses to.

The harder regulatory question is the one [HIP-4 raises](/hyperliquid-hip4-vs-polymarket) for prediction markets and the [onchain forex gap](/onchain-forex-asset-primitive-gap) raises for FX: a permissionless, no-KYC, offshore venue may own the long tail while being structurally locked out of the regulated flow that institutions can actually touch. Kraken buying Breakout is the bet on the other side of that, that the compliant, exchange-backed version is the one that scales.

## The Uncomfortable Questions

**If transparency is the product, why is the A/B logic still partly opaque?** Propr open-sources its classifier, which is the strongest version of the pitch. Hypernova's CEO describes the logic but the data threshold that promotes a trader from B-book to A-book is not published. Disclosing the engine in plain language is a real step past MyForexFunds, but "trust our classifier" is not the same as "verify how it was applied to me," and on a closed classifier you cannot check the second from the chain. The category's credibility rests on closing that gap.

**Is the payout reserve a feature or a fuse?** A public, finite reserve is more honest than an opaque balance sheet, and more fragile. The legacy firms that blew up did so quietly. An onchain firm whose reserve visibly drains toward zero during a good month for its A-booked traders has a transparency problem its predecessors never had to manage, in full public view.

**Does putting the conflict onchain make it acceptable, or just visible?** A B-booked trader is still trading against a house that profits when they lose. Disclosure is not alignment. The open question is whether sophisticated traders, once they can see they've been B-booked, simply leave, which would strand the firms with exactly the losing flow that makes the B-book pay, and exactly the selection problem that pushes a firm toward MyForexFunds-style behavior in the first place.

**Who actually wins as the category consolidates?** Kraken owns distribution and a license. XBorg is selling the stack to anyone who wants to run a firm. The independent onchain firms sit in between, more transparent than the incumbents but smaller than the exchange that just entered their market. The "100 onchain prop firms" future and the "one exchange owns it" future are not obviously compatible.

## The Takeaway

The onchain prop firm is a genuinely better answer to the question MyForexFunds got wrong, which was never "should the firm be the counterparty" but "should the firm be allowed to hide it and cheat the exit." Immutable rules, auditable payouts, and a counterparty you can see are real improvements, and the most credible version, Propr open-sourcing the classifier, is a meaningful raising of the bar.

But the conflict underneath is the one it has always been. Most traders pay a fee and lose. The firm keeps the losing flow and routes the winners. The drawdown limits that keep the firm solvent are the same ones that wash most customers out. Onchain doesn't change that arithmetic; it just runs it in public. And for the person buying the challenge, the expected value is what it always was, which is to say negative: most pay a fee for a sub-10% shot at ever collecting a payout. A transparent negative-EV product is more honest than an opaque one. It is not a better deal. The clearest-eyed way to read this whole category is as gambling with an audit trail, which is an improvement on gambling without one, and still gambling. What's genuinely new is narrower than the marketing: the A-book is real for the traders who earn it instead of faked for everyone, the rulebook can't be rewritten after you win, and the payout reserve is something you can actually watch. The conflict didn't get solved. It got put somewhere you can watch it.
