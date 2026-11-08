---
layout: blog
title: "Web3Auth identifies Keplr recovery wallets after key breach"
url: /web3auth-keplr-recovery-addresses.html
h1title: "Web3Auth identifies Keplr recovery wallets after key breach"
pagetitle: "Web3Auth identifies Keplr recovery wallets after key breach"
metadescription: "Web3Auth identifies recovery transfers from vulnerable Keplr accounts. Google and Apple login users are told to move remaining liquid assets."
category: blog
featured-image: /images/blog/web3auth-keplr-recovery-addresses-ogp.png
intro: "Web3Auth identified Keplr recovery wallets while affected Google and Apple login users were told to stop deposits and move remaining liquid assets."
author: sawinyh
tags: ["News"]
date: 2026-11-08T19:24:04+00:00
---

Web3Auth published a [list of Keplr recovery wallets](https://x.com/Web3Auth/status/2119314957057871935) on November 8 after moving assets out of vulnerable accounts. The company said it was securing funds with Keplr's assistance and that some transfers attributed to an attacker were its own recovery operations.

Keplr users who created accounts through Google or Apple login remain the potentially affected group. Keplr is telling them to stop sending funds to those accounts and move remaining liquid assets to a recovery-phrase or hardware-wallet account. Accounts originally created with a recovery phrase or hardware wallet are outside the incident's reported scope.

## Recovery transfers can explain an emptied account

Web3Auth said its partners began [whitehat recovery activities](https://x.com/Web3Auth/status/2119114303907196932) on vulnerable wallets that the attacker had not yet reached. The team described the operation as “utilizing the same path of the original attacker.” It did not explain the vulnerability or give technical details of how the recovery team reached the funds.

“We are aware that some of these transactions have been mistaken for attacker activity,” Web3Auth [said when introducing the list](https://x.com/Web3Auth/status/2119314958236401922). It identified the destinations as recovery addresses used to secure affected assets, not attacker-controlled wallets. Users checking an outgoing transfer can compare its destination with the addresses the company published.

Web3Auth had already acknowledged the difficulty of identifying those transfers. Its security team [said it was preparing verified addresses](https://x.com/Web3Auth/status/2119114423239647375) so users, blockchain teams and other stakeholders could separate legitimate recovery activity from potentially malicious transactions. The classification here relies on Web3Auth's attribution. This article has not independently reconciled the wallets' balances or transfers.

Keplr separately [warned that mitigation could leave accounts with reduced or empty balances](https://x.com/keplrwallet/status/2119117067500806350). It said a vulnerability in Web3Auth's infrastructure had led to a private-key breach for some social-login users and that it was helping protect their assets. An empty balance alone cannot establish how much was stolen: the account's outgoing transactions need to be checked.

Recovery work also covers assets that cannot be moved as readily as a liquid balance. “This is ongoing. Staked and locked assets add complexity and take longer,” Keplr said. Its transfer instruction concerns remaining liquid assets. The statement gives no completion timetable for handling staked or locked positions.

The published destinations span Cosmos Hub, Osmosis, Celestia, Akash and Noble in the [first address post](https://x.com/Web3Auth/status/2119314959624819054). A [second post](https://x.com/Web3Auth/status/2119314960891416918) names Injective, dYdX, Babylon, Axelar and Saga. The [final address post](https://x.com/Web3Auth/status/2119314962179060090) adds Agoric and an EVM destination. Web3Auth supplied these network labels and addresses; they do not establish how much was recovered on each network.

For Cosmos Hub, Web3Auth identifies `cosmos1atuap9kfnt6y8ykvn3437e7j3z8qffh3qtnmwu` as its recovery destination. For Injective, it identifies `inj1lqmdmuczn5rxn5jkc34wwrqdeh70etpf5wvt7g`. Its EVM destination is `0x413e4F4De7E5FF010913488F781E679e76f706dA`. These addresses are for checking past transfers. Affected users should not send more funds to them: Keplr's instructions direct remaining liquid assets to a recovery-phrase or hardware-wallet account.

Web3Auth [said it would extend the list](https://x.com/Web3Auth/status/2119314963420643529) as it verified additional addresses. The same post warned of impersonators and fraudulent recovery requests and directed users to official channels for subsequent updates.

## The response targets social-login wallets

In its [initial user alert](https://x.com/keplrwallet/status/2118926087615045807), Keplr said it had received reports of unauthorized transactions in accounts created with Google or Apple login and had raised them with Web3Auth. Its initial assessment excluded recovery-phrase and hardware-wallet accounts. The alert did not report a compromise across all Keplr accounts.

Keplr cofounder Josh Lee [located the incident at the provider](https://x.com/dogemos/status/2118984142151196677): “This was not a hack of Keplr's code. The incident originated at Web3Auth, a provider Keplr uses.” His statement also excluded secret-recovery-phrase and hardware-wallet accounts. Neither statement supplies a technical root-cause report that explains how the private keys became exposed.

Web3Auth had [temporarily paused its embedded wallet service](https://x.com/Web3Auth/status/2118814067359969745) when it first acknowledged the security issue. It said the issue affected services used by some third parties. “After an initial investigation, we’ve found no evidence that MetaMask users are impacted,” the company said. That assessment was qualified by the stage of the investigation.

The [developer documentation](https://docs.metamask.io/embedded-wallets) describes MetaMask Embedded Wallets as wallet infrastructure that applications integrate, not a standalone wallet. Its authentication flows serve dapps and blockchain wallets, handling onboarding and key management.

The [architecture documentation](https://docs.metamask.io/embedded-wallets/architecture/) describes front-end SDKs coordinating OAuth sign-in with the Embedded Wallets network. Applications use those SDKs to authenticate users, retrieve key material and create clients that sign requests on their behalf. The documented design splits wallet keys into shares and combines OAuth sign-in, trusted devices and recovery factors. It says no single party is intended to hold the full private key. The documentation describes the service's architecture; it does not identify which component failed in the Keplr incident.

## What affected users have been told to do

Keplr's current incident instructions are to avoid new deposits into potentially affected Google or Apple accounts and transfer remaining liquid assets to a recovery-phrase or hardware-wallet account. Its earlier alert also told users not to re-import or recreate the affected account elsewhere and said Google and Apple login was paused.

The wallet's [existing setup guide](https://help.keplr.app/extension/5R3bMyjtr2FwnBvJQuJwJu/create-a-new-wallet-with-keplr-extension/5R3bMyjtr4in9gwniq5zB6) distinguishes creating a new recovery-phrase account, importing an existing account and connecting a hardware wallet. It lists Ledger and Keystone as hardware options. The guide covers ordinary setup. Affected social-login users should follow the incident-specific notices for instructions on what to do now.

Keplr's support documentation also warns that its team will never reach out asking users to validate a wallet or type a recovery phrase or private key. Its incident notice directs users to Keplr's and Web3Auth's own accounts and warns against direct messages or links offering recovery.

Web3Auth [says recovered funds are safe](https://x.com/Web3Auth/status/2119114305475854345) and that it is working with Keplr on a path to return them, with further details to follow after operations finish. Keplr says an affected-account checking method is still being developed; the cited updates provide neither a claim procedure nor a return date.
