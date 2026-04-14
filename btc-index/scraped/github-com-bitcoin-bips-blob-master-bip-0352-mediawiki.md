# github.com -- Scraped Content

**URL:** https://github.com/bitcoin/bips/blob/master/bip-0352.mediawiki
**Category:** github
**Scrape status:** DONE
**Source notes:** BTC\Silent paymentsStealth Addresses.md
**Scraped:** 2026-04-12

---

**Repository:** bitcoin/bips
**File:** bip-0352.mediawiki

<pre>
  BIP: 352
  Layer: Applications
  Title: Silent Payments
  Authors: josibake <josibake@protonmail.com>
           Ruben Somsen <rsomsen@gmail.com>
           Sebastian Falbesoner <sebastian.falbesoner@gmail.com>
  Status: Complete
  Type: Specification
  Assigned: 2023-03-09
  License: BSD-2-Clause
  Discussion: 2022-03-13: https://gist.github.com/RubenSomsen/c43b79517e7cb701ebf77eec6dbb46b8 [gist] Original proposal
              2022-03-28: https://gnusha.org/pi/bitcoindev/CAPv7TjbXm953U2h+-12MfJ24YqOM5Kcq77_xFTjVK+R2nf-nYg@mail.gmail.com/ [bitcoin-dev] Silent Payments – Non-interactive private payments with no on-chain overhead
              2022-10-11: https://gnusha.org/pi/bitcoindev/P_21MLHGJicZ-hkbC4DGu86c5BtNKiH8spY4TOw5FJsfimdi_6VyHzU_y-s1mZsOcC2FA3EW_6w6W5qfV9dRK_7AvTAxDlwVfU-yhWZPEuo=@protonmail.com/ [bitcoin-dev] Silent Payment v4 (coinjoin support added)
              2023-08-04: https://gnusha.org/pi/bitcoindev/ZM03twumu88V2NFH@petertodd.org/ [bitcoin-dev] BIP-352 Silent Payments addresses should have an expiration time
  Version: 1.0.2
</pre>

== Introduction ==

=== Abstract ===

This document specifies a protocol for static payment addresses in Bitcoin without on-chain linkability of payments or a need for on-chain notifications.

=== Copyright ===

This BIP is licensed under the BSD 2-clause license.

=== Motivation ===

Using a new address for each Bitcoin transaction is a crucial aspect of maintaining privacy. This often requires a secure interaction between sender and receiver, so that the receiver can hand out a fresh address, a batch of fresh addresses, or a method for the sender to generate addresses on-demand, such as an xpub.

However, interaction is often infeasible and in many cases undesirable. To solve for this, various protocols have been proposed which use a static payment address and notifications sent via the blockchain<ref name="out_of_band_notifications">'''Why not use out-of-band notifications''' Out-of-band notifications (e.g. using something other than the Bitcoin blockchain) have been proposed as a way of addressing the privacy and cost concerns of using the Bitcoin blockchain as a messaging layer. This, however, simply moves the privacy and cost concerns somewhere else and increases the risk of losing money due to a notification not being reliably delivered, or even censored, and makes this notification data critical for backup to recover funds.</ref>. These protocols eliminate the need for interaction, but at the expense of increased costs for one-time payments and a noticeable footprint in the blockchain, potentially revealing metadata about the sender and receiver. Notification schemes also allow the receiver to link all payments from the same sender, compromising sender privacy.

