# 1intro

cannot predict if an execution can be benign->focus on prevention of malicious execution->2 categories: 1)guarantee the integrity of control flow 2) isolate 'bad' code including W^X

# 2

focus on redirecting the programs' execution

main contribution compared with its predecessors: Turing completeness without injecting code

## mitigations

stack smashing prevention: can be broken, and ROP do not rely on stack smashing

address-space layout randomization(ASLR), substitute of W^X, cannot prevent ROP since it only requires a bit of address information

control-flow integrity with an acceptable runtime cost, more effective than W^X?

# 3 X86 and SPARC

## x86

32 bit machine word, little-endian, allow unaligned access, complex instructions, variable-length instructions ranging from 1 to 12 bytes and unaligned, 8 gp regs, calling convention, 4 return insts, advantage of ROP on x86: see 3.1.7

## SPARC

load-store, fixed and aligned length instructions(32 bits), many gp regs, passed function arguments and ra through regs, has delay slots, regs that has different roles, start from 3.2.2 ignored...

# 4 ROP

what if sp substitutes pc?

when a `ret` is executed: read from the locations `%esp` points to and use the value to update `%eip`, and then `%esp+=4`, if the instruction `%eip` points to is also a `ret` then this process can repeat;

ROP stack layout: every element contains the start address of a code snippet ending with a `ret` inst, important thing: when executing a sequence, `%esp` has already pointed to the location on the stack containing the address of the next sequence

gadgets such as single load gadget, combination of several instruction pointers and imm on stack, 'instructions' of ROP,

how to start? through buffer overflow, overwrite `%eip` saved on the stack; but buffer overflow is not necessary, place payload on heap and let `%esp` point to its start addr(but how can we do this?); do not need to store the payload continuously, can even be loaded in multi-stages;

easy to find useful sequences compared to ret2libc, every sequence ending with a `ret`, on x86 even unaligned sequences can be tried(fetch in the middle, since x86 isa is dense);

**use a trie to analyze the budgets that can be found in a program**

# 5 x86 gadget catalog

## 5.1 load/store

## 5.2 Arithmetic and Logic

## 5.3 Control Flow

## 5.4 System Calls

## 5.5 Function Calls

just like ret2libc

## 5.6 shellcode

# 6 SPARC gadgets(ignored)

# 7 Gadget exploit framework

compiler & programming language(C like, but with less features) for SPARC



