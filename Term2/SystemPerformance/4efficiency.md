efficient code

bottleneck->we do not want to waste other resources->balanced systems->not a constant, function of a code section, not ideal

compute/latency/bandwidth-bound

low-level techniques

CPU-bound: poorly written, on small datasets, math-heavy, ...; metric: stall cycles, better than CPI, due to control/structural/data hazards; HW mitigate these hazards using pipelines, other design decisions...

speculative execution->some control hazards

superscalar: multiple(say, 4-way) instructions can be in the same pipeline stage

OOO->issue-commit side, mitigating data/structural hazards

SIMD, data-level parallelism,VLIW(rare)

**runtime predictable** code, partial evaluation, metaprogramming: time for helping the compiler(for example, constant generics, compiler knows the constant during code generation), inline functions(jump->local branches->even branch-free code, transferring control hazards to data hazards which requires more memory bandwidth)

branch predictor learns from a window of past branches, so sorted input may help

another tool: auto SIMD vectorization or explicit using intrinsics such as `_mm256_<op>_<suffix>`

sources of cache misses: compulsory versus capacity

memory bandwidth(bus is fully utilized)/latency bound(otherwise)

case1: compulsory+latency-bound->prefetching! `void __builtin_prefetch(const void *addr, ...)`

case2: bandwidth-bound->increase cache-line utilization by adjusting data layout

case3: capacity->reduce cache footprints(hot datasets), for example: loop tiling

multi-passing(radix sort???)

hazards from multicores->cache coherence protocol, memory consistency model; false sharing->every core works on its own cache-line by padding

