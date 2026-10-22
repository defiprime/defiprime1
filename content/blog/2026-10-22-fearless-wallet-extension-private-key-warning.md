---
layout: blog
title: "Polkadot warns Fearless extension users to replace exposed keys"
url: /fearless-wallet-extension-private-key-warning.html
h1title: "Polkadot warns Fearless extension users to replace exposed keys"
pagetitle: "Fearless Wallet extension leaked private keys, Polkadot warns"
metadescription: "Polkadot urges Fearless browser extension users to create new keys and move funds after a disclosure of key-stealing code in affected releases."
category: blog
featured-image: /images/blog/fearless-wallet-extension-private-key-warning-ogp.png
intro: "Polkadot has warned Fearless Wallet browser extension users to replace their private keys and move funds after investigators found code that exported account secrets."
author: sawinyh
tags: ["News"]
date: 2026-10-22T09:25:08+00:00
---

Polkadot issued a security alert on October 21, 2026, warning that the Fearless Wallet browser extension had leaked users’ private keys since February 2025. The [Polkadot Community Foundation notice](https://forum.polkadot.network/t/security-notice-fearless-wallet-browser-extension-leaked-private-keys/19058) tells anyone who used the extension during that period to generate a new private key outside Fearless and move funds to the new account.

The [announcement](https://x.com/Polkadot/status/2112910039207800970) follows an investigation by the Polkadot Technical Fellowship on behalf of the Foundation. Fearless is independently built and maintained. The Foundation says it has never been an official Polkadot wallet.

The notice identifies browser extension versions 3.0.1, 3.0.3, 3.0.4 and 3.0.5 as containing the offending code. Investigators traced its introduction into the public source to February 19, 2025. The code sent account secrets to an external server when a user entered the wallet password.

## Which accounts are exposed

The warning covers every account held in the browser extension, including accounts whose keys were later imported into another application. Moving to a different wallet interface protects the funds only if the user also creates a new keypair and transfers assets to it. Changing the password or reinstalling the extension leaves the exposed key in use.

Investigators confirmed the code in Chrome packages. Firefox used the same source, but its extension was no longer listed, and investigators could not recover the published packages. The Foundation tells people who used the Firefox extension during the affected period to consider their keys compromised too.

The [linked technical report](https://hackmd.io/@gWEUMERvQZyR5MStsH26g/HyNOm782zg) distinguishes what investigators verified in published packages from what they found in the source. They recovered signed Chrome Web Store packages for versions 3.0.3, 3.0.4 and 3.0.5 and found the same code in each. They could not recover the published packages for versions 3.0.1 and 3.0.2, so the report’s descriptions of those releases rely on the repository.

The reviewed Android and iOS applications did not contain matching code. Their users can still be exposed through a shared key. The notice specifically identifies restoring a Fearless Google Drive backup into the browser extension as a way a mobile account’s phrase could have become compromised.

## How the extension exported secrets

The technical report follows a function named `fetchJettonInfo`. Its name suggests token information, but the function takes part in collecting and sending account secrets. The wallet calls it after a password-entry attempt, including an unsuccessful one. An incorrect password prevents the export paths from decrypting the account material, so no key is collected or sent.

In versions 3.0.3 through 3.0.5, the function first requests a configuration file from the `eth-enabled` branch of the public `soramitsu/shared-features-utils` repository. A field named `ton` is both the switch that enables the function and the destination server address. If that field is absent, the function stops.

The code can collect a recovery phrase or an account’s keystore file together with the wallet password. This material gives control of the account; a public address, normally used to fetch a balance, does not. The report says the collection covers the wallet’s main accounts. The code skips accounts that return no material.

Before transmission, the code applies AES encryption with an empty passphrase. Anyone holding the transmitted text can reverse that operation using the same empty passphrase, the report explains. The encryption provides no protection against the receiving server or someone who can see the request.

The function joins the encrypted values into the address parameter of a GET request to the server’s whitelist endpoint. Because the payload is in the request address, the secrets can also appear in the server’s access logs. If the function encounters an error, it stops silently. The user sees no warning.

The later versions keep a local list named `myAddresses` and skip accounts already recorded there, preventing repeat sends of the same account material. The earlier 3.0.1 variant has its server address written directly into the code and has no remote configuration switch.

The report dates removal of the offending code from the source to June 25, 2026, and says the remote switch has been off since October 10, 2026. Installed copies of versions 3.0.3 through 3.0.5 still contain the function. They check the switch whenever the user enters the wallet password, and restoring the configuration field could reactivate those copies.

## Moving liquid assets and handling locked positions

The Foundation recommends creating a fresh keypair in a different, well-maintained wallet and checking every chain the old account uses. Where possible, it advises using another application to operate the old account instead of entering the password in Fearless again. Funds controlled by the same exposed key elsewhere also need to move.

Staked balances, nomination-pool positions and assets locked by a governance vote may not be immediately transferable. Before beginning to unstake, the notice directs affected users to consider PAPI Rescue, a service built by the polkadot-api team for compromised accounts. It explicitly says never to share private keys with anyone, including that team.

The notice lists warning signs for users to check: staking stopped without permission, unbonding initiated unexpectedly, a changed staking reward destination, departure from a nomination pool, a removed governance vote, or small unexplained transfers. The list describes what affected users should look for, not what investigators found in every account that used the extension.

Once funds are safe, the Foundation advises removing the extension. Users who have lost assets should preserve account addresses, transaction hashes, dates and amounts as evidence. The notice also warns against unsolicited recovery offers. Legitimate assistance does not require handing over a private key, and purported recovery agents may be another scam.

The technical report describes what the code did without determining who wrote it or why. Investigators did not contact the receiving server and do not have its records. What happened to the collected secrets remains unresolved.
