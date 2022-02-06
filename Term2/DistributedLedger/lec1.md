## Blockchain introduction

decentralized->{miner, developers, P2P network}

want: decentralized/privacy-preserving/efficient

Open and decentralized(Bitcoin, Ethereum)/permission-base blockchains, they are different

hash functions(SHA256/RIPEMD160): collision resistance, second pre-image resistance, pre-image resistance, hiding, 

pre-image resistance, for a given $h$, it is hard to find a $x$ s.t. $H(x)=h$

second pre-image resistance, for any given $x$, it is hard to find a $y$ s.t. $x\not=y$ and $H(x)=H(y)$

collision resistance, hard to find $(x,y)$ s.t. they collide

hiding: when $r$ is selected from a "unpredictable" distribution, given $H(r|x)$ where | means a concatenation, hard to find $x$, usage: when set of $x$ is limited

puzzle-friendly: for every possible n-bit $h$, for any given $r$ from a "unpredictable" distribution, not feasible to find a $x$ so that $H(r|x)=h$ in $\mathcal{O}(2^n)$

search puzzle: find $x$ so that $H(id|x)\in Y$

Merkle Tree: a tree hash where every node is a hash of their children

Elliptic Curve Signature Algorithm(ECDSA): use private key to sign the **transaction**, use the public key to verify it; mention that all the data in the blockchains are plaintext and are not encrypted

address: hash of a public key(2 i32 X and Y), 25 bytes, < 21 million bitcoin, 1 satoshi = 10^-8 bitcoin

use base58(for visible results) instead of base64 in order to avoid confusions such as i/l ...

transactions: from input to output, from sender address to {recipient address, change address}, $\sum\text{input}\geq\sum\text{output}$ due to possible transaction fees

transactions are linked together: output->another input,

coinbase transaction: the first transaction in a block, defined by the miner, no inputs are required

transaction script: stack-base PL, check if the transaction is valid, performance is critical for preventing DoS attack, many opcodes such as(OP_DUP, OP_HASH160, OP_EQUALVERIFY and so on), the execution is similar to the expression evaluation using two stacks

block=header{hash of previous block's header, Merkle hash, unix time, target, nonce, ...}+transactions,

lightweight clients: only consider own transactions, header-only blockchains, can verify proof-of-work, can find the longest chain, SPV transaction verification: verify if a specific transaction is in a specific block(use only headers, merge the Merkle hashes)