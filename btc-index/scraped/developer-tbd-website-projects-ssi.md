# developer.tbd.website -- Scraped Content

**URL:** https://developer.tbd.website/projects/ssi
**Category:** retry-wayback
**Scrape status:** DONE
**Source notes:** 
**Scraped:** 2026-04-13

---

*Archived version from 2024-07-19 via Wayback Machine*

Close

Ask Me Anything: 

.. and press ENTER to ask a question on web5, how to write code and more.

Skip to main content

# SSI: Self Sovereign Identity

## Putting you in control of your identity​

Self-sovereign identity (SSI) is an approach to digital identity that gives individuals control over the information they use to prove who they are to websites, services, and applications across the web.

SSI brings Decentralized Identity together with Verifiable Credentials. It lets devs focus on creating delightful user experiences, while returning ownership of data and identity to individuals.

The following is sometimes called the **triangle of trust** :

The Issuers are a trusted source of credentials, perhaps issuing passports of drivers licenses, or perhaps a trusted person. They can use services like the [SSI Service](https://github.com/TBD54566975/ssi-service) or the [SSI SDK](https://github.com/TBD54566975/ssi-sdk) to create new credentials and issue them to holders.

The holder provides their DID to the Issuer, who then decides whether or not to issue a credential to the holder. This is called Issuance.

The holders then keep their credentials for later use. The holder can present the credential (as a presentation, or as a JSON or [JWT](https://jwt.io/) string) to a Verifier. The Verifier will check that the credential belongs to the holder (via their DID), and that they (the Verifier) trusts the Issuer (via their DID). If they do, they can trust the Holder that they have the qualifications presented to them.

The SSI SDK and SSI Service provide utilities for issuing credentials and managing them, and the SSI SDK and (many other) libraries can help you validate presented credentials.

[🚀 SSI Docs](/docs)

[Contribute](/open-source/contributing)

[Chat on Discord](https://discord.gg/tbd)
