---
layout: blog
title: "Chainstack breach exposes account data; customers urged to rotate node credentials"
url: /chainstack-breach-node-credential-rotation.html
h1title: "Chainstack breach exposes account data; customers urged to rotate node credentials"
pagetitle: "Chainstack breach: account data exposure and node credential rotation"
metadescription: "Chainstack's technical disclosure traces its breach through Grafana and an unauthenticated MCP server, with node credential rotation required from customers."
category: blog
featured-image: /images/blog/chainstack-breach-node-credential-rotation-ogp.png
intro: "Chainstack's updated incident report asks customers to replace passwords, node credentials and platform API keys after an attacker reached production databases."
author: sawinyh
tags: ["News"]
date: 2026-11-12T10:21:23+00:00
---

On November 10, 2026, Chainstack added a technical account of its October intrusion to its [incident report](https://chainstack.com/security-incident-nov-2026/), tracing the attack from a test Grafana instance to production databases. The company is asking customers to change passwords, rotate node credentials and regenerate platform API keys.

The attacker accessed a database containing customer account information. Records potentially exposed include organization names, account holder names, members' email addresses and password hashes. The attacker also reached systems holding node credentials. Chainstack says it has no evidence those credentials were read, but is treating them as exposed.

Chainstack says its customer-facing services kept operating throughout the incident and that customer nodes, its console and its API were unchanged. Full payment-card numbers and security codes were not exposed because the company does not store them. The technical update sets out the checks behind its findings on customer workloads, along with the gaps in its reconstruction of the attack.

## Credential rotation requires deactivating the old set

The [node-management documentation](https://docs.chainstack.com/docs/manage-your-node) describes rotation in stages: generate new credentials, migrate applications while both sets work, then deactivate the old set. An organization Admin or Editor must perform the rotation. The process replaces the auth token in HTTPS and WSS endpoint URLs, the username and password for password-protected access, and the x-token for gRPC endpoints together.

Applications must use the new endpoint URLs and authentication values before the customer disables the old credentials. Both sets remain usable during the migration, and there is no time limit on that overlap. Generating a replacement leaves the old set active; the customer must complete the final deactivation step to stop it working.

In the console, the customer confirms that applications use the new endpoint URLs, then selects Deactivate old credentials. Chainstack rejects requests using the old credentials from that moment. The documentation calls this action permanent. For nodes with multiple active credential sets, each set must be selected and rotated separately. Rotating a node's credentials leaves its multichain auth token unchanged.

The incident notice also asks customers to change passwords on any other services where they reused their Chainstack password. Users of the platform API are asked to regenerate its keys. Chainstack is emailing customers and warning them to watch for phishing messages. It says it will never ask for passwords, tokens or keys.

## Default credentials opened a route into production

The report identifies the initial entry point as a test Grafana instance deployed to a development cluster in July. The instance was open to the internet, still used its default administrator credentials and had no additional authentication layer such as single sign-on. The attacker logged in, configured data sources pointing at internal addresses and used Grafana's proxy to reach internal services.

The proxy had no destination allowlist. Network policy also placed no restrictions on where Grafana could connect. Over about two hours, Chainstack records connections to dozens of identity, database, automation and monitoring services. The attacker reached an internal MCP tool server that exposed Kubernetes operations to AI agents. It required no authentication and held cluster-admin permissions.

Chainstack identifies that server as the likely command executor, based on network flows, its permissions and the changes that followed. The company could inspect those changes but could not recover the individual tool calls. Its reconstruction of the commands executed through the server remains incomplete.

On October 29, the attacker rewrote a workflow directly in an automation platform's database. Using a valid webhook token, the attacker made the workflow execute shell commands, then restored the original workflow. The run returned the automation pod's environment, its Kubernetes service-account token and a machine identity for Chainstack's infrastructure access gateway. The webhook requests came through Grafana.

That compromised gateway identity gave the attacker access beyond development. The attacker also used a second identity belonging to deployment automation and listed secrets from a production Kubernetes cluster. A list request returns the secrets' contents, Chainstack notes. Further individual reads included cloud and infrastructure credentials.

On October 31, a stolen VPN peer private key gave the attacker access to the database network. The tunnel endpoint switched between clients presenting the same identity, breaking a database replication pipeline. That failure triggered Chainstack's investigation. The report also describes queries run as an administrative user from attacker-created pods. The attacker removed the results through pod command output in base64 chunks.

Separately, the attacker used a compromised Kubernetes token to query PostgreSQL's password-hash view from a database connection-pooler pod. Chainstack dates its detection of the intrusion and the cutting of access paths to October 31. It closed its investigation on November 2.

## What containment and the service checks establish

Some copied credentials, including tokens for external services, still worked after Chainstack cut the access paths into its environments. The company observed their last use on November 2, before it had completed rotation. Development hosts briefly brought back online that morning re-ran attacker implants. Their outbound connections were blocked.

To check production workloads, Chainstack compared access-gateway audit logs, Kubernetes API audit logs and infrastructure-as-code apply records. It attributed production Kubernetes changes since October 29 to its staff, automation or cluster controllers, except for the attacker-created objects identified in the report. The company says those objects did not alter customer node, console or API workloads.

The console and API images matched their registry digests. According to Chainstack, images pushed during the intrusion window were deployed only through reviewed changes. No published deployment chart was overwritten, and ingress and routing changes came through the company's own deployments. These findings come from the operator's audit, not an independent inspection of its infrastructure.

Chainstack attributes the attack tooling to ARTEX, an open-source framework that orchestrates language-model agents, based on markers in attacker artifacts. It found no evidence of an exploited software vulnerability. The report instead describes default credentials, missing authentication, excessive permissions and long-lived credentials. Chainstack says the shared tooling does not identify the attacker: public reporting connects ARTEX to unrelated groups, and its investigation has not established who conducted this intrusion.
