---
git-date:
layout: blog
title: "Quoted in Nvidia: Inside the Stock-Paired Memecoin Boom"
url: /stock-paired-memecoins.html
h1title: "Inside the Stock-Paired Memecoin Boom"
pagetitle: "Quoted in Nvidia: Inside the Stock-Paired Memecoin Boom"
metadescription: "On Robinhood Chain, memecoins are priced in tokenized shares. We read 432 such pools, holding 17% of the onchain float across 19 stock tokens."
category: blog
featured-image: /images/blog/stock-paired-memecoins-ogp.png
intro: "On Robinhood Chain, memecoins are increasingly quoted in tokenized shares instead of stablecoins. We read the pools directly and found 432 of them, holding 17% of the onchain float across 19 tokenized equities and carrying 31% of their trading volume."
author: sawinyh
tags: ["Analysis", "RWAs"]
---

Artificial Inu, ticker $AI, is the largest stock-paired memecoin on Robinhood Chain, and its only deep market quotes it in tokenized Nvidia. The pool holds 8,783 $NVDA tokens, 16.2% of every tokenized Nvidia share on the chain. Buy the dog coin with stablecoins and the router buys Nvidia first, because Nvidia is where the depth is.

At least four launchpads now offer this as their default product, and it has become the single largest identifiable use of tokenized equities on the chain.

We read the pools directly. Across 19 of the most liquid Robinhood stock tokens, at block 51,651,897 (roughly 10:30 UTC on September 1, 2026), there are 432 live liquidity pools in which a tokenized equity is the quote asset for some other token. Those pools hold $8.84M of stock tokens against a total onchain float of $51.5M for the same 19 tickers, or 17.2%. In the last 24 hours they carried $95.3M of the $304.1M in DEX volume those tokens traded, or 31.3%.

Both figures are lower bounds, and the method is at the end of this piece. Prices and pool balances move fast here, so treat every number below as a snapshot at that block.

For scale: the 19 stock tokens traded $304M in the 24 hours before our read, while chain-wide DEX volume was $1.49B on August 31, the last complete day. Tokenized equities remain a minority of what happens on Robinhood Chain. The claim here is narrower: within that minority, memecoin pairs are now the dominant format.

## What Actually Got Built

We covered [Robinhood Chain at launch](/robinhood-chain) in July: an [Arbitrum](/arbitrum) Orbit L2 settling to [Ethereum](/ethereum), built for tokenized stocks, with [Uniswap](/uniswap-explained) v4 as the day-one AMM. The stock tokens are ERC-20 debt securities issued by a Robinhood subsidiary that track a share price without conferring ownership, blocked for US retail, and freely transferable by anyone who holds them.

That free transferability is what the launchpads built on. Anyone can put a stock token into an AMM pool against anything, and by mid-July several platforms had industrialized doing so.

