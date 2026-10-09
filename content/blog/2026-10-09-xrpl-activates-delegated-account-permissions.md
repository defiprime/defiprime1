---
layout: blog
title: "XRPL activates delegated account permissions"
url: /xrpl-activates-delegated-account-permissions.html
h1title: "XRPL activates delegated permissions for issuers"
pagetitle: "XRPL activates delegated account permissions"
metadescription: "XRPL's PermissionDelegationV1_1 lets issuers split payment and compliance duties while retaining control of the main account."
category: blog
featured-image: /images/blog/xrpl-activates-delegated-account-permissions-ogp.png
intro: "XRPL has activated granular account delegation for issuers and operators, with a warning still attached to one token-burning permission."
author: sawinyh
tags: ["Analysis"]
date: 2026-10-09T05:21:17+00:00
---

At 21:29:50 UTC on October 8, 2026, [ledger 107,524,865](https://livenet.xrpl.org/transactions/478284066BA0B83CC35CA1174F667F43D9577782F221440AFCC5541788F25A77) enabled PermissionDelegationV1_1 on XRPL. The amendment gives an account a way to authorize another account for selected actions. Each delegate relationship consumes one object reserve, and the delegate pays the fees on transactions it submits.

The change addresses a specific operational problem for token issuers and other organizations. Routine work such as sending payments, managing trust lines or authorizing counterparties previously required the keys of the account that held the relevant authority. The [XLS-75 specification](https://github.com/XRPLF/XRPL-Standards/tree/master/XLS-0075-permission-delegation) now lets the owner place a narrower set of permissions in a Delegate ledger object. The delegated account signs with its own keys and can act only within that recorded scope.

That separation reduces the need to keep a broadly privileged key in an online workflow. It does not make delegated access harmless. A payment permission can move funds, and transactions that create ledger objects can charge reserves. The same specification warns operators to treat broad administrative permissions as especially sensitive.

## What the amendment puts on ledger

PermissionDelegationV1_1 creates a Delegate ledger object and a DelegateSet transaction. The object identifies the account granting authority, the account receiving it and the permitted actions. Its identifier is derived from the two accounts and the namespace for Delegate objects. The permissions array can contain at most 10 entries.

The owner creates or updates the relationship with DelegateSet. A nonempty permissions list replaces the existing list rather than adding to it. An empty list deletes the Delegate object and removes the authority. This gives the owner a direct revocation path without taking custody of the delegate's keys. The receiving account must already exist, cannot be the same as the owner and cannot be a pseudo-account.

A delegated transaction keeps the owner in the Account field and adds the acting account in the Delegate field. The delegate supplies the signing public key and signature. If that account uses multisigning, it can use the same setup for delegated transactions. The payment or other ledger action still occurs on behalf of the owner.

Fee handling is deliberately separate. The delegate pays the transaction fee, while only the owner's sequence number advances. That prevents a delegate from draining the owner's native balance through fees alone. It also means an operator has to fund its own account well enough to perform the work assigned to it.

The object costs one reserve to the owner. The cost applies per delegated account, so dividing work among more operators increases the owner's reserve requirement. The specification contrasts this model with a signer list: a signer list is controlled by the owner and guards an action with multiple signatures, while a delegate controls its own keys and receives authority to perform named actions.

The distinction matters for issuer workflows. The specification's example assigns payments to one employee, trust-line management to another and trust-line authorization to an external customer-verification provider. The third party can authorize a holder without receiving unrelated account powers. A stablecoin issuer could use the same division to keep its main key away from a customer approval service.

The owner can revise that structure without rotating every operator's key. Replacing the permissions list changes what an existing delegate may do. Clearing the list removes the relationship. Adding a different operator creates another Delegate object and charges another reserve to the owner. This makes staffing changes and emergency revocation ledger actions, while each operator remains responsible for its own signing keys and transaction fees.

The limit of 10 entries applies to the permission array for one relationship, not to a shared role template. An issuer that separates payment and trust-line duties must record the intended list for each delegate. Because a nonempty update replaces the old list, an operator preparing DelegateSet transactions needs to submit the full desired scope. Leaving a previously granted action out removes it. That replacement behavior avoids permission accumulation, but it also makes review of the proposed list important before signing.

The ledger enforces the boundary at transaction time. A transaction fails when the owner has not authorized the delegate, when the requested action is outside the recorded permission or when the delegate uses a field or flag that its granular permission does not allow. New transaction types remain nondelegable until the delegation implementation has integrated and tested them.

## The controls that remain with the owner

The design withholds the transactions that could let a delegate rewrite the account's own security boundary. AccountSet, SetRegularKey, SignerListSet and DelegateSet are not delegable. AccountDelete is also excluded. A delegate therefore cannot use delegated authority to grant itself a different permission set, replace the regular key, change the signer list or delete the owner's account.

System transactions are outside the model as well. EnableAmendment, SetFee and UNLModify cannot be delegated. Batch is not delegable as a wrapper, although its inner transactions can carry the Delegate field. ConfidentialMPTConvert is excluded because it registers the account's ElGamal key for confidential transactions.

Those exclusions narrow the blast radius, but the remaining permissions still need role-by-role review. A delegated Payment action can access funds. A transaction that creates an object can increase the owner's reserve burden even though the delegate pays the network fee. The specification recommends heavy warnings in tooling for permissions that can affect funds or account controls.

The owner also has to consider the delegate's own security. Delegation does not place the delegate's keys under the owner's control. If that operator uses a multisign configuration, the delegated workflow inherits it. If the delegate's keys are compromised, the attacker receives the same recorded authority until the owner replaces the list or deletes the Delegate object.

This is why the amendment is more useful as a separation-of-duties primitive than as a general substitute for cold storage. The owner can keep broad control offline while online accounts receive narrowly defined jobs. The quality of that setup depends on how narrowly each permission is drawn, how quickly the owner can revoke it and how the delegate secures its own signing process.

## The PaymentBurn warning

The [official amendment record](https://xrpl.org/resources/known-amendments#permissiondelegationv1_1) marks PermissionDelegationV1_1 as enabled and says it replaced the original PermissionDelegation amendment after a critical bug was found. The replacement did not remove every caution around the feature. XRPL documentation advises operators not to delegate PaymentBurn until fixCleanup3_4_0 is enabled.

PaymentBurn is meant to authorize a delegate to destroy fungible tokens. Before the fix, that permission can also let the delegate mint new trust-line tokens or Multi-Purpose Tokens under certain conditions. The documentation says other granular permissions are unaffected. This warning concerns issued tokens, not the ledger's native asset.

The safeguard for operators is procedural for now: do not include PaymentBurn in a Delegate object. The owner can still use other granular permissions, and an existing list can be replaced or cleared with DelegateSet. Wallets, custody systems and issuer consoles should surface the exception rather than presenting every permission as equally ready for use.

The same official status page listed fixCleanup3_4_0 as open for voting at 77.14% on October 9. That status is not an activation date. The page states that an amendment can become enabled only after holding a supermajority for at least two weeks. Until the fix completes that process and activates, the warning remains part of the operating boundary.

## What changes for issuers and operators

For an issuer, the immediate change is that daily operations no longer need one key with every power. Customer authorization can sit with a compliance service, payments can sit with a treasury operator and trust-line settings can sit with another controlled account. Each operator signs independently. The owner retains the ledger object that defines and revokes the relationship.

For custody and wallet teams, the change adds a new policy surface. They need to display who granted the authority, which actions are allowed, which reserve is being consumed and which account pays fees. They also need to reject unsupported fields and flags before signing, because the ledger will reject a transaction that exceeds the granular permission.

For holders, delegation does not create a second claim on the issuer or transfer ownership of the issuer account. It changes which account may submit a permitted transaction on that issuer's behalf. The practical risk is therefore tied to the assigned permission. A compromised payment delegate can be more damaging than a compromised account limited to customer authorization.

The on-chain activation also makes revocation observable. A replaced list or deleted Delegate object changes the authority recorded by the ledger. An operator can check that object instead of relying only on an internal access-control database. That record does not show whether the issuer chose sensible roles or protected the delegate's keys.

The unresolved milestone is fixCleanup3_4_0. PermissionDelegationV1_1 is live, but PaymentBurn should remain outside production delegation until the separate amendment activates and the official warning is removed.
