# blink.sv -- Scraped Content

**URL:** https://blink.sv/blog/introducing-the-blink-plugin-for-btcpay-server
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\BTC Pay Server.md
**Scraped:** 2026-04-12

---

ESEN

[](/)

  * Features

  * API

  * [Blog](/en/blog/articles)
  * [Support](/en/support)
  * 


[BLOG -Blink announcements](/en/blog/articles)

# Introducing the Blink Plugin for BTCPay Server: Streamlining Lightning Payments

Big news for BTCPay Server users: the Blink Plugin is here! 

January 4, 2024

Author

Pretyflaco

Follow us

[](/en/social)

Share on FB Share on X

Big news for [BTCPay Server](https://btcpayserver.org) users: the Blink Plugin is here! This is a game-changer for merchants looking to tap into Lightning payments more easily. Developed through a community-driven bounty, this is a prime example of what we achieve together in the open-source bitcoin world.

‍

## **Background**

In our mission at Blink to enhance the Bitcoin payment experience, we've identified a common hurdle: the complexity of leveraging Lightning transactions for merchants using BTCPay Server. Running a Lightning Node or depending on third-party, often hobbyist custodians has been a significant barrier, especially for non-technical users. To address this, we've collaborated with the BTCPay Server team to create a seamless solution – the Blink Plugin.

‍

## **The Blink Plugin: Streamlining Lightning Payments with Practical Benefits**

Simple, powerful, and integrated: the Blink Plugin connects your Blink account to BTCPay Server, sidestepping the need for a Lightning Node. It’s all about making Lightning payments straightforward and accessible.

‍

### **Key Benefits:**

  * **Hassle-Free Management:** Ditch the complexity of running a Lightning Node. The Blink Plugin is custodial, handling liquidity management for you. It's simple: connect your Blink account to BTCPay Server and manage Lightning payments with ease. No technical deep dives needed.
  * **Stable Value with Stablesats:** Worried about Bitcoin's volatility? Choose Stablesats in Blink and tie the value of your sats to the US Dollar. This feature lets you receive payments in a stable value form, giving you peace of mind and financial stability in a fluctuating market.
  * **Lightning Payments for All:** We're tearing down technical barriers to make Lightning payments accessible to everyone. It doesn’t matter if you're new to Bitcoin or a seasoned merchant; the Blink Plugin is designed for easy adoption, expanding the reach of Lightning payments across the community.


Our goal with the Blink Plugin is clear: Make Lightning transactions straightforward and inclusive. Join us in embracing this next step in Bitcoin payments.

‍

Introducing the Blink Plugin for BTCPay Server! A groundbreaking integration making Lightning payments easier than ever.   
  
Thanks to [@BtcFrankenstein](https://twitter.com/BtcFrankenstein) for this fantastic teaser! 

Check it out 

‍

## **How It Works**

‍

Here’s how you get started:

  * **Install** : Begin by adding the Blink Plugin to your BTCPay Server, ensuring it's version 1.12.1 or higher.
  * **Select Bitcoin or Stablesats:** In your Blink mobile app, specify your default account – choose between Bitcoin or Stablesats. 
  * **Key Generation:** Create a READ+RECEIVE-only Blink API key via [your Blink dashboard](https://dashboard.blink.sv). This is a crucial security feature. The READ+RECEIVE-only nature of the key means that even if you use Blink on a third-party BTCPay Server instance, your funds remain secure. Even in the hands of a malicious server admin, your funds cannot be moved, offering you peace of mind. 
  * **Link Up:** Finally, connect your Blink account to your BTCPay Server Store. Navigate to ‘Lightning > Settings > Custom Node’ and enter your Blink API key with the connection string “type=blink;api-key=blink_…”


Ready to go! You're now set to receive Lightning payments directly to your chosen Blink account. For detailed steps, check out our [Blink Plugin documentation](https://dev.blink.sv/examples/btcpayserver-plugin).

‍

‍

## **User Benefits**

This isn’t just a technical tweak. It’s a way to make handling Bitcoin transactions simpler and smarter. Quick, efficient, and less tech-heavy.

‍

## **Looking Ahead**

We’re not stopping here. Expect regular updates to the Blink Plugin, driven by your feedback and the evolving needs of the community.

‍

## **Conclusion**

The Blink Plugin bridges BTCPay Server with Blink, uniting two open source powerhouses in the Bitcoin sphere. Dive in and see how it transforms your payment processing experience. [Download Blink now](https://get.blink.sv) to your iOS or Android phone and create your account with just a phone number in 2 minutes. Receiving Lightning payments has never been easier!

‍

### **Additional Resources**

  * [**Get Blink for your iOS or Android phone**](https://get.blink.sv)****
  * [**Blink Community & Support on Telegram**](https://t.me/btcpayserver)
  * [**BTCPay Server Community & Support on Telegram**](https://t.me/btcpayserver)
  * [**Blink API Documentation for the Blink Plugin**](https://dev.blink.sv/examples/btcpayserver-plugin)
  * [**Source Code of the Blink Plugin**](https://github.com/Kukks/BTCPayServerPlugins/tree/master/Plugins/BTCPayServer.Plugins.Blink)
  * [**Galoy Developer Chat on Mattermost**](https://chat.galoy.io)
  * [**BTCPay Server Developer Chat on Mattermost**](https://chat.btcpayserver.org)‍
  * TIP: The [BTCPay Server Directory](https://directory.btcpayserver.org/filter/hosts) lists multiple free or paid third-party hosts that you can register to, to start exploring BTCPay Server.


### **BTCPay Instances with Public Registration and active Blink Plugin**

  * [**Bitcoin Aruba** https://btcpay.btc.aw/](https://btcpay.btc.aw/)
  * [**BTCPay Bulgaria**](https://btcpay.btc.aw/)<https://app.btcpay.bg/>
  * [**withbitcoin.org** ](https://app.btcpay.bg/)<https://pay.withbitcoin.org/>
  * [**ideasarelikeflames** https://btcpay.ideasarelikeflames.org](https://btcpay.ideasarelikeflames.org/register)
  * [**Bitcoin Only South Africa** https://btcpay386617.lndyn.com](https://btcpay386617.lndyn.com/register)
  * [**Lightningshops.io** https://lns.lightningshops.io/](https://lns.lightningshops.io/register)


‍

### **Blink X BTCPay Workshop at Adopting Bitcoin Cape Town**

‍

‍

### **Developer 's Corner: Elevate Your Apps with Blink API**

> Harness the Blink API to integrate Lightning payments seamlessly into your apps, just like the Blink Plugin for BTCPay. Ideal for e-commerce, payment gateways, and innovative Bitcoin applications.

> **Effortless Integration:** User-friendly API, with comprehensive documentation. 

> **Secure and Adaptable:** Ensures safe transactions and supports both Bitcoin and Stablesats.

> **Build Your Own Solutions:** Follow the path of the Blink Plugin to create custom integrations for your apps.

> Get started with our [Blink API documentation](https://dev.blink.sv) and explore the possibilities.

### Did you find this valuable? Tip the author!

[Make your own donation button](https://donation-button.blink.sv/)

### Did you find this valuable? Tip the author!

[Make your own donation button](https://donation-button.blink.sv/)

Share on FB Share on X

[](/blog/how-bitcoin-atm-brands-are-integrating-the-blink-api-into-their-services)

## [How Bitcoin ATM Brands Are Integrating the Blink API into Their Services](/blog/how-bitcoin-atm-brands-are-integrating-the-blink-api-into-their-services)

[](/blog/bitcoin-atlantis-a-beacon-for-bitcoin-adoption)

## [Bitcoin Atlantis: A Beacon for Bitcoin Adoption](/blog/bitcoin-atlantis-a-beacon-for-bitcoin-adoption)

[](/blog/know-your-custodian)

## [Know Your Custodian: The Security and Reliability of Blink, Your Everyday Bitcoin Wallet](/blog/know-your-custodian)

## Download Blink

Start receiving and sending bitcoin now

[App Store](https://apps.apple.com/ng/app/bitcoin-beach-wallet/id1531383905)[Google Play](https://play.google.com/store/apps/details?id=com.galoyapp)[App Gallery ](https://appgallery.huawei.com/app/C105387593)[Get APK](https://github.com/blinkbitcoin/blink-mobile/releases/)[Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzprl98vm4rr3ah6d6kfkezg5jqqwchzpda9zkk7cgkc2ljyku3062qqxxxmmd9enkzmr009shquq4za20d)

## Follow us

[](/en/social)

[Born in El Zonte](/)

Resources

[Blink Brand](/en/brand)[Onboarding resources](https://www.blink.sv/en/brand#resources)[Blink merch](https://blinkstuff.com/)[Bitcoin whitepaper ](https://cdn.prod.website-files.com/6720ed07d56bdfa402a08023/6720ed07d56bdfa402a08263_bitcoin.pdf)

BLINK.SV

[About](/en/about)[Features](/en/features)[Bounties](/en/bounties)[API](/en/api)[Blog](/en/blog/blink-news)[Support](/en/support)[Join the Beta](/en/beta)[Blink Private](/private)

Info

[FAQ](https://faq.blink.sv/)[Dev Docs](https://dev.blink.sv/)[Github](https://github.com/blinkbitcoin/blink-mobile)[Status Page](https://blink.statuspage.io/)[Node](https://mempool.space/lightning/node/02fcc5bfc48e83f06c04483a2985e1c390cb0f35058baa875ad2053858b8e80dbd)[WalletScrutiny](https://walletscrutiny.com/android/com.galoyapp/)

Made with ♥ in Próspera 

‍  
© 2026 Blink Technologies LLC  
[ Terms & Conditions](/en/terms-conditions) | [Privacy policy](/en/privacy-policy)

[](https://api.whatsapp.com/send?phone=50369835117)

We use cookies for analytics and to improve site functionality. Feel free to opt-out.

AcceptReject