[Long](https://x.com/longdotxyz) arrived on the chain on July 14, letting a creator pick a stock token as the pricing and pairing asset for a new launch. Bankr followed on July 20 with the same idea across more than 90 tickers, [pitching it](https://cryptobriefing.com/bankr-stock-paired-tokens-robinhood-chain/) as pools denominated in Tesla or Apple instead of stablecoins. Flap brought over its Stocks Vault, where, [per its launch coverage](https://airdropalert.com/blogs/what-is-flap-launchpad/), the meme pays holders a drip of $AAPL, $GOOGL, $NVDA, $PLTR, $SPY or the SpaceX wrapper out of fee revenue. PAIR, whose first pools appeared on August 29, quotes new tokens against a basket of several stock tokens at once rather than a single ticker, and [describes itself](https://www.globenewswire.com/news-release/2026/08/31/3353221/0/en/pair-launches-the-first-multipool-rwa-launchpad-on-robinhood-chain-pairing-new-tokens-with-baskets-of-tokenized-stocks-partners-with-aws-to-scale-its-infrastructure.html) as the first multipool RWA launchpad.

The mechanic is the same at all four. A conventional memecoin pool is TOKEN/$USDC or TOKEN/$ETH. These are TOKEN/$NVDA, TOKEN/$HIMS, TOKEN/$SPCX. Because that pool is where the liquidity is concentrated, dollar and $ETH buyers get routed through the stock token to reach it. Net demand for the joke becomes a standing bid for the equity wrapper, and the wrapper accumulates inside the pool as the other half of the memecoin's liquidity.

## The Numbers

Stock tokens ranked by how much of their onchain supply now sits inside pools where they are the quote asset, read from the token contracts and DexScreener pool reserves at block 51,651,897:

| Ticker | Onchain supply | Paired pools | Held in them | % of float | 24h volume via paired pools | Largest pair |
|---|---|---|---|---|---|---|
| $HIMS | 73,685 | 18 | 39,136 | 53.1% | $13.5M (43.9%) | $BONER |
| $MSTR | 8,941 | 24 | 2,952 | 33.0% | $5.1M (42.9%) | $SAYLORMOON |
| $RBLX | 8,217 | 14 | 2,603 | 31.7% | $5.4M (41.5%) | $OOF |
| $NVDA | 54,091 | 41 | 13,450 | 24.9% | $12.9M (23.6%) | $AI |
| $TSLA | 6,735 | 27 | 1,451 | 21.5% | $3.9M (60.1%) | $LONGDOG |
| $GME | 100,379 | 36 | 19,888 | 19.8% | $4.9M (26.6%) | $SHORT |
| $AAPL | 10,701 | 26 | 1,853 | 17.3% | $6.3M (37.7%) | $BELIEVE |
| $PLTR | 6,562 | 27 | 1,124 | 17.1% | $3.6M (54.5%) | $HI |
| $SPCX | 41,107 | 30 | 6,425 | 15.6% | $13.2M (32.9%) | $SPACEHOOD |
| $GOOGL | 5,204 | 21 | 664 | 12.8% | $2.5M (44.2%) | $GOOGOL |
| $INTC | 11,387 | 16 | 1,415 | 12.4% | $0.6M (41.0%) | $INCEL |
| $AMZN | 6,453 | 30 | 769 | 11.9% | $3.2M (54.1%) | $SENDER |
| $META | 2,028 | 21 | 191 | 9.4% | $1.0M (49.2%) | $SLOP |
| $COIN | 5,287 | 22 | 443 | 8.4% | $1.0M (40.3%) | $PANDA |
| $SPY | 14,771 | 31 | 1,018 | 6.9% | $15.7M (19.3%) | $STARTUP |
| $AMD | 3,175 | 22 | 191 | 6.0% | $0.9M (51.0%) | $CHIP |
| $QQQ | 2,682 | 22 | 68 | 2.5% | $1.5M (32.1%) | $CHAD |

Float here means onchain supply, the tokens that exist on Robinhood Chain, not the company's shares outstanding. The percentage in the volume column is the share of that ticker's total 24-hour DEX volume that ran through memecoin pairs. The aggregate totals also include $LMT and $IONQ, which are left out of the table: their entire onchain floats are worth $1,076 and $7,748 respectively, which makes the percentages meaningless. For eleven of the seventeen tickers above, more than 40% of the wrapper's trading is a side effect of somebody trading a joke.

Those percentages are possible because the floats are tiny. Tokenized Meta is 2,028 tokens, about $1.2M. Tokenized Palantir is 6,562 tokens, about $1.2M. At that size a single memecoin can absorb a large share of the supply without anything unusual happening.

Reserves relative to volume are just as thin. The $STARTUP/$SPY pool turned over $3.5M in a day on 27.4 $SPY tokens of inventory, roughly $21K worth. A pool that shallow reprices on almost any order, which is the fragility behind the weekend premium described later.

The two largest pools: $AI/$NVDA holds 8,783 $NVDA against a memecoin marked at roughly $188M, and it did $6.2M of volume in 24 hours. $BONER/$HIMS holds 37,172 $HIMS on its own, 50.4% of every tokenized Hims & Hers token on the chain, against a $55M memecoin, and it did $12.5M. Long's own account [claimed on August 27](https://x.com/longdotxyz/status/2093097393608958360) that "23%+ of the total NVDA supply is now backing $AI," a broader definition than pool reserves that presumably includes its vault; our verified pool-only figure is 16.2%, and 24.9% once every NVDA-quoted pool on the chain is counted.

## The Jokes Are About the Companies

The largest pair for each ticker follows a pattern. $SAYLORMOON against MicroStrategy. $INCEL against Intel. $CHIP against AMD. $SLOP against Meta. $SHORT against GameStop. $OOF against Roblox. $GOOGOL against Alphabet. $SPACEHOOD against the SpaceX wrapper. $BONER against the company that sells erectile dysfunction treatment.

Every one of them is a joke about the company whose token quotes it. In the last memecoin cycle the reference point was usually a cat or a politician. Here it is an equity, and the coin carries a view about that equity.

The namespace collides as a result. There is a token on this chain called GameStop, ticker $GME, marked at $4.06M, that is not Robinhood's tokenized GameStop; it is a memecoin quoted against Robinhood's tokenized GameStop, and it traded $652K in 24 hours. There is a "NVIDIA Robinhood Coin" with the ticker $NVDA at $880K that is not the $NVDA anyone means. A buyer reading a ticker rather than a contract address on this chain is one click from owning something entirely different from what they think.

## Why Anyone Builds This

The format spread because it solves a real problem for a launchpad: a memecoin's fees are normally paid in a currency nobody wants to hold.

Artificial Inu publishes its mechanic [on its own site](https://artificialinu.com/how-it-works). Buys pay their fee in $NVDA, and 80% of that goes to a community vault described as "real stock tokens, held forever." Sells pay their fee in $AI, and that half is split evenly between a burn and a permanent lock in the same vault. The stated net effect is that "the Vault only grows and the $AI supply only shrinks. Volume is the engine." Long [said on August 30](https://x.com/longdotxyz/status/2094182592753045702) that roughly $3M of $AI had been taken out of circulation through its burn and lock mechanisms.

The result is a token whose treasury accumulates Nvidia exposure out of its own churn. Flap applies the same logic more literally, passing the fee revenue straight through to holders as a stream of tokenized stock. Bankr, [per Foresight News](https://global.foresightnews.pro/article/16845), pays creator fees out in the paired stock token.

A dog coin paired against $ETH turns speculative churn into $ETH for whoever collects the fees. A dog coin paired against $NVDA turns the same churn into a claim on a wrapper that tracks a real company, held by a token treasury. Whether that vault survives the token going quiet is the open question, and no project has reached that point yet.

Most of the money, though, is being collected a layer down. Uniswap V4 on Robinhood Chain earned $6.5M in fees in 24 hours, out of $14.3M chain-wide, per DefiLlama at the time of writing. The Pons launchpad's V2 contract earned $4.2M. Chain TVL reached $740M on September 1, up from $374M on August 1, and DEX volume on the last complete day, August 31, was $1.49B.

## What It Does to the Stock Token

The mechanism has one well-documented failure mode, and it happened over last weekend. We covered it in detail: a memecoin absorbed most of the tokenized Hims & Hers float, [pushing the wrapper as much as 112% above its NYSE close](/tokenized-stock-float-squeeze) during the 48 hours when the issuer could not mint more, and the premium collapsed within two hours of the first Monday mint.

Since then, Robinhood's issuer has minted aggressively into that gap, and the tokenized $HIMS float has gone from the 15,227 tokens we measured before the squeeze to 73,685 at our pinned block, an expansion of 4.8x in about two days. And 53.1% of that much larger float is sitting back inside the memecoin's pool. The supply response worked, in the sense that the premium is gone. It did not reduce the share of the float the memecoin controls; it just gave the pool more to absorb.

The pattern generalizes past $HIMS. Long [posted on August 29](https://x.com/longdotxyz/status/2093518946637168812) that fourteen of its markets each held at least 5% of the circulating supply of their paired stock. Our own read puts three tickers above 30% and eight above 17%. The float squeeze was the expected behavior of a design that is now replicated across dozens of tickers, and it recurs every weekend that a stock token's issuance calendar goes dark while its AMM stays open.

The analyst [@0xSammy](https://x.com/0xSammy/status/2094464115062276488), whose thread triggered our coverage of the $HIMS event, put the same worry in one line on August 31: "user growth is currently outrunning available onchain float." He counts 203,000 wallets holding tokenized equities, up 46% in three days, and reports a second isolated pool, $CINEMA against tokenized $AMC, trading at multiples of spot on the same weekend. We have not independently verified the $AMC pool.

## Where the Mechanism Stops

Some coverage of this boom has claimed that stock-paired memecoins are moving real share prices. Nothing we can see supports that, because the mechanism ends at the wrapper.

When $BONER cornered the tokenized $HIMS float, no Hims & Hers share changed hands, no short position was touched, and the NYSE opened Monday to a stock that did not know anything had happened. The wrapper is a warehouse receipt; you can corner the receipts without touching the commodity. What the memecoin flow genuinely does is create inventory pressure on the issuer, which mints when its broker acquires the underlying, so sustained memecoin demand does eventually reach the real market. That flow is a few million dollars against companies capitalized in the billions.

The gate asymmetry we flagged in July has not moved either. The wrapper is blocked for US retail; the memecoin quoted against it is not. In the [Distributed versus Represented framing](/distributed-vs-represented-rwa-framework) we use for [tokenized assets](/assets-tokenization), the composable half of these tokens has been fully colonized while the half that keeps them honest stays permissioned and on a Monday-to-Friday schedule.

## The Frontier Is Leverage as a Quote Asset

At 01:19 UTC on September 1, Long [announced](https://x.com/longdotxyz/status/2094595951478632458) LongX: an ERC-20 called $NVDA3x that wraps a 3x leveraged Nvidia perpetual position held on Lighter, mintable and redeemable against the contract, and tradeable in its own pool. The stated plan is to open full pairing mode so anyone can launch a memecoin quoted in it. At 05:06 UTC the team [said](https://x.com/longdotxyz/status/2094653138108293601) that LongX already held 16% of all $NVDA open interest on Lighter, bootstrapped through that single asset. Their own post calls the system experimental and asks people to trade carefully.

The stack now runs four deep: a share of Nvidia, wrapped as a debt security by a broker, wrapped again as a 3x perpetual position on a separate venue, wrapped a third time as an ERC-20, then used as the pricing asset for a joke token. Each wrapper adds a peg that holds only while its own maintenance mechanism is awake, and the weekend problem that produced the $HIMS squeeze applies to every one of them at once.

## What to Watch

Robinhood Chain launched with a 90-day gas subsidy, which by [several ecosystem accounts](https://www.techflowpost.com/en-US/article/33642) expires around early October. Some unknown share of the volume in the table above is fee-insensitive churn that has never had to pay for itself.

The vaults are the other unresolved question. Every stock-paired launch promises that fee revenue accumulates into stock tokens held permanently, and none of these projects has yet gone through the part of the cycle where the memecoin stops trading and somebody has to decide what the vault is for. Until one does, the treasury claim is an untested design.

Target selection is worth tracking too, because small floats are what make a corner cheap. Of the nineteen tickers we read, nine carry less than $1.5M of onchain float, seven of them in the table above. The only real fix on the issuer's side is carrying inventory across the weekend, which costs money and which nothing in the supply data suggests anyone is doing yet.

So far the most successful use anyone has found for tokenized equities is as the denominator of a memecoin, which is some distance from what Robinhood described in July. It is generating real fee revenue and has put equity wrappers into a couple of hundred thousand wallets. It also breaks the wrapper's price most weekends, and the launchpads are still adding tickers.

## Method and Caveats

Token supplies are read via `totalSupply` on each Robinhood stock token contract at block 51,651,897 on Robinhood Chain, roughly 10:30 UTC on September 1, 2026. Pool membership, reserves, and 24-hour volumes come from DexScreener at the same time, taking the union of its per-token pool listing and five search queries per ticker, then deduplicating by pool address.

That union is not exhaustive. DexScreener caps its per-token listing at 30 pools, which is why our first pass showed zero paired pools for $SPY and $SPCX and the second pass found 31 and 30. Both aggregate figures, 17.2% of float and 31.3% of volume, are therefore floors rather than measurements. Prices used to value floats in dollars are the DexScreener spot marks at the same read, which are onchain prices and can sit above or below the reference share price. Where a figure comes from a launchpad's own account or from a third-party analyst rather than our reads, it is attributed inline.
