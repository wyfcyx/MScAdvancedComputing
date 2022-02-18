fork&join, create threads on demand: higher switching overhead

work dispatching/work thread pool: job generator cycles, problems: imbalance since it takes different time to handle different jobs, which is also found in event-driven models

shared job queue&work stealing: cons: lock-free shared queue; trick: dequeue multiple jobs at a time to mitigate contention, but imbalance

streaming: each job is multi-stage, pipeline across threads, 

evolved streaming: stages event-driven arch, each stage contains in/out queues and a thread pool; observable/reactive  bottleneck/load; however: stages across threads(communication) hurt performance

---

multi-processing

difference with multi-threading: no implicit memory sharing; communication is explicit

communication is key for performance/programmability; socket/pipe has a lot intermediate copies; explicit shared memory across processes, local-only, although zero-copy(think about futex: mutex across processes based on shared memory)

---

tools

* valgrind
* linux perf
* coz
* multi-threading memory allocator: 2 level: global->per-thread; examples: tcmalloc or jemalloc

patterns:

* RAII

* async programming: `std::promise<Type>, std::future<Type>`

  co_await

* lock-free algorithms, **non-blocking**, example: stack, hard to make it correct!, possible solution: RCU



