smart contracts, not turing-complete, computerized transaction, code executed by all users, with global consensus, auto verification and enforcement, do not need to trust intermediaries, 

smart contracts are also **contracts**! For example, it Alice is late, she have to pay some penalty.

smart contract {spec: solidity code->bytecode/asm}, {identity&consensus: digital signatures}, {dispute resolution: decentralized platform}, ...

smart contract is built upon bitcoin scripts

program size depends time/memory consumption and also transaction fees!

---

namecoin, first fork of bitcoin, similar to DNS, name-related extension to bitcoin scripts, 

---

ethereum: replicated state machine(store explicit states), slow(12s), expensive(pay gas), more flexible than bitcoin

states S: address, EVM code, storage(variables), balance, nonce: number of transactions sent by this addr

inputs I(transactions that modify states): from addr, signature(from payer's private key), nonce(increase each time), to addr, data: arguments?, value in ETH, gaslimit, gasprice(ETH per gas)

transition f: validate & execute code

ethereum blockchain structure: in block header, height/state root/transaction root/receipt(contains {final state, gas payed and some output}) root of a mapping implemented using a compressed trie(or a suffix tree) 

---

2 types of states: accounts or contracts

for a contract, address=Hash(creator, nonce), code=EVM code, storage=Merkle storage root, balance=ETH balance, nonce

3 types of transactions:

* send{sender, signature of sender, nonce, receiver, #NODATA, amount in ETH, gaslimit, gasprice}
* create(a smart contract){creator, signature, nonce, #NODATA, EVM bytecode, start_balance, gaslimit, gasprice}
* call(a smart contract){caller, signature, nonce, contract addr, f+args(which function from the contract to call with arguments), ETH amount, gaslimit, gasprice}

smart contract can be seen as a list of functions

---

Ethereum virtual machine

memory: storage(permanent, very expensive, 6.4USD/KiB), and memory which is volatile

---

gas: transaction fee per opcode, overpriced opcodes are preferred, GAS_LIMIT(maximum per block) may halt execution

---

Live session:

front-running: someone found that you want to register a name, then he registers it before you and expect you will buy it from him at a high price