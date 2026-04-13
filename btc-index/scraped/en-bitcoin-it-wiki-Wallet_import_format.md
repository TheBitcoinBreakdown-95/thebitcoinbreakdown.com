# en.bitcoin.it -- Scraped Content

**URL:** https://en.bitcoin.it/wiki/Wallet_import_format
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Full list of Bitcoin address prefixes.md
**Scraped:** 2026-04-12

---

# Wallet import format

From Bitcoin Wiki

Jump to navigation Jump to search

This page contains sample addresses and/or private keys. Do not send bitcoins to or import any sample keys; you will lose your money.

A **wallet import format** (**WIF** , also known as a **wallet export format**) is a way of encoding a private ECDSA key so as to make it easier to copy. 

## Contents

  * 1 Private key to WIF
  * 2 WIF to private key
  * 3 WIF checksum checking
  * 4 References


## Private key to WIF

1\. Take a private key. 
    
    
       0C28FCA386C7A227600B2FE50B7CAE_SAMPLE_PRIVATE_KEY_DO_NOT_IMPORT_11EC86D3BF1FBE471BE89827E19D72AA1D
    

2\. Add a `0x80` byte in front of it for mainnet addresses or `0xef` for testnet addresses. Also add a `0x01` byte at the end if the private key will correspond to a compressed public key. 
    
    
       800C28FCA386C7A227600B2FE50B7C_SAMPLE_PRIVATE_KEY_DO_NOT_IMPORT_AE11EC86D3BF1FBE471BE89827E19D72AA1D
    

3\. Perform SHA-256 hash on the extended key. 
    
    
       8147786C4D15106333BF278D71DADAF1079EF2D2440A4DDE37D747DED5403592
    

4\. Perform SHA-256 hash on result of SHA-256 hash. 
    
    
       507A5B8DFED0FC6FE8801743720CEDEC06AA5C6FCA72B07C49964492FB98A714
    

5\. Take the first 4 bytes of the second SHA-256 hash; this is the checksum. 
    
    
       507A5B8D
    

6\. Add the 4 checksum bytes from point 5 at the end of the extended key from point 2. 
    
    
       800C28FCA386C7A227600B2FE50B7CAE11EC8_SAMPLE_PRIVATE_KEY_DO_NOT_IMPORT_6D3BF1FBE471BE89827E19D72AA1D507A5B8D
    

7\. Convert the result from a byte string into a base58 string using [Base58Check encoding](/wiki/Base58Check_encoding "Base58Check encoding"). This is the wallet import format (WIF). 
    
    
       5HueCGU8rMjxEXxiPuD5BDk_SAMPLE_PRIVATE_KEY_DO_NOT_IMPORT_u4MkFqeZyd4dZ1jvhTVqvbTLvyTJ
    

## WIF to private key

1\. Take a wallet import format (WIF) string. 
    
    
       5HueCGU8rMjxEXxiPuD5BDk_SAMPLE_PRIVATE_KEY_DO_NOT_IMPORT_u4MkFqeZyd4dZ1jvhTVqvbTLvyTJ
    

2\. Convert it to a byte string using [Base58Check encoding](/wiki/Base58Check_encoding "Base58Check encoding"). 
    
    
       800C28FCA386C7A227600B2FE50B7CAE11EC_SAMPLE_PRIVATE_KEY_DO_NOT_IMPORT_86D3BF1FBE471BE89827E19D72AA1D507A5B8D
    

3\. Drop the last 4 checksum bytes from the byte string. 
    
    
       800C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D
    

