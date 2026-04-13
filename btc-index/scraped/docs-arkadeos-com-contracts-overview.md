# docs.arkadeos.com -- Scraped Content

**URL:** https://docs.arkadeos.com/contracts/overview
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Modern Bitcoin Contracts.md
**Scraped:** 2026-04-12

---

Skip to main content

[Build on Arkade home page](/)

Search...

⌘KAsk AI

Search...

Navigation

Deep dive

[Learn](/)[Wallet & Payments](/wallets/v0.4/getting-started/introduction)[Assets](/learn/arkade-assets/overview)[Contracts & Apps](/contracts/deep-dive)[Server & API](/arkd/what-is-arkd)[FAQ](/learn/faq/what-problem-does-arkade-solve)

  * [Deep dive](/contracts/deep-dive)


##### Working with Tapscript

  * [Setup](/contracts/setup)
  * [Escrow Contract](/contracts/escrow)
  * [Hash Time Locked Contract](/contracts/hashlock)
  * [Spilman Channel](/contracts/spilman-channel)
  * [Dryja-Poon Channel](/contracts/dryja-poon-channel)


##### Use Cases

  * [Lightning Swaps](/contracts/lightning-swaps)
  * [Lightning Channels](/contracts/lightning-channels)
  * [Chain Swaps](/contracts/chain-swaps)


##### Experimental

  * [Arkade Compiler](/experimental/arkade-compiler)
  * [Arkade Functions](/experimental/arkade-functions)
  * [Non-Interactive Swaps](/experimental/non-interactive-swaps)


On this page

  * VTXOs
  * Script compatibility and path rules
  * Timelocks
  * Input/output structure
  * Two-phase transaction flow
  * PSBTs and the Transaction class
  * Next steps


# Deep dive

Copy page

Learn about VTXOs, the two-phase transaction flow, and Tapscript helpers

Copy page

## 

​

VTXOs

Virtual Transaction Outputs (VTXOs) behave like Bitcoin UTXOs but execute offchain:

  * **Offchain execution** \- Instant transactions without waiting for block confirmation
  * **Onchain settlement** \- Backed by presigned Bitcoin transactions publishable at any time
  * **Server co-signing** \- Server provides preconfirmations but never controls funds


## 

Learn more about VTXOs and their security model

## 

​

Script compatibility and path rules

Arkade executes standard Bitcoin Script semantics inside VTXOs, so scripts that work onchain can be executed offchain. There are two protocol rules for spending paths:

  * **Collaborative path (offchain, instant)** must include the server pubkey so the operator can co-sign.
  * **Unilateral path (onchain, timelocked)** must include a CSV Exit Delay using the value from `getInfo()`. The server signature is not required.


    
    
    const info = await arkProvider.getInfo();
    const serverPubkey = hex.decode(info.signerPubkey).slice(1);
    const exitDelay = BigInt(info.exitDelay);
    
    const collaborativePath = MultisigTapscript.encode({
      pubkeys: [userPubkey, serverPubkey],
    }).script;
    
    const unilateralPath = CSVMultisigTapscript.encode({
      pubkeys: [userPubkey],
      timelock: exitDelay // Exit Delay from getInfo()
    }).script;
    
    const vtxoScript = new VtxoScript([collaborativePath, unilateralPath]);
    

CSV (relative timelocks) can only be used for unilateral exit paths. For collaborative paths, you MUST use CLTV (absolute timelocks).

## 

​

Timelocks

Type| VTXO Path| Unit| Example  
---|---|---|---  
**CLTV**|  Collaborative| Seconds (Unix timestamp)| `BigInt(Date.now() / 1000) + 86400n` (1 day from now)  
**CSV**|  Unilateral| Seconds (relative)| `exitDelay` from `getInfo()`  
  
The SDK provides helpers for common patterns:
    
    
    // N-of-N multisig
    MultisigTapscript.encode({ pubkeys: [pubkeyA, pubkeyB, serverPubkey] });
    
    // Absolute timelock (CLTV) - use for offchain paths
    CLTVMultisigTapscript.encode({
      pubkeys: [pubkeyA, serverPubkey],
      absoluteTimelock: BigInt(Math.floor(Date.now() / 1000)) + 86400n
    });
    
    // Relative timelock (CSV) - unilateral exit path in case of server liveness failure; emergency only
    CSVMultisigTapscript.encode({
      pubkeys: [pubkeyA, serverPubkey],
      relativeTimelock: 86528n // ~1 day in seconds
    });
    

## 

​

Input/output structure

**Inputs** specify which VTXO and spending path:
    
    
    const input = {
      txid: vtxo.txid,
      vout: vtxo.vout,
      value: vtxo.value,                                      // Must match exactly
      tapLeafScript: vtxoScript.findLeaf(hex.encode(leaf)),   // Spending path
      tapTree: vtxoScript.encode(),                           // Full tree
    };
    

**Outputs** specify destinations:
    
    
    const outputs = [{ amount: 10000n, script: pkScript }];
    

## 

​

Two-phase transaction flow

Arkade uses a two-phase protocol:

  1. **SubmitTx** \- Client submits signed transaction + unsigned checkpoints → Server validates, co-signs, and returns partially signed checkpoints
  2. **FinalizeTx** \- Client completes checkpoint signatures → Transaction receives preconfirmation status


    
    
    const { arkTx, checkpoints } = buildOffchainTx(inputs, outputs, serverUnrollScript);
    
    // Sign the main Arkade transaction
    const signedTx = await signer.sign(arkTx);
    
    const { arkTxid, signedCheckpointTxs } = await arkProvider.submitTx(
      base64.encode(signedTx.toPSBT()),
      checkpoints.map((cp) => base64.encode(cp.toPSBT()))
    );
    
    // Finalize by fully signing each checkpoint (spending-path signers required)
    const finalCheckpoints = await Promise.all(
      signedCheckpointTxs.map(async (cpB64) => {
        const cpTx = Transaction.fromPSBT(base64.decode(cpB64));
        const signedCp = await signer.sign(cpTx, [0]);
        return base64.encode(signedCp.toPSBT());
      })
    );
    
    await arkProvider.finalizeTx(arkTxid, finalCheckpoints);
    

## 

Deep dive into the offchain execution workflow

## 

​

PSBTs and the Transaction class

You can craft a classic PSBT using `@scure/btc-signer`. When decoding Arkade PSBTs, pass `{ allowUnknown: true }` to preserve Arkade-specific fields:
    
    
    const decoded = btc.Transaction.fromPSBT(psbt, { allowUnknown: true });
    

We **strongly recommend** using the SDK’s `Transaction` class instead. It matches `@scure/btc-signer` 1:1, so the same API calls (and `{ allowUnknown: true }`) work:
    
    
    import { Transaction } from '@arkade-os/sdk';
    
    const tx = new Transaction();
    tx.addInput({
      txid,
      index: vout,
      witnessUtxo: { script: inputScript, amount: inputValue },
    });
    tx.addOutput({ script: recipientScript, amount: outputValue });
    
    const psbt = tx.toPSBT();
    const decoded = Transaction.fromPSBT(psbt);
    

## 

​

Next steps

## Lightning swaps

Integrate Lightning Network

## Spilman channels

Build payment channels

## Experimental contracts

Advanced contract patterns

## API reference

Full SDK documentation

[Setup](/contracts/setup)

⌘I

Assistant

Responses are generated using AI and may contain mistakes.
