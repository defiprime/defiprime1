---
layout: blog
title: "Polygon proposal seeks hard fork to recover 70.49M POL"
url: /polygon-proposes-hard-fork-for-blocked-pol-recovery.html
h1title: "Polygon proposal seeks hard fork to recover 70.49M POL"
pagetitle: "Polygon proposal seeks hard fork to recover 70.49M POL"
metadescription: "A Polygon proposal would move blocked native POL to Polymarket and Binance recovery wallets, subject to governance approval and a coordinated hard fork."
category: blog
featured-image: /images/blog/polygon-proposes-hard-fork-for-blocked-pol-recovery-ogp.png
intro: "A Polygon governance proposal seeks a one-time hard fork to recover native POL blocked after the Polymarket and Binance incidents."
author: sawinyh
tags: ["Analysis", "Prediction Markets"]
date: 2026-11-04T19:32:06+00:00
---

On November 4, 2026, a [proposal on Polygon's governance forum](https://forum.polygon.technology/t/pip-proposal-recovery-of-funds-held-in-blocked-addresses-following-the-polymarket-and-binance-incidents/22497) asked validators to approve a hard fork recovering about 70.49 million POL from addresses blocked after the Polymarket and Binance incidents. The proposed change would zero the listed addresses' native balances and credit recovery wallets designated by the affected companies.

The proposal is scheduled for presentation at the Polygon Protocol Governance Call on November 5 at 14:30 UTC. Its activation block, fork name and client release are still undecided. The recovery effort remains at the forum-proposal stage, with no approved upgrade or completed return of funds under this proposal.

The governance request follows [the Polymarket frontend drain](/polymarket-debugbear-frontend-drain.html). It asks the network to change account balances through consensus, affecting validators, RPC providers and anyone reconstructing balances from transactions. The recovery destinations belong to the affected companies. The proposal specifies no direct distribution from the fork to individual users.

Polymarket's [October 30 postmortem](https://status.polymarket.com/cmvvek1i90eme14ruga1z6tuj) said reimbursement was already underway, with 95% of affected wallets refunded in full that afternoon. Its stated $3.9M return included $2.7M plus $1.2M for pause-related losses. The company said users needed no claims or tickets because it identified eligible wallets from on-chain and trading data. The refund policy covered slippage when the malicious script force-sold positions, as well as qualifying losses during the trading pause. Polymarket reported those reimbursements before this proposal to recover balances at the network level.

## What is blocked, and what would move

The proposal identifies four Polymarket-linked addresses and one Binance-linked address for recovery, calling them Class A. Its reference tables put the Polymarket total at 23,862,736.07 POL at block 96,399,251 and the Binance balance at 46,626,593.27 POL at block 96,413,185. The document dates both reference blocks to October 29. These historical reference amounts do not fix the eventual fork's payout amounts.

We independently queried native balances through Polygon RPC at those exact blocks. At the Polymarket reference block, the address beginning `0xe4C4` held 15331308.287708954252254 POL, `0x5392` held 4295442 POL, `0xc91e` held 4235982.731885163313955003 POL and `0x3f70` held 3.052420374918193426 POL. At the Binance reference block, `0x5227` held 46626593.2666666 POL. These readings verify historical balances. They establish neither ownership nor the complete path of the stolen funds.

The proposal describes the Polymarket incident as involving about 28 million POL. It records onward transfers totaling 3,282,275.71 POL from `0xe4C4` to `0x3f70` at 18:30:34 and 18:35:59 UTC on October 29. Only a small balance remained at the latter address at the reference block. The recovery would take the funds still held at the listed addresses, so incoming-transfer amounts and available balances are different figures.

For Binance, the document identifies block 96,406,484 as the transfer point for 46,626,589.6 POL and 6,185,900.1 USDT from a hot wallet to `0x5227`. It says Tether has frozen the stablecoins. The proposed consensus change covers native $POL only. Other tokens, including $USDT, are outside its scope. Our historical native balance reading does not independently verify the stablecoin freeze.

At the start of the activation block, before ordinary transactions execute, the client would read each Class A address's balance from the preceding block's post-state. It would set that balance to zero and add the same amount to the corresponding recovery address. This would transfer existing native balances and leave total supply unchanged. The specification says the design is proposed and subject to confirmation by Bor engineering.

The Polymarket destination is `0x3dcE0a29139A851Da1dFCa56Af8e8a6440b4D952`; Binance's is `0xd9fd39103674cb061d64d9c3b73b878dbe610b80`. Before activation, each company must provide its address in the discussion, prove control through a signed message or test transfer confirmed by Polygon Labs, and confirm in writing that it owns the destination. Listing an address in the table leaves those verification requirements to be completed.

## The limits of the existing block list

According to the proposal, the validator-elected block producers added the attacker addresses to Bor's transaction block list at the affected parties' request. That stopped outgoing movement, but the block list has no mechanism for returning the funds. The fork would make that state change without requiring the holder's private key to authorize a transaction.

Each producer reads its list at startup, so updating the filter requires a deployment and a Bor restart or span rotation. Entries never expire automatically. The filter covers outer transaction senders and EIP-7702 authorities, leaving other ways an asset can move outside its coverage. The authors say no bypass has been found, while warning that the mechanism is not a complete asset freeze.

The authors also report continued pressure on the block producers. A pending transaction offering a fee of about 219,450 POL was observed on October 30, and the attacker contacted validators offering cash for help unblocking a transaction. These reports come from the governance record; our balance checks did not independently reproduce the transactions. The proposal says Polymarket opened an on-chain recovery channel through the SEAL Safe Harbor Recovery safe without receiving a response.

Binance supplied further addresses for blocking, designated Class B. Those addresses would stay outside the recovery sweep. The security section specifically names Binance Hot Wallet 34 as a smart-contract wallet accepting ERC-4337 UserOperations, which the authors say a sender-based filter cannot stop. It remains a Class B entry and would supply no funds to the fork.

The authors acknowledge that a wrongly classified Class A address would lose a legitimate balance under the proposed rule. They cite that attribution risk as the reason not to sweep Binance's Class B addresses. The fork's address list is closed. Cleanup of the broader block list would follow a separate process after activation.

## Approval, rehearsal and the consequences for nodes

Activation requires approval through Polygon governance, published postmortems that remain consistent with the on-chain record, and continued enforcement of the block lists until the fork takes effect. The Class A balances must be read again at the snapshot block, with any changes from the reference tables published. These conditions must hold at both the final vote and the Amoy sign-off.

The rehearsal would use test accounts standing in for the affected addresses and recovery wallets. Its checks include the balance transfer, unchanged supply and the absence of changes to other accounts. A mainnet-fork replay would use the Class A snapshot balances. The test list also requires a node running old software to reject the activation block. Recovery-address verification must finish on mainnet before the release is tagged.

The rollout table calls about two weeks after approval workable for client development and the Amoy deployment and rehearsal, describing one week as tight. Before mainnet, validators, RPC providers and explorers would receive notice. The proposal reports validator operations' expectation that about 70 to 80% of stake could reach the required version quickly after release. That estimate describes the expected rollout; no such upgrade rate has yet been observed.

Nodes that fail to upgrade will follow a different chain from the activation block, according to the compatibility section. The proposal leaves Heimdall, the StakeManager and bridge contracts unchanged, and alters no state before that block. Bor would make the consensus-breaking change that reassigns the native balances.

Explorers, indexers and accounting tools would have to account for the protocol-level adjustment. Replaying only the activation block's transactions would not reproduce its final balances: the recovery happens before those transactions, without a transfer transaction of its own. After activation, the plan calls for publication of the transaction-free balance change and a verification script.

Block-list removal would follow the recovery. Class B entries would be removed on Binance's confirmation, while Class A entries would be reviewed for removal after becoming empty. Passing the fork would leave these separate removal steps in place, with no automatic deletion of every related block-list entry.

## The proposed exception and its unresolved edges

The authors reject a general freeze-and-recover facility because it would create permanent power over user funds. They also reject indefinite blocking as a stable endpoint and describe negotiated return as dependent on attacker cooperation. Their case for an exception rests on acknowledged theft, affected parties presenting the proposal, universal producer blocking, traceable funds and an amount large enough to justify a fork.

Anyone can send native $POL to a listed address before activation. Under the full-balance rule, that later credit would move to the recovery wallet too. The proposal acknowledges this possibility and requires a fresh snapshot reading. The reference totals therefore cannot promise that exactly those amounts would be reassigned, with later deposits excluded.

The security section identifies recovery-wallet compromise and chain splits as risks. The proposed safeguards include proof of control, written confirmation, publication of any multisig signers, the Amoy rehearsal and a release date chosen after stake coverage is confirmed. Neither the presenters nor Polygon Labs promise the outcome of the vote. Bor engineering still has to confirm the transition design, and the activation block and release remain unset.
