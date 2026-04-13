# en.bitcoin.it -- Scraped Content

**URL:** https://en.bitcoin.it/wiki/Transaction
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Full list of Bitcoin address prefixes.md
**Scraped:** 2026-04-12

---

# Transaction

From Bitcoin Wiki

Jump to navigation Jump to search

[](/wiki/File:TxBinaryMap.png)Byte-map of Transaction with each type of TxIn and TxOut

A **transaction** is a transfer of Bitcoin value that is broadcast to the [network](/wiki/Network "Network") and collected into [blocks](/wiki/Block "Block"). A transaction typically references previous transaction outputs as new transaction inputs and dedicates all input Bitcoin values to new outputs. Transactions are not encrypted, so it is possible to browse and view every transaction ever collected into a block. Once transactions are buried under enough [confirmations](/wiki/Confirmation "Confirmation") they can be considered [irreversible](/wiki/Irreversible_Transactions "Irreversible Transactions"). 

This article is about **on-chain transactions**. See also: [Off-Chain Transactions](/wiki/Off-Chain_Transactions "Off-Chain Transactions")

Standard transaction outputs nominate [addresses](/wiki/Address "Address"), and the redemption of any future inputs requires a relevant signature. 

All transactions are visible in the [block chain](/wiki/Block_chain "Block chain"), and can be viewed with a hex editor. A [block chain browser](/wiki/Block_chain_browser "Block chain browser") is a site where every transaction included within the block chain can be viewed in human-readable terms. This is useful for seeing the technical details of transactions in action and for verifying payments. 

## Contents

  * 1 General format of a Bitcoin transaction (inside a block)
  * 2 Principle example of a Bitcoin transaction with 1 input and 1 output only
    * 2.1 Data
    * 2.2 Explanation
      * 2.2.1 Input
      * 2.2.2 Output
      * 2.2.3 Witness
      * 2.2.4 Verification
  * 3 Types of Transaction
    * 3.1 Pay-to-PubkeyHash
    * 3.2 Pay-to-Script-Hash
  * 4 Generation
  * 5 General format (inside a block) of each input of a transaction - Txin
  * 6 General format (inside a block) of each output of a transaction - Txout
  * 7 See Also


### General format of a Bitcoin transaction (inside a block)

