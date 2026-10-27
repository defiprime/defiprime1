---
layout: blog
title: "Balancer asks former users to check buffer shares and legacy rewards"
url: /balancer-users-check-legacy-rewards-buffer-shares.html
h1title: "Balancer asks former users to check buffer shares and legacy rewards"
pagetitle: "Balancer flags legacy rewards and internal buffer shares"
metadescription: "Balancer flags historical buffer positions and unclaimed partner rewards, with guidance for checking internal shares, gauges and legacy pool exits."
category: blog
featured-image: /images/blog/balancer-users-check-legacy-rewards-buffer-shares-ogp.png
intro: "Balancer is asking former users to check internally recorded buffer shares and legacy rewards that may remain after a liquidity exit."
author: sawinyh
tags: ["DeFi", "News"]
date: 2026-10-27T07:22:58+00:00
---

On October 26, 2026, [Balancer asked previous users to check for funds and rewards left in the protocol](https://x.com/Balancer/status/2114744157352894717) after contributors reviewing DAO-owned assets also examined historical positions belonging to outside users. A [companion forum notice](https://forum.balancer.fi/t/a-heads-up-for-long-time-balancer-users/7148) identifies liquidity-buffer positions associated with Ethena and Gauntlet, and legacy $LDO rewards belonging to Gnosis DAO and its stakeholders.

The notice asks former liquidity providers to check internally recorded buffer shares, unclaimed partner rewards and pool positions that may still be staked in gauges. Contributors reported the findings. This article has not independently measured the balances or verified the reported withdrawals on-chain.

## Buffer shares require the original depositing account

The forum contributor reports that external parties still held funds in Balancer v3 liquidity buffers. Most identified entities had been notified and started withdrawals. These positions use the Vault's internal accounting, and the notice warns that block explorers, DeBank and other portfolio dashboards may miss them. A dashboard showing no position can still leave a historical buffer deposit unaccounted for.

[Balancer's buffer documentation](https://docs.balancer.fi/concepts/vault/buffer.html) explains how the Vault tracks these deposits. A buffer depositor receives internally recorded shares instead of $BPT. The Vault records the total shares issued and each liquidity provider's share balance. The shares cannot be transferred, and only the account or contract that supplied the liquidity can remove it. Identifying the original depositing account comes before attempting an exit.

Buffers hold an underlying asset alongside its ERC4626 vault token. They supply liquidity for entering the wrapped position without routing every conversion through the lending protocol's wrapping or unwrapping operation. Balancer's documentation says this additional liquidity avoids the higher gas costs of that route. A buffer balance is a position in that internal conversion mechanism, separate from an ordinary pool-token holding.

Buffer funding also has different economics from pool liquidity. Balancer documents no swap fees, no yield participation compared with simply holding the assets, and no connection to the liquidity-mining system. Funding is permissionless. When reconciling historical buffer deposits, the balances to check are the recorded shares and underlying position. The buffer itself has no pool-fee balance or liquidity-mining entitlement to look for.

The documented withdrawal function is `removeLiquidityFromBuffer` on the Vault. The caller specifies how many shares to remove, and the function burns those buffer shares and returns the corresponding tokens. The share balance is the input to the removal operation. The documentation describes the function, but the evidence reviewed for this article includes no account-specific call, simulation or receipt establishing an executable withdrawal amount for Ethena, Gauntlet or another named holder.

Balancer also explains why removal goes directly through the Vault. A Router handling removal would need governance authorization because the Vault would have to trust it to report the correct sender. Revoking that authorization could lock funds; authorizing a malicious Router could allow theft. The documentation gives these risks as the reason for the withdrawal design. It does not report that either event occurred during the review of historical positions.

## Rewards can survive a liquidity exit

The forum notice separately identifies funds in legacy Balancer v2 liquidity-mining contracts. Some users had already withdrawn their liquidity while partner rewards remained claimable. The contributor names legacy $LDO rewards associated with Gnosis DAO and its stakeholders as an example. Those rewards require a separate check after a liquidity withdrawal: exiting the pool can leave the associated partner rewards unclaimed.

The contributor points users to the Balancer Portfolio page, which integrates checks for supported legacy positions and rewards. Its coverage is limited to those supported positions. A clean result there leaves any historical contracts outside that support unchecked. The forum post provides the team's recommended interface and the accompanying exit guidance, but describes no exhaustive inventory of every historical contract.

For users with remaining pool exposure, the contributor says the legacy interface will remain available for withdrawals from Balancer v1, v2 and v3 pools and for unstaking gauge positions. Users can follow that interface's guidance instead of constructing contract calls manually. The notice also directs users who need direct contract interaction to the manual exit guide, which covers protocol versions and gauge withdrawals.

## Match the contract before constructing an exit

[Balancer's manual exit guide](https://github.com/balancer/exit-ui/blob/main/MANUAL_EXIT.md) explains how staking changes the tokens a wallet displays. Staked $BPT sits in a gauge contract, while the wallet holds a gauge token. The guide instructs users to find gauge entries in the chain configuration whose `lpToken` matches their pool address, then read `balanceOf` for their account on each matching gauge. A search limited to unstaked pool tokens can miss the staked position.

The guide calls for identifying the protocol before choosing a withdrawal recipe. It treats the `getVault()` address as definitive for distinguishing v2 from v3 because contract names overlap; v1 has no Vault. It also provides factory checks for v1 pools and `Vault.isPoolRegistered(pool)` for v3. These contract checks determine which withdrawal path to use when a familiar pool name alone cannot identify the protocol version.

Before any interaction or approval, the guide requires users to verify addresses against its registry or through its contract checks. It also instructs users to simulate before sending and derive minimum output amounts from that simulation with a slippage allowance. The guide describes zero minimums as a last resort, corresponding to the interface's emergency mode. They are not the standard withdrawal setting.

The SDK covers fewer cases than the manual recipes. The guide excludes v1, several specialized pool types and gauges from SDK coverage, directing users with those positions to contract recipes or its code. It also warns that deprecated pools may disappear from the Balancer API. For those cases, it shows how to construct pool state using on-chain data through `Vault.getPoolTokens`.

Current claimable rewards and remaining buffer shares for each named account remain unverified in this article. Establishing those balances requires account-specific contract reads beyond the checks described in the reminder and documentation.
