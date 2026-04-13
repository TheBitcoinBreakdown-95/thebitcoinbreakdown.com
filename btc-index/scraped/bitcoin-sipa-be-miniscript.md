# bitcoin.sipa.be -- Scraped Content

**URL:** https://bitcoin.sipa.be/miniscript
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Miniscript.md
**Scraped:** 2026-04-12

---

### Introduction

_Miniscript_ is a language for writing (a subset of) Bitcoin Scripts in a structured way, enabling analysis, composition, generic signing and more. 

Bitcoin Script is an unusual stack-based language with many edge cases, designed for implementing spending conditions consisting of various combinations of signatures, hash locks, and time locks. Yet despite being limited in functionality it is still highly nontrivial to:

  * Given a combination of spending conditions, finding the most economical script to implement it.
  * Given two scripts, construct a script that implements a composition of their spending conditions (e.g. a multisig where one of the "keys" is another multisig).
  * Given a script, find out what spending conditions it permits.
  * Given a script and access to a sufficient set of private keys, construct a general satisfying witness for it.
  * Given a script, be able to predict the cost of spending an output.
  * Given a script, know whether particular resource limitations like the ops limit might be hit when spending.


Miniscript functions as a representation for scripts that makes these sort of operations possible. It has a structure that allows composition. It is very easy to statically analyze for various properties (spending conditions, correctness, security properties, malleability, ...). It can be targeted by spending policy compilers (see below). Finally, compatible scripts can easily be converted to Miniscript form - avoiding the need for additional metadata for e.g. signing devices that support it. 

Miniscript is designed for (P2SH-)P2WSH and Tapscript (as defined in BIP342) embedded scripts. Most of its constructions work fine in P2SH as well, but some of the (optional) security properties rely on Segwit-specific rules. Furthermore, the implemented policy compilers assume a Segwit-specific cost model. 

Miniscript was designed and implemented by Pieter Wuille, Andrew Poelstra, and Sanket Kanjalkar at Blockstream Research, but is the result of discussions with several other people. 

