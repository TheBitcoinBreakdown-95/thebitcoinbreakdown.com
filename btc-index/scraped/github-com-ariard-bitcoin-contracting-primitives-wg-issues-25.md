# github.com -- Scraped Content

**URL:** https://github.com/ariard/bitcoin-contracting-primitives-wg/issues/25
**Category:** github
**Scrape status:** DONE
**Source notes:** BTC\The Great Script Restoration (GSR).md
**Scraped:** 2026-04-12

---

**Issue #25:** Specify opcodes for MATT
**Author:** bigspider
**State:** open

**_Edit_**: Obsolete, see [below](https://github.com/ariard/bitcoin-contracting-primitives-wg/issues/25#issuecomment-1595762674) for the latest attempt.

---

Hello, I hope it's fine if I slightly abuse this space to get feedback on my specific proposal - please let me know if this is not appreciated and I'll find a different venue.

I'm trying to formalize the exact opcodes for [MATT](https://merkle.fun) for the purpose of implementing them for bitcoin-inquisition.

One thing that was left unspecified in the initial sketch (h/t @darosior for pointing that out) is that a way is needed to make "arguments" passed to the covenant non-malleable, if they are passed via the witness.
Building on top of [Antoine Riard's PR on the annex format](https://github.com/bitcoin-inquisition/bitcoin/pull/9), I think using the annex for this purpose is the best course of action.

***I would love if someone more experienced with bitcoin-core would like to help with putting together a good PR.***
MATT needs your help! :)

This is what I'm planning right now for an (almost) complete set of opcodes - please let me know if you have any comments or suggestions.

## MATT tentative specs

Covenant opcodes: verify or commit to data in the taproot internal key of an input/output
- `OP_CHECKINPUTCOVENANTVERIFY`: let `x`, `d` be the two top elements of the stack; fail if any of `x` and `d` is not exactly 32 bytes; otherwise, check that the `x` is a valid x-only pubkey, and the internal pubkey `P` of the current input is indeed obtained by tweaking `lift_x(x)` with `d`.
- `OP_CHECKOUTPUTCOVENANTVERIFY`: given a number `out_i` and three 32-byte hash elements `x`, `d` and `taptree` on top of the stack, verifies that the `out_i`-th output is a P2TR output with the taproot internal key computed as above, and tweaked with `taptree`. Fail if if any of `x`, `d` or `taptree` is not exactly 32 bytes.

Data manipulation:
- `OP_CAT`: pop the top two stack elements, push their concatenation; fail if the concatenation is longer than a predefined limit (256 bytes?).

Additional introspection (compulsory):
- `OP_PUSH_ANNEX_RECORD`: details TBD; push an annex record onto the stack. To build on top of https://github.com/bitcoin-inquisition/bitcoin/pull/9.

Additional introspection (optional): one can probably do some interesting things without, but these would allow concepts like "pay to a contract" or "withdraw from a contract", where the contract is a covenant-encumbered UTXO.
- `OP_INSPECTNUMINPUTS` and `OP_INSPECTNUMOUTPUTS`: push to the stack the number of inputs/outputs.
- `OP_INSPECTINPUTVALUE` and `OP_INSPECTOUTPUTVALUE`: given an index `i` popped from the top of the stack, push to the stack the amount in sats of a certain input/output.

Still unresolved: as [pointed out by Anthony Towns](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2021-September/019420.html), amounts do not fit in 32-bytes; therefore, some way of enabling 64-bit maths would be desirable. It's a technicality, so it might safely be left for later.

## Comments

- `OP_CHECKINPUTCOVENANTVERIFY` and `OP_CHECKOUTPUTCOVENANTVERIFY` could be replaced with more general opcodes to inspect input/output scriptPubKey, and do some elliptic curve maths. Those are already available in Liquid, see [here](https://github.com/ElementsProject/elements/blob/master/doc/tapscript_opcodes.md).
