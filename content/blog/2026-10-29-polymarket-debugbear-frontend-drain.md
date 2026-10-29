---
git-date:
layout: blog
title: "Polymarket Drained Again: A Hijacked Monitoring Script and $2.6M in POL"
url: /polymarket-debugbear-frontend-drain.html
h1title: "Polymarket Drained Again Through a Monitoring Script"
pagetitle: "Polymarket Drained Again: A Hijacked Monitoring Script and $2.6M in POL"
metadescription: "A DebugBear performance script on polymarket.com was swapped for a drainer that sold users' positions and pulled their cash. No contract was touched."
category: blog
featured-image: /images/blog/polymarket-debugbear-frontend-drain-ogp.png
intro: "A performance-monitoring script that Polymarket loaded from DebugBear was replaced with a drainer built for Polymarket. It sold email users' positions without a single wallet prompt, moved self-custody users' outcome tokens out, and routed the proceeds through Polymarket's own gasless relayer. The attacker's address held about $2.6M in POL an hour after the first theft."
author: sawinyh
tags: ["Analysis", "Prediction Markets"]
---

At 17:10:23 UTC on Thursday, October 29, 2026, in [Polygon](/polygon.html) block 96,392,296, the address [0x3F99139F1C5854bb628c2e576Aaf638e99dFfc18](https://polygonscan.com/address/0x3F99139F1C5854bb628c2e576Aaf638e99dFfc18) received its first POL. At 17:45:57 UTC, Polymarket trader [@CarOnPolymarket](https://x.com/CarOnPolymarket/status/2115862718452298234) posted: "If you are a Polymarket user, lock down your account. I just got drained $800,000." A follow-up ten minutes later said, "All my positions were sold." The JavaScript bundle polymarket.com serves now carries a build timestamp of 17:59:20 UTC and the commit message `chore(polymarket): remove debugbear rum script (#15337)`. At 18:00:58 UTC, DebugBear, the company that makes that script, [posted](https://x.com/DebugBear/status/2115866496643535293): "We're impacted by an ongoing security incident. If you use our RUM product, please remove the embed code from your website."

By 18:19:58 UTC, in block 96,395,079, the attacker's address held 28,636,284 POL, about $2.64 million at DefiLlama's price of $0.0922. It had not moved.

This is Polymarket's second frontend drain in four months, and its third security incident since May. Like the June one, it touched no smart contract. The Conditional Tokens contract, the order book and the exchange all worked as designed. What broke was a piece of third-party JavaScript running inside the page where users trade.

This piece reflects what the chain and the script showed at about 18:20 UTC, roughly 70 minutes after the first funds arrived. Polymarket had not published a statement on its X account at that point. A message attributed to the team, relayed from Discord by [@TheGreekTrader](https://x.com/TheGreekTrader/status/2115867928960860516), said the exchange was in cancel-only mode with relayer actions paused. Loss figures for individual users come from those users and have not been confirmed by Polymarket.

## What DebugBear Is and Why It Was on the Page

DebugBear sells website performance monitoring. Its RUM product (real user monitoring) is a small script a site owner embeds on every page. It runs in each visitor's browser, measures how fast the page loads and responds, and reports those timings back to DebugBear's servers. RUM scripts are a standard part of the modern web stack, and the trade-off is the same on every site that runs one: to measure what the visitor experiences, the script has to run inside the page with the page's full privileges.

On most sites, a script with those privileges can read cookies or scrape a form. On Polymarket it sits next to a trading client that can place orders and a signer that can authorize withdrawals. The RUM script doesn't need either of those to do its job. It had access to both anyway, because the browser does not separate scripts loaded into the same page.

## What the Script Did

The file that drained users was served at `cdn.debugbear.com/C7xcKKrjUnXK.js`. We fetched it at 18:13 UTC, when Cloudflare's edge was still serving a cached copy. A cache-bypassing request shortly afterwards returned 404. It is 15,187 bytes of minified JavaScript. Nothing in it measures performance. Every part of it was written for Polymarket.

On load, it reads three items from the browser's local storage: `polymarket.auth.params`, which records whether the user signed in with an email account or a self-custody wallet, `polymarket.auth.proxyWallet`, and `poly_clob_api_key_map`, which holds the API credentials Polymarket's order book issues to a logged-in session. It then walks React's internal component tree, starting from up to 400 buttons and links on the page, looking for any object that has a `postOrder` method and a `createOrder` or `createMarketOrder` method. That object is Polymarket's live order-book client, and once the script has it, it can trade as the user.

Next it asks Polymarket's public data API for the user's positions and balances, and it calls `polymarket.com/api/geoblock` with the user's cookies. It posts a summary of the portfolio, position by position, to `data.debugbear.com/metrics/submit`, tagged with the user's deposit and wallet addresses, IP address, country, operating system and login type, and it reports each completed theft back to the same domain with the transaction hash. It does not send the order-book API credentials it reads; it uses them in place. Its configuration, including the recipient address and the minimum portfolio worth stealing, is fetched from `data.debugbear.com/metrics/init`. If that request fails, the script falls back to defaults baked into the file: send everything to 0x3F99…fc18, skip any portfolio worth less than $10, skip any position worth less than $10, and prefer POL as the payout token. Because both requests go to the vendor's own domains, to anyone watching the network they would look like the RUM product's ordinary telemetry.

From there it takes one of two paths, depending on how the user signed in.

Users who sign in with email get a Magic wallet, which is embedded in the page. During a session the page can ask it to sign without showing the user anything: there is no browser extension and no confirmation window. The script uses the hijacked order-book client to sell the user's positions into the book with fill-and-kill orders, which execute against whatever bids exist and cancel the rest. This is the path that matches Car's "all my positions were sold" and the reports from users who said they were drained without ever signing anything.

For users who connected MetaMask or another external wallet, the script encodes an ERC-1155 `safeBatchTransferFrom` call on the [Conditional Tokens contract](https://polygonscan.com/address/0x4D97DCd97eC945f40cF65F87097ACe5EA0476045), moving every outcome token above the $10 floor from the user's deposit wallet to the attacker. It submits that call through Polymarket's gasless relayer at `relayer-v2.polymarket.com`. These users would have seen a signature request, and screenshots of one circulated on X as the "scam transaction" to reject.

The order depends on where the money is. If the user's pUSD balance (Polymarket's dollar collateral token) is larger than the value of their positions, the script sweeps the cash before touching the positions. It approves the pUSD and converts it through a second contract, fetches a swap quote from `api.fun.xyz`, and bundles the conversion and the swap into a single relayed batch that pays out in POL. Polymarket's relayer exists so that users never have to hold gas. On Thursday it paid the gas for the attack too.

## The Trail on Chain

The attacker's address had a zero balance and had never sent a transaction before 17:10 UTC. Every POL in it arrived on Thursday afternoon.

| Item | Value | Source |
|---|---|---|
| First POL received | block 96,392,296, 17:10:23 UTC | Polygon RPC |
| First outcome-token batch received | block 96,392,940, 17:26:29 UTC | Conditional Tokens logs |
| Last token transfer received | block 96,394,398, 18:02:56 UTC | USDC logs |
| POL held at 17:25 / 17:40 / 17:55 / 18:03 UTC | 0.81M / 11.2M / 22.1M / 28.5M | Polygon RPC, historical balance |
| POL held at 18:19:58 UTC | 28,636,284 (about $2.64M) | Polygon RPC, DefiLlama price |
| Outcome-token batch transfers received | 36 | Conditional Tokens TransferBatch logs |
| USDC and USDC.e received directly | about $16,700 | ERC-20 Transfer logs |
| Distinct addresses sending USDC or outcome tokens | 47 | ERC-20 and ERC-1155 logs |
| Transactions sent by the attacker | 31 | Polygon RPC nonce |

The last transfer into the address landed at 18:02:56 UTC, three and a half minutes after the build timestamp on the version without DebugBear, which fits browsers that still had the old page open (a build timestamp is also not the moment a deploy reaches every visitor). The dollar value is almost entirely in POL, delivered through swaps, so the 47 direct senders are not a victim count. Some victims' value arrived only as POL, and some direct senders may be swap infrastructure rather than users. The address holds almost none of the USDC it received directly. As of 18:20 UTC, none of the POL had left.

The first deposit was small, 1,957 POL. By 17:25:29 UTC the address held 0.81 million POL, by 17:40:29 it held 11.2 million, by 17:55:29 it held 22.1 million, and by 18:02:56 it held 28.5 million. Most of the money moved in the 37 minutes after 17:25, and Car's post landed in the middle of that run.

A timestamp from Tuesday sits outside that window. When we fetched the drainer, the CDN reported its last-modified time as Tuesday, October 27, at 12:50:43 UTC. If that header reflects when the drainer was written to the file, it existed more than two days before the first theft on chain. CDN metadata isn't always that literal. Whether it was already being served to Polymarket visitors during those two days, or was staged and switched on Thursday, the header can't say.

## The Response

The build timestamp on Polymarket's fix is 48 minutes and 57 seconds after the first POL arrived, and 13 minutes and 23 seconds after Car's public post. That bundle drops the DebugBear script, and the content security policy Polymarket serves now does not list any DebugBear domain. DebugBear's warning followed 98 seconds after the build timestamp.

What the fix could not do was reach browsers that already had the page loaded. The drainer kept working in those sessions until they were closed or refreshed, which is why the cancel-only mode and relayer pause described in the Discord message, if accurate, mattered as much as the code change. Cancel-only stops new orders matching, so a hijacked order-book client has nothing to sell into. Pausing the relayer stops the gasless transfers and swaps. Together they close both of the script's paths, at the cost of freezing every honest user too.

DebugBear's post told all RUM customers to remove its embed code, not just Polymarket. The drainer we read was written for Polymarket specifically, and nothing public yet says whether other DebugBear customers were served anything malicious.

## The Third Time This Year

In [May](/polymarket-key-compromise.html), an attacker drained roughly $600,000 from a dormant Polymarket operational wallet using a leaked private key. In June, Polymarket [confirmed](https://thedefiant.io/news/hacks/polymarket-confirms-3-million-loss-third-party-front-end-supply-chain-breach) that a compromised third-party vendor had injected a malicious script into its frontend for some users; estimates put the loss near $3 million, and Polymarket [said it would refund](https://crypto.news/polymarket-to-refund-users-after-2-94m-frontend-phishing-attack/) affected users in full. Polymarket never named the June vendor. A [write-up by cside](https://cside.com/blog/polymarket-client-side-supply-chain-attack), a company that sells script-monitoring products, described it as a compromised analytics SDK the platform had trusted for months. Whether June's vendor was DebugBear is not public.

Thursday follows June's pattern. A legitimate third-party script on polymarket.com was swapped for a hostile one, and users who visited the real domain and did nothing wrong lost money.

It is also the second vendor-hosted compromise to hit a prediction market this week. On Tuesday, Predict.fun [reported](https://x.com/predictdotfun/status/2115089547528950108) about 400,000 USDT in unauthorized transfers and said its API documentation site, "hosted by a third-party provider, may have been compromised." Nothing public links the two incidents.

## What the Script Got Right About Polymarket

The drainer is built around how Polymarket's web app works, and it gets the details right.

It assumed the trading client would be reachable from any script on the page, through React's own component tree. It assumed an email user's session could sign with no human in the loop, which is what makes email login feel like a normal app. It assumed the order book would take a burst of fill-and-kill sells from a logged-in client, since that's how the API is meant to work, and that the relayer would pay for the exit. All of them held.

Each is a reasonable product decision, and combined they let a performance-monitoring script empty an account. Embedded email wallets, gasless transactions and sessions that trade without prompts are what let people use Polymarket, and much of the [Polymarket ecosystem](/definitive-guide-to-the-polymarket-ecosystem.html) built around it, without ever touching a seed phrase. The cost is that anything running in the browser tab can act as the user, and that includes every vendor script loaded into it.

The questions Polymarket's post-mortem should answer:

- Why did a RUM script run in the same page as the signing session? Performance monitoring doesn't need access to the order-book client or the wallet. Loading it in an isolated frame, or not at all on pages where a session can trade, would have left the drainer with nothing to grab.
- Why could one vendor's CDN change the code running on polymarket.com? Pinning third-party scripts to a known hash with subresource integrity, or self-hosting them, means a vendor compromise breaks the script instead of weaponizing it. After June, this was the obvious control to add.
- Should withdrawals and full-portfolio liquidations from an email session need a second step? A sell-everything burst followed by a sweep of the whole balance to an address the account has never paid looks nothing like normal trading, and the relayer is in a position to notice.
- Who gets refunded, and on what basis? In June the answer was everyone affected, in full. Going by the attacker's balance alone, Thursday's losses are of a similar size, and email users never saw a prompt to decline. Self-custody users did. If Polymarket draws a line between the two, it should say so plainly.

## If You Use Polymarket

Until Polymarket says the site is clean and the relayer is back:

- Close any open polymarket.com tabs, and reload before you trade again. The fix only reaches a fresh page load.
- Don't sign anything the site asks for that you didn't start yourself, especially a batch transfer of outcome tokens.
- If you connected an external wallet, remember that the outcome-token transfer was a one-off signature, not a standing approval. Revoking approvals won't undo it, so the protection is not signing it in the first place.
- Ignore DMs, emails and links offering refunds, claims or "V2 migration" help. Drains like this are usually followed by phishing that borrows the incident's name.

We'll update this piece when Polymarket publishes its account of what happened, and if the attacker's POL moves.
