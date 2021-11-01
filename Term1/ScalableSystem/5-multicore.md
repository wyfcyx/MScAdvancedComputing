OLTP, small updates, main

past: computation&memory constitute 60% of latency, > 50% are processor stalls(memory/IO/branch misprediction); for memory, most are L1 ins and L2 data

Moore's Law: doubling of transistors ok, clock rate and power hit the wall

processor trends: multithreading->SMP->multi-socket multicore, goal: scalability, power?

IPC~1 while maximum=4, why?; 70% processor stalling

extended storage hierarchy: more sockets; each socket has its own memory; inter-socket links; goal: exploit abundant parallism

OLTP perf go with threads increasing: up->down->stay, due to locking or contention, BN: access latency; OLAP: up->stay; RO, no contention, BN: mem bandwidth

L1 no penalty; L2/L3/mem has possible stalls

stalls in cloud workloads: IPC depends on application; average mem cycles > 2; so IPC is low;

sources of mem stalls: **L1 ins and L3 data**

data misses are **unavoidable**! so focus on L1 ins locality and utilize cache line for data

## prefetching

simple prefetching: miss A, fetch A+1; miss A,A+1, fetch A+2,A+3; miss A,A+20, fetch A+40,A+60; not for instructions, we can use branch predictions; preferred on real HW, easy to impl

(maybe for HW)temporal streaming: recurring control flow(same flow of cache blocks are accessed even if different input is given)

SW prefetching: e.g. prefetch child when accessing parent when traversing

## cache conscious

code opt: simplified code for smaller instruction footprint; better code layout: minimize jumps to utilize next-line prefetcher, static profile-guided opt, dynamic JIT opt; compile to native/machine code instead of something like byte code, BN when accessing mem

cache-conscious data layout: go back to the architecture's MM, row stores is good for OLTP which accesses many cols, col stores is good for OLAP on the other hand; other data structures?

vectorized execution: good data&ins locality; exploiting SIMD

## exploiting common instructions

many data is cold(most data only accessed once): higher overlap in same-type transaction

computation spreading: move the transaction onto the core which contains its instruction & data

## locking

multi-threads access the same data: contention

latching & locking: a big part of the transaction latency

critical section types: unbounded(number of threads can be in the CS at the same time)/fixed/cooperative, idea: unbounded->fixed/cooperative

example: scaling an OLTP

hot/cold lock, speculative lock inheritance: send lock directly to the next thread for hot lock

data-oriented transaction execution: a thread always access a subset of all the data, thread-lock, avoid centralized locking

in-memory DB: not wait for disk, light concurrency

same idea as data-oriented: physically partition the data structure; for example, B+ Tree divide from the root in terms of key, how to achieve load balance?

logging: aether holistic logging: early lock release/flush pipelining/consolidation array????

## non-uniform access

do not want multi-socket access!

difference between share-everything, share-nothing between islands, share-nothing between cores

although share-everything, we can use psychological partitioning or data-oriented 



