## Lec1: Introduction & background

simple cryptography/merkle trees/addresses/transactions(coinbase transaction, or genesis block)/bitcoin script&transaction types/bitcoin wallets/chain of blocks/SPV(for Simple Payment Verification) transaction verification

## Lec2: Mining & forks

* merged mining
* mining pool
* decentralized mining: p2pool & smart pool based on Ethereum Smart contracts
* hard forks(function++, clients must upgrade their SW's version) & soft forks(function--, old clients can still recognize the new transactions)

## Lec3: Smart Contract Programming

* bitcoin scripts
* extending bitcoin scripts: namecoin(3 new opcodes, avoid front-running)
* Ethereum
* solidity

## Lec4: Consensus protocols & P2P

* classical consensus
* blockchain bootstapping
* Denial of Service protection
* network gossip protocol(hash, 36B,  or header, 80B, first?), bitcoin fibre
* eclipse attacks(double spending, denial of service{some figures here}, hardening the P2P layer, selfish mining)

## Lec6: Scaling

* channel networks
  * state replacement: Lightning
  * sync: HTLC/Perun
  * routing: source-routing/per-hop routing
  * summary: p88
* TEE
* payment channel hubs
* commit-chains
  * plasma cash(non-fungible)
  * NOCUST
  * summary: p147

## Lec7: Privacy

* network layer(txprobe)

* transaction layer(linkability/traceability)

  * bitcoin address clustering(p30)

* privacy by design

  * CoinJoin(Decoy of K-anonymity privacy)

  * ZCash(N-anonymity privacy, bitcoin fork, ZKP validation, t-addr/z-addr)

  * Monero(Decoy of K-anonymity privacy)

    unlinkability: stealth addresses

    untraceability: ring signatures(verify against a set of public keys)/RingCT

* privacy by add-on/mixers

  * tornado cash

* bloom filter

