scaling-up

Dennard Scaling in 1974: as transistors shrink, faster, consume less power, cheaper based on manufacturing technology

2004, end of Dennard Scaling, single-thread perf/freq/power do not grow as fast as it used to

Parallelism: DLP/ILP/Task-level parallelism(GPU, POSIX thread which programmers must extract manually)

Parallelism: executed at the same time using multiple computing resources; Concurrency: 'during overlapping periods'

parallelism is good for: performance/cost-efficiency(share everything, fully utilize all kind of resources, depend on workloads, reduce total cost of ownership-TCO)

Amadhl's law: speedup(p, s)=1/(1-p+p/s)

efficiency: single CPU is not enough! multiple machines/cores/or both

1s 125MiB/1KiB=125000coming requests

1 CPU can handle 1/50/10^-6=100000/5=20000requests per sec

---

multi-threading

simple model: concurrent, share address space

in reality more complicated: low-level operations, thread management & communication

critical path analysis: profiler cannot help, if we optimize a function, the critical path may change to another one without the optimized function!

for example: -- A --  C --

​						\  B  /

opt A&B at the same time!

communication&synchronization:

explicit sharing: cache coherency&memory consistency, atomic operations: CAS; C atomic primitives cumbersome to use while C++'s are more handy;

critical sections: **want to avoid concurrency access**

> memory consistency: consistency of multiple memory locations
>
> idea: single location(itself->cache coherency) 'controls' an larger memory area(by memory ordering, synchronize all data before the ownership is transferred)

sync primitives: mutex/rwlock/condvar/barrier/...

locks: U level, just spin, waste CPU cycles, starvation, no guarantee on order; K level, syscall(heavy overhead) to resched when waiting, however can guarantee the order and fairness; Hybrid, `pthread_mutex_lock` + `futex`, spin only for a while and then yield

false sharing: threads content on the same cache-line although their working areas do not overlap at all; mitigating it: padding, or `__attribute__((aligned(CACHE_LINE_SIZE)))`, `aligned_alloc`, `mem_align`, `posix_memalign`

thread management: create a thread per job on demand, huge data contention overhead;

