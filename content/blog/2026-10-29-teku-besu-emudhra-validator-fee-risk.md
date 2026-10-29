---
layout: blog
title: "Teku and Besu remove eMudhra roots after validator fee-risk warning"
url: /teku-besu-emudhra-validator-fee-risk.html
h1title: "Teku and Besu remove eMudhra roots after validator fee-risk warning"
pagetitle: "Teku and Besu eMudhra fixes: validator fee risks"
metadescription: "Teku and Besu patch Docker certificate trust after the eMudhra compromise. Remote HTTPS endpoints can expose validator fees; host Java needs separate checks."
category: blog
featured-image: /images/blog/teku-besu-emudhra-validator-fee-risk-ogp.png
intro: "Teku and Besu removed eMudhra trust roots from Docker images to close an HTTPS impersonation risk affecting some validator configurations."
author: sawinyh
tags: ["News"]
date: 2026-10-29T06:24:01+00:00
---

On October 27, 2026, [Teku released version 26.10.3](https://github.com/Consensys-Incorporated/teku/releases/tag/26.10.3), removing compromised-certificate trust roots from its Docker images. [Besu's version 26.10.2](https://github.com/besu-eth/besu/releases/tag/26.10.2), released on October 26, makes the same Docker change. The fixes address a route through which an attacker intercepting a validator's outbound HTTPS connections could redirect fees or disrupt validator duties.

Exposure depends on configuration. Teku's [security advisory](https://hackmd.io/@teku/S1DCreh2Ge), updated October 28, says: “A default Teku node on mainnet is not affected and needs no action.” It defines default as having no HTTPS URLs in the configuration. The advisory also states: “No exploitation has been reported.” The attacks it describes are possible outcomes, not accounts of stolen rewards.

## How certificate trust reaches validator fees

The advisory traces the problem to eight eMudhra intermediate certificate authorities whose private keys were shown to be recoverable from public certificates on October 17. They were revoked on October 18. Java does not check revocation by default. Its runtimes therefore need their own remediation, even after browsers and other systems blocked the certificates.

An attacker with a compromised key can impersonate an HTTPS service trusted by an unpatched runtime, but still needs to intercept traffic between Teku and that service. The exposure is in outbound connections. Teku does not accept client certificates on its APIs, so the advisory identifies no inbound exposure through that mechanism. Peer-to-peer networking uses no certificate authorities and is unaffected.

The advisory rates the external signer as the highest-risk endpoint. By impersonating it, an attacker could obtain signatures for irreversible voluntary exits and builder registrations that redirect fees, or capture credentials embedded in the signer URL. It also lists slashable signatures as a possibility when the signer's own slashing protection is disabled. If the signer requires Teku to present a client certificate, mutual TLS prevents the attacker from relaying requests to it. That limits the impact to denial of service.

An impersonated remote beacon node could supply blocks paying fees to an attacker. The validator client does not check the payload before signing. The node could also cause missed or incorrect attestations, though Teku's own slashing protection still blocks slashable signatures in this scenario. The advisory rates exposure for an internet-connected remote beacon node above that of the execution-client connection, which is usually local.

Proposer configuration fetched from a URL gives an attacker another way to change fee recipients. An attacker could substitute fee recipients and builder settings for every validator using that configuration. With refresh enabled, the substitution could repeat every epoch. The advisory describes remotely loaded proposer configuration as uncommon; a successful substitution would affect the validators covered by that configuration.

A directly connected builder or relay could deliver a block paying the attacker, censor transactions, or withhold the payload after signing and cause a missed proposal. A local mev-boost checks relay keys itself. An impersonated remote execution client could report invalid payloads as valid and supply proposed payloads containing the attacker's fee recipient. The advisory rates the execution-client scenario very low because the Engine API usually stays on the same host or a private network.

Startup downloads carry a separate risk. Substituted checkpoint state, network configuration or peers could leave a node stuck. Combined with control of its peers, they could keep it on a fake chain. The advisory limits checkpoint-sync exposure to startup with an empty database, so startup configuration needs inspection alongside the endpoints a validator uses continuously.

## What the Docker releases fix

Teku's release removes trust in emSign ECC Root CA - G3, emSign Root CA - G1, emSign Root CA - G2 and AAA Certificate Services. Its release notes explicitly say the Eclipse Temurin base images do not yet include the fix. Besu lists the same roots and identifies the G1 removal as precautionary.

The Teku advisory still tells Docker users to watch for a future fixed image. That instruction conflicts with the release notes, which document the root removal. The advisory's displayed update date follows the release date, but its forward-looking remediation passage does not reflect the fix documented in the release. The release notes establish that the Docker fix exists.

Container and host runtimes need separate attention. The advisory identifies Teku images through version 26.10.2, including its alternative JDK tags, as carrying an unfixed runtime. Updating Java on the host leaves Java inside those images unchanged. Besu says its root removal applies only to Docker images: an archive installation using a distribution or vendor JDK may still trust the roots. Teku's binary distribution likewise uses the runtime installed by its operator.

## Checking the runtime actually in use

[OpenJDK's guidance](https://openjdk.org/emudhra) supplies a CheckCerts.java diagnostic to test runtime exposure. For standalone installations, its root-removal procedure calls for backing up the keystore, removing the relevant certificates and restarting live runtime instances. Operators must repeat the procedure for each installed runtime. Checking a different Java installation from the one running the client leaves that client's exposure unchecked.

Operating-system packages take different paths. OpenJDK says updating system certificates is likely sufficient for distributions including Fedora and Red Hat Enterprise Linux. On Debian and Ubuntu, a bug in the Java certificate package means updating the certificate packages alone is insufficient. The guidance requires removing and recreating the system Java keystore. FreeBSD and Homebrew runtimes do not use the system certificates and require direct package updates.

Teku also documents controls for individual connections. An external signer truststore containing only the signer's certificate authority narrows trust for that connection; a client keystore enables mutual authentication. Startup state, peer lists and proposer configuration can be supplied as local files. Teku has no certificate-pinning options for remote beacon, execution-client and builder connections. The advisory recommends keeping them on the same host or a private network and using local mev-boost.

The advisory recommends HTTPS with a fixed Java runtime. Switching remote connections to plain HTTP removes authentication altogether. Neither client release notice supplies a measured count of exposed validators, and Teku's published account remains a risk disclosure with no reported exploitation.
