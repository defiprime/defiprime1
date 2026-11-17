---
layout: blog
title: "Curve discloses $38,200 DAO fee theft from CowSwapBurner"
url: /curve-cowswapburner-fee-theft-disclosure.html
h1title: "Curve discloses $38,200 DAO fee theft from CowSwapBurner"
pagetitle: "Curve discloses $38,200 DAO fee theft from CowSwapBurner"
metadescription: "Curve traced a DAO fee theft to missing order-hash checks in CowSwapBurner; user funds were unaffected and Ethereum fee conversion remains paused."
category: blog
featured-image: /images/blog/curve-cowswapburner-fee-theft-disclosure-ogp.png
intro: "Curve disclosed a theft of DAO fee revenue through its Ethereum CowSwapBurner while proposing a replacement for the disabled contract."
author: sawinyh
tags: ["News", "DEXs"]
date: 2026-11-17T20:26:46+00:00
---

On November 17, 2026, Curve disclosed that an attacker stole about $38,200 of DAO fee revenue from its Ethereum CowSwapBurner on November 10. The [incident disclosure](https://github.com/curvefi/security-incident-reports/blob/main/disclosures/2026-11-10.md) identifies a missing order-hash check and says the Emergency DAO disabled the affected fee machinery at 13:59 UTC that day.

The funds belonged to the DAO. Curve said: "No user funds were affected." Pools, lending markets and $crvUSD were outside the incident, according to the disclosure. The stolen revenue remains unrecovered. Ethereum fee conversion is paused, though fees continue to accrue.

Curve puts the forged orders' proceeds at 38,205.76 USDC. The regular weekly conversion still delivered 97,317.74 crvUSD to the FeeCollector. The attacker sold a separate set of accumulated balances, most of them too small to clear the burner's normal sale minimum.

## A valid description attached to the wrong order

The affected contract handles fee conversion for [Curve Finance](/curve.html). Curve collects admin fees from pools and markets into a FeeCollector, moves them to a burner on Monday, and sells them during a 24-hour window opening Tuesday at 00:00 UTC. Distribution of the resulting $crvUSD follows on Wednesday.

CowSwapBurner has handled Ethereum conversions since June 2024. For each fee token, it offers a standing CoW Protocol order to sell its entire balance for $crvUSD. The order names the FeeCollector as recipient and requires at least 500 crvUSD in return. The burner gives CoW Protocol unlimited allowances for those tokens. Curve says it had settled 6,420 orders and delivered about 20.5 million crvUSD before the attack.

CoW Protocol asks the contract to validate an order through ERC-1271, calling `isValidSignature(orderHash, signature)`. The hash identifies the order about to execute. The signature data contains a full order description for the burner to inspect.

The burner checked that description for $crvUSD as output, the FeeCollector as receiver and the minimum sale amount, then returned the signature-validation success value. It never checked whether the description matched the order hash. Curve's disclosure states: "The function explicitly ignored `_hash`:"

An attacker could attach a legitimate burner order's description to a different order, choosing another output token and recipient. The burner would approve it even though the actual trade sent proceeds elsewhere. The exchange window still had to be open for the forged order to receive approval.

## Small balances sold through ordinary settlement

Curve dates the first forged settlement to 00:07 UTC on November 10, shortly after the weekly window opened. That order sold the burner's $YB for $USDC and named the attacker as receiver. Its signature attachment described the burner's own genuine $YB order.

The attacker reused that attachment for 137 further orders involving other tokens. According to the disclosure, 133 orders filled within 17 minutes, with the remaining five settling over the following hours. The last forged settlement occurred at 11:10 UTC. Solvers competed to fill the trades as usual, at prices close to market.

Curve's table separates 36 regular orders covering 35 tokens from 138 forged orders covering 135 tokens. The token groups did not overlap. The forged sales largely consumed balances that had accumulated below the 500 crvUSD threshold, leaving the normal conversion able to complete.

The median forged order was worth about $254; only two exceeded $500. Among tokens that had previously been sold, the median interval since the last sale was 161 days. Curve says it reviewed every settled burner order since deployment, 6,558 in total. Only the disclosed forged orders paid somewhere other than the FeeCollector.

The team also traced proceeds beyond Ethereum. It says the attacker swapped 37,611.76 USDC into $ETH, split funds across four addresses, bridged to Arbitrum and deposited 37,229.89 USDC into Hyperliquid within four hours. There, the funds were exchanged for 65.41 XMR1, a Monero-linked asset. Curve reported that balance unchanged as of November 16.

Curve also describes a later transfer of the remainder left on Ethereum. On November 15, according to the disclosure, the attacker swapped the remaining 594 USDC into $ETH and deposited 0.3 ETH into Tornado Cash.

The settlement totals and cross-chain tracing are Curve's findings. Defiprime's independent RPC checks confirmed deployed code at the [burner](https://etherscan.io/address/0xc0fc3ddfec95ca45a0d2393f518d3ea1ccf44f8b) and [FeeCollector](https://etherscan.io/address/0xa2bcd1a4efbd04b63cd03f5aff2561106ebcce00) at Ethereum block 26,384,965. Those checks did not reconstruct the stolen balances or establish the exchange-disable flag. The generic paused-field reads returned no value.

## Conversion stays paused while replacement goes to a vote

Curve's timeline says an external vulnerability report arrived around 12:40 UTC on November 10. The Emergency DAO proposed its disabling transaction at 13:39 UTC and executed it at 13:59 UTC. According to the disclosure, disabling collection stops new fees from reaching the burner, while disabling exchange makes it reject orders.

The Emergency DAO took the same precaution on Arbitrum and Base at 16:55 UTC. Curve reported finding no forged orders on Arbitrum or Gnosis. On November 17, it swept residual balances from the old Ethereum, Base and Arbitrum burners back to their respective FeeCollectors.

The code has also been reused outside Curve. The team says it notified operators of known derived deployments before publication. Those operators have a specific check to make: whether an accepted CoW Protocol order hash is bound to the order description their contract validated. Curve's disclosure does not list those deployments or certify their remediation.

DAO vote 1524, opened on November 13, proposes a replacement burner using a descending-price auction. Curve says the replacement requires any accepted CoW Protocol order hash to match the checked order. The replacement remains a proposal in the disclosure, with fees continuing to accumulate during the conversion pause.

The vote closes on November 20, 2026, according to Curve. The disclosure gives no date for resuming Ethereum fee conversion and reports no recovery of the stolen revenue.
