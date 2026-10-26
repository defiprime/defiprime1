---
layout: blog
title: "Keystone breach exposes device authentication key"
url: /keystone-breach-device-authentication-key.html
h1title: "Keystone breach exposes device authentication key"
pagetitle: "Keystone breach exposes device authentication key"
metadescription: "Keystone says a website attacker stole its device authentication key and customer data, prompting shipping suspensions and extra checks for recent deliveries."
category: blog
featured-image: /images/blog/keystone-breach-device-authentication-key-ogp.png
intro: "Keystone says a stolen authentication key could let counterfeit wallets pass verification, with recent deliveries requiring additional checks."
author: sawinyh
tags: ["News"]
date: 2026-10-26T15:25:29+00:00
---

Keystone disclosed on October 26, 2026, that an attacker stole customer information and the key used to authenticate its hardware wallets through a breach of its official website. In its [incident statement](https://x.com/KeystoneWallet/status/2114719318722404578), the company said it had suspended unshipped website orders and would destroy 18,835 devices carrying the old authentication key.

The stolen WebAuth key can allow counterfeit devices to pass Keystone's authenticity checks, the company warned. Keystone said the breach did not expose recovery phrases, wallet private keys or other wallet credentials. It warned that customers receiving counterfeit devices could lose assets, but reported no on-chain theft.

Keystone detected unusual website access through its security monitoring on October 20. It disabled sensitive functions and blocked unauthorized access points that day. Investigators traced the intrusion to a vulnerability in a third-party data monitoring tool that allowed the attacker to escalate privileges. Keystone says it fixed the vulnerability and began a forensic investigation. Its statement does not name the tool.

## Which devices need another check

Keystone's guidance depends on when a device arrived. The company says authentication still works for devices delivered before October 20, and owners can use them normally if they pass the check. Keystone bases that assessment on the date it discovered the unauthorized access.

Devices received after October 20 that contain the old key need another check, even if they pass authentication. Keystone says it cannot completely rule out a counterfeit in those cases. It directs customers to contact support through the device authentication page for additional verification. Those customers should use the device only after its authenticity has been confirmed.

The leaked key was written into devices during manufacturing and cannot be erased or rewritten, according to the disclosure. It is used only for device authentication and plays no part in recovery phrase generation, private-key derivation or transaction signing. The company does not offer a firmware update as a way to replace the exposed key in existing units.

Keystone says production will stop using the old key immediately. Newly manufactured devices will receive a replacement, and the company will destroy affected inventory without selling or shipping it. Website sales will move to preorders while production of devices with the new key is completed. Shipping will resume once that production is complete; Keystone gives no restart date.

Existing owners are not being asked to return devices. Keystone warns that anyone claiming there is a recall and asking customers to ship their wallets should be treated as a scammer. It also says customers need not transfer assets solely because of this incident. Its warning covers unsolicited offers of asset migration, wallet verification or investigation assistance.

## What the authentication page can establish

The [device verification page](https://keyst.one/authentication/) describes a challenge-response workflow. The device scans a QR code, the customer enters the code displayed on the device, and the website returns a result. At the time of review, the page's general FAQ still said that passing verification confirms genuine, untampered hardware and firmware. The disclosure limits that assurance for old-key devices received after October 20.

Keystone's [earlier explanation of Web Authentication](https://blog.keyst.one/web-authentication-a-counter-to-supply-chain-attacks-62d0272f656b), published June 16, 2021, describes authentication keys installed in the Secure Element during manufacturing. Those keys are separate from the wallet master keys generated during initialization. The explanation describes a backend hardware security module and the device exchanging a cryptographic challenge using their public and private keys.

The earlier description explains the separation between authentication and transaction signing, but leaves gaps in the breach account. The incident statement does not identify which component of that architecture exposed the key or explain how the monitoring-tool vulnerability gave access to it. Keystone's current warning is that counterfeit devices could pass the check.

The verification page gives separate instructions for a failed check: stop using the device and, especially, do not enter a seed phrase. Customers should preserve the failed result and contact official support. That procedure applies to devices that fail authentication; the disclosure now also requires additional verification for affected devices that pass.

## Customer records outlasted the retention policy

Keystone says the intrusion involved 51,083 buyer records from purchases through its website's Shopify store. It had already permanently erased personal information associated with 25,119 records, leaving anonymized order information. The remaining 25,964 records retained names, contact details, shipping addresses and order information covering 2024 to 2026. These figures count company-reported records, not independently verified victims.

The company says the affected purchase information excludes purchases through Amazon and other sales channels. Bank payment information and government-issued identification numbers were also outside the breach's scope, according to Keystone. Shopify separately held 12,873 unpaid checkout records containing submitted names, contact details and shipping information. Keystone included those records in its response, although some entries may be incomplete or inaccurate. Customers did not have to complete a purchase for their personal information to remain on file.

Keystone's stated policy required erasure after 180 days. The company says manual processing in Shopify was inefficient, so it built a bulk-erasure tool. The tool failed to run reliably, and Keystone missed failed tasks. Personal information remained on file beyond the promised period. The company accepted responsibility and shortened retention to 90 days, effective immediately.

On October 24, Keystone says it requested erasure of buyer personal data older than 90 days and checkout personal data older than 30 days. It attributes a 10-day waiting period for buyer-data erasure to Shopify's rules and expects completion on November 3. Keystone has submitted the requests and promises an update confirming the result once erasure is complete.

Keystone plans individual email notifications, a breach lookup page and a separate page for checking erasure status. It also plans a security audit and says it has submitted reports in the EU, UK and other jurisdictions. The disclosure gives no launch date for the lookup tools and does not explain the additional verification procedure support will use to clear old-key devices received after October 20.
