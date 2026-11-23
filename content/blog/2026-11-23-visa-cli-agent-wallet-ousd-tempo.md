---
layout: blog
title: "Visa CLI launches agent wallet for earning $OUSD on Tempo"
url: /visa-cli-agent-wallet-ousd-tempo.html
h1title: "Visa CLI launches agent wallet for earning $OUSD on Tempo"
pagetitle: "Visa CLI agent wallet brings $OUSD task payments to Tempo"
metadescription: "Visa CLI lets eligible US cardholders verify agents and earn $OUSD on Tempo, with task approvals, payment recovery rules and limits for older registrations."
category: blog
featured-image: /images/blog/visa-cli-agent-wallet-ousd-tempo-ogp.png
intro: "Visa Crypto Labs launched an agent wallet for eligible United States cardholders to earn $OUSD on Tempo, with card verification separate from wallet payments."
author: sawinyh
tags: ["News", "Payments", "Stablecoins"]
date: 2026-11-23T03:22:57+00:00
---

Visa Crypto Labs launched a new version of Visa CLI on November 22, 2026, offering an agent wallet that lets eligible United States Visa cardholders verify an AI agent and earn $OUSD for creative tasks. Cuy Sheffield [announced the release](https://x.com/cuysheffield/status/2124555774320062807) with a link to the product, saying users could try it immediately.

The wallet uses $OUSD on Tempo for earnings and payments. A Visa card verifies the owner. Adding it does not charge the card or make it the agent's spending source; the agent spends from the wallet balance. Visa's documentation describes real money and task payouts on mainnet, although its status page still says accounts are approved by invitation.

## A card verifies the owner, a wallet pays

The [card requirements](https://app.visacli.sh/docs/your-visa-card.md) limit access to supported US Visa cards. Prepaid and corporate cards are excluded, as are cards from banks that cannot support the verification step. Visa can still decline other cards. The owner needs an approved account and access to the verification code sent by the bank.

The owner verifies the card once for the account, entering card information in fields hosted by a card vault and confirming a code sent by the bank. The documentation describes the wallet created during this process as self-custodial. Card details travel from the browser to the vault. Subsequent public agent lookups expose the agent's name and key, but not the card issuer, country, owner's name or contact details.

A person with a card can currently have up to 25 agents, with multiple agents sharing a wallet. Each agent gets its own key and limit. The owner does not repeat card verification for each agent, but a card already attached to another owner's account cannot be attached again.

Card verification has a narrower meaning than a compliance check. Visa's documentation states: "It isn't a KYC, KYB or sanctions check." A business accepting an agent's signed request cannot treat the verified badge as evidence that its owner passed those checks.

The [wallet documentation](https://app.visacli.sh/docs/wallet-and-ousd.md) says only the owner can add funds. When the agent reports that funds are needed, the owner uses Receive and sends $OUSD on Tempo to the displayed address. The wallet shows no other token. To withdraw, the owner enters a destination through the Wallet page. Visa screens withdrawal addresses before signing and also screens wallet payees.

## Earning requires accepted work or approved settlement

The [task workflow](https://app.visacli.sh/docs/tasks-and-earning.md) starts with an agent finding paid work that has passed Visa's automated screening. Listings show the reward and closing time. Screening checks what a task asks for, not the quality of the requester or the finished work. A task without a stake requires no deposit.

By default, the owner approves claiming a task when a claim is required, then approves the submission. The "Pays on its own" setting lets an agent on the owner's computer claim, submit and release screened tasks without asking each time. The owner must still approve forfeiting, rejecting and settling.

Submissions can incur a fee after a marketplace's free entries are exhausted. The wallet must hold enough to pay, and the owner approves that charge. Each submission has a fee limit; setting it to zero allows only a free entry. Visa screens tasks when they are listed, before a signed step and before payment. It screens changed tasks again.

An accepted submission pays its reward into the owner's wallet. If the requester misses the review deadline, the marketplace does not automatically release the reward. The agent asks to settle, and the owner must approve. The documentation cautions that completing a task alone is not proof that its reward was paid. Owners can check the payment in Activity.

New Taskmarket posts made through Visa require a verified worker by default. On mainnet, that means the worker's key must be in the Visa Agent Directory. A requester can choose to accept any worker instead. If an approval is already waiting, the requester must decline it before changing that requirement.

## Older agents face a separate registration barrier

Visa's [status page](https://app.visacli.sh/docs/status.md) dates production directory registration for newly connected agents to November 18, 2026. Agents connected before that date remain in the directory's sandbox. Those older registrations cannot satisfy the mainnet verified-worker requirement, even though the task rewards themselves are real mainnet funds.

Claiming or submitting a verified-worker task on mainnet also requires Visa CLI version 5.0.0 or later. Earlier releases may return `verifier_unavailable` without signing or paying. An agent whose registration is still in the sandbox can seek unrestricted work while its production listing is resolved.

The directory and marketplace use different labels. Every Visa CLI agent appears as `known` in the Visa Agent Directory, including agents described as Verified with Visa. That badge refers to the owner's card verification. Marketplace verified-worker eligibility can coexist with the directory's `known` label because the labels describe different checks.

## Payment recovery depends on the purchase reference

For spending, Visa CLI pays APIs that charge per request through MPP. Paid requests carry an agent signature tagged `agent-payer-auth`, and the merchant verifies the payment itself. The separate identity-check path rejects that paid profile as `tap_malformed`, so a merchant must use the checks intended for paid requests.

Each purchase has an `idempotency_key`. Retrying the same request continues that purchase instead of starting another. Visa reads the payment result from the chain rather than accepting a merchant's reply alone as proof. Its recovery instruction is explicit: "If a payment's result goes missing, don't pay again. Check the payment in **Activity**."

Sheffield invites eligible US users to try the product, while the status page still describes accounts as invitation-only. Visa publishes change dates on individual documentation pages but has no separate changelog to reconcile those access descriptions.
