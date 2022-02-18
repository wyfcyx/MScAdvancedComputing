sanitizers: instrumentation about runtime checks during compilation

Address/memory/UB/thread sanitizers

`valgrind`: works on binary, do not rely on source; based on dynamic instrumentation instead of static that sanitizers is based on; detect less bugs due to the lack of information; more monolithic than sanitizers that are specialized; 10x slower than sanitizers

ASAN: allocate **red zones**(128B) around memory objects, track freed memory, mark them as poisoned; heap allocation: use own allocator; stack allocation: generate code during compilation; quarantine(track freed memory, collect them into a finite FIFO), check use-after-free; shadow memory from Valgrind: metadata use to check if an address is poisoned, for example, a 9-state for every 8B, shadow memory mapping: shadow->invalid; no false positives by design; false negatives: overflows bypassing red zones, size limit of malloc FIFO, ...

MSAN: detect uninitialized memory access at a bit-level granularity; eliminating false positives, report what uninit reads?

UBSAN

cannot combine ASAN and MSAN

---

runtime security



