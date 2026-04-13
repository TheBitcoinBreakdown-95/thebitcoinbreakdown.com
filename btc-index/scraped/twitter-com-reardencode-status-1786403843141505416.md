# twitter.com -- Scraped Content

**URL:** https://twitter.com/reardencode/status/1786403843141505416
**Category:** tweet
**Scrape status:** DONE
**Source notes:** BTC\The Great Script Restoration (GSR).md
**Scraped:** 2026-04-12

---

**@reardencode** (Rearden Vibes 🛩 fork/acc)

Briefly, here's the definition of restored script:
* Restore all opcodes from bitcoin 0.3.4 (with L/RSHIFT renamed to UP/DOWNSHIFT)
* Protect from DOS by using a varops validation budget that ensures that scripts cannot have a worse worst case validation time than today
* Convert all script number handling to variable length whole numbers
* Remove all opcodes dealing with negative numbers
* Add opcodes to better introspect the transaction than CAT and Schnorr tricks (TX, TXHASH, TXHASHVERIFY for bare)
* Replace sighash with TXHASH's TxFieldSelector to provide efficient access to the same hashing modes for signed and unsigned commitments
* Add an opcode to support mandatory prefix validation with OP_SUCCESS semantics (SEGMENT)
* Add opcodes to interact with Taproot (TWEAKADD, BYTEREV)
* Add opcodes for checking signatures on data from the stack (CHECKSIGFROMSTACK(VERIFY,ADD?))
* Remove the penalty for using taproot without an internal key, and restore parity to keys (most likely using segwit v1 with 33-byte keys with the lowest bit being parity and the 2nd to lowest being set to indicate the absence of an internal key - the other 6 bits, if set, act as anyone can spend)

This set of improvements restores bitcoin to being programmable money, without horse trading between various minimal things none of which solve the fundamental problems of working with script.

Open work on this project:
* Finish the work on the varops budget
  * Benchmarking
  * TX vs. input vs. witness bytes for the budget
* Work out a few details of TXHASH
* Implement variable length whole number division
* Decide whether CHECKSIGADD and/or CHECKSIGFROMSTACKADD deserve a place in restored script
* Write a reference script interpreter for Restored Script (either within the existing interpreter or cleanly separated)
* Write updates to BIPs (340, 341, 327, 346, CSFS)
* Write new BIPs (Restored Script validation rules)
* Write documentation for Restored Script
* Implement restored script support in various tools

cc @rusty_twit how'd I do?