Links:

  * This [website](http://bitcoin.sipa.be/miniscript) and C++ compiler: [[code]](https://github.com/sipa/miniscript)
  * Bitcoin Core compatible C++ implementation: [[code]](https://github.com/sipa/miniscript/tree/master/bitcoin/script)
  * Rust-miniscript implementation: [[code]](https://github.com/apoelstra/rust-miniscript)
  * Talk about (an early version of) Miniscript at [SBC'19](https://cyber.stanford.edu/sbc19): [[video]](https://www.youtube.com/watch?v=XM1lzN4Zfks) [[transcript]](http://diyhpl.us/wiki/transcripts/stanford-blockchain-conference/2019/miniscript/) [[slides]](https://prezi.com/view/KH7AXjnse7glXNoqCxPH/)


### Policy to Miniscript compiler

Here you can see a demonstration of the P2WSH Miniscript compiler. Write a spending policy according to the instructions below, and observe how it affects the constructed Miniscript. 

Policy and(pk(A),or(pk(B),or(9@pk(C),older(1000))))

Supported policies: 

  * pk(_NAME_): Require public key named _NAME_ to sign. _NAME_ can be any string up to 16 characters.
  * after(_NUM_), older(_NUM_): Require that the nLockTime/nSequence value is at least _NUM_. _NUM_ cannot be 0.
  * sha256(_HEX_), hash256(_HEX_): Require that the preimage of 64-character _HEX_ is revealed. The special value H can be used as _HEX_.
  * ripemd160(_HEX_), hash160(_HEX_): Require that the preimage of 40-character _HEX_ is revealed. The special value H can be used as _HEX_.
  * and(_POL_ ,_POL_): Require that both subpolicies are satisfied.
  * or([_N_ @]_POL_ ,[_N_ @]_POL_): Require that one of the subpolicies is satisfied. The numbers N indicate the relative probability of each of the subexpressions (so 9@ is 9 times more likely than the default).
  * thresh(_NUM_ ,_POL_ ,_POL_ ,...): Require that NUM out of the following subpolicies are met (all combinations are assumed to be equally likely).


Fill field with: 

  * [A single key](javascript:load_policy\("pk\(key_1\)"\))
  * [One of two keys (equally likely)](javascript:load_policy\("or\(pk\(key_1\),pk\(key_2\)\)"\))
  * [One of two keys (one likely, one unlikely)](javascript:load_policy\("or\(99@pk\(key_likely\),pk\(key_unlikely\)\)"\))
  * [A user and a 2FA service need to sign off, but after 90 days the user alone is enough](javascript:load_policy\("and\(pk\(key_user\),or\(99@pk\(key_service\),older\(12960\)\)\)"\))
  * [A 3-of-3 that turns into a 2-of-3 after 90 days](javascript:load_policy\("thresh\(3,pk\(key_1\),pk\(key_2\),pk\(key_3\),older\(12960\)\)"\))
  * [The BOLT #3 to_local policy](javascript:load_policy\("or\(pk\(key_revocation\),and\(pk\(key_local\),older\(1008\)\)\)"\))
  * [The BOLT #3 offered HTLC policy](javascript:load_policy\("or\(pk\(key_revocation\),and\(pk\(key_remote\),or\(pk\(key_local\),hash160\(H\)\)\)\)"\))
  * [The BOLT #3 received HTLC policy](javascript:load_policy\("or\(pk\(key_revocation\),and\(pk\(key_remote\),or\(and\(pk\(key_local\),hash160\(H\)\),older\(1008\)\)\)\)"\)) 


Compile

### Analyze a Miniscript

Here you can analyze the structure of a Miniscript expression and more. 

Miniscript and_v(v:pk(K),pk(A)) Provide a well-typed miniscript expression of type "B".

Analyze

### Miniscript reference

#### P2WSH or Tapscript?

The Miniscript specifications vary only slightly between P2WSH and Tapscript embedded scripts. Differences are pointed inline. If no information specific to the context is given you can assume it is valid for both P2WSH and Tapscript. 

#### Translation table

This table shows all Miniscript _fragments_ and their associated semantics and Bitcoin Script. Fragments that do not change the semantics of their subexpressions are called _wrappers_. Normal fragments use a "fragment(arguments,...)" notation, while wrappers are written using prefixes separated from other fragments by a colon. The colon is dropped between subsequent wrappers; e.g. `dv:older(144)` is the `d:` wrapper applied to the `v:` wrapper applied to the `older` fragment for 144 blocks. Note how key expressions in this table and the followings are implicitly 32 bytes "x-only" public key in Tapscript and 33 bytes compressed public keys in P2WSH. 

Semantics| Miniscript fragment| Bitcoin Script  
---|---|---  
false | `0` | 0  
true | `1` | 1  
check(key) | `pk_k(key)` | <key>  
`pk_h(key)` | DUP HASH160 <HASH160(key)> EQUALVERIFY  
`pk(key) = c:pk_k(key)` | <key> CHECKSIG  
`pkh(key) = c:pk_h(key)` | DUP HASH160 <HASH160(key)> EQUALVERIFY CHECKSIG  
nSequence ≥ n (and compatible) | `older(n)` | <n> CHECKSEQUENCEVERIFY  
nLockTime ≥ n (and compatible) | `after(n)` | <n> CHECKLOCKTIMEVERIFY  
len(x) = 32 and SHA256(x) = h | `sha256(h)` | SIZE <20> EQUALVERIFY SHA256 <h> EQUAL  
len(x) = 32 and HASH256(x) = h | `hash256(h)` | SIZE <20> EQUALVERIFY HASH256 <h> EQUAL  
len(x) = 32 and RIPEMD160(x) = h | `ripemd160(h)` | SIZE <20> EQUALVERIFY RIPEMD160 <h> EQUAL  
len(x) = 32 and HASH160(x) = h | `hash160(h)` | SIZE <20> EQUALVERIFY HASH160 <h> EQUAL | (_X_ and _Y_) or _Z_ | `andor(_X_ ,_Y_ ,_Z_)` | _[X]_ NOTIF _[Z]_ ELSE _[Y]_ ENDIF  
_X_ and _Y_ | `and_v(_X_ ,_Y_)` | _[X]_ _[Y]_  
`and_b(_X_ ,_Y_)` | _[X]_ _[Y]_ BOOLAND  
`and_n(_X_ ,_Y_)` = `andor(_X_ ,_Y_ ,0)` | _[X]_ NOTIF 0 ELSE _[Y]_ ENDIF  
_X_ or _Z_ | `or_b(_X_ ,_Z_)` | _[X]_ _[Z]_ BOOLOR  
`or_c(_X_ ,_Z_)` | _[X]_ NOTIF _[Z]_ ENDIF  
`or_d(_X_ ,_Z_)` | _[X]_ IFDUP NOTIF _[Z]_ ENDIF  
`or_i(_X_ ,_Z_)` | IF _[X]_ ELSE _[Z]_ ENDIF  
_X 1_ \+ ... + _X n_ = k | `thresh(k,_X 1_,...,_X n_)` | _[X 1]_ _[X 2]_ ADD ... _[X n]_ ADD ... <k> EQUAL  
check(key1) + ... + check(keyn) = k _(P2WSH only)_ | `multi(k,key1,...,keyn)` | <k> <key1> ... <keyn> <n> CHECKMULTISIG  
check(key1) + ... + check(keyn) = k _(Tapscript only)_ | `multi_a(k,key1,...,keyn)` |  <key1> CHECKSIG <key2> CHECKSIGADD ... <keyn> CHECKSIGADD <k> NUMEQUAL  
_X_ (identities) | `a:_X_` | TOALTSTACK _[X]_ FROMALTSTACK  
`s:_X_` | SWAP _[X]_  
`c:_X_` | _[X]_ CHECKSIG  
`t:_X_` = `and_v(_X_ ,1)` | _[X]_ 1 | `d:_X_` | DUP IF _[X]_ ENDIF  
`v:_X_` | _[X]_ VERIFY (or VERIFY version of last opcode in _[X]_)  
`j:_X_` | SIZE 0NOTEQUAL IF _[X]_ ENDIF  
`n:_X_` | _[X]_ 0NOTEQUAL  
`l:_X_` = `or_i(0,_X_)` | IF 0 ELSE _[X]_ ENDIF  
`u:_X_` = `or_i(_X_ ,0)` | IF _[X]_ ELSE 0 ENDIF  
  
The `pk`, `pkh`, and `and_n` fragments and `t:`, `l:`, and `u:` wrappers are syntactic sugar for other Miniscripts, as listed in the table above. In what follows, they will not be included anymore, as their properties can be derived by looking at their expansion. 

Hash preimages are constrained to 32 bytes to disallow various forms of griefing, including making non-standard(un-relayable) transactions, consensus-invalid swaps across blockchains, as well as ensure that satisfaction cost can be accurately calculated. Finally, note that `&lt20;>` are in hex representation in this document. 

#### Correctness properties

Not every Miniscript expression can be composed with every other. Some return their result by putting true or false on the stack; others can only abort or continue. Some require subexpressions that consume an exactly known number of arguments, while others need a subexpression that has a nonzero top stack element to satisfy. To model all these properties, we define a correctness type system for Miniscript. 

Every miniscript expression has one of four basic types:

  * **"B"** Base expressions. These take their inputs from the top of the stack. When satisfied, they push a nonzero value of up to 4 bytes onto the stack. When dissatisfied, they push an exact 0 onto the stack (if dissatisfaction without aborting is possible at all). This type is used for most expressions, and required for the top level expression. An example is `older(n)` = <n> CHECKSEQUENCEVERIFY.
  * **"V"** Verify expressions. Like "B", these take their inputs from the top of the stack. Upon satisfaction however, they continue without pushing anything. They cannot be dissatisfied (will abort instead). A "V" can be obtained using the `v:` wrapper on a "B" expression, or by combining other "V" expressions using `and_v`, `or_i`, `or_c`, or `andor`. An example is `v:pk(key)` = <key> CHECKSIGVERIFY.
  * **"K"** Key expressions. They again take their inputs from the top of the stack, but instead of verifying a condition directly they always push a public key onto the stack, for which a signature is still required to satisfy the expression. A "K" can be converted into a "B" using the `c:` wrapper (CHECKSIG). An example is `pk_h(key)` = DUP HASH160 <Hash160(key)> EQUALVERIFY
  * **"W"** Wrapped expressions. They take their inputs from one below the top of the stack, and push a nonzero (in case of satisfaction) or zero (in case of dissatisfaction) either on top of the stack, or one below. So for example a 3-input "W" would take the stack "A B C D E F" and turn it into "A B F 0" or "A B 0 F" in case of dissatisfaction, and "A B F n" or "A B n F" in case of satisfaction (with n a nonzero value). Every "W" is either `s:B` (SWAP B) or `a:B` (TOALTSTACK B FROMALTSTACK). An example is `s:pk(key)` = SWAP <key> CHECKSIG.


Then there are 5 type modifiers, which guarantee additional properties:

  * **"z"** Zero-arg: this expression always consumes exactly 0 stack elements.
  * **"o"** One-arg: this expression always consumes exactly 1 stack element.
  * **"n"** Nonzero: this expression always consumes at least 1 stack element, no satisfaction for this expression requires the top input stack element to be zero.
  * **"d"** Dissatisfiable: a dissatisfaction for this expression can unconditionally be constructed. This implies the dissatisfaction cannot include any signature or hash preimage, and cannot rely on timelocks being satisfied.
  * **"u"** Unit: when satisfied, this expression will put an exact 1 on the stack (as opposed to any nonzero value).


This tables lists the correctness requirements for each of the Miniscript expressions, and its type properties in function of those of their subexpressions: 

Miniscript| Requires| Type| Properties  
---|---|---|---  
`0`| | B| z; u; d  
`1`| | B| z; u  
`pk_k(key)`| | K| o; n; d; u  
`pk_h(key)`| | K| n; d; u  
`older(n)`, `after(n)`| 1 ≤ n < 231| B| z  
`sha256(h)`| | B| o; n; d; u  
`ripemd160(h)`| | B| o; n; d; u  
`hash256(h)`| | B| o; n; d; u  
`hash160(h)`| | B| o; n; d; u  
`andor(_X_ ,_Y_ ,_Z_)`| _X_ is Bdu; _Y_ and _Z_ are both B, K, or V| same as Y/Z| z=zXzYzZ; o=zXoYoZ or oXzYzZ; u=uYuZ; d=dZ  
`and_v(_X_ ,_Y_)`| _X_ is V; _Y_ is B, K, or V| same as _Y_|  z=zXzY; o=zXoY or zYoX; n=nX or zXnY; u=uY  
`and_b(_X_ ,_Y_)`| _X_ is B; _Y_ is W| B| z=zXzY; o=zXoY or zYoX; n=nX or zXnY; d=dXdY; u  
`or_b(_X_ ,_Z_)`| _X_ is Bd; _Z_ is Wd| B| z=zXzZ; o=zXoZ or zZoX; d; u  
`or_c(_X_ ,_Z_)`| _X_ is Bdu; _Z_ is V| V| z=zXzZ; o=oXzZ  
`or_d(_X_ ,_Z_)`| _X_ is Bdu; _Z_ is B| B| z=zXzZ; o=oXzZ; d=dZ; u=uZ  
`or_i(_X_ ,_Z_)`| both are B, K, or V| same as X/Z| o=zXzZ; u=uXuZ; d=dX or dZ  
`thresh(k,_X 1_,...,_X n_)`| 1 ≤ k ≤ n; _X 1_ is Bdu; others are Wdu| B| z=all are z; o=all are z except one is o; d; u  
`multi(k,key1,...,keyn)`| 1 ≤ k ≤ n| B| n; d; u  
`multi_a(k,key1,...,keyn)`| 1 ≤ k ≤ n| B| d; u  
`a:X`|  _X_ is B| W| d=dX; u=uX  
`s:X`|  _X_ is Bo| W| d=dX; u=uX  
`c:X`|  _X_ is K| B| o=oX; n=nX; d=dX; u  
`d:X`|  _X_ is Vz| B| o; n; d; (Tapscript only) u  
`v:X`|  _X_ is B| V| z=zX; o=oX; n=nX  
`j:X`|  _X_ is Bn| B| o=oX; n; d; u=uX  
`n:X`|  _X_ is B| B| z=zX; o=oX; n=nX; d=dX; u  
  
#### Detecting timelock mixing

The nSequence field in a transaction input, or the nLockTime field in transaction can be specified either as a time or height but not both. Therefore it is not possible to spend scripts that require satisfaction of both, height based timelock and time based timelock of the same type. 

  * **"k"** No timelock mixing. This expression does not contain a mix of heightlock and timelock of the same type. If the miniscript does not have the "k" property, the miniscript template will not match the user expectation of the corresponding spending policy.


#### Resource limitations

Various types of Bitcoin Scripts have different resource limitations, either through consensus or standardness. Some of them affect otherwise valid Miniscripts: 

  * Scripts over 10000 bytes are invalid by consensus (bare, P2SH, P2WSH, P2SH-P2WSH). In Tapscript scripts are only implicitly bounded by the maximum standard transaction size (of 100k virtual bytes), which makes the maximum script size a bit less than 400000 bytes.
  * Scripts over 520 bytes are invalid by consensus (P2SH).
  * Script satisfactions where the total number of non-push opcodes plus the number of keys participating in all executed `multi`s, is above 201, are invalid by consensus (bare, P2SH, P2WSH, P2SH-P2WSH).
  * Anything but `pk(key)` (P2PK), `pkh(key)` (P2PKH), and `multi(k,...)` up to n=3 is invalid by standardness (bare).
  * Scripts over 3600 bytes are invalid by standardness (P2WSH, P2SH-P2WSH).
  * Script satisfactions with a serialized scriptSig over 1650 bytes are invalid by standardness (P2SH).
  * Script satisfactions with a witness consisting of over 100 stack elements (excluding the script itself) are invalid by standardness (P2WSH, P2SH-P2WSH).
  * Script satisfactions that make the stack exceed 1000 elements during or before script execution are invalid by consensus (bare, P2SH, P2WSH, P2SH-P2WSH, Tapscript).

For P2WSH, a Miniscript whose script is larger than 3600 bytes is invalid. For all the other limits, Miniscript makes it easy to verify they don't impact the ability to satisfy a script. Note that this is different from verifying whether the limits are never reachable at all (which is also possible). Consider for example an `or_b(_X_ ,_Y_)` where both _X_ and _Y_ require a number of large `multi`s to be executed to satisfy. It may be the case that satisfying just one of _X_ or _Y_ does not exceed the ops limit, while satisfying both does. As it's never required to satisfy both, the limit does not prevent satisfaction. 

#### Security properties

The type system above guarantees that the corresponding Bitcoin Scripts are:

  * **consensus and standardness complete** : Assuming the resource limits listed in the previous section are not violated and there is no timelock mixing, for every set of met conditions that are permitted by the semantics, a witness can be constructed that passes Bitcoin's consensus rules and common standardness rules.
  * **consensus sound** : It is not possible to construct a witness that is consensus valid for a Script unless the spending conditions are met. Since standardness rules permit only a subset of consensus-valid satisfactions (by definition), this property also implies **standardness soundness**. 


The completeness property has been extensively tested for P2WSH by verifying large numbers of random satisfactions for random Miniscript expressions against Bitcoin Core's consensus and standardness implementation. The soundness can be reasoned about by considering all possible execution paths through each of the fragments' scripts. 

In order for these properties to not just apply to script, but to an entire transaction, it's important that the witness commits to all data relevant for verification. In practice this means that scripts whose conditions can be met without any digital signature are insecure. For example, if an output can be spent by simply passing a certain nLockTime (an `after(n)` fragment in Miniscript) but without any digital signatures, an attacker can modify the nLockTime field in the spending transaction. 

### Satisfactions and malleability

#### Basic satisfactions

The following table shows all valid satisfactions and dissatisfactions for every Miniscript, using satisfactions and dissatisfactions of its subexpressions. Multiple possibilities are separated by semicolons. Some options are not actually necessary to produce correct witnesses, and are called _non-canonical_ options. They are listed for completeness, but marked in [grey] below. 

Miniscript| Dissatisfactions (dsat)| Satisfactions (sat) | `0`| | -  
---|---|---  
`1`| -|   
`pk_k(key)`| 0| sig  
`pk_h(key)`| 0 key| sig key  
`older(n)`| -|   
`after(n)`| -|   
`sha256(h)`| any 32-byte vector except the preimage| preimage  
`ripemd160(h)`| any 32-byte vector except the preimage| preimage  
`hash256(h)`| any 32-byte vector except the preimage| preimage  
`hash160(h)`| any 32-byte vector except the preimage| preimage  
`andor(_X_ ,_Y_ ,_Z_)`| dsat(_Z_) dsat(_X_); [dsat(_Y_) sat(_X_)]| sat(_Y_) sat(_X_); sat(_Z_) dsat(_X_)  
`and_v(_X_ ,_Y_)`| [dsat(_Y_) sat(_X_)]| sat(_Y_) sat(_X_)  
`and_b(_X_ ,_Y_)`| dsat(_Y_) dsat(_X_); [sat(_Y_) dsat(_X_)]; [dsat(_Y_) sat(_X_)]| sat(_Y_) sat(_X_)  
`or_b(_X_ ,_Z_)`| dsat(_Z_) dsat(_X_)| dsat(_Z_) sat(_X_); sat(_Z_) dsat(_X_); [sat(_Z_) sat(_X_)]  
`or_c(_X_ ,_Z_)`| -| sat(_X_); sat(_Z_) dsat(_X_)  
`or_d(_X_ ,_Z_)`| dsat(_Z_) dsat(_X_)| sat(_X_); sat(_Z_) dsat(_X_)  
`or_i(_X_ ,_Z_)`| dsat(_X_) 1; dsat(_Z_) 0| sat(_X_) 1; sat(_Z_) 0  
`thresh(k,_X 1_,...,_X n_)`| All dsats [Sats/dsats with 1 ≤ #(sats) ≠ k]| Sats/dsats with #(sats) = k  
`multi(k,key1,...,keyn)`| 0 0 ... 0 (k+1 times)| 0 sig ... sig  
`multi_a(k,key1,...,keyn)`| 0 ... 0 (n times)| sig/0 with #(sig) = k and #(sigs/0) = n   
`a:_X_`|  dsat(_X_)| sat(_X_)  
`s:_X_`|  dsat(_X_)| sat(_X_)  
`c:_X_`|  dsat(_X_)| sat(_X_)  
`d:_X_`|  0| sat(_X_) 1  
`v:_X_`|  -| sat(_X_)  
`j:_X_`|  0; [dsat(_X_) (if nonzero top stack)]| sat(_X_)  
`n:_X_`|  dsat(_X_)| sat(_X_)  
  
The correctness properties in the previous section are based on the availability of satisfactions and dissatisfactions listed above. The requirements include a "d" for every subexpression whose dissatisfaction may be needed in building a satisfaction for the parent expression. The "d" properties themselves rely on the "d" properties of subexpressions. An interesting property is that in a well-typed Miniscript, dissatisfying a non-"d" subexpress

[... truncated at 20,000 characters ...]
