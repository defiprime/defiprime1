---
layout: blog
title: "Electrum patches server attack that turns fee bumps into theft"
url: /electrum-fee-bump-server-attack.html
h1title: "Electrum patches server attack that turns fee bumps into theft"
pagetitle: "Electrum patches fee-bump server attack in 4.8.3"
metadescription: "Electrum disclosed an active server attack that substitutes a payment before a fee bump. Version 4.8.3 checks wallet-input signatures before adding history."
category: blog
featured-image: /images/blog/electrum-fee-bump-server-attack-ogp.png
intro: "Electrum released a fix after a user reported losing money by raising the fee on a transaction a malicious server had substituted into wallet history."
author: sawinyh
tags: ["News"]
date: 2026-10-26T06:23:42+00:00
---

On October 24, 2026, Electrum disclosed an active malicious-server attack that could turn a routine transaction fee increase into a payment to an attacker. The wallet's [security advisory](https://github.com/spesmilo/electrum/security/advisories/GHSA-6jp4-8v48-cc5v) identifies version 4.8.3 as the fix, following a user report of money lost after signing a fee bump.

The developers received two reports with different outcomes. One user noticed that wallet history showed a different transaction after broadcasting a payment. The other increased the fee on the substituted transaction and lost money. The first user also reported that the original payment never reached Bitcoin's peer-to-peer network. The server had held it back.

## How the substituted payment becomes valid

The attack begins when a client broadcasts a new transaction through a malicious server. The server withholds the transaction and supplies a conflicting one in the client's history, replacing the intended outputs with an address controlled by the attacker. The wallet shows the substitute as an unconfirmed transaction. The original disappears from its history.

The replacement has invalid signatures at this point. Electrum's light-client design did not check those signatures before displaying the unconfirmed transaction. When the user manually increases its fee through replace-by-fee, or RBF, the client signs the substituted transaction with a higher fee. That signature authorizes the attacker-controlled payment, which previously lacked the authorization to spend the funds.

Both reporters said the attacker's destination was generated to match the last four characters of the legitimate recipient's address. A user checking only that suffix would see the expected characters even though the payment destination had changed. The advisory describes an attack that pairs a substituted transaction with an address made to resemble the intended recipient's at the end.

In the theft report, the server gave the substitute a zero fee. The developers presume this was meant to encourage the user to increase it; they do not establish the motive as fact. The reported loss followed the user's fee-bump signature on the altered payment that the server had placed in the wallet's history.

Electrum's [documented fee-increase workflow](https://electrum.readthedocs.io/en/latest/faq.html) starts in the history tab. The user right-clicks a replaceable transaction, chooses “Increase Fee”, sets the fee and confirms with “OK”. A window then displays an unsigned transaction. The user must choose “Sign” and “Broadcast” to complete the process, with a signing decision between selecting the history entry and sending the replacement.

Electrum makes transactions replaceable by default, except for Lightning channel opening and closing transactions. The transaction details screen marks an eligible payment with “Replace by fee: True”. The documentation gives replaceability as the condition for increasing a transaction's fee. Users can make that change as part of the wallet's ordinary handling of unconfirmed payments.

## Multiple servers, one transaction history

Electrum's [server-trust documentation](https://electrum.readthedocs.io/en/latest/faq.html#does-electrum-trust-servers) says the client tries to maintain connections to approximately ten servers by default. It subscribes to block-header notifications from all of them and periodically requests dynamic fee estimates. Those are the only jobs for every connected server except one. The multiple header sources help the client detect lagging servers, chain splits and forks.

The remaining connection supplies transaction history. Through that server, the client subscribes to its own addresses using hashes of their output scripts. It receives notifications of transactions that touch those addresses and synchronizes their existing history. The FAQ also describes the privacy cost: the server gets enough information to reasonably infer that the addresses belong to the same entity.

The client checks confirmed transactions through Simple Payment Verification, or SPV. For unconfirmed transactions, the documented trust model relies on the server. A server can also omit relevant transactions from what it supplies to the client, whether they are confirmed or unconfirmed. The block headers obtained through the other connections leave these limits on transaction history in place.

Fee estimates follow their own selection rules. With auto-connect disabled, the client uses only estimates supplied by the main server. With auto-connect enabled, it takes the median of estimates received from connected servers. Both modes apply low and high sanity limits. These settings govern the fee estimate; the disclosed attack changes the payment outputs in a history entry.

## What the patch checks

The fix, identified in the advisory as commit `90fe308`, checks signatures for mempool transaction inputs that belong to the wallet before adding those transactions to local history. Electrum calls these `wallet.is_mine` inputs. The check runs where the client previously accepted the invalid substitute into the history from which a user could select it for a fee bump.

The patch stops short of full transaction validation. Inputs paying from addresses outside the wallet, including those of incoming transactions, remain outside this signature check. Electrum lacks a full consensus engine and script interpreter. The developers say checking those other inputs would also require recursively validating unconfirmed parent transactions until reaching mined transactions, which the client already checks using SPV.

The advisory tells users who have not upgraded to verify output addresses and amounts against what they intended whenever they sign a transaction. That includes signing a fee increase. It also says this attack does not affect clients connected to servers they trust, such as servers they run themselves.

The first private disclosure arrived on October 11, before the fee-bump attack path was recognized. On October 18, the second reporter, Raju-K12, privately reported losing money after a fee bump. The fixed release was tagged on October 23; binaries and the public disclosure followed on October 24.

The advisory publishes neither the stolen amount nor transaction identifiers or attacker addresses. The loss is reported in the developer disclosure, which supplies no transaction trail for independent on-chain verification.
