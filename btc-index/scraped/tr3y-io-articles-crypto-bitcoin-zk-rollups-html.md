# tr3y.io -- Scraped Content

**URL:** https://tr3y.io/articles/crypto/bitcoin-zk-rollups.html
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Validity Rollups.md, BTC\ZK Rollups.md
**Scraped:** 2026-04-12

---

Bitcoin zk-rollups _Updated 2022-05-19: Fixed a few typos and other notes after it was shared on Twitter :)_ _Updated 2022-11-04: I noticed an inconsistency with a gadget name I made up._ For the uninitiated, a “rollup” is a scaling solution developed in the Ethereum ecosystem that relies on performing the “execution” of transactions off-chain, posting unexecuted transaction data on-chain, and committing to the state of this system to allow trustlessly entering and leaving the system. It comes in two major variations: the “optimistic” rollup that relies on a fraud game to prove the state commitments are correct with respect to the the transaction history, and the “zk” rollup that uses a zero knowledge proof to verify the state commitments. Rollups give very strong security guarantees and allow for rich kinds of state transition logic. An advantage of this approach is that much of the complexity of state tracking is shifted into off-chain bookkeeping. This can allow for significant reductions in the size of data posted to the chain, most impressively reducing the size of an account-to-account transfer to as little as 12 bytes when amortized along with a large number of other transactions. [More on that here.](https://vitalik.ca/general/2021/01/05/rollup.html) Another advantage to rollups is that they can be optimized for specific applications without having to shift complexity to the base chain. While current rollup implementations are very dependent on how Ethereum-style contracts store state and represent settlement, there is no fundamental reason that a UTXO-based ledger cannot support rollups. In this article I aim to explore and sketch out some designs for how a zk rollup might function on a future version of Bitcoin that supports some additional script primitives. When reading this you may want to have a working understanding of how both Lightning and Plasma work at a low level, as rollups are an extension of those concepts. The link above touches on them at a high level. Most of _my_ understanding of how they work in practice is based on work done by the good folks at Matter Labs on [zkSync](https://github.com/matter-labs/zksync). **Disclaimer:** these code snippets have not been actually tested, they’re here to illustrate that it’s _possible_ and to describe the flow of data, but they most certainly have some bugs Prereqs I expect that practical implementation of a prototype might happen on Liquid, as [Elements has many of the opcodes we would use](https://github.com/ElementsProject/elements/blob/2dda79cf616e8928346eeb9e3282f5744955aa88/doc/tapscript_opcodes.md). This zk-rollup design relies heavily on recursive covenants. It may be possible to do some hacks with bounded partially recursive covenants, but that’s unclear at this time. An alternative to using Liquid-style covenants may be to use something like the OP_TXHASH proposed a few times on the bitcoin-dev mailing list, but this has its own challenges. The other major component is a zk-SNARK verification primitive. It has been put forward that Bitcoin should permit some kind of elliptic curve pairing primitive that would enable this, however in practice it would still be very expensive to build a script to verify a zero-knowledge proof (zkp) and actually execute it. It has also been discussed that introducing the concept of jets to enable more performance without overspecializing. It could be done using Simplicity, but I’m leaving that out of scope as most of the ideas discussed here would transfer over. Another more minor limitation is the max stack element size of 520 bytes. This is really annoying but shouldn’t fundamentally limit us if we’re clever. Tapscript ups some of the limits but increasing this to be on the order of a few kilobytes would be much nicer. This design is made assuming we don’t have this limitation, but see the Replacements section near the end so _some_ of them might be able to be circumvented. But generally speaking most of these limits need to be removed. For ease of circuit design, it would also be beneficial to have SNARK-friendly hash ops, but we leave those out here. And finally, since we have a lot of different spend paths, support for something like OP_EVAL would help _significantly_ reduce costs in some areas, especially for some more advanced variants discussed later. Basic design The working principle is that since we have a zkp that can verify all of the constraints of the rollup’s state transition function, we can treat that as a black box for asserting the structure of the transaction and only use enough opcodes to enforce the recursive covenant and expose the transaction data to the script. The particular design of the circuit is left as an exercise to the reader, because I’m not a cryptographer. :) Most of this description considers a hypothetical rollup with a relatively simple data model and a single centralized sequencer. But these are mostly not fundamental restrictions to the design. Here I take a very “brute force” approach with a very complex and monolithic script, it may turn out to be that a more elegant approach could be had using taproot, OP_TLUV, and some other novel primitives. But that’s also left as an exercise for the reader. One major downside is that we have to include the verification key in the witness on every update. For PlonK, verification keys are ~1 KiB, which is large, but not absurdly so, so this is considered a minor barrier. Gadgets Storing state There’s a certain amount of state that we need to carry forwards between steps of the protocol. For the purposes of this gadget we can ignore its internal structure and discuss just how we assert that it’s carried forward properly. The structure of the script should push the current state onto the stack in the first opcode, and be structured to use it from there. The rest of the script from there on would be static. The offset of the “real” start of the script is as `<programstartoff>` and `[push_op]` is the op to push a buffer of the size of the state (pushed in its own push op, like `PUSHDATA1(4c04deadbeef)`).
    
    # (stack: <newstate> <curscriptpubkey>)
    
    # get the script hash and throw away the 0
    PUSHCURRENTINPUTINDEX INSPECTINPUTSCRIPTPUBKEY DROP
    
    # verify provided script is correct
    DUP TOALTSTACK SHA256 EQUALVERIFY
    
    # compute new output, including pushing the state
    FROMALTSTACK <programstartoff> RIGHT
    OVER $pushop SWAP CAT SWAP CAT SHA256
    
    # assert that output matches
    <output> INSPECTOUTPUTSCRIPTPUBKEY
    0 EQUALVERIFY 2DROP EQUALVERIFY 2DROP
    
    # (stack: <newstate>)

Except this is actually a little clumbsy. Usually we want to extract the old state, do some stuff to figure out the new state, and _then_ assert the new state. So actually we’d structure it more like this:
    
    # (start: <cur_scriptpubkey>)
    
    # compute what the input scriptPubKey *should* be
    DUP SHA256 # TODO make sure this is how it gets computed for segwit v0
    
    # get the script hash and throw away the 0, then verify it
    PUSHCURRENTINPUTINDEX INSPECTINPUTSCRIPTPUBKEY DROP EQUALVERIFY
    
    # now extract the program and save it, then get just the actual state on the stack
    DUP <program_start_off> RIGHT TOALTSTACK
    len([push_op]) <state_size> SUBSTR
    
    # (do stuff here: <old state> -> <new state>)
    
    # reassemble what the output should be
    # TODO make sure that this correctly compute what the segwit thing should be
    [push_op] SWAP
    FROMALTSTACK # restore the program
    CAT CAT # put it all together
    
    # hash it to compute what the segwit v0 output should be
    SHA256
    
    # now assert everything matches up
    <output> INSPECTOUTPUTSCRIPTPUBKEY
    0 EQUALVERIFY EQUALVERIFY
    
    # (stack cleaned up)

So this is sneaky because it hides its state in the altstack, so as long as our stack hygiene there is good too, then it’ll all be okay. This would be improved if we had a `PUSHSCRIPT` opcode that would push the currently executing script, as the script could pull the old script program directly. Since we’ve established that that functionality is already possible it makes sense to introduce an opcode that removes the necessity to restate the script as part of the scriptsig. Something nice about this structure means that any signatures for any other funds that are spent with this _do_ commit to the new state of the recursive covenant as long as they commit to the outputs. This is useful because it means we don’t have to worry about signatures being reused in different state transition. Exposing tx data to ZKP verifier Since we’re just relying on the circuit to enforce many of the constraints of the flow of funds, we have to expose that data to the verification somehow. It’s unclear what a SNARK primitive in Bitcoin would look like, so we have to take some liberties to imagine what it _might_ look like, more on that later. But somehow we’d have to expose the transaction outputs to the SNARK verifier. The simple way to do this is to do something like a `DUP SHA256 CHECKTEMPLATEVERIFY` on a copy of the outputs data provided as part of the witness, but that’s super inefficient! Verification keys are already huge so we want to avoid that! More concretely, we can stitch together a blob of bytes that represent what are care about from the transaction outputs:
    
    # create an buffer of 36 0x01 to use for outputs we don't have, this filler
    # doesn't actually matter because we use the first byte of each 36 to signal if
    # it's present or not
    1 DUP CAT DUP CAT DUP CAT DUP DUP CAT DUP CAT CAT TOALTSTACK
    
    # for each of the outputs
    0 INSPECTNUMOUTPUTS
    {
        # condition on if we have the output we're checking for
        DUP i GREATERTHANOREQUAL
        IF
            # attach the output data on, make sure it's taproot
            1 i INSPECTOUTPUTSCRIPTPUBKEY
            1 EQUALVERIFY 2DROP
            i INSPECTOUTPUTVALUE SCRIPTNUMTOLE64
            CAT
        ELSE
            # push the empty buffer on
            PUSHDATA1(0) FROMALTSTACK
            DUP TOALTSTACK
        ENDIF
        CAT CAT
    } for i in 1..n
    
    # get rid of the empty buffer
    FROMALTSTACK DROP

And then of course tweak that to simplify the stack manipulation. Merkle root update In a few places we have to take a merkle root and replace a leaf with another leaf. We do this with the rollup state tree to execute withdrawals, but there’s other uses. We _can_ do this with a zkp, but that’s overkill. We want to do it with regular script ops. Our life gets easier if we keep a fixed size tree. We do this process in two steps since it would be inefficient to shuffle the elements around on the fly. You could probably get away without this by having the proof be provided _already_ in parts, but let’s just put it here for simplicity:
    
    TOALTSTACK TOALTSTACK TOALTSTACK
    DUP 32 LEFT SWAP
    { DUP (32 * i) 32 SUBSTR SWAP } for i in 1..n-1
    (32 * (n-1)) RIGHT
    FROMALTSTACK FROMALTSTACK FROMALTSTACK

You also might be able to avoid this if you play around with the stack structure in this gadget. So conceptually, when performing an update to a merkle root the stack ends up looking like this:
    
    <root> <cohash 1> <cohash 2> ... <cohash n> <leaf> <update> <idx>

This requires some stack finagling in order to split the proof apart, but you could tweak this design to pull out the next lowest cohash from the proof progressively. The core guts to doing each step looks like this:
    
    DUP TOALTSTACK # save the current path bits
    1 AND # condition on the lowest bit
    IF
        # hash with our accumulators to the right
        TOALTSTACK TOALTSTACK DUP
        FROMALTSTACK CAT SHA256 SWAP
        FROMALTSTACK CAT SHA256
    ELSE
        # hash with our accumulators to the left
        TOALTSTACK TOALTSTACK DUP
        FROMALTSTACK SWAP CAT SHA256 SWAP
        FROMALTSTACK SWAP CAT SHA256
    ENDIF
    FROMALTSTACK 1 RSHIFT # take the rest of the path bits and shave one off

After repeating this `n` times, our stack looks like this:
    
    <root> <computed root> <new root> 0

So we can just finalize it like this, leaving the new root on the stack:
    
    DROP TOALTSTACK EQUALVERIFY DROP DROP FROMALTSTACK

These can probably be optimized a little bit using other stack manipulation ops, but this is the general idea. We’ll refer to this with the alias `~MERKLEUPDATE<n>` used like this:
    
    <old root> <proof> <leaf> <update> <idx>
    ->
    <new root>

As said before, we may want to use a SNARK-friendly hash function instead of SHA-256. In-place buf replace Since we do this in a few places I wanted to define a simple gadget to avoid having to rewrite it many times. This just replaces a subsequence in a buffer with a different sequence of bytes. This seems clunkier than it should be, maybe someone else will figure out something simpler.
    
    DUP
    <n> RIGHT TOALTSTACK
    <n> LEFT
    SWAP CAT FROMALTSTACK CAT

Let’s call it `~BUFUPDATE<n, m>`, where `n` and `m` are the start and end of the replaced buffer and it’s used like this:
    
    <seq> <buf>
    ->
    <updated buf>

High level design approach 7Rollups naturally lend themselves to account-like data models, as having static public keys allows referring to accounts by short indexes. The signatures for these transactions can then be omitted from the public part of the ZKP witness. This is not ideal for privacy, but there are privacy oriented rollup designs like Aztec that can be investigated in another work. The particular semantics of the state transition function of the rollup can vary wildly depending on the application, but we can describe the common high level external behavior relevant to the function of the rollup that we are responsible for.
      * assert that the batch transactions, when played out on top of the old state root, yields the new state root
      * spend deposits into the rollup utxo
      * execute withdrawals from within the rollup
Since the goal of our Bitcoin script logic is to just expose transaction data and the rollup state commitments to the SNARK verifier, our goal is to use the SNARK circuit itself to enforce some of the more involved requirements of the transaction structure to make the rollup work. Note that we have to have the recursive covenant logic done by ourselves in regular script. In order to have the circuit assert that we would effectively have to have the circuit know the hash of its own verification key (or something similar), which is impossible. Actually there’s a few cases here where it seems like we could simplify some logic, but we run into similar issues like that where a hash would have to be present in its preimage. The funds in the rollup are stored in a single utxo that has this recursive covenant structure that we’ve been outlining applied to it as the first input and output to each rollup update transaction. The normal update spend path is locked behind a timelock to permit forced withdrawal transactions to be submitted, although there’s some issues that still persist that we discuss below. Strictly speaking, supporting deposits and withdrawals isn’t actually required if all we care about is improving the throughput of the ledger. This might be useful if we layer lightning channels inside the rollup and we only use it as mechanism to cheaply manage channels. But it limits its generality so we will still look to support them in our design. Normal rollup-initiated withdrawals in a batch are exposed to the chain as extra outputs to the transaction going to their appropriate destinations. The script uses the Liquid inspection opcodes to extract the scriptpubkeys for these outputs and add a commitment to that data as part of the public input to the rollup. There is a maximum number of withdrawals that we can support at once due to the limitations of snark circuits, but concrete limitations are unclear at this time. // TODO make diagram somewhere? Handling deposits Deposits are more involved to accomplish. The way I see is similar to how the forced withdrawal mechanism works (see below), by introducing another spend path that verifies the same basic requirements for continuing the recursive covenant, but instead of applying a state transition the user supplies a public key for the account they intend to create in the rollup. This does not immediately create the account, but instead requires that the sequencer does the work to insert the accounts themselves. It should be investigated if it would actually be cheaper to use a merkle mountain range like construction instead of just always having a fixed sized merkle tree. It also seems like we’re doing a lot of stack manipulation here that might be able to be simplified by rearranging things. Forced withdrawals Forced withdrawals are tricky and there’s several different ways to make them work. If the sequencer(s) is(/are) misbehaving and are censoring withdrawal transactions, then we would like to be able to force a withdrawal in some way. The obvious way to do this is to just submit a merkle proof for the account in the state tree and use that to update the root with the entry removed. This is a little bit tricky because the proofs could be large. A naive design might treat the state tree as a sparse merkle tree and have the bits of each address be the merkle path (as an earlier iteration of this did), but since we address accounts by a short index, our merkle tree is _much_ shorter. We can get away with 20 bit indexes for a max of 1048576 accounts and a withdrawal proof size of 640 bytes, or even 400 bytes if we decided to use 20 byte hashes. This brings the size of the proof onto the scale of the size of the program itself. But this might still be a little bit high and if the sequencer is censoring one user they may be censoring others as well, so an alternative approach may be to add an extra spend path to do a batched forced withdrawal. Verifying multiple merkle proofs is expensive, and by the time you have 2 or 3 merkle proofs in the transaction it may actually be cheaper to simply use another ZKP, so that avenue should be investigated eventually. There’s a potential fee sniping attack here where an attacker can keep a rollup busy and keep submitting forced withdrawals to it as honest users are trying to withdraw _or_ while the sequencer is trying to submit a state transition. This isn’t great because if they can keep it occupied long enough then they can force it over the sequencer failure deadline. Sloppy ways to solve this would be to also require some PoW or VDF in order to submit a withdrawal proof or to simply increase the failure deadline. The cost of the sequencer failing to defend is nearly zero (whatever the cost of proving an update) and the cost of the attacker succeeding is relatively high (blockchain fees, and eliminating an account they can attack with), so I don’t think in practice this attack vector will be very common. One way to defend against this is to limit the number of withdrawals that can be made between updates. That’s can still prevent people from exiting the rollup, but it can’t force it to fail. A cheaper alternative to using merkle trees is to use [_verkle_ trees](https://vitalik.ca/files/misc_files/verkle.pdf). These rely on pairings, but we’re using pairings already anyways in the ZKP so that doesn’t add any additional security assumptions. Sequencer failure In the event that the sequencer abandons their duties the rollup will not be able to make progress. A more ideal solution for this is to have some system involving a rotating set of sequencers that can sign over their right or a mechanism where sequencer rights for a period can be auctioned off. There’s other discussion of this that’s out of scope for this discussion. Regardless of the choice, if the sequencer fails and the rollup can’t make progress the simplest thing to do is al

[... truncated at 20,000 characters ...]
