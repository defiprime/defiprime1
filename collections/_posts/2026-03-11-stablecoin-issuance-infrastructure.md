---
git-date:
layout: [blog]
title: "Stablecoin Issuance Infrastructure in 2026: The Full Map"
permalink: stablecoin-issuance-infrastructure-2026
h1title: "Stablecoin Issuance Infrastructure in 2026: The Full Map"
pagetitle: "Stablecoin Issuance Infrastructure in 2026: The Full Map"
metadescription: "A comprehensive guide to stablecoin issuance in 2026: models, regulatory frameworks, technical architecture, service providers, stablechains, and step-by-step launch guidance."
category: blog
featured-image: /images/blog/stablecoin-issuance-ogp.png
intro: "Everything you need to know about issuing a stablecoin in 2026: models, regulation, infrastructure, and the new stablechains."
author: sawinyh
tags: ["DeFi Guides"]
---

Stablecoins are blockchain tokens pegged 1:1 to a fiat currency, usually the U.S. dollar. They give you the programmability and speed of crypto without the price swings. That simple combination has turned them into plumbing for DeFi, cross-border payments, remittances, treasury management, and on-chain settlement.

The market crossed $250 billion in total supply by mid-2025 and has continued growing. As of early 2026, total stablecoin market capitalization is [above $310 billion](https://defillama.com/stablecoins) according to DefiLlama data. Tether's USDT sits around $183-187B (roughly 60% of the market), Circle's USDC around $74-76B. Growth has been driven by regulatory clarity in the U.S. and EU and a wave of institutional adoption.

This article is for anyone considering issuing a stablecoin, evaluating the infrastructure to do so, or trying to map the competitive field. It covers issuance models, regulatory frameworks, technical architecture, service providers, the new "stablechains," step-by-step launch guidance, and the risks worth planning for.

---

## How stablecoin issuance works

Issuing a stablecoin means designing, launching, and operating a token where new units are minted only when equivalent reserves or collateral are locked up. Tokens can be burned (destroyed) when someone redeems. The issuer's job is keeping that mint-burn cycle trustworthy, transparent, and compliant.

You can either build it yourself with custom smart contracts, banking partnerships, and compliance infrastructure, or use a turnkey platform (often called "Stablecoin-as-a-Service"). Most organizations in 2026 choose the turnkey route, at least to start. But understanding both matters. Even turnkey solutions force architectural decisions that stick with you for years.

---

## Which issuance model fits?

Every stablecoin starts with a model decision. Your choice determines capital requirements, regulatory burden, revenue mechanics, and risk profile.

![Four stablecoin issuance models: fiat-backed, crypto-collateralized, algorithmic, and tokenized deposits](/images/blog/stablecoin-issuance-models.png)

### Fiat-backed (custodial / off-chain reserves)

The dominant model, accounting for over 90% of the market. Also the one regulators prefer.

Users or institutions deposit fiat (USD cash, Treasuries, repos, money market funds, or insured bank deposits) with the issuer or a qualified custodian. The issuer mints an equivalent number of tokens on-chain. When someone redeems, the tokens get burned and the reserves are released. Reserves sit in segregated, audited accounts.

The economics: issuers earn yield on reserves, primarily from short-term Treasuries. That's how Circle, Tether, and Paxos make money.

The trade-off is centralization. You depend on banks and custodians, you need licenses, and you're subject to ongoing audits. But for most businesses, this is the right starting point. USDC, USDT, PayPal's PYUSD, and newer entrants like KlarnaUSD (issued via Bridge) all use this model.

### Crypto-collateralized (on-chain, over-collateralized)

Users deposit volatile crypto (typically ETH) into smart contracts at 120-200% collateralization ratios. Price oracles are central to this model. They're external data feeds (Chainlink is the most widely used) that supply real-time asset prices to on-chain contracts. If oracle data is stale, manipulated, or delayed, liquidations can misfire or fail entirely, potentially threatening the peg. Oracle risk is one of the less-discussed but more dangerous failure modes in crypto-collateralized stablecoins. If the collateral ratio drops below a threshold, automatic liquidation kicks in. Minting and burning happen entirely through smart contracts.

This model is fully transparent and doesn't need traditional banking relationships. The downside is capital inefficiency: you lock up significantly more value than you mint. Liquidation risk during volatile markets is real. MakerDAO's DAI is the best-known example. Ethena's USDe is a newer hybrid.

Revenue comes from stability fees and liquidation penalties rather than reserve yield.

### Algorithmic / hybrid

Pure algorithmic stablecoins use smart contracts to expand and contract supply through incentive mechanisms, with little or no collateral backing. After the TerraUSD collapse in 2022, this model is largely discredited. Most regulators have banned or restricted it. The EU's MiCA framework prohibits purely algorithmic stablecoins outright.

Hybrids like FRAX combine partial reserves with algorithmic mechanisms, but adoption remains niche. Unless you have a very specific reason, avoid this model in 2026.

### Tokenized deposits / bank-integrated

Tokens represent direct claims on insured bank deposits or tokenized reserves on permissioned or public chains. JPMorgan's JPM Coin (now JPMD) is the primary example. These stablecoins integrate directly with traditional banking rails.

The advantage is deposit insurance and the trust infrastructure of established banks. The downside is ecosystem lock-in and limited multichain reach. This model works best for large financial institutions that already have a banking charter and want to extend their rails onto blockchain.

---

## Regulatory frameworks in 2026

Regulation is simultaneously the biggest barrier and biggest enabler of stablecoin issuance. If you don't understand the regulatory environment, the rest of this article won't matter much.

The global picture has converged around a few core requirements: 1:1 reserves in high-quality liquid assets, licensing, redemption rights at par, regular audits, and AML/KYC compliance. Most frameworks also restrict or prohibit yield payments directly to stablecoin holders, keeping the instrument classified as a payment tool rather than a security. But the specifics vary by jurisdiction, and the debate around yield-bearing stablecoins is active (the White House held closed-door meetings on this topic as recently as February 2026).

![World map highlighting major stablecoin regulatory jurisdictions: US, EU, UK, Singapore, Japan, and Hong Kong](/images/blog/stablecoin-regulatory-landscape.png)

### United States: the GENIUS Act and federal/state oversight

The GENIUS Act, passed in 2025, created the first comprehensive federal framework for stablecoin issuance. Only "permitted" issuers can operate: FDIC-insured banks and their subsidiaries, or federally/state-qualified non-bank issuers.

An important structural detail: oversight is split between federal and state regulators depending on issuer type and size. Non-bank issuers with under $10B in circulation can be regulated at the state level under existing money transmitter frameworks. Larger issuers and bank-affiliated issuers fall under federal oversight via banking regulators, with the OCC playing a role for non-bank issuers at the federal level. It's not a single-regulator model.

Requirements: 1:1 reserves in cash, Treasuries, repos, and insured deposits. Monthly attestations and annual audits for large issuers. Redeemable at par. No interest payments to holders under the current framework. Foreign issuers face restrictions unless their home jurisdiction has equivalence arrangements.

### European Union: MiCA

The Markets in Crypto-Assets regulation took effect across 2024-2025 and creates two categories: e-money tokens (EMTs, pegged to a single currency) and asset-referenced tokens (ARTs). Issuers must be EU credit institutions or authorized electronic money institutions. Reserves must be held in high-quality liquid assets at EU banks.

Pure algorithmic stablecoins are banned. Redemption at par is mandatory, often without fees. The ECB has oversight authority for systemically important stablecoins. Full authorization is required by July 1, 2026 for all issuers operating in the EU.

### Other jurisdictions

The UK is building its framework through FCA and Bank of England e-money rules, with caps for systemic stablecoins. Singapore requires a MAS license and full backing. Japan restricts issuance to banks and trust companies. Hong Kong has introduced HKMA licensing for HKD-pegged stablecoins.

The pattern across all of these: convergence on reserves, redemption rights, and licensing. Differences mainly come down to issuer eligibility and acceptable reserve assets. The U.S. favors Treasuries, the EU favors bank deposits.

---

## Technical architecture: what a modern stablecoin stack looks like

Whether you build or buy, you need to understand the components.

![Layered architecture diagram of the modern stablecoin technology stack, from blockchain layer up to fiat on/off-ramps](/images/blog/stablecoin-tech-stack-architecture.png)

### Core smart contracts

Deployed on one or more blockchains (Ethereum, Solana, Algorand, others), these handle minting, burning, and transfer logic. For 2026 compliance, your contracts need role-based access control (minter, burner, pauser, blacklister, clawback roles), pause and freeze functionality for AML and sanctions enforcement, and blacklisting and clawback for court orders.

Most teams start with audited frameworks like OpenZeppelin's ERC-20Upgradeable combined with Pausable, AccessControl, and UUPS proxy patterns for upgradeability. Some blockchains offer built-in compliance controls at the protocol level. Algorand, for instance, has native freeze and clawback functions that make it attractive for institutional issuers without requiring custom contract logic.

Advanced standards like Tempo's TIP-20 (on their payments-first L1) add native protocol-level features: built-in mint/burn/transfer restrictions, RBAC, transfer memos for reconciliation, and native yield distribution, all without extra contract complexity.

### Issuer backend system

A secure, centralized system (typically API-driven) that authorizes minting and burning events. It verifies that fiat deposits arrived before instructing the smart contract to mint, and confirms burn events before releasing fiat for redemption. This is the operational core that ties on-chain activity to off-chain banking.

### Custody and reserve layer

Fiat and other reserve assets sit in custody accounts at regulated banks or trust companies. Qualified custodians provide regular attestations. Typical reserve composition includes cash, short-term U.S. Treasuries, repos, money market funds, and insured bank deposits. Increasingly, reserves also include tokenized Treasuries from providers like BlackRock, WisdomTree, and Superstate, which generate yield while maintaining liquidity. As a point of reference, [Tether's Q4 2025 attestation](https://tether.io/news/tether-delivers-10b-profits-in-2025-6-3b-in-excess-reserves-and-record-141-billion-exposure-in-u-s-treasury-holdings/) reported $141 billion in total U.S. Treasury exposure (direct holdings plus overnight reverse repos), making it one of the largest holders of U.S. sovereign debt globally.

### Compliance and identity layer

KYC/AML checks and transaction monitoring tools integrate with the issuance and redemption flow. Only verified users can mint or redeem. All on-chain activity gets screened for illicit finance. Blockchain analytics providers like Chainalysis and Blockaid are standard parts of the stack.

### Fiat on/off-ramps

The bridges between blockchain and traditional finance. Licensed money services businesses like Coinme provide the infrastructure to move funds between bank accounts, cards, and on-chain stablecoins.

### Multichain deployment

Most stablecoins in 2026 operate across multiple chains. You can deploy natively on each chain, use cross-chain bridges or interoperability protocols (Axelar, LayerZero, Circle's CCTP), or issue on specialized payment-focused L1s. The choice depends on your target users and use cases.

### Security

Multiple independent audits are table stakes. Beyond that: timelocks on critical contract functions, multi-sig governance, invariant checks, and HSM or MPC-based key custody. Daily reconciliation between on-chain supply and off-chain reserves is standard practice, along with monthly attestations.

---

## Stablecoin-as-a-Service providers

Most businesses in 2026 use a turnkey provider rather than building from scratch.

### Paxos

The most established player, operating since 2018. Paxos is the issuer behind PayPal's PYUSD and has partnerships with Interactive Brokers and other large enterprises. They handle regulatory compliance, reserve custody, and minting/redeeming technology across multiple blockchains.

They've processed over $180B in activity and focus on enterprise partnerships. Expect enterprise-level pricing to match.

### Circle

Circle is first and foremost the issuer of USDC, the second-largest stablecoin. They don't offer white-label issuance of fully custom-branded stablecoins the way Brale or Bridge do. What they do offer is programmable wallets, Circle Mint for institutional USDC access, and the Circle Payments Network (CPN) for connecting financial institutions. If you want to build payment products on top of an existing, highly regulated stablecoin rather than issuing your own, Circle's stack is the natural choice.

Circle supports 20+ blockchains, offers API-based integration, and charges transaction-based fees. Their cross-chain transfer protocol (CCTP) is a real differentiator for multichain deployments. Circle also went public on the NYSE in 2025, adding another layer of transparency.

### Brale

A U.S.-regulated issuance platform that lets businesses create and manage their own fiat-backed stablecoins. Brale acts as the legal issuer under its money transmitter licenses, handling custody, reserve management, and compliance while providing APIs for minting and burning across 20+ blockchains.

Good option for organizations that want a custom-branded stablecoin without building the regulatory infrastructure themselves. Revenue-share pricing model.

### Bridge (Stripe-acquired)

Bridge offers an Open Issuance API to launch and manage a branded stablecoin with minimal code. They handle reserves, liquidity, compliance, and fiat on/off-ramps. Stripe's acquisition gives Bridge access to an enormous merchant network.

Bridge has received preliminary approval to establish a national trust bank, which would let them offer regulated custody and reserve management under a federal framework.

### Coinbase Custom Stablecoins

[Launched December 18, 2025](https://www.coinbase.com/developer-platform/products/stablecoin-as-a-service), this is Coinbase's "stablecoin-as-a-service" offering. It lets businesses create custom-branded stablecoins backed 1:1 by USDC and other USD-stablecoins, with Coinbase handling issuance, smart contracts, compliance, and custody. First partners include Flipcash, Solflare, and R2. [Separately](https://www.pymnts.com/blockchain/2025/coinbase-launches-stablecoin-as-a-service-to-help-businesses-create-their-own-tokens), Coinbase is also powering stablecoin-denominated institutional funding for Klarna via USDC.

Important nuance: at launch, Custom Stablecoins use USDC as the underlying collateral rather than direct fiat reserves. That means Coinbase is acting as an issuance layer on top of Circle's stablecoin, not as a direct fiat-to-stablecoin issuer like Paxos or Brale. Coinbase has applied for an OCC national trust charter, which could eventually allow it to custody reserves directly.

### Frax Finance

Known for its hybrid stablecoin model, Frax now offers "GENIUS-compatible" white-label infrastructure. Per project announcements, Sonic Labs used Frax's framework to launch a USSD stablecoin backed by tokenized Treasuries. Frax provides modular smart contract infrastructure with built-in composability through LayerZero.

The DeFi-native option, designed for teams comfortable with on-chain tooling.

### Stably

A primary partner for blockchain platforms like Algorand and Stacks. Stably provides a Stablecoin-as-a-Service suite including fiat on/off-ramps, multi-chain issuance, and compliance. They specialize in stablecoins pegged to various fiat currencies beyond the dollar.

### M0

M0 is a programmable stablecoin issuance protocol that separates token logic from reserve custody. It lets businesses build "stablecoin extensions," which are custom-branded tokens with their own compliance rules, yield mechanics, and access controls, all built on a shared liquidity and interoperability layer. M0 raised a [$40M Series B](https://thedefiant.io/newsletter/real-world/heres-how-stablecoin-issuer-m0-is-different) and has over $779M in on-chain supply minted. [Bridge (Stripe) uses M0's protocol under the hood](https://www.coindesk.com/business/2025/08/20/stripe-s-bridge-teams-up-with-m0-protocol-to-issue-stablecoins-starting-with-metamask-s-musd) for stablecoin issuance, as confirmed when MetaMask launched mUSD. [MoonPay's PYUSDx framework](https://www.crypto-reporter.com/press-releases/moonpay-m0-and-paypal-announce-pyusdx-the-infrastructure-platform-for-pyusd-backed-stablecoins-123263/) also runs on M0 infrastructure.

Worth watching closely. M0's approach of decoupling reserve management from token issuance could become the default pattern for application-specific stablecoins.

### Other providers worth noting

**Agora** offers regulated stablecoin issuance with a trust-based approach. **Bastion** takes a similar regulated trust posture. **Anchorage Digital** is primarily a federally chartered crypto bank providing qualified custody and regulated banking services. It's not a full stablecoin issuance platform, but it plays a role in the custody and compliance layer that issuers need. **Fireblocks** provides infrastructure and custody tooling (MPC wallets, workflow automation, settlement) across 100+ chains. It processes roughly 15% of global stablecoin volume and is used by 300+ banks and payment providers, but it's infrastructure plumbing, not a legal issuer of stablecoins. **BitGo** offers qualified custody infrastructure. **Cobo** provides full-suite payment operations, combining MPC custody, payment APIs, and Wallet-as-a-Service across 80+ chains. **Tassat** focuses on tokenized deposits and real-time settlement for institutional digital asset operations, including its Link platform for real-time collateral and settlement workflows.

---

## The stablechains: purpose-built L1s for stablecoin payments

This is probably the most interesting development in stablecoin infrastructure right now. Starting in 2025, a new category of "stablechains" appeared: Layer-1 blockchains built specifically for stablecoin payments and issuance. Instead of deploying on general-purpose chains like Ethereum or Solana, issuers can use infrastructure where stablecoins are first-class citizens rather than an afterthought.

Three projects lead this category: Tempo, Circle Arc, and Tether Plasma. All three are EVM-compatible, target sub-second finality, and aim to make stablecoin transactions competitive with Visa, ACH, and SWIFT. They differ in philosophy, ecosystem, and who they're designed for.

A word of caution: this category is very early. As of March 2026, only Plasma has a live mainnet with real production volume. Tempo and Arc are on public testnet with mainnet launches expected later in 2026. Performance claims (TPS targets, finality times) are based on testnet data or design targets, not proven production metrics at scale. Partnership announcements reflect stated intentions and early pilots, not necessarily live integrations processing real money. That said, the backers (Stripe, Circle, Tether) have the resources and distribution to make these projects matter, which is why they're worth tracking closely.

![Three stablechains side by side: Tempo (multi-stablecoin, payments-first), Circle Arc (USDC-native, FX engine), and Tether Plasma (USDT-native, zero-fee transfers)](/images/blog/stablechains-tempo-arc-plasma.png)

### Tempo

Incubated by Stripe and Paradigm with over $500M raised. Tempo is a payments-first L1 that takes a deliberately neutral approach. No native token. Gas fees can be paid in any stablecoin through an enshrined AMM that auto-swaps to validators. Issuers aren't forced into any single stablecoin ecosystem.

Tempo's native TIP-20 token standard includes built-in mint/burn restrictions, protocol-level compliance (TIP-403 Policies), delegatable RBAC with on-chain audit logs, transfer memos for off-chain reconciliation, and native yield distribution. Design targets include 100,000+ TPS and roughly 0.6-second deterministic finality (no re-orgs), though these are pre-mainnet projections, not production-verified metrics.

Other protocol primitives: a Fee AMM (pay gas in any stablecoin, creating structural demand), a native stablecoin DEX for on-chain liquidity and FX (on roadmap), dedicated payment lanes with guaranteed blockspace, and account abstraction with passkey support.

Per Tempo's announcement materials, the ecosystem roster includes Stripe, Shopify, Nubank, Klarna, DoorDash, Deel, Revolut, Visa, Anthropic, and Deutsche Bank. These are announced partnerships, not necessarily confirmed live integrations. Klarna's involvement is separately confirmed through its [Coinbase stablecoin funding announcement](https://www.pymnts.com/blockchain/2025/coinbase-launches-stablecoin-as-a-service-to-help-businesses-create-their-own-tokens).

Status: public testnet live, mainnet expected H1 2026.

Best for issuers who want maximum flexibility, multi-stablecoin support, and deep payments integration with minimal vendor lock-in. Contact: partners@tempo.xyz.

### Circle Arc

Circle's own L1, announced August 2025. Arc makes USDC the native gas token, creating a fully dollar-denominated chain. It uses Malachite BFT consensus for sub-second finality (around 780ms) and targets over 50,000 TPS.

The defining feature is a built-in FX engine with on-chain RFQ and PvP settlement, which makes it attractive for cross-currency treasury operations. Arc deeply integrates Circle's stack: CCTP, native mint/burn, Gateway, and on/off-ramps. It also offers opt-in privacy designed for compliance-ready institutional use.

Partners include BlackRock, Visa, Goldman Sachs, Mastercard, HSBC, AWS, Coinbase, and OpenAI.

Status: public testnet with 100+ institutional participants, strong activity since October 2025. Mainnet expected 2026.

Best for institutions already in the USDC ecosystem, or those needing on-chain FX and capital markets infrastructure.

### Tether Plasma

The only stablechain with a fully live mainnet as of March 2026. Plasma is Tether's chain, built around USDT with a zero-fee transfer model using a Paymaster contract. Sub-second finality at 1,000+ TPS. Over $373M raised.

Plasma supports 25+ stablecoins but is clearly USDT-centric. Per Tether's communications, it has attracted significant deposits and become one of the larger USDT networks by balance. It includes a native Bitcoin bridge and optional confidential transactions. The ecosystem spans 100+ DeFi partners (including Aave) per project announcements.

Best for USDT-focused use cases, retail and emerging-market payments, and anyone who wants live production volume today.

### How to choose between them

The decision comes down to a few questions.

What's your primary stablecoin? USDT points to Plasma. USDC points to Arc. Multi-stablecoin or custom-branded points to Tempo.

Who are your target users? Retail and emerging-market payments: Plasma. Enterprise and institutional capital markets: Arc. Fintechs, merchants, embedded finance: Tempo.

How much execution risk can you tolerate? Plasma is live but carries heavier regulatory scrutiny as a Tether-affiliated project. Tempo and Arc have strong backers but are pre-mainnet.

Many issuers are hedging by testing or launching on multiple chains simultaneously.

---

## End-to-end launch stacks

Several providers bundle token issuance, reserve management, compliance, and payment rails into a single integrated offering.

**Polygon's Open Money Stack** bundles blockchain settlement, enterprise-grade wallets, and regulated fiat on/off-ramps (via Coinme) into one API. Transactions settle in under 2 seconds at roughly $0.002 each. Institutions can move money from a bank account into a stablecoin, settle on-chain, and convert back to fiat without juggling multiple vendors.

**Cobo** combines MPC custody, payment APIs, and Wallet-as-a-Service for high-volume stablecoin operations. It supports 80+ chains and plugs into existing treasury systems.

**Brale's unified platform** lets an enterprise launch a stablecoin and have it instantly provisioned with on/off-ramps, pricing, APIs, and reporting, all under Brale's regulatory umbrella.

---

## Step-by-step: how to issue a stablecoin in 2026

The practical sequence, from concept to production.

![7-step roadmap for launching a stablecoin: define purpose, secure reserves, build technology, set up mint/burn flows, ensure compliance, launch and distribute, ongoing operations](/images/blog/stablecoin-launch-roadmap.png)

**1. Define purpose and structure.** What is the stablecoin for? Payments, treasury management, loyalty programs, embedded finance? Your answer determines which issuance model, platform, and chain make sense. Fiat-backed is the right choice for most use cases. Pick your platform early since switching later is expensive.

**2. Secure banking and reserves.** Partner with qualified custodians or banks. Set up segregated 1:1 reserve accounts holding cash, short-term Treasuries, repos, money market funds, or insured deposits. Diversify across custodians where possible. Stress-test your liquidity for redemption spikes. Turnkey providers like Brale or Paxos handle much of this, but you still need visibility into the reserve structure.

**3. Develop or integrate the technology.** If building custom: write and audit your smart contracts (start with OpenZeppelin frameworks), implement compliance controls (RBAC, pause, freeze, clawback), choose your target chains, and get multiple independent security audits. If using a platform: integrate via API (Bridge, Brale) or deploy using native token standards (TIP-20 on Tempo).

**4. Set up issuance and redemption flows.** Mint tokens when verified fiat deposits arrive. Burn tokens on redemption and release corresponding reserves. Build continuous reconciliation between on-chain supply and off-chain reserves. Publish monthly attestations.

**5. Ensure compliance and transparency.** Obtain the necessary licenses (or confirm your turnkey provider holds them). Implement KYC/AML for all mint and redeem operations. Set up transaction monitoring. Publish reserve reports and audit results. Under the GENIUS Act, large issuers need monthly attestations and annual audits. MiCA requires full authorization by mid-2026.

**6. Launch and distribute.** Deploy on your target chain(s). Get listed on exchanges and DEXs. Provide initial liquidity. Monitor the peg continuously. Integrate into real payment flows: payroll via Deel on Tempo, merchant checkout through Stripe, remittance corridors.

**7. Ongoing operations.** This is where most of the work lives. Regular audits, risk monitoring, smart contract upgrades, regulatory reporting, and responding to compliance events (sanctions, court orders, suspicious activity). It never stops.

---

## Provider comparison

| Provider | Core capability | Target customers | Supported chains | Complexity / cost |
|---|---|---|---|---|
| Paxos | Regulated issuance, custody, proven at scale | Large enterprises, fintechs | Ethereum, others | Medium. High cost (enterprise contracts) |
| Circle | USDC issuer, programmable wallets, CPN, high liquidity | Startups to enterprises | 20+ chains | Low. Transaction-based fees |
| Brale | Full-stack issuance, acts as legal issuer, multi-chain | Startups to enterprises | 20+ chains | Low. Revenue-share pricing |
| Bridge (Stripe) | Open Issuance API, fiat on/off-ramps, Stripe distribution | Enterprises, fintechs | Multiple chains + Tempo | Low. Transaction-based fees |
| M0 | Programmable issuance protocol, shared liquidity layer | Developers, fintechs, wallets | Ethereum, multi-chain | Low-medium. Protocol-based |
| Coinbase Custom Stablecoins | Stablecoin-as-a-service, USDC-collateralized branded tokens | Enterprises, fintechs | Base, Ethereum (expanding) | Low. Revenue-share |
| Frax | White-label modular infrastructure, RWA backing | Blockchain networks, protocols | EVM-compatible via LayerZero | Medium. Variable cost |
| Polygon | End-to-end "Open Money Stack" | Institutions, payment companies | Polygon, multi-chain via Agglayer | Low. Volume-based pricing |
| Cobo | Enterprise payments, MPC custody, treasury automation | High-volume institutions | 80+ chains | Medium. Institutional pricing |
| Fireblocks | Infrastructure/custody tooling, MPC wallets, settlement (not an issuer) | Large institutions | 100+ chains | Medium. Institutional licensing |

## Stablechains comparison

| Aspect | Tempo | Circle Arc | Tether Plasma |
|---|---|---|---|
| Backing | Stripe + Paradigm ($500M+) | Circle | Tether/Bitfinex ($373M+) |
| Status (March 2026) | Public testnet, mainnet H1 2026 | Public testnet, mainnet 2026 | Mainnet live |
| Performance | 100k+ TPS target (unverified), ~0.6s finality (design) | 50k+ TPS target, ~780ms finality (testnet) | 1k+ TPS, sub-second finality (production) |
| Gas model | Any stablecoin (no native token) | Native USDC | USDT-native + Paymaster (zero-fee USDT) |
| Stablecoin focus | Issuer-agnostic, multi-stablecoin | USDC-centric | USDT-centric (25+ supported) |
| Key primitives | Stable DEX, payment memos, dedicated lanes, TIP-20 | FX engine, opt-in privacy, CCTP integration | Zero-fee USDT, Bitcoin bridge, confidential txs |
| Target users | Fintechs, merchants, embedded finance | Institutions, capital markets | Retail, emerging markets, DeFi |

---

## Real-world examples

A few cases that show how this infrastructure comes together in practice. Note: some of these are announced projects or early-stage deployments, not fully scaled production systems. Where possible, I've verified against public announcements and press coverage.

**MetaMask USD (mUSD) on M0/Bridge.** [Announced August 2025](https://metamask.io/news/metamask-announces-stablecoin-metamask-usd) by Consensys, MetaMask's native stablecoin is the first issued by a self-custodial wallet. It uses Bridge for issuance and reserve management with [M0's protocol for the on-chain infrastructure](https://www.coindesk.com/business/2025/08/20/stripe-s-bridge-teams-up-with-m0-protocol-to-issue-stablecoins-starting-with-metamask-s-musd). Planned to launch on Ethereum and Linea, with spending via MetaMask Card at Mastercard merchants.

**Klarna's stablecoin initiatives.** [Klarna partnered with Coinbase](https://www.pymnts.com/blockchain/2025/coinbase-launches-stablecoin-as-a-service-to-help-businesses-create-their-own-tokens) in December 2025 for USDC-denominated institutional funding. Separately, Tempo's announcement materials list Klarna as an ecosystem partner launching "KlarnaUSD" via Bridge on Tempo, but public documentation of that specific deployment is limited beyond Tempo's own communications. Worth monitoring but not yet a confirmed live product.

**Sonic Labs' USSD via Frax.** Per Frax and Sonic project communications, Sonic used Frax's white-label infrastructure and backed USSD with tokenized Treasuries. Independent documentation is thin, but it illustrates the modular approach: a blockchain network launching a native stablecoin by composing existing infrastructure rather than building from scratch.

**Stablecorp's QCAD.** A Canadian dollar stablecoin that uses VersaBank as federally regulated custodian for reserves through VersaBank's VersaVault platform. Stablecorp manages issuance and compliance while leaning on established banking infrastructure for credibility.

**Stable Sea with BitGo.** A B2B infrastructure platform that partners with BitGo for regulated custody and trading. Newer platforms can assemble best-in-class services from existing providers rather than building everything internally.

---

## Risks worth planning for

Good infrastructure reduces risk. It doesn't eliminate it. Here's what actually goes wrong.

**Depegging.** Market shocks, collateral liquidation cascades, or loss of confidence can push a stablecoin off its peg. Even fiat-backed stablecoins aren't immune. USDC briefly lost its peg in March 2023 when Silicon Valley Bank failed with a portion of Circle's reserves held there.

**Custody and banking failures.** Your stablecoin is only as safe as your custodian. Diversify where possible and understand the insolvency protections (or lack thereof) for your reserve accounts.

**Smart contract bugs.** A vulnerability in your minting or burning logic can be catastrophic. Multiple independent audits are the minimum. Timelocks, multi-sig controls, and bug bounty programs add layers of defense.

**Regulatory changes.** The GENIUS Act and MiCA are still relatively new. Rules will evolve. Non-compliance carries real consequences: fines, loss of license, blocked market access. Build compliance into the product from day one, not as an afterthought.

**Sanctions and illicit finance exposure.** Stablecoins are tools, and bad actors use them. You need transaction monitoring and the ability to freeze or clawback assets when legally required.

**Operational risk.** Stablecoin operations run around the clock. Reconciliation errors, oracle failures (for crypto-collateralized models), and infrastructure outages compound quickly.

**Algorithmic model risk.** If you're considering an algorithmic or lightly collateralized design, this carries the highest systemic risk. The TerraUSD collapse proved that incentive mechanisms alone can't maintain a peg under stress.

---

## Best practices for 2026 issuers

Automate reconciliation between on-chain supply and off-chain reserves. Manual processes break at scale.

Use bankruptcy-remote structures for reserve accounts. If your company has financial trouble, the reserves should be legally protected for token holders.

Build compliance into the product. Freeze, clawback, and blacklisting capabilities aren't just regulatory checkboxes. They're what institutional customers and regulators look for before working with you.

Partner with blockchain analytics providers from day one. Chainalysis, Blockaid, and similar firms provide transaction monitoring that regulators expect.

Publish clear redemption policies. Specify timelines, fees (if any), minimum amounts, and the process for large redemptions. Ambiguity erodes trust.

Start with a USD peg for maximum liquidity and market access. Non-USD pegs have their place, but infrastructure, liquidity, and regulatory clarity are all strongest for dollar stablecoins.

Plan for multichain or dedicated-chain deployment from the start. Retrofitting cross-chain support later is painful.

Consider starting on a turnkey platform or specialized L1 for speed, then evaluate custom infrastructure as you scale.

---

## Where this is heading

The infrastructure to launch a compliant stablecoin in 2026 exists. You can go from concept to live product in weeks through turnkey providers and purpose-built L1s. That speed would have been absurd even two years ago.

The decisions you face: which issuance model fits (fiat-backed for almost everyone), which platform or chain to deploy on (determined by your target users and stablecoin preference), and how much infrastructure to own versus rent.

White-label platforms like Bridge, Paxos, Brale, and Coinbase, issuance protocols like M0, or payments-optimized L1s like Tempo, offer the lowest barrier for most businesses. Custom builds still make sense for large institutions that need complete control and have the engineering team to maintain it.

One thing I'd flag: the temptation to over-engineer early is strong, especially for technical teams. The businesses actually getting stablecoins into production in 2026 are the ones that started with a turnkey provider, shipped, and iterated from there. The fundamentals, robust reserves, transparent operations, and clear redemption policies, matter more than the specific technology stack underneath.
