# bitcoin.stackexchange.com -- Scraped Content

**URL:** https://bitcoin.stackexchange.com/questions/29554/explanation-of-what-an-op-return-transaction-looks-like
**Category:** wayback-waf
**Scrape status:** DONE
**Source notes:** 
**Scraped:** 2026-04-13

---

*Archived version from 2026-01-06 via Wayback Machine*

Skip to main content

#### Stack Exchange Network

Stack Exchange network consists of 183 Q&A communities including [Stack Overflow](https://stackoverflow.com), the largest, most trusted online community for developers to learn, share their knowledge, and build their careers. 

[Visit Stack Exchange](https://stackexchange.com)

Loading…

[ ](https://bitcoin.stackexchange.com)

**Stack Internal**

Knowledge at work

Bring the best of human thought and AI automation together at your work.

[ Explore Stack Internal ](https://stackoverflow.co/internal/?utm_medium=referral&utm_source=bitcoin-community&utm_campaign=side-bar&utm_content=explore-teams-compact-popover)

# [Explanation of what an OP_RETURN transaction looks like](/questions/29554/explanation-of-what-an-op-return-transaction-looks-like)

[ Ask Question ](/questions/ask)

Asked 11 years, 5 months ago

Modified [8 months ago](?lastactivity "2025-04-26 22:44:57Z")

Viewed 50k times 

68 

[](/posts/29554/timeline "Show activity on this post.")

How is OP_RETURN used and why was it introduced in the first place?

  * [transactions](/questions/tagged/transactions "show questions tagged 'transactions'")
  * [protocol](/questions/tagged/protocol "show questions tagged 'protocol'")
  * [script](/questions/tagged/script "show questions tagged 'script'")
  * [op-return](/questions/tagged/op-return "show questions tagged 'op-return'")


[Share](/q/29554 "Short permalink to this question")

[Improve this question](/posts/29554/edit)

Follow 

[edited Jan 6, 2015 at 18:57](/posts/29554/revisions "show all edits to this post")

[](/users/307/deathandtaxes)

[DeathAndTaxes](/users/307/deathandtaxes)

8,85722 gold badges4040 silver badges6565 bronze badges

asked Jul 17, 2014 at 21:56

[](/users/17080/almel)

[almel](/users/17080/almel)

2,51611 gold badge1919 silver badges1717 bronze badges


Add a comment   | 

##  4 Answers 4

Sorted by:  [ Reset to default ](/questions/29554/explanation-of-what-an-op-return-transaction-looks-like?answertab=scoredesc#tab-top)

Highest score (default)  Date modified (newest first)  Date created (oldest first) 

99 

[](/posts/29555/timeline "Show activity on this post.")

Note: I went out and learned about how the `OP_RETURN` opcode works at the byte level in a bitcoin transaction. I’m writing it here so that others can learn quickly. First, a brief history of why we’re even talking about `OP_RETURN`.

Back in 2013 different players in the bitcoin ecosystem were trying to include bits of information into transactions so that they could take advantage of the irreversibility of the blockchain. Imagine for instance you wanted to write a contract and place it in an unchangeable location that at any future date one could go back to verify it existed. You can do this by using the blockchain. You add some bits to the transaction's scriptSig value that don't alter the end result of running that script, but allow you to store information like “I hereby declare to give asset A to address XYZ at time UNIX_TIMESTAMP”. There were even stranger ways people would add extra bits, like including it in the BTC value of an output. Some members of the community did not like this, as they saw these extra bits as polluting the blockchain. The extra bits were a network efficiency concern because more bits meant larger block chains and more of an onus on those who are running full nodes, and it was also a community consensus concern because they thought “we all implicitly agreed to store financial data in the blockchain, which is important to everyone, but we did not agree to store data like small text messages and invoice text”.

To reach a middle ground in these opposing views, the core-developers made the opcode OP_RETURN a valid opcode to be used in a bitcoin transaction, which allows 80 arbitrary bytes to be used in an unspendable transaction. A good explanation of this can be found in [Bitcoin Core Development Update #5 (archived)](https://web.archive.org/web/20150924060726/https://bitcoinfoundation.org/bitcoin/core-development-update-5/).

Later in February 2014, the bytes count was reduced from 80 to 40 bytes. This change is documented in [Bitcoin Core pull request #3737](https://github.com/bitcoin/bitcoin/pull/3737). Note that in this pull discussion we learn that no more than one output with OP_RETURN can be included in a single transaction.

Now that we’ve got the reason behind OP_RETURN down, let’s look at an example of OP_RETURN. I used chain.com’s API to find a transaction which has an OP_RETURN in its scriptSig. That tx’s hash is
    
    
    8bae12b5f4c088d940733dcd1455efc6a3a69cf9340e17a981286d3778615684 
    

Make sure you are connected to a fully-loaded bitcoind node, and run this command:
    
    
    $> bitcoind getrawtransaction 8bae12b5f4c088d940733dcd1455efc6a3a69cf9340e17a981286d3778615684 1
    

which will give you this output:
    
    
    {
    "hex" : "0100000001c858ba5f607d762fe5be1dfe97ddc121827895c2562c4348d69d02b91dbb408e010000008b4830450220446df4e6b875af246800c8c976de7cd6d7d95016c4a8f7bcdbba81679cbda242022100c1ccfacfeb5e83087894aa8d9e37b11f5c054a75d030d5bfd94d17c5bc953d4a0141045901f6367ea950a5665335065342b952c5d5d60607b3cdc6c69a03df1a6b915aa02eb5e07095a2548a98dcdd84d875c6a3e130bafadfd45e694a3474e71405a4ffffffff020000000000000000156a13636861726c6579206c6f766573206865696469400d0300000000001976a914b8268ce4d481413c4e848ff353cd16104291c45b88ac00000000",
    "txid" : "8bae12b5f4c088d940733dcd1455efc6a3a69cf9340e17a981286d3778615684",
    "version" : 1,
    "locktime" : 0,
    "vin" : [
        {
            "txid" : "8e40bb1db9029dd648432c56c295788221c1dd97fe1dbee52f767d605fba58c8",
            "vout" : 1,
            "scriptSig" : {
                "asm" : "30450220446df4e6b875af246800c8c976de7cd6d7d95016c4a8f7bcdbba81679cbda242022100c1ccfacfeb5e83087894aa8d9e37b11f5c054a75d030d5bfd94d17c5bc953d4a01 045901f6367ea950a5665335065342b952c5d5d60607b3cdc6c69a03df1a6b915aa02eb5e07095a2548a98dcdd84d875c6a3e130bafadfd45e694a3474e71405a4",
                "hex" : "4830450220446df4e6b875af246800c8c976de7cd6d7d95016c4a8f7bcdbba81679cbda242022100c1ccfacfeb5e83087894aa8d9e37b11f5c054a75d030d5bfd94d17c5bc953d4a0141045901f6367ea950a5665335065342b952c5d5d60607b3cdc6c69a03df1a6b915aa02eb5e07095a2548a98dcdd84d875c6a3e130bafadfd45e694a3474e71405a4"
            },
            "sequence" : 4294967295
        }
    ],
    "vout" : [
        {
            "value" : 0.00000000,
            "n" : 0,
            "scriptPubKey" : {
                "asm" : "OP_RETURN 636861726c6579206c6f766573206865696469",
                "hex" : "6a13636861726c6579206c6f766573206865696469",
                "type" : "nulldata"
            }
        },
        {
            "value" : 0.00200000,
            "n" : 1,
            "scriptPubKey" : {
                "asm" : "OP_DUP OP_HASH160 b8268ce4d481413c4e848ff353cd16104291c45b OP_EQUALVERIFY OP_CHECKSIG",
                "hex" : "76a914b8268ce4d481413c4e848ff353cd16104291c45b88ac",
                "reqSigs" : 1,
                "type" : "pubkeyhash",
                "addresses" : [
                    "1HnhWpkMHMjgt167kvgcPyurMmsCQ2WPgg"
                ]
            }
        }
    ],
    "blockhash" : "000000000000000004c31376d7619bf0f0d65af6fb028d3b4a410ea39d22554c",
    "confirmations" : 2655,
    "time" : 1404107109,
    "blocktime" : 1404107109
    }
    

Now, look at this transaction’s list of outputs, in particular the 1st one. By referencing [the Bitcoin Wiki’s page on Script](https://en.bitcoin.it/wiki/Script), Bitcoin’s stack-based programming language, we can see here that the `OP_RETURN` opcode is represented by the hex value 0x6a. This first byte it followed by a byte which represents the length of the rest of the bytes in the scriptPubKey. In this case we see the hex value 0x13, which means there are 19 more bytes. These bytes comprise the arbitrary less-than-40 bytes you are allowed to send in a transaction marked by the `OP_RETURN` opcode. If you pop the message bytes into a UTF8 decoder, you’ll see that
    
    
    636861726c6579206c6f766573206865696469
    

becomes “charley loves heidi”. Aw! It’s almost like a digital version of a couple’s romantic heart tree carving. Now you understand at a byte level how `OP_RETURN` is supposed to work. You can write software now that searches for the `OP_RETURN` opcode in an output’s scriptPubKey, and use it to verify a contract or some other digital asset.

[Share](/a/29555 "Short permalink to this answer")

[Improve this answer](/posts/29555/edit)

Follow 

[edited Apr 26, 2025 at 22:44](/posts/29555/revisions "show all edits to this post")

[](/users/-1/community)

[Community](/users/-1/community)Bot

1

answered Jul 17, 2014 at 22:00

[](/users/17080/almel)

[almel](/users/17080/almel)

2,51611 gold badge1919 silver badges1717 bronze badges

15

  * 14

An important aspect of OP_RETURN is that outputs which use it in the standard way are provable unspendable. This means that nodes can immediately remove such outputs from their unspent outputs cache and potentially forget about them altogether (though Bitcoin Core doesn't do this yet). This makes OP_RETURN transactions _much_ less expensive for the network than other ways of stuffing data into the block chain.

theymos

–  [theymos](/users/403/theymos "9,064 reputation")

2014-07-17 22:47:49 +00:00

Commented Jul 17, 2014 at 22:47

  * 10

FYI if anyone is looking to decode that message `636861726c6579206c6f766573206865696469` in php, it's the hex value so use `hex2bin()`

OACDesigns

–  [OACDesigns](/users/19005/oacdesigns "143 reputation")

2015-02-02 10:34:11 +00:00

Commented Feb 2, 2015 at 10:34

  * Why does this cost less to the network that just sending 1 satoshi to an arbitrary address that contains the 20 bytes of information itself ?

Nathan Parker

–  [Nathan Parker](/users/27866/nathan-parker "758 reputation")

2015-09-08 08:23:28 +00:00

Commented Sep 8, 2015 at 8:23

  * 6

@NathanParker Because with OP_RETURN, the node knows that the transaction output index is unspendable and can just ignore it. Whereas when sending 1 satoshi, the node will need to keep that unspent output in memory or in a database, waiting until someone spends it someday.

Nayuki

–  [Nayuki](/users/23340/nayuki "892 reputation")

2015-09-16 23:43:53 +00:00

Commented Sep 16, 2015 at 23:43

  * 1

For those wishing to decode the message using JavaScript, the one-liner in Node would be `Buffer.from('636861726c6579206c6f766573206865696469', 'hex').toString('utf8');`

thalisk

–  [thalisk](/users/41988/thalisk "503 reputation")

2019-03-12 11:43:15 +00:00

Commented Mar 12, 2019 at 11:43


 |  Show **10** more comments 

12 

[](/posts/40616/timeline "Show activity on this post.")

If you want to write OP_RETURNs to the blockchain without getting into the internals of how transactions are built, an easy way is to use our libraries for PHP and Python:

<https://github.com/coinspark/php-OP_RETURN>

<https://github.com/coinspark/python-OP_RETURN>

These support either sending individual transactions with one OP_RETURN attached, or else sending a batch of linked transactions to embed larger pieces of content. That content can then be retrieved from the blockchain using a single identifier.

Assuming you're using Bitcoin Core 0.11, you can change the value of `OP_RETURN_MAX_BYTES` to `80`, rather than `40` as it currently stands in the code.

[Share](/a/40616 "Short permalink to this answer")

[Improve this answer](/posts/40616/edit)

Follow 

answered Sep 21, 2015 at 5:44

[](/users/27169/gideon-greenspan)

[Gideon Greenspan](/users/27169/gideon-greenspan)

37433 silver badges66 bronze badges


Add a comment   | 

5 

[](/posts/101451/timeline "Show activity on this post.")

**`OP_RETURN` is a way to get arbitrary data into the blockchain with less burden to the network**

As a consequence, the data will also be present in less clients, as `OP_RETURN` data can be pruned out.

The goal of this answer is to explain what <https://bitcoin.stackexchange.com/a/29555/21282> explained but with a bit more context for Bitcoin newbies.

**How a standard transaction looks like**

As seen in the JSON disassembly from <https://bitcoin.stackexchange.com/a/29555/21282> each transaction has a list of outputs, and each output has a script.

The [most common script by far](https://bitcoin.stackexchange.com/questions/5883/is-there-a-listing-of-strange-or-unusual-scripts-found-in-transactions/105392#105392) is [pay-to-pubkey-hash](https://en.bitcoin.it/wiki/Script#Standard_Transaction_to_Bitcoin_address_.28pay-to-pubkey-hash.29) which basically says:

> this output can be consumed by the person who controls the private key to this public key

or in simpler terms "pay X bitcoint to address Y".

That script has format:
    
    
    OP_DUP OP_HASH160 <length-of-hash> <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
    

where pubKeyHash is 20 bytes and all other 5 fields are 1 byte.

**It is impossible to know if a standard transaction hash is an actual hash or arbitrary data**

Because `pubKeyHash` is a hash, it is impossible to know if that is the actual hash of something, or arbitrary data someone wants to encode into the blockchain.

The catch is: if you add arbitrary data there, you won't have a corresponding private key to claim back those funds. So what people do is to make transactions with the smallest amount possible that miners are willing to take for the verification work.

Now, every transaction in the blockchain takes as input a previous unspent output.

Therefore, embedding this data costs you a little, because that output is unspendable: it can never be used as an input of another transaction.

In order to verify if a transaction is valid, Bitcoin implementations have to keep around a full list of every unspent output ever created, known as the [UTXO set](https://en.bitcoin.it/wiki/UTXO).

Spent outputs can be pruned to save space, but unspent ones can't.

Therefore, whenever you burn your fake pubkey hash output, you force every single implementation to keep that information around forever, since those funds can never be spent.

**How`OP_RETURN` solves that problem**

OP return is another type of script transaction different from the standard pay-to-pubkey-hash transaction.

As mentioned at: <https://en.bitcoin.it/wiki/Script#Provably_Unspendable.2FPrunable_Outputs> the transaction has simply the form:
    
    
    OP_RETURN <data>
    

`OP_RETURN` simply stops the script execution with a failure, making it impossible for anyone to use that output as the input of another transaction.

Therefore, when a bitcoin implementation sees that transaction, it can immediately decide that it is unspendable, unlike the pay-to-pubkey-hash transaction above, where it is impossible to make that decision. That's why this transaction is called "provably unspendable".

So the miner can mine if for a mining fee, but then implementations immediately prune it from the UTXO set.

This allows the UTXO set to be smaller, thus making bitcoin more efficient to everyone.

But on the other hand, it also means that your embedded data will be present in less people's computers.

[Share](/a/101451 "Short permalink to this answer")

[Improve this answer](/posts/101451/edit)

Follow 

[edited Nov 29, 2021 at 13:23](/posts/101451/revisions "show all edits to this post")

answered Jan 14, 2021 at 9:05

[](/users/21282/ciro-santilli-ourbigbook-com)

[Ciro Santilli OurBigBook.com](/users/21282/ciro-santilli-ourbigbook-com)

33122 silver badges88 bronze badges

2

  * If I "add arbitrary data", won't it make the transaction invalid and not accepted in the blockchain? Or is it just the address of the recipient and instead of putting my own address I just put some arbitrary data?

Rony Tesler

–  [Rony Tesler](/users/127077/rony-tesler "329 reputation")

2021-09-20 01:33:42 +00:00

Commented Sep 20, 2021 at 1:33

  * 1

@RonyTesler you just put arbitrary data instead of an actual address you control. But since addresses look completely random in nature (they are public keys) it is impossible for peers to distinguish, so it has to be added to the chain. And because you don't have the private key, it is impossible for you (or anyone else) to claim funds later on.

Ciro Santilli OurBigBook.com

–  [Ciro Santilli OurBigBook.com](/users/21282/ciro-santilli-ourbigbook-com "331 reputation")

2021-09-20 07:13:26 +00:00

Commented Sep 20, 2021 at 7:13


Add a comment   | 

1 

[](/posts/95121/timeline "Show activity on this post.")

In case you are here trying to convert OP_RETURN to readable values:

_Note: This is javascript / typescript_
    
    
    export default class OpReturnConverter {
    
        // Input -> <Buffer 35 33 36 39...>
        // Output -> 53696d706c6520616e737765722120f09f988a
        public static convertBufferToHex(buffer: Buffer) {
            const str = buffer.toString('hex')
            return Buffer.from(str, 'hex').toString()
        }
    
        // Input -> 53696d706c6520616e737765722120f09f988a
        // Output -> Simple answer! 😊
        public static convertHexToString(hex: string) {
            return Buffer.from(hex, 'hex').toString()
        }
    
        // Input -> Simple answer! 😊
        // Output -> <Buffer 35 33 36 39...>
        public static convertStringToBuffer(message: string) {
            const hexBuffer = Buffer.from(message).toString('hex')
            return Buffer.from(hexBuffer)
        }
    
    }
    

* * *

**Results**
    
    
    const string = 'Simple answer! 😊'
    console.log('Original ->', string)
    
    const buf = OpReturnConverter.convertStringToBuffer(string)
    console.log('Buffer ->', buf)
    
    const hex = OpReturnConverter.convertBufferToHex(buf)
    console.log('Hex ->', hex)
    
    const unhex = OpReturnConverter.convertHexToString(hex)
    console.log('Unhex ->', unhex)
    

[Share](/a/95121 "Short permalink to this answer")

[Improve this answer](/posts/95121/edit)

Follow 

answered Apr 5, 2020 at 0:45

[](/users/51663/michael)

[Michael](/users/51663/michael)

18311 silver badge88 bronze badges


Add a comment   | 

##  Your Answer 

Draft saved

Draft discarded

### Sign up or [log in](/users/login?ssrc=question_page&returnurl=https%3a%2f%2fbitcoin.stackexchange.com%2fquestions%2f29554%2fexplanation-of-what-an-op-return-transaction-looks-like%23new-answer)

Sign up using Google 

Sign up using Email and Password 

Submit

### Post as a guest

Name

Email

Required, but never shown

Post Your Answer  Discard 

By clicking “Post Your Answer”, you agree to our [terms of service](https://stackoverflow.com/legal/terms-of-service/public) and acknowledge you have read our [privacy policy](https://stackoverflow.com/legal/privacy-policy).

Start asking to get answers

Find the answer to your question by asking.

[Ask question](/questions/ask)

Explore related questions

  * [transactions](/questions/tagged/transactions "show questions tagged 'transactions'")
  * [protocol](/questions/tagged/protocol "show questions tagged 'protocol'")
  * [script](/questions/tagged/script "show questions tagged 'script'")
  * [op-return](/questions/tagged/op-return "show questions tagged 'op-return'")


See similar questions with these tags.

  * The Overflow Blog 
  * [What’s new at Stack Overflow: January 2026](https://stackoverflow.blog/2026/01/05/what-s-new-at-stack-overflow-january-2026/)

  * [Search engine bots crawled so AI bots could run](https://stackoverflow.blog/2026/01/06/search-engine-bots-crawled-so-ai-bots-could-run/)

  * Featured on Meta 
  * [Native Ads coming soon to Stack Overflow and Stack Exchange](https://meta.stackexchange.com/questions/415259/native-ads-coming-soon-to-stack-overflow-and-stack-exchange)

  * [A proposal for bringing back Community Promotion & Open Source Ads](https://meta.stackexchange.com/questions/416429/a-proposal-for-bringing-back-community-promotion-open-source-ads)


#### 

[... truncated at 20,000 characters ...]
