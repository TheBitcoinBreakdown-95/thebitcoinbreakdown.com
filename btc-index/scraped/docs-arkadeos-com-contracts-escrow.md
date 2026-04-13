# docs.arkadeos.com -- Scraped Content

**URL:** https://docs.arkadeos.com/contracts/escrow
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

Working with Tapscript

Escrow Contract

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

  * Build the Tapscript
  * Script breakdown
  * Next steps


Working with Tapscript

# Escrow Contract

Copy page

Build your escrow contract with three spending paths using the TypeScript SDK

Copy page

## Install the SDK

If you haven’t already, install the SDK and set up your environment

An escrow with three spending paths: cooperative release, arbiter resolution, and buyer refund after timeout.

Path| Condition| When to use  
---|---|---  
**Collaborative**|  Buyer + seller + server signatures| Both parties agree on release  
**Arbiter**|  Arbiter + server signatures| Dispute resolution  
**Refund**|  Buyer + server signatures (after 30 days)| Seller unresponsive  
  
## 

​

Build the Tapscript
    
    
    import {
      RestArkProvider,
      RestIndexerProvider,
      MnemonicIdentity,
      VtxoScript,
      Transaction,
      MultisigTapscript,
      CLTVMultisigTapscript,
      buildOffchainTx,
      CSVMultisigTapscript,
      networks
    } from '@arkade-os/sdk';
    import { hex, base64 } from '@scure/base';
    
    // Setup
    const arkProvider = new RestArkProvider('https://arkade.computer');
    const indexerProvider = new RestIndexerProvider('https://arkade.computer');
    const info = await arkProvider.getInfo();
    // Convert 33-byte compressed pubkey to 32-byte x-only
    const serverPubkey = hex.decode(info.signerPubkey).slice(1);
    
    // Identities
    const buyer = MnemonicIdentity.fromMnemonic("abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about");
    const seller = MnemonicIdentity.fromMnemonic("zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo wrong");
    const arbiter = MnemonicIdentity.fromMnemonic("legal winner thank year wave sausage worth useful legal winner thank yellow");
    
    // Build escrow script with 3 paths
    const buyerPubkey = await buyer.xOnlyPublicKey();
    const sellerPubkey = await seller.xOnlyPublicKey();
    const arbiterPubkey = await arbiter.xOnlyPublicKey();
    
    // Path 1: Buyer and seller both agree
    const collaborativePath = MultisigTapscript.encode({ 
      pubkeys: [buyerPubkey, sellerPubkey, serverPubkey] 
    }).script;
    
    // Path 2: Arbiter resolves dispute
    const arbiterPath = MultisigTapscript.encode({ 
      pubkeys: [arbiterPubkey, serverPubkey] 
    }).script;
    
    // Path 3: Refund to buyer after 30 days
    const startTime = BigInt(Math.floor(Date.now() / 1000));
    const refundPath = CLTVMultisigTapscript.encode({ 
      pubkeys: [buyerPubkey, serverPubkey],
      absoluteTimelock: startTime + (86400n * 30n) // 30 days
    }).script;
    
    // Assemble VtxoScript
    const escrowScript = new VtxoScript([collaborativePath, arbiterPath, refundPath]);
    const escrowAddress = escrowScript.address(networks.bitcoin.hrp, serverPubkey).encode();
    
    console.log('Escrow address:', escrowAddress);
    
    // Query VTXOs at escrow address
    const result = await indexerProvider.getVtxos({
      scripts: [hex.encode(escrowScript.pkScript)],
      spendableOnly: true,
    });
    
    if (result.vtxos.length === 0) {
      console.log('No VTXOs found at escrow address');
      process.exit(0);
    }
    
    const vtxo = result.vtxos[0];
    
    // Build transaction to release funds (cooperative path)
    const serverUnrollScript = CSVMultisigTapscript.decode(
      hex.decode(info.checkpointTapscript)
    );
    
    const input = {
      txid: vtxo.txid,
      vout: vtxo.vout,
      value: vtxo.value,
      tapLeafScript: escrowScript.findLeaf(hex.encode(collaborativePath)),
      tapTree: escrowScript.encode(),
    };
    
    const outputs = [
      {
        amount: vtxo.value, // Input amount must equal output amount
        script: recipientScript.pkScript
      },
    ];
    
    const { arkTx, checkpoints } = buildOffchainTx(
      [input],
      outputs,
      serverUnrollScript
    );
    
    // Sign with buyer and seller
    const psbt = arkTx.toPSBT();
    const txBuyer = Transaction.fromPSBT(psbt);
    const signedByBuyer = await buyer.sign(txBuyer);
    
    const txSeller = Transaction.fromPSBT(signedByBuyer.toPSBT());
    const signedByBoth = await seller.sign(txSeller);
    
    // Submit
    const checkpointPsbts = checkpoints.map(c => c.toPSBT());
    const { arkTxid, signedCheckpointTxs } = await arkProvider.submitTx(
      base64.encode(signedByBoth.toPSBT()),
      checkpointPsbts.map(c => base64.encode(c))
    );
    
    // Finalize - checkpoint needs all parties from the spending path
    const finalCheckpoints = await Promise.all(
      signedCheckpointTxs.map(async (cpB64) => {
        const cpTx = Transaction.fromPSBT(base64.decode(cpB64));
        const signedByBuyer = await buyer.sign(cpTx, [0]);
        const signedByBoth = await seller.sign(
          Transaction.fromPSBT(signedByBuyer.toPSBT()),
          [0]
        );
        return base64.encode(signedByBoth.toPSBT());
      })
    );
    
    await arkProvider.finalizeTx(arkTxid, finalCheckpoints);
    console.log('Escrow released!');
    

## 

​

Script breakdown

Opcode| Effect  
---|---  
`CHECKSIG`| Verify signature, return result  
`CHECKSIGVERIFY`| Verify signature, continue if valid  
`CHECKLOCKTIMEVERIFY`| Enforce absolute timelock (CLTV)  
`DROP`| Remove top stack element  
  
## 

​

Next steps

## Deep dive

Learn about VTXOs, transaction flow, and Tapscript helpers

## Lightning swaps

Integrate Lightning Network

[Setup](/contracts/setup)[Hash Time Locked Contract](/contracts/hashlock)

⌘I

Assistant

Responses are generated using AI and may contain mistakes.
