---
layout: blog
title: "XRPL patches payment overflow that could mint $XRP"
url: /xrpl-patches-payment-overflow-that-could-mint-xrp.html
h1title: "XRPL patches payment overflow that could mint $XRP"
pagetitle: "XRPL patches critical $XRP minting overflow"
metadescription: "XRPL fixed a payment-engine overflow that could create spendable $XRP, then published the source after validators upgraded to xrpld 3.4.1."
category: blog
featured-image: /images/blog/xrpl-patches-payment-overflow-that-could-mint-xrp-ogp.png
intro: "XRPL shipped an emergency payment-engine fix after a bug bounty report showed how one transaction could create spendable $XRP."
author: sawinyh
tags: ["News"]
date: 2026-10-11T18:20:06+00:00
---

On October 10, 2026, XRPL [published the full source for xrpld 3.4.1](https://api.github.com/repos/XRPLF/rippled/releases/408417250), the emergency release that closed a payment-engine overflow. The researcher who reported it said a single crafted transaction could create 18 trillion $XRP, or 184 times the intended 100 billion supply.

The [official disclosure](https://xrpl.org/blog/2026/vulnerabilitydisclosurereport-bug-20261009) says the bug let an attacker create $XRP from nothing and spend it like ordinary $XRP. RippleX reproduced the mint on a standalone server, verified that the new $XRP could be spent in a follow-up payment, and raised the finding from major to critical. XRPL says it found no evidence that anyone exploited the flaw on a public network.

The report arrived through the XRPL Bug Bounty program on September 22. Engineers developed and reviewed the fix over September 22 and 23, merged it into the xrpld 3.4.1 release branch on September 23, and released version 3.4.1 on September 25. More than 80 percent of validators on the default Unique Node List were running the patched version that day.

## How one payment could create $XRP

The exploit started with a few hundred attacker-controlled accounts. Each account placed an offer selling a tiny amount of another token for a very large amount of $XRP. Every offer was valid on its own. A payment from another account then consumed all those offers in one pass through the order book.

XRPL stored $XRP amounts as fixed-size integers. The payment engine used unchecked 64-bit addition to calculate what the buyer owed across the offers. Once the sum exceeded the integer limit, it wrapped to a small value. The engine credited every offer owner with the full amount while charging the buyer only the wrapped total. The gap became newly created $XRP.

The protocol's two relevant safety checks failed to stop it. The no-$XRP-created invariant also used a 64-bit accumulator, so its calculation wrapped in the same way and made the net change resemble an ordinary transaction fee. The per-account balance check could not detect the aggregate mint because the attacker spread the $XRP across hundreds of accounts, leaving each balance below the supply limit.

The attack required only a few hundred $XRP for account and offer reserves, plus normal transaction fees. The reserves would be returned after the objects were removed. It could not happen through a normal payment or trade. An attacker had to build hundreds of offers with prices no real trader would use and then submit a payment designed to consume them together.

The researcher said Veria's agent found both underlying bugs, chained them, and produced a working exploit on a local network. Veria reported the issue through the bug bounty program after manually checking the proof of concept. Ripple awarded the team the program's maximum $250,000 bounty. The researcher described it as the largest bounty paid for a vulnerability discovered entirely by an AI agent, while the official report credits Cayden Liao and Veria AI for the original report and proof of concept.

The disclosure says the overflow had been present since the current payment engine was written in 2015. The no-$XRP-created invariant arrived two years later with the same unchecked arithmetic. That left a safety check and the code it monitored vulnerable to the same failure mode.

## What xrpld 3.4.1 changes

The patch adds overflow checks when the payment engine totals amounts across offers. A sum that would overflow now fails cleanly with a normal path-dry or partial-payment result. The release also checks the step that combines results from multiple payment paths.

Developers widened the no-$XRP-created invariant's counter so that it cannot wrap in the same way. They also hardened other balance-aggregation paths as a precaution. The [source commit](https://github.com/XRPLF/rippled/commit/578224f2e6395d1beb80b945c21b18a0bc824f1b) changed seven files with 168 additions and 10 deletions, including the payment path code and the invariant.

The repair separates the production guard from the backup invariant. Payment aggregation now refuses the invalid sum before balances change. The wider invariant remains a second line of defense if another transaction path ever attempts to create $XRP through a different arithmetic error. Operators therefore need the new binary even if their applications never construct unusual order-book routes, because transaction validity is enforced by the server rather than the client.

XRPL shipped the payment fix without an amendment. Transaction-processing changes normally activate only after more than 80 percent of trusted validators support an amendment for two weeks. That route would have exposed the bug in public source while leaving it usable during the upgrade and voting window.

Direct activation created a different risk. During the upgrade, patched servers would reject the exploit while older servers would accept it. An attempted exploit could therefore have pushed old nodes out of sync or halted validation. XRPL judged that temporary risk safer than publishing an open minting exploit that would remain active for weeks.

For operators, the requirement is immediate: servers must run xrpld 3.4.1 or newer to stay synchronized. Older releases are now amendment blocked because the same release also included fixBatchV1_2, which became active on October 9. Payment and trading interfaces should treat a path-dry or partial-payment response on an extreme aggregate as the intended result rather than retrying around it.

For holders and venues, the important result is that XRPL found no public-network exploitation and says the malformed offers could not practically block normal payments. Their pricing put them below real liquidity, so ordinary payment and path-finding results did not reach them. The remaining open question is whether the new release re-verification step, which retests every fixed security finding against a release candidate, will uncover other arithmetic assumptions shared by transaction code and its invariants.
