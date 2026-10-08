---
layout: blog
title: "Cardano Foundation Spins Out Veridian With Tokenized Shares"
url: /cardano-foundation-veridian-tokenized-shares.html
h1title: "Cardano Foundation Spins Out Veridian With Tokenized Shares"
pagetitle: "Cardano Foundation Tokenizes Veridian Shares on Cardano"
metadescription: "Cardano Foundation spun out Veridian and tokenized its shares under CIP-0113, a proposed standard for programmable assets on Cardano."
category: blog
featured-image: /images/blog/cardano-foundation-veridian-tokenized-shares-ogp.png
intro: "Cardano Foundation spun out digital identity company Veridian and tokenized its shares as Swiss ledger-based securities under the proposed CIP-0113 standard."
author: sawinyh
tags: ["News"]
date: 2026-10-08T21:19:53+00:00
---

On 8 October 2026, the [Cardano Foundation announced](https://cardanofoundation.org/blog/veridian-spinout) the commercial spinout of Veridian and said the company's shares had been tokenized on Cardano under CIP-0113. The shares are ledger-based securities under Switzerland's DLT Act. The Foundation described them as the first asset of this kind deployed on Cardano.

Veridian is a digital identity company led by chief executive Thomas A. Mayfield. It was developed inside the Cardano Foundation for three years before the spinout. The company issues credentials for people, organizations and software agents. Those credentials can be verified or revoked without relying on a central identity database.

The equity deployment gives [CIP-0113](https://cips.cardano.org/cip/CIP-0113) a concrete securities use case. The proposal defines programmable tokens as assets that require a script to execute successfully before ownership can change. It remains in proposed status after an update on 29 September 2026.

## How the programmable shares work

Ordinary Cardano native tokens can move between addresses without transfer restrictions after minting. The CIP identifies that behavior as a barrier for tokenized securities because issuers may need allowlists, denylists, customer checks or other compliance rules. CIP-0113 adds those controls with existing Cardano primitives rather than a hard fork. From the ledger's perspective, the assets remain normal Cardano native tokens.

The standard separates shared infrastructure from the rules for each asset. Its first layer is an on-chain registry. Each registered token gets a node with the token policy and the hashes of its configuration scripts. The registry orders those nodes by policy and checks that a new token is configured correctly before accepting it. The proposal also provides deterministic smart-wallet addresses for immediate wallet support.

A second layer supplies common validation infrastructure. Programmable tokens sit at addresses controlled by a base script, while a user's stake credential identifies ownership. When a holder transfers one of these assets, the base script reads the live protocol configuration and delegates the transaction to the relevant validator. Every transaction spending programmable tokens must include a reference input containing the protocol parameters NFT.

The issuer supplies the third layer. A transfer script decides whether a holder-initiated transfer is allowed. A separate third-party script can define actions taken without the holder's permission, including seizure or forced transfers. An issuance script sets who can mint or burn the asset and under what conditions. The configuration can also include global state for information such as whether transfers are paused or the token is frozen.

Registration binds those rules to the asset policy. The registry checks that the declared minting credential matches the credential stored in the node, reconstructs the expected issuance policy, and requires the token's minting logic to run in the registration transaction. Registration may occur before the first mint, a sequence the proposal says is expected for real-world assets and supply-aware designs.

An issuer starts by writing the asset's transfer and issuance scripts. A third-party action script is optional. The issuer then deploys an issuance policy and adds a node to the registry with the hashes of the relevant scripts. The registry rejects a duplicate policy or an incorrectly constructed issuance policy. Tokens minted during or after registration must go to the common programmable-token script.

Each later transfer carries proof of whether the token policy is registered. If it is registered, the transfer must execute the script recorded for that policy in the same transaction. If the policy is absent, the validator treats the asset as a normal, non-programmable Cardano native token. This proof step is how the shared address distinguishes restricted assets from ordinary tokens.

Holders cannot assume that ownership permits an unrestricted transfer. Each transfer must satisfy the issuer's transfer script. A permitted third party may also act without holder consent if the asset's configuration allows it. Wallets and applications need to derive the user's smart-wallet address, supply registry proofs, and include the validator calls required by the standard.

For issuers, the design puts compliance behavior in token-specific scripts while sharing the registry and validation infrastructure across assets. The standard allows rules for transfers, issuance, seizure and pausing without changing Cardano's base ledger. It also means the exact rights attached to any programmable asset depend on its registered scripts, not only on the token appearing in a wallet.

## What Veridian is taking to market

The tokenized equity sits alongside Veridian's identity product. The company uses KERI and ACDC identity standards, and chief technology officer Fergal O'Connor maintains their core libraries. Veridian Wallet is live on iOS and Android. The company says it has mapped all 142 requirements in Utah's State-Endorsed Digital Identity implementation guide.

Veridian is already used by Masumi, an AI agent payment and identity network on Cardano. Masumi uses Veridian credentials so a counterparty can check an agent's identity before payment and revoke that identity if the agent is compromised. This connects the company's identity product with payment authorization, while the tokenized shares demonstrate the programmable-asset standard on the same network.

The spinout also changes Veridian's corporate structure. Cardano Foundation chief executive Frederik Gregaard is chair of Veridian. Gregaard and the Foundation's chief legal officer, Nicolas Jacquemart, joined the board. Mayfield said independence would let the company sell to governments and enterprises after development inside the Foundation.

Veridian plans to seek strategic partners and investors in 2027. It intends to expand work with US state governments, its European enterprise business, its issuer network in Asia-Pacific and identity tools for AI agents. The next technical question is whether CIP-0113 moves beyond proposed status with the deployed Veridian equity as its first announced securities implementation.