Field  | Description  | Size   
---|---|---  
Version no  | currently 1. Set to 2 if you use OP_CHECKSEQUENCEVERIFY to enable timelocks  | 4 bytes   
Flag  | If present, always 0001, and indicates the presence of witness data  | optional 2 byte array   
In-counter  | positive integer [VI = VarInt](/wiki/Protocol_specification#Variable_length_integer "Protocol specification") | 1 - 9 bytes   
list of inputs  | the first input of the first transaction is also called "coinbase" (its content was ignored in earlier versions) | <in-counter>-many inputs   
Out-counter  | positive integer [VI = VarInt](/wiki/Protocol_specification#Variable_length_integer "Protocol specification") | 1 - 9 bytes   
list of outputs  | the outputs of the first transaction spend the mined bitcoins for the block | <out-counter>-many outputs   
Witnesses  | A list of witnesses, 1 for each input, omitted if flag above is missing  | variable, see [Segregated_Witness](/wiki/Segregated_Witness "Segregated Witness")  
lock_time  | if non-zero and sequence numbers are < 0xFFFFFFFF: block height or timestamp when transaction is final  | 4 bytes   
  
There is no version 0 transaction - it is undefined. Versions greater than 2 are reserved for future use by the protocol. Flag and Witness are mandatory for any transaction that includes [Segwit](/wiki/Segwit "Segwit") inputs, and should be omitted for legacy transactions that do not make use of Segwit. 

### Principle example of a Bitcoin transaction with 1 input and 1 output only

#### Data
    
    
    Input:
    Previous tx: f5d8ee39a430901c91a5917b9f2dc19d6d1a0e9cea205b009ca73dd04470b9a6
    Index: 0
    scriptSig: 304502206e21798a42fae0e854281abd38bacd1aeed3ee3738d9e1446618c4571d10
    90db022100e2ac980643b0b82c0e88ffdfec6b64e3e6ba35e7ba5fdd7d5d6cc8d25c6b241501
    
    Output:
    Value: 5000000000
    scriptPubKey: OP_DUP OP_HASH160 404371705fa9bd789a2fcd52d2c580b65d35549d
    OP_EQUALVERIFY OP_CHECKSIG

#### Explanation

The input in this transaction imports 50 BTC from output #0 in transaction f5d8... Then the output sends 50 BTC to a Bitcoin address (expressed here in hexadecimal 4043... instead of the normal base58). When the recipient wants to spend this money, he will reference output #0 of this transaction in an input of his own transaction. 

##### Input

Field  | Description  | Size   
---|---|---  
Outpoint hash  | The previous transaction that contains the spendable output  | 32 bytes   
Outpoint index  | The index within the previous transaction's output array to identify the spendable output  | 4 bytes   
Script length  | positive integer [VI = VarInt](/wiki/Protocol_specification#Variable_length_integer "Protocol specification") | 1 - 9 bytes   
Script signature  | Information required to spend the output (see below for details)  | Variable   
Sequence number  | if sequence number is < 0xFFFFFFFF: Makes the transaction input [Replace-By-Fee](/wiki/RBF "RBF") | 4 bytes   
  
  
An **input** is a reference to an output from a previous transaction. Multiple inputs are often listed in a transaction. All of the new transaction's input values (that is, the total coin value of the previous outputs referenced by the new transaction's inputs) are added up, and the total (less any transaction fee) is completely used by the outputs of the new transaction. **Previous tx** is a [hash](/wiki/Hash "Hash") of a previous transaction. **Index** is the specific output in the referenced transaction. **ScriptSig** is the first half of a [script](/wiki/Script "Script") (discussed in more detail later). 

The script contains two components, a signature and a public key. The public key must match the hash given in the script of the redeemed output. The public key is used to verify the redeemers signature, which is the second component. More precisely, the second component is an [ECDSA](/wiki/ECDSA "ECDSA") signature over a hash of a simplified version of the transaction. It, combined with the public key, proves the transaction was created by the real owner of the bitcoins in question. Various flags define how the transaction is simplified and can be used to create different types of payment. 

##### Output

Field  | Description  | Size   
---|---|---  
Value  | The monetary value of the output in satoshis  | 8 bytes   
Script length  | positive integer [VI = VarInt](/wiki/Protocol_specification#Variable_length_integer "Protocol specification") | 1 - 9 bytes   
Script  | A calculation which future transactions need to solve in order to spend it  | Variable   
  
An **output** contains instructions for sending bitcoins. **Value** is the number of Satoshi (1 BTC = 100,000,000 Satoshi) that this output will be worth when claimed. **ScriptPubKey** is the second half of a script (discussed later). There can be more than one output, and they share the combined value of the inputs. Because each output from one transaction can only ever be referenced once by an input of a subsequent transaction, the entire combined input value needs to be sent in an output if you don't want to lose it. If the input is worth 50 BTC but you only want to send 25 BTC, Bitcoin will create two outputs worth 25 BTC: one to the destination, and one back to you (known as "[change](/wiki/Change "Change")", though you send it to yourself). Any input bitcoins not redeemed in an output is considered a [transaction fee](/wiki/Transaction_fee "Transaction fee"); whoever generates the block can claim it by inserting it into the coinbase transaction of that block. 

[](/wiki/File:Bitcointransactions.JPG)A sends 6.102 BTC to C and C generates 6.25 BTC. C sends 3.12009 BTC to D, and he needs to send himself some change. D sends the 3.12009 BTC to someone else, but they haven't redeemed it yet. Only D's output and C's change are capable of being spent in the current state.

##### Witness

For Segwit transactions, there is a list of witness fields after the outputs, with each witness field corresponding to an input of the same index. Each witness field contains a varint which tells the number of elements on the witness' stack, and the stack elements themselves contains pairs of varints, signifying the length of the data, followed by the data itself. 

It is important to note that when parsing a raw transaction, the witness fields are **not** congregated together into one "witness" field in structured, deserialized output, but each witness is placed in its own "witness" key under the respective input. 

Transactions which do not have any native segwit (such as P2WPKH or P2WSH) inputs must use the legacy transaction format. Witness fields are only added for native segwit inputs, so a transaction with no such inputs cannot use the segwit transaction format, including the marker and flag. Additionally, each witness field corresponds to its respective native segwit input in the order which they are defined in the transaction. This means that in the raw transaction, the first witness field is for the first native segwit input in the transaction, and so on. 

##### Verification

To verify that inputs are authorized to collect the values of referenced outputs, Bitcoin uses a custom Forth-like [scripting](/wiki/Script "Script") system. The input's scriptSig and the _referenced_ output's scriptPubKey are evaluated (in that order), with scriptPubKey using the values left on the stack by scriptSig. The input is authorized if scriptPubKey returns true. Through the scripting system, the sender can create very complex conditions that people have to meet in order to claim the output's value. For example, it's possible to create an output that can be claimed by anyone without any authorization. It's also possible to require that an input be signed by ten different keys, or be redeemable with a password instead of a key. 

### Types of Transaction

Bitcoin currently creates two different scriptSig/scriptPubKey pairs. These are described below. 

It is possible to design more complex types of transactions, and link them together into cryptographically enforced agreements. These are known as [Contracts](/wiki/Contracts "Contracts"). 

#### Pay-to-PubkeyHash
    
    
    scriptPubKey: OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
    scriptSig: <sig> <pubKey>
    

A Bitcoin [address](/wiki/Address "Address") is only a hash, so the sender can't provide a full public key in scriptPubKey. When redeeming coins that have been sent to a Bitcoin address, the recipient provides both the signature and the public key. The script verifies that the provided public key does hash to the hash in scriptPubKey, and then it also checks the signature against the public key. 

Checking process: 

Stack  | Script  | Description   
---|---|---  
Empty.  | <sig> <pubKey> OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG  | scriptSig and scriptPubKey are combined.   
<sig> <pubKey> | OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG  | Constants are added to the stack.   
<sig> <pubKey> <pubKey> | OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG  | Top stack item is duplicated.   
<sig> <pubKey> <pubHashA> | <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG  | Top stack item is hashed.   
<sig> <pubKey> <pubHashA> <pubKeyHash> | OP_EQUALVERIFY OP_CHECKSIG  | Constant added.   
<sig> <pubKey> | OP_CHECKSIG  | Equality is checked between the top two stack items.   
true  | Empty.  | Signature is checked for top two stack items.   
  
#### Pay-to-Script-Hash
    
    
    scriptPubKey: OP_HASH160 <scriptHash> OP_EQUAL 
    scriptSig: ..signatures... <serialized script>
    
    
    
    m-of-n multi-signature transaction:
    scriptSig: 0 <sig1> ... <script>
    script: OP_m <pubKey1> ... OP_n OP_CHECKMULTISIG
    

  
P2SH addresses were created with the motivation of moving "the responsibility for supplying the conditions to redeem a transaction from the sender of the funds to the redeemer. They allow the sender to fund an arbitrary transaction, no matter how complicated, using a 20-byte hash"[1](https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki#motivation). Pay-to-Pubkey-hash addresses are similarly a 20-byte hash of the public key. 

Pay-to-script-hash provides a means for complicated transactions, unlike the Pay-to-pubkey-hash, which has a specific definition for scriptPubKey, and scriptSig. The specification places no limitations on the script, and hence absolutely any contract can be funded using these addresses. 

The scriptPubKey in the funding transaction is script which ensures that the script supplied in the redeeming transaction hashes to the script used to create the address. 

In the scriptSig above, 'signatures' refers to any script which is sufficient to satisfy the following serialized script. 

Checking process: 

Stack  | Script  | Description   
---|---|---  
Empty.  | 0 <sig1> <sig2> OP_2 <pubKey1> <pubKey2> <pubKey3> OP_3 OP_CHECKMULTISIG  | Only the scriptSig is used.   
0 <sig1> <sig2> OP_2 <pubKey1> <pubKey2> <pubKey3> OP_3  | OP_CHECKMULTISIG  | Constants are added to the stack.   
true  | Empty  | Signatures validated in the order of the keys in the script.   
  
  
See also [BIP 0016](/wiki/BIP_0016 "BIP 0016")

### Generation

Generations have a single input, and this input has a "[coinbase](/wiki/Coinbase "Coinbase")" parameter instead of a scriptSig. The data in "coinbase" can be anything; it isn't used. Bitcoin puts the current compact-format [target](/wiki/Target "Target") and the arbitrary-precision "extraNonce" number there, which increments every time the Nonce field in the [block header](/wiki/Block_hashing_algorithm "Block hashing algorithm") overflows. Outputs can be anything, but Bitcoin creates one exactly like an IP address transaction. The extranonce contributes to enlarge the domain for the proof of work function. Miners can easily modify nonce (4byte), timestamp and extranonce (2 to 100bytes). 

### General format (inside a block) of each input of a transaction - Txin

Field  | Description  | Size   
---|---|---  
Previous Transaction hash  | doubled [SHA256](http://en.wikipedia.org/wiki/SHA-256 "wikipedia:SHA-256")-[hashed](/wiki/Hash "Hash") of a (previous) to-be-used transaction  | 32 bytes   
Previous Txout-index  | non negative integer indexing an output of the to-be-used transaction  | 4 bytes   
Txin-script length  | non negative integer [VI = VarInt](/wiki/Protocol_specification#Variable_length_integer "Protocol specification") | 1 - 9 bytes   
Txin-script / scriptSig  | [Script](/wiki/Script "Script") | <in-script length>-many bytes   
sequence_no  | normally 0xFFFFFFFF; irrelevant unless transaction's lock_time is > 0  | 4 bytes   
  
The input sufficiently describes where and how to get the bitcoin amout to be redeemed. If it is the (only) input of the first transaction of a block, it is called the generation transaction input and its content completely ignored. (Historically the Previous Transaction hash is 0 and the Previous Txout-index is -1.) 

### General format (inside a block) of each output of a transaction - Txout

Field  | Description  | Size   
---|---|---  
value  | non negative integer giving the number of [Satoshis(BTC/10^8)](/wiki/FAQ#What_do_I_call_the_various_denominations_of_bitcoins.3F "FAQ") to be transfered  | 8 bytes   
Txout-script length  | non negative integer  | 1 - 9 bytes [VI = VarInt](/wiki/Protocol_specification#Variable_length_integer "Protocol specification")  
Txout-script / scriptPubKey  | [Script](/wiki/Script "Script") | <out-script length>-many bytes   
  
The output sets the conditions to release this bitcoin amount later. The sum of the output values of the first transaction is the value of the mined bitcoins for the block plus possible transactions fees of the other transactions in the block. 

## See Also

  * [Script](/wiki/Script "Script")
  * [Protocol rules - "tx" messages](/wiki/Protocol_rules#"tx"_messages "Protocol rules")
  * [Protocol documentation - Transaction Verification](/wiki/Protocol_documentation#Transaction_Verification "Protocol documentation")
  * [Raw Transactions](/wiki/Raw_Transactions "Raw Transactions")
  * [Coin analogy](/wiki/Coin_analogy "Coin analogy")
  * [Transaction Malleability](/wiki/Transaction_Malleability "Transaction Malleability")
  * [Transaction broadcasting](/wiki/Transaction_broadcasting "Transaction broadcasting")


Retrieved from "[https://en.bitcoin.it/w/index.php?title=Transaction&oldid=70030](https://en.bitcoin.it/w/index.php?title=Transaction&oldid=70030)"

[Categories](/wiki/Special:Categories "Special:Categories"): 

  * [Technical](/wiki/Category:Technical "Category:Technical")
  * [Vocabulary](/wiki/Category:Vocabulary "Category:Vocabulary")


## Navigation menu

### Search

[](/wiki/Main_Page "Visit the main page")
