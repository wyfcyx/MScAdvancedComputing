Each block contains the hash of the previous block.

After a node receives a block, it checks the validity of the transactions inside the block, if it accepts the block, then it start to collect new transactions from the network before they can be packed into a full block. Then, it finds a *nonce*, a part of the new block, which makes the first several bits of the hash of the whole block are all zero(It is called proof-of-work). Finally, the node broadcasts the node to the network.

A node may receive multiple blocks whose previous blocks are the same. In this case, it generates new block based on one of them but also record the other branch. If the node finds that the other branch is longer than the current branch later, it can switch to the other branch.

Missed blocks: A node can request previous blocks of a block from the network until it reaches a block which is known to it. This can explain how a node compare the length of two branches.

block header: previous hash, nonce, and a root hash(Merkle tree), 80B(4.2MiB per year if every 10min a block), which means that we can store all the block headers on the blockchain in memory

check: receive enough blocks to confirms that a part of the longest chain has been fetched(LCA of all the blocks received), 

transaction: one or multiple inputs and at most 2 outputs(for payment and returning back to the sender), thus transactions are linked together to a huge graph