This proposal aims to address the limitations of these current approaches by presenting a solution that eliminates the need for interaction, eliminates the need for notifications, and protects both sender and receiver privacy. These benefits come at the cost of requiring wallets to scan the blockchain in order to detect payments. This added requirement is generally feasible for full nodes but poses a challenge for light clients. While it is possible today to implement a privacy-preserving light client at the cost of increased bandwidth, light client support is considered an area of open research (see [[#appendix-a-light-client-support|Appendix A: Light Client Support]]).

The design keeps collaborative transactions such as CoinJoins and inputs with MuSig and FROST keys in mind, but it is recommended that the keys of all inputs of a transaction belong to the same entity as there is no formal proof that the protocol is secure in a collaborative setting.

== Goals ==

We aim to present a protocol which satisfies the following properties:

* No increase in the size or cost of transactions
* Resulting transactions blend in with other bitcoin transactions and can't be distinguished
* Transactions can't be linked to a silent payment address by an outside observer
* No sender-receiver interaction required
* No linking of multiple payments to the same sender
* Each silent payment goes to a unique address, avoiding accidental address reuse
* Supports payment labeling
* Uses existing seed phrase or descriptor methods for backup and recovery
* Separates scanning and spending responsibilities
* Compatible with other spending protocols, such as CoinJoin
* Light client/SPV wallet support
* Protocol is upgradeable

== Overview ==

We first present an informal overview of the protocol. In what follows, uppercase letters represent public keys, lowercase letters represent private keys, ''||'' refers to byte concatenation, ''·'' refers to elliptic curve scalar multiplication, ''G'' represents the generator point for secp256k1, and ''n'' represents the curve order for secp256k1. Each section of the overview is incomplete on its own and is meant to build on the previous section in order to introduce and briefly explain each aspect of the protocol. For the full protocol specification, see [[#specification|Specification]].

''' Simple case '''

Bob publishes a public key ''B'' as a silent payment address. Alice discovers Bob's silent payment address, selects a UTXO with private key ''a'', public key ''A'' and creates a destination output ''P'' for Bob in the following manner:

* Let ''P = B + hash(a·B)·G''
* Encode ''P'' as a [https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki BIP341] taproot output

Since ''a·B == b·A'' ([https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman Elliptic-curve Diffie–Hellman]), Bob scans with his private key ''b'' by collecting the input public keys for each transaction with at least one unspent taproot output and performing the ECDH calculation until ''P'' is found (i.e. calculating ''P = B + hash(b·A)·G'' and seeing that ''P'' is present in the transaction outputs).

''' Creating more than one output '''

In order to allow Alice to create more than one output for Bob<ref name="why_more_than_one_output">'''Why allow for more than one output?''' Allowing Alice to break her payment to Bob into multiple amounts opens up a number of privacy improving techniques for Alice, making the transaction look like a CoinJoin or better hiding the change amount by splitting both the payment and change outputs into multiple amounts. It also allows for Alice and Carol to both have their own unique output paying Bob in the event they are in a collaborative transaction and both paying Bob's silent payment address.</ref>, we include an integer in the following manner:

* Let ''k = 0''
* Let ''P<sub>0</sub> = B + hash(a·B || k)·G''
* For additional outputs:
** Increment ''k'' by one (''k++'')
** Let ''P<sub>i</sub> = B + hash(a·B || k)·G''

Bob detects this output the same as before by searching for ''P<sub>0</sub> = B + hash(b·A || 0)·G''. Once he detects the first output, he must:

* Check for ''P<sub>1</sub> = B + hash(b·A || 1)·G''
* If ''P<sub>1</sub>'' is not found, stop
* If ''P<sub>1</sub>'' is found, continue to check for ''P<sub>2</sub>'' and so on until an additional output is not found

Since Bob will only perform these subsequent checks after a transaction with at least one output paying him is found, the increase to his overall scanning requirement is negligible. It should also be noted that the order in which these outputs appear in the transaction does not affect the outcome.

''' Preventing address reuse '''

If Alice were to use a different UTXO from the same public key ''A'' for a subsequent payment to Bob, she would end up deriving the same destinations ''P<sub>i</sub>''. To prevent this, Alice should include an input hash in the following manner:

* Let ''input_hash = hash(outpoint || A)''<ref name="why_include_A">'''Why include A in the input hash calculation?''' By committing to A in input hash, this ensures that the sender cannot maliciously choose a private key ''a&prime;'' in a subsequent transaction where ''a&prime; = input_hash·a / input_hash&prime;'', which would force address reuse in the protocol.</ref>
* Let ''P<sub>0</sub> = B + hash(input_hash·a·B || 0)·G''

Bob must calculate the same ''input_hash'' when scanning.

''' Using all inputs '''

In our simplified example we have been referring to Alice's transactions as having only one input ''A'', but in reality a Bitcoin transaction can have many inputs. Instead of requiring Alice to pick a particular input and requiring Bob to check each input separately, we can instead require Alice to perform the tweak with the sum of the input public keys<ref name="other_inputs">'''What about inputs without public keys?''' Inputs without public keys can still be spent in the transaction but are simply ignored in the silent payments protocol.</ref>. This significantly reduces Bob's scanning requirement, makes light client support more feasible<ref name="using_all_inputs">'''How does using all inputs help light clients?''' If Alice uses a random input for the tweak, Bob necessarily has to have access to and check all transaction inputs, which requires performing an ECC multiplication per input. If instead Alice performs the tweak with the sum of the input public keys, Bob only needs the summed 33 byte public key per transaction and only does one ECC multiplication per transaction. Bob can then use BIP158 block filters to determine if any of the outputs exist in a block and thus avoids downloading transactions which don't belong to him. It is still an open question as to how Bob can source the 33 bytes per transaction in a trustless manner, see [[#appendix-a-light-client-support|Appendix A: Light Client Support]] for more details.</ref>, and protects Alice's privacy in collaborative transaction protocols such as CoinJoin<ref name=""all_inputs_and_coinjoin">'''Why does using all inputs matter for CoinJoin?''' If Alice uses a random input to create the output for Bob, this necessarily reveals to Bob which input Alice has control of. If Alice is paying Bob as part of a CoinJoin, this would reveal which input belongs to her, degrading the anonymity set of the CoinJoin and giving Bob more information about Alice. If instead all inputs are used, Bob has no way of knowing which input(s) belong to Alice. This comes at the cost of increased complexity as the CoinJoin participants now need to coordinate to create the silent payment output and would need to use [https://gist.github.com/RubenSomsen/be7a4760dd4596d06963d67baf140406 Blind Diffie–Hellman] to prevent the other participants from learning who Alice is paying. Note it is currently not recommended to use this protocol for CoinJoins due to a lack of a formal security proof.</ref>.

Alice performs the tweak with the sum of her input private keys in the following manner:

* Let ''a = a<sub>1</sub> + a<sub>2</sub> + ... + a<sub>n</sub>''
* Let ''input_hash = hash(outpoint<sub>L</sub> || (a·G))'', where ''outpoint<sub>L</sub>'' is the smallest outpoint lexicographically<ref name="why_smallest_outpoint">'''Why use the lexicographically smallest outpoint for the hash?''' Recall that the purpose of including the input hash is so that the sender and receiver can both come up with a deterministic nonce that ensures that a unique address is generated each time, even when reusing the same scriptPubKey as an input. Choosing the smallest outpoint lexicographically satisfies this requirement, while also ensuring that the generated output is not dependent on the final ordering of inputs in the transaction. Using a single outpoint also works well with memory constrained devices (such as hardware signing devices) as it does not require the device to have the entire transaction in memory in order to generate the silent payment output.</ref>
* Let ''P<sub>0</sub> = B + hash(input_hash·a·B || 0)·G''

''' Spend and Scan Key '''

Since Bob needs his private key ''b'' to check for incoming payments, this requires ''b'' to be exposed to an online device. To minimize the risks involved, Bob can instead publish an address of the form ''(B<sub>scan</sub>, B<sub>spend</sub>)''. This allows Bob to keep ''b<sub>spend</sub>'' in offline cold storage and perform the scanning with the public key ''B<sub>spend</sub>'' and private key ''b<sub>scan</sub>''. Alice performs the tweak using both of Bob's public keys in the following manner:

* Let ''P<sub>0</sub> = B<sub>spend</sub> + hash(input_hash·a·B<sub>scan</sub> || 0)·G''

Bob detects this payment by calculating ''P<sub>0</sub> = B<sub>spend</sub> + hash(input_hash·b<sub>scan</sub>·A || 0)·G'' with his online device and can spend from his cold storage signing device using ''(b<sub>spend</sub> + hash(input_hash·b<sub>scan</sub>·A || 0)) mod n'' as the private key.

''' Labels '''

For a single silent payment address of the form ''(B<sub>scan</sub>, B<sub>spend</sub>)'', Bob may wish to differentiate incoming payments. Naively, Bob could publish multiple silent payment addresses, but this would require him to scan for each one, which becomes prohibitively expensive. Instead, Bob can label his spend public key ''B<sub>spend</sub>'' with an integer ''m'' in the following way:

* Let ''B<sub>m</sub> = B<sub>spend</sub> + hash(b<sub>scan</sub> || m)·G'' where m is an incrementable integer starting from 1
* Publish ''(B<sub>scan</sub>, B<sub>1</sub>)'', ''(B<sub>scan</sub>, B<sub>2</sub>)'' etc.

Alice performs the tweak as before using one of the published ''(B<sub>scan</sub>, B<sub>m</sub>)'' pairs. Bob detects the labeled payment in the following manner:

* Let ''P<sub>0</sub> = B<sub>spend</sub> + hash(input_hash·b<sub>scan</sub>·A || 0)·G''
* Subtract ''P<sub>0</sub>'' from each of the transaction outputs and check if the remainder matches any of the labels (''hash(b<sub>scan</sub> || 1)·G'', ''hash(b<sub>scan</sub> || 2)·G'' etc.) that the wallet has previously used

It is important to note that an outside observer can easily deduce that each published ''(B<sub>scan</sub>, B<sub>m</sub>)'' pair is owned by the same entity as each published address will have ''B<sub>scan</sub>'' in common. As such, labels are not meant as a way for Bob to manage separate identities, but rather a way for Bob to determine the source of an incoming payment.

''' Labels for change '''

Bob can also use labels for managing his own change outputs. We reserve ''m = 0'' for this use case. This gives Bob an alternative to using BIP32 for managing change, while still allowing him to know which of his unspent outputs were change when recovering his wallet from the master key. It is important that the wallet never hands out the label with ''m = 0'' in order to ensure nobody else can create payments that are wrongly labeled as change.

While the use of labels is optional, every receiving silent payments wallet should at least scan for the change label when recovering from backup in order to ensure maximum cross-compatibility.

== Specification ==

We use the following functions and conventions:

* ''outpoint'' (36 bytes): the <code>COutPoint</code> of an input (32-byte txid, least significant byte first || 4-byte vout, least significant byte first)<ref name="why_little_endian">'''Why are outpoints little-endian?''' Despite using big endian throughout the rest of the BIP, outpoints are sorted and hashed matching their transaction serialization, which is little-endian. This allows a wallet to parse a serialized transaction for use in silent payments without needing to re-order the bytes when computing the input hash. Note: despite outpoints being stored and serialized as little-endian, the transaction hash (txid) is always displayed as big-endian.</ref>
* ser<sub>32</sub>(i): serializes a 32-bit unsigned integer ''i'' as a 4-byte sequence, most significant byte first.
* ser<sub>256</sub>(p): serializes the integer p as a 32-byte sequence, most significant byte first.
* ser<sub>P</sub>(P): serializes the coordinate pair P = (x,y) as a byte sequence using SEC1's compressed form: (0x02 or 0x03) || ser<sub>256</sub>(x), where the header byte depends on the parity of the omitted Y coordinate.

For everything not defined above, we use the notation from [https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki#specification BIP340]. This includes the ''hash<sub>tag</sub>(x)'' notation to refer to ''SHA256(SHA256(tag) || SHA256(tag) || x)''.

=== Versions ===

This document defines version 0 (''sp1q''). Version is communicated through the address in the same way as bech32 addresses (see [https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki#bech32 BIP173]. Future upgrades to silent payments will require a new version. As much as possible, future upgrades should support receiving from older wallets (e.g. a silent payments v0 wallet can send to both v0 and v1 addresses). Any changes that break compatibility with older silent payment versions should be a new BIP.

Future silent payments versions will use the following scheme:

{| class="wikitable"
|-
!
!0
!1
!2
!3
!4
!5
!6
!7
!Compatibility
|-
!+0
|q||p||z||r||y||9||x||8||rowspan="4" | backwards compatible
|-
!+8
|g||f||2||t||v||d||w||0
|-
!+16
|s||3||j||n||5||4||k||h
|-
!+24
|c||e||6||m||u||a||7|| -
|}

''v31'' (l) is reserved for a backwards incompatible change, if needed. For silent payments v0:

* If the receiver's silent payment address version is:
** ''v0'': check that the data part is exactly 66-bytes. Otherwise, fail
** ''v1'' through ''v30'': read the first 66-bytes of the data part and discard the remaining bytes
** ''v31'': fail
* Receiver addresses are always [https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki BIP341] taproot outputs<ref name="why_taproot">'''Why only taproot outputs?''' Providing too much optionality for the protocol makes it difficult to implement and can be at odds with the goal of providing the best privacy. Limiting to taproot outputs helps simplify the implementation significantly while also putting users in the best eventual anonymity set.</ref>
* The sender should sign with one of the sighash flags ''DEFAULT'', ''ALL'', ''SINGLE'', ''NONE'' (''ANYONECANPAY'' is unsafe). It is strongly recommended implementations use ''SIGHASH_ALL'' (''SIGHASH_DEFAULT'' for taproot inputs) when possible<ref name="why_not_sighash_anyonecanpay">'''Why is it unsafe to use ''SIGHASH_ANYONECANPAY''?''' Since the output address for the receiver is derived from the sum of the [[#inputs-for-shared-secret-derivation|Inputs For Shared Secret Derivation]] public keys, the inputs must not change once the sender has signed the transaction. If the inputs are allowed to change after the fact, the receiver will not be able to calculate the shared secret needed to find and spend the output. It is currently an open question on how a future version of silent payments could be made to work with new sighash flags such as ''SIGHASH_GROUP'' and ''SIGHASH_ANYPREVOUT''.</ref>
* Inputs used to derive the shared secret are from the ''[[#inputs-for-shared-secret-derivation|Inputs For Shared Secret Derivation]]'' list

=== Scanning silent payment eligible transactions ===

For silent payments v0 a transaction MUST be scanned if and only if all of the following are true:

* The transaction contains at least one BIP341 taproot output (note: spent transactions optionally can be skipped by only considering transactions with at least one unspent taproot output)
* The transaction has at least one input from the ''[[#inputs-for-shared-secret-derivation|Inputs For Shared Secret Derivation]]'' list
* The transaction does not spend an output with SegWit version > 1<ref name="skip_txs_with_unknown_prevouts">'''Why skip transactions that spend SegWit version > 1?''' Skipping transactions that spend unknown output scripts allows us to have a clean upgrade path for silent payments by avoiding the need to scan the same transaction multiple times with different rule sets. If a new SegWit version is added in the future and silent payments v1 is released with support, we would want to avoid having to first scan the transaction with the silent payment v0 rules and then again with the silent payment v1 rules. Note: this restriction only applies to the inputs of a transaction.</ref>

=== Address encoding ===

A silent payment address is constructed in the following manner:

* Let ''B<sub>scan</sub>, b<sub>scan</sub> = Receiver's scan public key and corresponding private key''
* Let ''B<sub>spend</sub>, b<sub>spend</sub> = Receiver's spend public key and corresponding private key''
* Let ''B<sub>m</sub> = B<sub>spend</sub> + hash<sub>BIP0352/Label</sub>(ser<sub>256</sub>(b<sub>scan</sub>) || ser<sub>32</sub>(m))·G'', where ''hash<sub>BIP0352/Label</sub>(ser<sub>256</sub>(b<sub>scan</sub>) || ser<sub>32</sub>(m))·G'' is an optional integer tweak for labeling
** If no label is applied then ''B<sub>m</sub> = B<sub>spend</sub>''
* The final address is a [https://github.com/bitcoin/bips/blob/master/bip-0350.mediawiki Bech32m] encoding of:
** The human-readable part "sp" for mainnet, "tsp" for testnets (e.g.  signet, testnet)
** The data-part values:
*** The character "q", to represent a silent payment address of version 0
*** The 66-byte concatenation of the receiver's public keys, ''ser<sub>P</sub>(B<sub>scan</sub>) || ser<sub>P</sub>(B<sub>m</sub>)''

Note: [https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki BIP173] imposes a 90 character limit for Bech32 segwit addresses and limits versions to 0 through 16, whereas a silent payment address requires ''at least'' 117 characters<ref name="why_117_chars"> ''' Why do silent payment addresses need at least 117 characters?''' A silent payment address is a bech32m encoding comprised of the following parts:


* HRP [2-3 characters]
* separator [1 character]
* version [1-2 characters]
* payload, 66 bytes concatenated pubkeys [ceil(66*8/5) = 106 characters]
* checksum [6 characters]


For a silent payments v0 address, this results in a 117-character address when using a 3-character HRP. Future versions of silent payment addresses may add to the payload, which is why a 1023-character limit is suggested.</ref> and allows versions up to 31. Additionally, since higher versions may add to the data field, it is recommended implementations use a limit of 1023 characters (see [https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki#checksum-design BIP173: Checksum design] for more details).

=== Inputs For Shared Secret Derivation ===

While any UTXO with known output scripts can be used to fund the transaction, the sender and receiver MUST use inputs from the following list when deriving the shared secret:

* ''P2TR''
* ''P2WPKH''
* ''P2SH-P2WPKH''
* ''P2PKH''

Inputs with conditional branches or multiple public keys (e.g. ''CHECKMULTISIG'') are excluded from shared secret derivation as this introduces malleability and would allow a sender to re-sign with a different set of public keys after the silent payment output has been derived. This is not a concern when the sender controls all of the inputs, but is an issue for CoinJoins and other collaborative protocols, where a malicious participant can participate in deriving the silent payment address with one set of keys and then re-broadcast the transaction with signatures for a different set of public keys. P2TR can have hidden conditional branches (script path), but we work around this by using only the output public key.

For all of the output types listed, only X-only and compressed public keys are permitted<ref name="why_only_compressed_public_keys">''' Why only compressed public keys ''' Uncompressed and hybrid public keys are less common than compressed keys and generally considered to be a bad idea due to their blockspace inefficiency. Additionally, [https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki#restrictions-on-public-key-type BIP143] recommends restricting P2WPKH inputs to compressed keys as a default policy.</ref>.

''' P2TR '''

'' Keypath spend ''

    witness:      <signature>
    scriptSig:    (empty)
    scriptPubKey: 1 <32-byte-x-only-key>
                  (0x5120{32-byte-x-only-key})

The sender uses the private key corresponding to the taproot output key (i.e. the tweaked private key). This can be a single private key or an aggregate key (e.g. taproot outputs using MuSig or FROST)<ref name="musig_frost_support">'''Are key aggregation techniques like FROST and MuSig supported?''' While we do not recommend it due to lack of a security proof (except if all participants are trusted or are the same entity), any taproot output able to do a key path theoretically is supported. Any offline key aggregation technique can be used, such as FROST or MuSig. This would require participants to perform the ECDH step collaboratively e.g. ''ECDH = a<sub>1</sub>·B<sub>scan</sub> + a<sub>2</sub>·B<sub>scan</sub> + ... + a<sub>t</sub>·B<sub>scan</sub>'' and ''P = B<sub>spend</sub> + hash(input_hash·ECDH || 0)·G''. Additionally, it may be necessary for the participants to provide a DLEQ proof to ensure they are not acting maliciously.</ref>. The receiver obtains the public key from the ''scriptPubKey'' (i.e. the taproot output key).

'' Script path spend ''

    witness:      <optional witness items> <leaf script> <control block>
    scriptSig:    (empty)
    scriptPubKey: 1 <32-byte-x-only-key>
                  (0x5120{32-byte-x-only-key})

Same as a keypath spend, the sender MUST use the private key corresponding to the taproot output key. If this key is not available, the output cannot be included as an input to the transaction. Same as a keypath spend, the receiver obtains the public key from the ''scriptPubKey'' (i.e. the taproot output key)<ref name="why_always_output_pubkey">''' Why not skip all taproot script path spends? ''' This causes malleability issues for CoinJoins. If the silent payments protocol skipped taproot script path spends, this would allow an attacker to join a CoinJoin round, participate in deriving the silent payment address using the tweaked private key for a key path spend, and then broadcast their own version of the transaction using the script path spend. If the receiver were to only consider key path spends, they would skip the attacker's script path spend input when deriving the shared secret and not be able to find the funds. Additionally, there may be scenarios where the sender can perform ECDH with the key path private key but spends the output using the script path.</ref>.

The one exception is script path spends that use NUMS point ''H'' as their internal key (where ''H'' is constructed by taking the hash of the standard uncompressed encoding of the secp256k1 base point ''G'' as X coordinate, see [https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki#constructing-and-spending-taproot-outputs BIP341: Constructing and spending Taproot outputs] for more details), in which case the input will be skipped for the purposes of shared secret derivation<ref name="why_ignore_h">'''Why skip outputs with H as the internal taproot key?''' If use cases get popularized where the taproot key path cannot be used, these outputs can still be included without getting in the way of making a silent payment, provided they specifically use H as their internal taproot key.</ref>. The receiver determines whether or not to skip the input by checking in the control block if the taproot internal key is equal to ''H''.

''' P2WPKH '''

    witness:      <signature> <33-byte-compressed-key>
    scriptSig:    (empty)
    scriptPubKey: 0 <20-byte-key-hash>
                  (0x0014{20-byte-key-hash})

The sender performs the tweak using the private key for the output and the receiver obtains the public key as the last witness item.

''' P2SH-P2WPKH '''

    witness:      <signature> <33-byte-compressed-key>
    scriptSig:    <0 <20-byte-key-hash>>
                  (0x160014{20-byte-key-hash})
    scriptPubKey: HASH160 <20-byte-script-hash> EQUAL
                  (0xA914{20-byte-script-hash}87)

The sender performs the tweak using the private key for the nested ''P2WPKH'' output and the receiver obtains the public key as the last witness item.

''' P2PKH '''

    scriptSig:    <signature> <33-byte-compressed-key>
    scriptPubKey: OP_DUP HASH160 <20-byte-key-hash> OP_EQUALVERIFY OP_CHECKSIG
                  (0x76A914{20-byte-key-hash}88AC)

The receiver obtains the public key from the ''scriptSig''. The receiver MUST parse the ''scriptSig'' for the public key, even if the ''scriptSig'' does not match the template specified (e.g. <code><dummy> OP_DROP <Signature> <Public Key></code>). This is to address the [https://en.bitcoin.it/wiki/Transaction_malleability third-party malleability of ''P2PKH'' ''scriptSigs''].

=== Sender ===

==== Selecting inputs ====

The sending wallet performs coin selection as usual with the following restrictions:

* At least one input MUST be from the ''[[#inputs-for-shared-secret-derivation|Inputs For Shared Secret Derivation]]'' list
* Exclude inputs with SegWit version > 1 (see ''[[#scanning-silent-payment-eligible-transactions|Scanning silent payment eligible transactions]]'')
* For each taproot output spent the sending wallet MUST have access to the private key corresponding to the taproot output key, unless ''H'' is used as the internal public key

==== Creating outputs ====

After the inputs have been selected, the sender can create one or more outputs for one or more silent payment addresses in the following manner:

* Collect the private keys for each input from the ''[[#inputs-for-shared-secret-derivation|Inputs For Shared Secret Derivation]]'' list
* For each private key ''a<sub>i</sub>'' corresponding to a [https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki BIP341] taproot output, check that the private key produces a point with an even Y coordinate and negate the private key if not<ref name="why_negate_taproot_private_keys">'''Why do taproot private keys need to be checked?

[... truncated ...]
