---
layout: blog
title: "Lido Earn adds Firelight loss protection to its vaults"
url: /lido-earn-firelight-loss-protection.html
h1title: "Lido Earn adds Firelight loss protection to its vaults"
pagetitle: "Lido Earn adds Firelight loss protection to its vaults"
metadescription: "EarnETH and EarnUSD add Firelight protection ahead of the DAO buffer, with fixed coverage periods, eligibility tests and capital-dependent payouts."
category: blog
featured-image: /images/blog/lido-earn-firelight-loss-protection-ogp.png
intro: "Lido Earn has added Firelight loss protection ahead of its DAO-funded buffer for EarnETH and EarnUSD depositors."
author: sawinyh
tags: ["DeFi", "News"]
date: 2026-11-05T17:27:34+00:00
---

Lido added Firelight loss protection to EarnETH and EarnUSD on November 5, 2026, placing it ahead of the DAO-funded buffer already operating in both vaults. The [launch announcement](https://blog.lido.fi/lido-earn-introducing-two-layers-of-loss-protection/) sets initial Firelight limits at up to 5.7% of EarnETH’s total value locked and 8% of EarnUSD’s. Payment depends on eligible losses, approval and available capital.

Depositors do not need to enroll or request compensation after an incident. Both layers apply at the vault level to all depositors in the affected vault. The vault pages display the current limits. Current Meta Treasury pays for the new protection, so the cost currently does not come out of vault returns.

Lido Earn deploys $ETH or stablecoins into curated DeFi strategies with daily, auto-compounded earnings. Depositors receive $earnETH or $earnUSD tokens representing their share of the vault, with a value that reflects deposits and performance. The change applies to those vaults. They are separate from the [Lido Lend markets based on Morpho Blue](/lido-lend-morpho-blue-isolated-markets.html) that contributors unveiled in October.

## Protection resets at period boundaries

Firelight is an on-chain protection protocol built on Flare and incubated by Sentora. Its layer draws on a protocol-owned reserve and capital that stakers commit in $FXRP. Coverage applies to the Earn vault contracts and approved DeFi markets used by their strategies. The reserve pays first, before staked capital.

Protection runs in fixed 30-day periods. Before each period starts, Lido Earn contributors confirm the protected markets and limits with Firelight. Those terms stay fixed for the whole period. If a strategy moves funds into a new market partway through, that position becomes protected only when a later period includes the market.

Coverage includes smart-contract exploits, oracle failures and governance exploits. It also includes bad debt, depegs or redemption failures caused by a protocol mechanism malfunction. Normal price moves and liquidations using accurate prices are excluded. The exclusions also cover stolen keys, user error, off-chain problems and flaws known before the protection period began.

Firelight’s [coverage documentation](https://docs.firelight.finance/resources/cover-scope) specifies which economic losses qualify. It excludes losses from market conditions acting on a mechanism that works as designed. Economic losses are measured after a 24-hour stabilization period unless the Risk Consortium sets a different period. Coverage follows the recorded markets, so it does not extend to every exposure a vault might acquire.

## Approval and mitigation still govern payment

Firelight monitors protected markets in real time and assesses losses after an incident. An independent Risk Consortium of five security and risk firms approves or rejects the assessment. Once it approves a loss, the payout runs automatically, drawing first on the reserve and then on staked capital.

The program operator still has obligations even though depositors do not have to file claims. For bad debt, depeg and redemption events, the operator must take reasonable steps to limit losses and provide information when asked. Firelight can reduce a payout in proportion to losses the operator could reasonably have avoided. Its documentation says on-chain evidence determines whether the operator met that duty.

An instantaneous exploit with no reasonable opportunity to act satisfies the mitigation duty automatically. In other cases, the Incident Reporter assesses mitigation from on-chain records and the consortium validates it. If the record is inconclusive, the operator is responsible for demonstrating compliance.

The rules also prevent duplicate recovery. Events that affect multiple covered markets through the same root cause within 24 consecutive hours count as one incident. Each market is still assessed against its own limit. When reconstructing exposure, the assessment disregards position increases after public disclosure or detection, whichever came first.

An incident must be validated and settled before the end of the period following the one in which it was created. Incidents can reference exploits only from the current or immediately preceding period. Other stated processing times are service-level targets, not deadlines enforced by the protocol.

## The DAO buffer remains a separate mandate

The [existing DAO mechanism](https://blog.lido.fi/lido-earn-first-loss-protection-dao-alignment/) began with an allocation of $3 million in $wstETH to EarnETH and $2 million in $USDC to EarnUSD. The DAO pays the same fees and holds the same vault shares as other depositors. Burning those shares reduces total supply, letting the DAO’s position absorb losses for the remaining holders.

Under the mandate, a confirmed loss of at least 1% of a vault’s TVL allows the Growth Committee, acting for the DAO, to burn up to 100% of the DAO-held shares in that vault. This layer can cover losses beyond Firelight’s specified causes. Losses remaining after Firelight’s contribution can reach the DAO buffer, subject to the buffer’s own conditions.

Lido says the DAO protection has been used once. Following the Kelp DAO $rsETH incident in April, the DeFi United effort addressed the main backing shortfall. EarnETH’s residual loss was below the mandate’s threshold. The DAO approved a one-off exception and burned shares worth 144.77 ETH. According to Lido, EarnETH depositors were ultimately made whole.

The DAO position changes as vault rewards compound and asset values move. Its [quarterly treasury report](https://research.lido.fi/t/lido-earn-dao-treasury-allocation-q3-2026/11996) says rewards remain in vault share prices instead of being remitted to the treasury. The original seed amounts do not describe the capital available at every later date.

Lido’s launch illustration puts EarnETH TVL at $212.9M and EarnUSD at $50.3M. For EarnETH, it lists up to $12.1M of Firelight protection and $3.2M of DAO protection. For EarnUSD, it lists up to $4M and $2.1M respectively. These are the operator’s illustrative amounts, not guaranteed recoveries.

Firelight describes its cover as a conditional, collateral-backed release mechanism, not insurance or an indemnity. Its documentation says a validated loss can exceed the amount actually paid because collateral is finite and fluctuates. Payment still depends on the capital available at settlement, even after a loss is approved.
