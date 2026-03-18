---
git-date:
layout: [blog]
title: "Stripe's MPP vs. x402: What Actually Happened Today"
permalink: stripe-mpp-vs-x402
h1title: "Stripe's MPP vs. x402: What Actually Happened Today"
pagetitle: "Stripe's MPP vs. x402: Machine Payments Compared"
metadescription: "Two competing visions for machine-to-machine payments shipped on the same day. Here's how x402 and MPP differ, and why Stripe is betting on both."
category: blog
featured-image: /images/blog/stripe-mpp-vs-x402-ogp.png
intro: "Two competing visions for machine-to-machine payments shipped on the same day. Here's how x402 and MPP differ, and why Stripe is betting on both."
author: sawinyh
tags: ["DeFi Guides", "Payments"]
---

HTTP status code 402 has been waiting for something to do since the [HTTP/1.1 spec](https://datatracker.ietf.org/doc/html/rfc2068) defined it in the late 1990s. "Payment Required." That was the idea: bake payments into the protocol layer of the web so machines could buy things the way they request pages. It mostly didn't happen. The code saw [occasional niche use](https://www.abstractapi.com/guides/http-status-codes/402) over the years, Shopify rate-limit responses and Apple MobileMe billing errors, but no one built the micropayment future it implied. Instead we got credit cards, subscription paywalls, and API keys. All built for humans with fingers.

Today, two competing visions for that future shipped on the same day. I want to walk through what they are, how they differ, and why Stripe is betting on both.


## x402: the simple one

Coinbase [publicly launched x402 in May 2025](https://www.coinbase.com/developer-platform/discover/launches/x402), and the core idea is almost aggressively minimal. A client requests a resource. The server responds with HTTP 402 and tells the client how much it costs, in what token, on what chain. The client pays on-chain, staples a payment proof to the retry request, and the server delivers the goods.

That's it. No accounts, no API keys, no subscriptions. Just an HTTP round-trip with money in the middle.

Stripe now offers [native x402 integration](https://docs.stripe.com/payments/machine/x402) in its payments stack, so merchants can accept these payments through their existing dashboard. But x402 is fundamentally Coinbase's protocol, governed by the [x402 Foundation](https://www.cloudflare.com/press/press-releases/2025/cloudflare-and-coinbase-will-launch-x402-foundation/) that Coinbase and Cloudflare announced in September 2025 (see also [Cloudflare's blog](https://blog.cloudflare.com/x402/) and [Coinbase's announcement](https://www.coinbase.com/blog/coinbase-and-cloudflare-will-launch-x402-foundation)). It's fully open-source under Apache 2.0, with TypeScript, Go, and Python SDKs.

[Coinbase's documentation](https://docs.cdp.coinbase.com/x402/welcome) lists production facilitator support for ERC-20 payments on Base, Polygon, and Solana. The broader ecosystem is experimenting on [additional chains like Avalanche, Sui, and Near](https://www.dwf-labs.com/research/inside-x402-how-a-forgotten-http-code-becomes-the-future-of-autonomous-payments), though at varying levels of maturity.

Now, the adoption numbers. They're complicated. Coinbase says x402 has processed [over 50 million transactions](https://www.coinbase.com/developer-platform/discover/launches/agentic-wallets) through its Agentic Wallets infrastructure. That sounds impressive until you read a [CoinDesk report from March 11](https://www.coindesk.com/markets/2026/03/11/coinbase-backed-ai-payments-protocol-wants-to-fix-micropayment-but-demand-is-just-not-there-yet), which cited Artemis on-chain analysis: roughly 131,000 daily transactions, about $28,000 in volume, $0.20 average payment. About half of it looked like testing or gamified activity, not real commerce.

I don't think that's as bad as it sounds. The protocol is designed for a market that barely exists, where agents pay sub-cent amounts for API calls and data lookups. The merchants who would serve that market are still showing up. [Coinbase's developer blog](https://www.coinbase.com/developer-platform/discover/launches/google_x402) describes x402 integrated into Google's Agentic Payments Protocol (AP2), part of the A2A framework, with a Lowe's Innovation Lab demo showing an agent discovering, researching, and checking out products in one flow. World, Sam Altman's identity project, [launched AgentKit for x402](https://www.theblock.co/post/393920/sam-altman-world-identity-toolkit-ai-bots-coinbase-x402-protocol) this week, attaching human-identity proofs to agent wallets.

The thesis: make payments as lightweight as HTTP requests, and the use cases show up. We'll see.


## MPP: the full-stack one

Stripe and Tempo took a different approach. The Machine Payments Protocol launched today alongside [Tempo's mainnet](https://tempo.xyz/blog/mainnet), and where x402 is a thin shim on existing chains, MPP is built for the specific problem of agents transacting at high frequency.

The key mechanism is "sessions." Rather than one blockchain transaction per resource request, an agent can authorize a spending limit upfront and stream micropayments against it continuously. If you're an AI querying a data feed thousands of times an hour, you do not want to sign and broadcast a chain transaction each time. Sessions solve that.

Tempo's chain was built for this. It processes tens of thousands of transactions per second with sub-second finality, and there's no native gas token. You pay fees in stablecoins, which eliminates the annoying step of buying some random token just to move money.

The other piece worth understanding: Stripe's broader [Agentic Commerce Suite](https://stripe.com/blog/introducing-our-agentic-commerce-solutions) includes Shared Payment Tokens (SPTs). These are a Stripe construct, not part of MPP itself, but they work alongside it. SPTs let an agent securely pass a buyer's card or wallet credentials to a merchant without revealing the actual data. They're scoped to a single transaction, time-limited. Think of them as a programmable, self-destructing authorization. In practice, that means an agent paying through MPP can use USDC on Tempo, or a user's linked Visa, or both.

According to [Tempo's mainnet blog](https://tempo.xyz/blog/mainnet), the company lists collaborations with Anthropic, DoorDash, Mastercard, Nubank, OpenAI, Ramp, Revolut, Shopify, Standard Chartered, and Visa. [The Block reported](https://www.theblock.co/post/394131/tempo-mainnet-goes-live-with-machine-payments-protocol-for-agents) over 100 services in the payments directory at launch, including Alchemy, Dune Analytics, Merit Systems, and Parallel Web Systems. Matt Huang, who co-founded both Paradigm and Tempo, said in a Fortune interview that the space is early and the protocol is designed to extend beyond Tempo's chain over time.


## Why Stripe is supporting both

If you already have a Stripe integration, the practical answer is: you don't have to pick.

Stripe supports x402 and MPP through separate integration paths, not a single abstraction layer. For x402, [their docs](https://docs.stripe.com/payments/machine/x402) walk through deposit address generation, blockchain monitoring, and settlement into your Stripe balance. You serve the 402 challenge, they handle the crypto plumbing. Currently it supports USDC on Base, more coming. For MPP, merchants get session-based streaming payments flowing into the same PaymentIntents API.

The [Agentic Commerce Suite](https://stripe.com/newsroom/news/agentic-commerce-suite) that Stripe shipped in December 2025 sits on top of both rails. Upload your product catalog, pick which AI agents you want to sell through, and Stripe takes care of discovery, checkout, fraud, and tax. URBN, Etsy, Coach, Kate Spade, and Ashley Furniture are already onboarding. Platforms like Wix, WooCommerce, BigCommerce, Squarespace, and commercetools have [integrated it](https://stripe.com/blog/agentic-commerce-suite).

The strategy is clear enough: own the abstraction layer, let the protocols compete underneath.


## Side by side

Both protocols do the same thing at a high level: let machines pay for resources over HTTP. The details matter.

| Aspect | x402 (Coinbase-led) | MPP (Stripe + Tempo) |
|---|---|---|
| **Standardization** | Fully open (Apache 2.0). Multi-vendor support via the x402 Foundation (Coinbase, Cloudflare, Visa, Google). | Open standard, co-authored by Stripe and Tempo. Part of Stripe's Agentic Commerce Suite. |
| **HTTP Mechanism** | Revives HTTP 402. Uses `PAYMENT-REQUIRED` header and `PAYMENT-SIGNATURE` for retries. | Similar challenge-response handshake, uses a Payment HTTP Authentication Scheme (IETF draft) with HMAC-bound challenge IDs. |
| **Payment Rails** | Chain-agnostic by design. Production facilitator support for Base, Polygon, and Solana ([docs](https://docs.cdp.coinbase.com/x402/welcome)). Broader ecosystem experimenting on additional chains. | Tempo blockchain: payments-optimized L1 with 10k+ TPS, sub-second finality, no native gas token. Designed to be rail-agnostic over time. |
| **Payment Methods** | Pure stablecoins. On-chain only. | USDC on Tempo + [SPTs](https://stripe.com/blog/introducing-our-agentic-commerce-solutions) (a Stripe construct) for hybrid fiat (cards, wallets, BNPL). |
| **Settlement** | On-chain per network (~200ms to a few seconds). Facilitators like Coinbase verify and settle. | Tempo sub-second finality. Stripe auto-captures into the merchant's balance with full compliance. |
| **Merchant Integration** | Open-source middleware (Express, Hono, Next.js). DIY or use facilitators. | Existing Stripe PaymentIntents API. Fraud, tax, refunds, and reporting come built in. |
| **Key Innovation** | Simplicity. No vendor lock-in. The "Unix philosophy" of payments. | Throughput and fiat hybrid. Sessions for streaming, micropayment aggregation, programmable spending controls via SPTs. |
| **Key Partners** | Coinbase, Cloudflare, Google (A2A/AP2), Visa, World, Anthropic (MCP). | Stripe, Visa, Lightspark (Lightning), Anthropic, DoorDash, Mastercard, OpenAI, Shopify, Revolut, Standard Chartered. |

x402 is the protocol you'd reach for if you're building something open. An indie API, a decentralized data market, a service where the developer shouldn't need to register with a payment processor just to get paid. The spec fits in a whitepaper. The integration is a middleware import and a wallet address. There's a purity to it that I find appealing, even if the "pure crypto" constraint limits its audience.

MPP is a different animal. It's what you want when your agents need to transact hundreds or thousands of times per session without each one being a chain event. Sessions keep you off-chain until settlement. Stripe's compliance stack handles fraud and tax. And the SPT hybrid model means agents aren't limited to stablecoins, they can tap a user's Visa too. It's less elegant, more practical.

What strikes me about the positioning: these aren't really competitors. x402 covers the long tail. MPP covers enterprise traffic. Stripe doesn't care which one wins, only that settlements land in Stripe balances. That's a good place to be.


## What's actually live

Here's the thing: almost none of this has real volume yet.

According to Coinbase's [x402 launch post](https://www.coinbase.com/developer-platform/discover/launches/x402), early partners include Hyperbolic (GPU inference payments) and Anthropic (MCP protocol integration). Stripe's [blog](https://stripe.com/blog/10-lessons) mentions agents paying per API call, with CoinGecko as an example. Tempo's directory lists 100+ services at launch. [Cloudflare's Agents SDK](https://blog.cloudflare.com/x402/) supports x402 natively. A growing number of smaller projects are experimenting with x402-gated services on Base L2.

But the volume is tiny. The merchant count is small. Most of the activity still looks experimental. That's fine, probably. Every payment rail starts slow. I've seen enough crypto launch-day partner lists to know that "collaboration" can mean anything from "we signed an LOI" to "we're live in production," and today's announcements don't always distinguish between those.

What's harder to dismiss is the weight behind the infrastructure. Stripe processed [$1.9 trillion in total payment volume in 2025](https://www.pymnts.com/news/fintech-investments/2026/stripe-reaches-record-valuation-global-volume-hits-2-trillion-dollars/), per its annual letter, up 34% year-over-year. Coinbase, Cloudflare, Visa, Google, and the full Tempo partner roster are all committed. The rails exist now. Whether agents actually need them at scale in 2026, or whether this is more like laying fiber in 1998, is the bet.


## So which one?

If you're building something open and permissionless, x402 is the obvious choice. Decentralized services, indie APIs, pay-per-request models. No vendor to sign up for, no payment processor to negotiate with. You import a middleware, point it at a wallet, and you're accepting payments. The tradeoff is that you're on your own for compliance, fraud, and fiat settlement.

If you're on Stripe and you want agent traffic without rebuilding your finance stack, MPP is what you want. Sessions, streaming payments, hybrid fiat-crypto, the full compliance suite. It's designed to feel like a config change, not a replatform.

And if you'd rather just accept money from any agent regardless of what protocol it prefers? Stripe supports both. That's probably the point.

HTTP 402 is finally doing something. Only took about twenty-seven years.