4\. Drop the first byte (it should be `0x80`, however legacy Electrum[1][2] or some SegWit vanity address generators[3] may use `0x81-0x87`). If the private key corresponded to a compressed public key, also drop the last byte (it should be `0x01`). If it corresponded to a compressed public key, the WIF string will have started with K or L (or M, if it's exported from legacy Electrum[1][2] etc[3]) instead of 5 (or c instead of 9 on testnet). This is the private key. 
    
    
       0C28FCA386C7A227600B2FE50B7CAE1_SAMPLE_PRIVATE_KEY_DO_NOT_IMPORT_1EC86D3BF1FBE471BE89827E19D72AA1D
    

## WIF checksum checking

1\. Take the wallet import format (WIF) string. 
    
    
       5HueCGU8rMjxEXxiPuD5BD_SAMPLE_PRIVATE_KEY_DO_NOT_IMPORT_ku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ
    

2\. Convert it to a byte string using [Base58Check encoding](/wiki/Base58Check_encoding "Base58Check encoding"). 
    
    
       800C28FCA386C7A227600B2FE50B7CAE11E_SAMPLE_PRIVATE_KEY_DO_NOT_IMPORT_C86D3BF1FBE471BE89827E19D72AA1D507A5B8D
    

3\. Drop the last 4 checksum bytes from the byte string. 
    
    
       800C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D
    

4\. Perform SHA-256 hash on the shortened string. 
    
    
       8147786C4D15106333BF278D71DADAF1079EF2D2440A4DDE37D747DED5403592
    

5\. Perform SHA-256 hash on result of SHA-256 hash. 
    
    
       507A5B8DFED0FC6FE8801743720CEDEC06AA5C6FCA72B07C49964492FB98A714
    

6\. Take the first 4 bytes of the second SHA-256 hash; this is the checksum. 
    
    
       507A5B8D
    

7\. Make sure it is the same as the last 4 bytes from point 2. 
    
    
       507A5B8D
    

8\. If they are, and the byte string from point 2 starts with `0x80` (`0xef` for testnet addresses), then there is no error. 

## References

  1. ↑ 1.0 1.1 [[1]](https://github.com/spesmilo/electrum/blob/3.0.0/RELEASE-NOTES#L42)
  2. ↑ 2.0 2.1 [[2]](https://github.com/spesmilo/electrum/blob/3.1.0/RELEASE-NOTES#L58)
  3. ↑ 3.0 3.1 [[3]](https://github.com/nym-zone/segvan/blob/388b157c68c3b45f7c3200cc62a2fea6ffcb5555/segvan.c#L88)


[](/wiki/File:Hashbtc.jpg)_This page is a stub. Help by expanding it._

|  [Bitcoin Core](/wiki/Bitcoin_Core "Bitcoin Core") documentation  
---  
User documentation|  [Alert system](/wiki/Alert_system "Alert system") • [Bitcoin Core compatible devices](/wiki/Bitcoin_Core_compatible_devices "Bitcoin Core compatible devices") • [Data directory](/wiki/Data_directory "Data directory") • [Fallback Nodes](/wiki/Fallback_Nodes "Fallback Nodes") • [How to import private keys in Bitcoin Core 0.7+](/wiki/Help:How_to_import_private_keys_in_Bitcoin_Core_0.7%2B "Help:How to import private keys in Bitcoin Core 0.7+") • [Installing Bitcoin Core](/wiki/Help:Installing_Bitcoin_Core "Help:Installing Bitcoin Core") • [Running Bitcoin](/wiki/Running_Bitcoin "Running Bitcoin") • [Transaction fees](/wiki/Transaction_fees "Transaction fees") • [Vocabulary](/wiki/Vocabulary "Vocabulary")  
Developer documentation|  [Accounts explained](/wiki/Help:Accounts_explained "Help:Accounts explained") • [API calls list](/wiki/Original_Bitcoin_client/API_calls_list "Original Bitcoin client/API calls list") • [API reference (JSON-RPC)](/wiki/API_reference_\(JSON-RPC\) "API reference \(JSON-RPC\)") • [Block chain download](/wiki/Block_chain_download "Block chain download") • [Dump format](/wiki/Dump_format "Dump format") • [getblocktemplate](/wiki/Getblocktemplate "Getblocktemplate") • [List of address prefixes](/wiki/List_of_address_prefixes "List of address prefixes") • [Protocol documentation](/wiki/Protocol_documentation "Protocol documentation") • [Script](/wiki/Script "Script") • [Technical background of version 1 Bitcoin addresses](/wiki/Technical_background_of_version_1_Bitcoin_addresses "Technical background of version 1 Bitcoin addresses") • [Testnet](/wiki/Testnet "Testnet") • [Transaction Malleability](/wiki/Transaction_Malleability "Transaction Malleability") • Wallet import format  
History & theory|  [Common Vulnerabilities and Exposures](/wiki/Common_Vulnerabilities_and_Exposures "Common Vulnerabilities and Exposures") • [DOS/STONED incident](/wiki/DOS/STONED_incident "DOS/STONED incident") • [Economic majority](/wiki/Economic_majority "Economic majority") • [Full node](/wiki/Full_node "Full node") • [Original Bitcoin client](/wiki/Original_Bitcoin_client "Original Bitcoin client") • [Value overflow incident](/wiki/Value_overflow_incident "Value overflow incident")  
  
Retrieved from "[https://en.bitcoin.it/w/index.php?title=Wallet_import_format&oldid=70077](https://en.bitcoin.it/w/index.php?title=Wallet_import_format&oldid=70077)"

[Category](/wiki/Special:Categories "Special:Categories"): 

  * [Bitcoin Core documentation](/wiki/Category:Bitcoin_Core_documentation "Category:Bitcoin Core documentation")


Hidden category: 

  * [Stubs](/wiki/Category:Stubs "Category:Stubs")


## Navigation menu

### Search

[](/wiki/Main_Page "Visit the main page")
