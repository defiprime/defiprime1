---
layout: blog
title: "Blast shuts down and opens Ethereum recovery through November 2027"
url: /blast-shuts-down-opens-ethereum-recovery.html
h1title: "Blast shuts down and opens Ethereum recovery through November 2027"
pagetitle: "Blast shutdown opens Ethereum fund recovery"
metadescription: "Blast has shut down its L2. Its Ethereum recovery site covers remaining ETH, WETH, USDB and unfinished withdrawals, with support ending November 4, 2027."
category: blog
featured-image: /images/blog/blast-shuts-down-opens-ethereum-recovery-ogp.png
intro: "Blast has shut down its L2 and opened an Ethereum recovery website for remaining funds, including unfinished withdrawals and Blast Mobile holdings."
author: sawinyh
tags: ["News", "DeFi"]
date: 2026-11-04T18:33:59+00:00
---

Blast [confirmed its L2 had shut down](https://x.com/blast/status/2117993462356197406) on November 4, 2026, and directed users with remaining funds to a recovery website on Ethereum. The operator said the website would remain active for 12 months, with a final support date of November 4, 2027.

The announcement covers funds in L2 wallets, pending withdrawals and Blast Mobile. The [recovery interface](https://blast.io/) lists $ETH, $WETH and $USDB as eligible assets and says users withdraw claims directly from recovery smart contracts on Ethereum mainnet.

## What the recovery site checks

Recovery starts with an address lookup. Users can enter the address that held their funds on Blast or a wallet approved to claim for that address. The interface gives the owner of a Safe or another smart wallet as an example of an approved claimant. It checks the connected wallet by default, but users can enter a different address.

The lookup includes unfinished withdrawals. The site's FAQ says: “It's included automatically. Check your address and it shows up with everything else.” This covers users who had started moving funds to Ethereum but had not completed their withdrawal when the chain closed.

The recovery interface also includes $WETH. The [ordinary withdrawal guide](https://docs.blast.io/withdrawals/withdraw-to-ethereum) describes a different process: the bridge did not support wrapped ether directly or count it in the withdrawable ether balance. Users had to unwrap it on Blast before initiating an ether withdrawal. Those steps describe the old bridge flow. They are not instructions to start a new transaction on the closed L2.

The smart-wallet lookup differs from the old website's restrictions, too. The ordinary bridge documentation covered externally owned accounts, including MetaMask, Rabby and hardware wallets. It directed Safe users and other contract accounts to separate contract-withdrawal guides. The recovery site now describes how to check an approved claimant's address as well as the address that held the assets.

## Blast Mobile has a different recovery instruction

Blast Mobile users are told to import their Mobile seed phrase into a wallet application such as MetaMask or Rabby, then connect that wallet to the recovery site. The FAQ warns that the resulting address will look different from the Blast Mobile address and says this is normal. According to the site, the Mobile balance then appears ready to claim.

The security instruction is explicit: “Only ever type your seed phrase into your wallet app, never into a website.” Users connect to the website after importing into the wallet application. The recovery page says the original Blast Mobile address does not exist on Ethereum, which is why Mobile users need this separate route.

This reverses an instruction readers may still find in the [older Blast Mobile withdrawal guide](https://docs.blast.io/withdrawals/blast-mobile). That guide said not to import the Mobile seed phrase into MetaMask because it belonged to a different address. It instead described withdrawing from the Earn App, sending funds from Mobile to a regular wallet on Blast, and bridging from that wallet to Ethereum. Those instructions required transfers on the operating L2.

The older Mobile guide also warned that the smart wallet could not manage funds on Ethereum. Transfers directly to its address there could become stuck or only recoverable back to Blast. Gas requirements differed between the app and the bridge wallet: sending from Mobile was free, but the separate wallet needed ether on Blast to initiate a withdrawal and ether on Ethereum to complete it. These requirements applied to the retired transfer route, not the current recovery claim.

The ordinary bridge sent withdrawals to the same wallet address on Ethereum that initiated them on Blast. Its History tab preserved unfinished work between visits. The recovery FAQ's different-address warning applies to the Mobile recovery procedure. Users should not substitute the old same-address bridge instructions for that procedure.

## The October deadline was for the normal interface

Blast first [announced the wind-down on October 2](https://x.com/blast/status/2106032805280891073). It said ongoing maintenance costs exceeded L2 revenue and that it saw no credible path to making the chain economically sustainable.

The plan gave users until October 26, 2026, to withdraw through the normal Blast interface. It also said assets would remain withdrawable afterward through bridge contracts on Ethereum L1. Defiprime previously covered [SynFutures' warning to Blast users ahead of that deadline](/synfutures-tells-blast-users-to-withdraw-by-october-26.html). November's announcement confirms the shutdown and provides the new recovery route. It does not reopen the October withdrawal window.

The October plan also called for withdrawing Blast's Lido assets, which the team expected to take approximately one week. Withdrawals were to be temporarily unavailable during that work, then resume with a reduced 24-hour delay. Those timings described the announced wind-down arrangements. They were not a processing-time promise for claims on the current recovery website.

## Why the old contract guides need context

The [ether contract-withdrawal guide](https://docs.blast.io/withdrawals/eth-from-contracts) describes the Ethereum yield manager and withdrawal queue behind the bridge. Users initiated a withdrawal on Blast, then proved it on Ethereum to add it to the queue. Finalization claimed ether from that queue and sent it to the recipient. The guide warned that even a finalized withdrawal could fail delivery if the recipient rejected ether or the call ran out of gas.

In the old ether flow, the messenger retained funds when delivery failed. Anyone could retry the failed message with `relayMessage` on the L1CrossDomainMessenger, supplying more gas or first fixing the recipient. That retry mechanism handled the bridge's delivery stage. It is not the recovery website's instruction for making a claim after shutdown.

The [stablecoin contract guide](https://docs.blast.io/withdrawals/usdb-from-contracts) describes $USDB withdrawals paying out as $DAI. Finalization created a withdrawal request in the Ethereum USD queue, and the recipient claimed the funds afterward. The recipient itself had to call the yield manager's claim function. Multisigs could do that, while some deposit-forwarder and sweeper contracts could not.

Under these bridge workflows, initiation, finalization and receipt of funds were separate stages. The guides describe those workflows; they are not independently verified readings of today's recovery contracts or outstanding balances. The current recovery page includes unfinished withdrawals in its address lookup and directs claims to recovery contracts on Ethereum.

Blast's announcement gives a final support date for the recovery website. It does not specify what access to unclaimed funds will look like after November 4, 2027.
