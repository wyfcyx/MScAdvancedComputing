do not need debugging information, no runtime overhead

# 1intro

ASLR not effective since some addresses cannot be randomized, or easy to locate in some cases

debugging information & runtime overhead: see 1.4

cannot completely guarantee, but a good supplement(low overhead,easy to apply to 3rd party apps)

# 2 background

sequences ending with `call` or `jmp` instead of `ret` are also useful,

in practice ROP just works as a first stage that allocate a W&X memory area using something like `VirtualAlloc`, then DEP

# 3 approach

break gadget semantics in the address space of a running process, not effect program code stored on the disk

main observation: a gadget relies on the execution of all the previous gadgets, if one gadget(on the chain)'s semantic has been changed, then the whole gadget chain would be effected severely

## A why in-place

some methods require a complete view of the program, maybe including relocation(presented in Windows DLL and EXEs) and debugging information which has been stripped out from released executable

in place: use only binary code manipulation, do not change the size and location of code and data

limited transformations(narrow-scope, cannot block-reordering), but safe! without complete disasm coverage??? cannot modify overall structure but suffice to disable gadgets

## B code extraction and modification

no completely accurate disassembler for stripped x86!

conservatively, only choose confident parts to modify without symbolic information,

code extraction->our internal representation->in-place transformation, only apply on the segments which contains budgets

how it works: each application has multiple randomized copies, randomly choose one to run each time

# 4 transformations

## A atomic instruction substitution

substitute single instruction with a functionally equivalent one with the same length(not hard to find). this will break many unintended instruction seq on x86

## B instruction reordering

also significantly impact unintended inst seqs

1) intra basic block reordering: ensure that code is still correct through dependence(RAW/WAR/WAW) graph
2) reordering of register preservation code: push/pop in function prologue/epilogues, pops are important in gadget construction, change the order of how these regs are placed on the stack,

## C register reassignment

store variable value in another reg at some program point(now gadgets manipulate different regs unexpectedly), liveness analysis on machine code directly, suitable for private functions

# 5 experiment

## A randomization

## B correctness and performance

## C effectiveness

