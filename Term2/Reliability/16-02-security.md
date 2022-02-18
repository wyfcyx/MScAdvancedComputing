prevent control-flow changes: canary, need recompile, small perf overhead

prevent injected code from being executed: W^X, cannot defense ROP attacks

return-to-libc attack->ASLR, ROP can also pass ASLR+W^X by guess or leaked information

detect invalid control-flow transfers, guarantee control-flow integrity: insert a instruction to the position after a function is called, before this function returns check whether the content ra points to is equal to the instruction

write integrity: each instruction can only write to a finite set of objects!

data-flow integrity: data of each read can only from a finite set of writes