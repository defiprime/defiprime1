---
layout: blog
title: "Based Visa Card Discloses User Data Breach After Dashboard Attack"
url: /based-card-discloses-user-data-breach.html
h1title: "Based Visa Card Discloses User Data Breach After Dashboard Attack"
pagetitle: "Based Card Discloses User Data Breach"
metadescription: "Based says an attacker accessed user data through an internal card dashboard but failed to reach deposited funds."
category: blog
featured-image: /images/blog/based-card-discloses-user-data-breach-ogp.png
intro: "Based disclosed that an attacker accessed user data through an internal card dashboard while deposited funds remained out of reach."
author: sawinyh
tags: ["News"]
date: 2026-10-08T10:20:05+00:00
---

At 09:05 UTC on October 8, 2026, [Based co-founder Edison Chen disclosed](https://x.com/edison0xyz/status/2108121505884504310) a security incident involving the Based Visa Card program. Based said it discovered and contained the attack on October 5 after a security alert, but the attacker had already accessed some user data. The company said the attacker tried and failed to reach deposited funds.

The incident began in an internal dashboard used to manage the card program. Based said an unauthorized party gained access to that dashboard. The company did not identify the vulnerability, the attacker's access method, the data fields exposed, the number of affected cardholders, or how long the access remained available before the alert.

## What Based disclosed

Based said it stopped and contained the attack when it discovered the incident. It then fixed the vulnerability and tightened access controls. The statement did not describe either change, so users cannot independently assess which system failed or whether the fix addressed the full path used by the attacker.

The attacker attempted to reach deposited funds but did not succeed, according to the company. Based said funds on the Based Visa Card remained safe and cards remained operational. It also said funds in the Based App wallet and Trading Terminal were safe and unaffected. No loss amount was reported because the company said the attempted access to funds failed.

Based reviewed its other systems after the attack and said it found no sign that they had been compromised. That statement limits the known incident to the card management environment, but it does not establish which records the attacker viewed or copied inside that environment. The company described the exposure only as some user data and did not publish a field-by-field description.

The distinction matters for cardholders. A failed attempt to reach funds does not reverse the disclosure of personal information. Depending on the fields exposed, stolen data can be used for targeted phishing, impersonation, account-recovery attempts, or social engineering. Based itself warned affected users that sophisticated actors may use the information to trick them. The company did not state that any of those follow-on attacks had occurred.

Affected cardholders were notified after Based said it had audited its systems and added security precautions. The public statement did not provide the notification date or explain how the company determined which users were affected. It also did not say whether a regulator, card issuer, banking partner, or data-protection authority had been notified.

## What cardholders can verify

Based directed account questions to the in-app support chat. The company said this is the most secure support route because it allows the team to verify account ownership. It also warned that nobody from Based would contact users on X or Telegram about their accounts. A message claiming to come from support on either platform should therefore be treated as inconsistent with the company's stated process.

Users can separately check whether their card remains operational and whether balances in the Based App wallet or Trading Terminal have changed. Those checks address the systems that Based said were unaffected. They cannot show what personal data left the internal dashboard, because Based has not published the accessed fields or individual exposure records.

The disclosure gives users two immediate risk categories to separate. The first is asset risk. Based says the attacker failed to reach deposits and that the card, app wallet, and trading terminal funds remain safe. The second is identity and account-security risk. That risk remains open because some user data was accessed, and the company has not specified its contents.

Cardholders should use only the in-app channel for account questions and should be skeptical of unsolicited contact that refers to the incident. Based's warning is especially relevant if a message includes personal details that make it appear credible. The public statement does not authorize any support process through a social platform.

The disclosed sequence begins with the October 5 security alert. Based then contained the attack, fixed the vulnerability, tightened access controls, reviewed other systems, and added security precautions. The company said it notified affected users only after those reviews and precautions. The statement does not give a time for the alert, a containment duration, or the interval between individual notifications and the public post at 09:05 UTC on October 8.

Continued card operation is part of Based's account of the incident. The company did not say it suspended card transactions, froze balances, or took the app wallet or Trading Terminal offline. That operational status addresses access to services. It does not answer what data was accessed in the management dashboard, so a working card is not evidence that a cardholder's information was outside the exposed set.

A useful follow-up needs to connect the data incident to the remediation. Based has said the vulnerability was fixed and controls were tightened, but it has not described the original control, the replacement, or the audit scope. It has also not explained whether dashboard logs can determine which records the attacker opened. Those details would let cardholders compare the company's security changes with the data each person may have exposed.

The disclosure also leaves the notification threshold unclear. Based said affected users were contacted, but it did not explain whether that group includes every cardholder whose record was available in the dashboard or only users whose records appeared in access logs. Until the company defines that threshold, receipt or absence of a notice cannot resolve the broader question of what the unauthorized party could see.

Based has not published a technical postmortem, incident timeline, affected-user count, data inventory, or remediation report. It also has not named a date for a further update. The next verifiable milestone is a disclosure that identifies the exposed fields, explains the dashboard access path, and states whether an independent incident-response review or regulatory notification is complete.
