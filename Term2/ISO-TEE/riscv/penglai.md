ring3 TEE even with a secure monitor(in theory, ring-2) in the ROM

## Abstract

problems of existing TEEs: scalability of the secure memory protection

PengLai: "dynamic, fine-grained, large-scale, fast-initialization(fork-style based on 'shadow enclaves')"

critical points:

* GPT(guarded page table): page table pages are also protected(similar to Sanctum?)
* MMT(mountable merkle tree)

## 1 Intro

background: emergence of micro-service & serverless

> IaaS versus PaaS versus SaaS versus FaaS
>
> I->infrastructure, that is a virtual server which provides CPU/network/storage
>
> P->platform, that is a container which software can run inside it like Docker
>
> S->software like basic UNIX utilities
>
> F->functions

main limitation of current TEE memory protection methods: stable/limited secure DRAM area partition; hard to scale traditional merkle tree; long time is taken to create an enclave, which is longer than the whole lifecycle of a micro-service

## 2 Motivation

Intel SGX: only 128/256MiB per enclave; long init time; a recent extension can increase the scalability but sacrifices integrity and still requires static allocation

AMD SEV: protect VMs without size limits; but the number of VMs is limited to 16;

Intel TDX: isolate trusted VMs from untrusted hypervisors; cannot defend **memory replay attacks**; only support 64 private keys thus 64 VMs(still not enough)

> replay attack: a kind of man-in-the-middle attack; collect information about one context, and use it in a different context

ARM TrustZone: **Komodo; Sanctuary;(application-level TEE even based on TrustZone)** unlimited enclave number & secure memory capacity; however fixed region number & no encryption or integrity guarantees

RISC-V: Keystone based on PMP thus limited protected memory regions, on-chip computing is secure but inefficient; Cure: enclave-ID based access control, hardware arbiter, support 13 memory regions; Sanctum; TIMBER-V: unlimited enclave number but large overhead;

current problems: limited SoC RAM capacity(fine-grained memory isolation); guarantee integrity for more memory->more memory consumption(large-scale memory integrity guarantee); enclave creation latency(existing enclave management layer: TrustZone secure OS or libOS in Occlum): do not consider attestation, or no optimization for repetitive creations

## 3 Overview

goals:

* scalability: unlimited number of enclaves; secure memory per enclave
* performance: low overhead
* security: threat model: untrusted privilege SW; HW replay attacks; side-channel attacks(microarchitectural)

### 3.1 architecture

secure monitor: partition of OS-application world(untrusted) and the enclave world; be responsible for enclave(thus secure OS in TrustZone is not needed here, it can provide client APIs like secure OS)/GPT/MMT/memory(both fine-grained and large-scale) management, other hardware management tasks are left to OS to reduce the TCB size

> how to understand fine-grained?
>
> (concurrent) enclave number, secure memory capacity per enclave, page size,

### 3.2 threat model

TCB: only HW and the secure monitor(no secure OS now, sounds great)

attacks: privileged/physical(bus between CPU and other HW & other HW are not trustworthy)/side-channel attacks(only cover controlled and cache-based side-channel attacks, other attacks are orthogonal?)

*do not consider DoS attack performed by untrusted HW/SW*

## 4 Design

### 4.1 fine-grained flexible memory isolation

physical page ownership based on bitmap: secure(used by secure monitor, enclave, also their page table pages), non-secure(OS, application), or intermediate node

> granularity: 4KiB; bitmap protected by PMP, managed by secure monitor

check ownership during a memory access: double check, a overhead of 25.2, see Timber-v

use GPT(guarded page table) to accelerate the ownership checking

observation: if all page tables of untrusted SW do not map to secure pages, many checks can be avoided(yes!)

2 kinds of page tables: host page table(HPT) for untrusted SW, enclave page table for enclaves

HPTs are put in an *protected* memory area called HPT Area, all modifications in the HPT Area are monitored by the secure monitor, the secure monitor ensures that no HPT maps to a secure physical page(don't forget to flush the TLB)

CSRs: `reg_hptarea_start, reg_hptarea_size` indicates the range of HPT Area; `reg_ms` indicates that whether current CPU is running an enclave's code; **enhanced page walker**: if translated PPN is out of the range of HPT Area and CPU isn't running enclave's code then it raises an exception which is handled by the secure monitor

> Question: Is the overhead smaller than checking ownership bitmap ahead?

enclave page tables: are marked with secure memory, all managed by the secure monitor, can map to both secure/non-secure physical pages;

huge page support: HPT Area is divided into several subareas, each of which contains pages of a specific size

summary: no in-memory metadata like SGX EPCM; HPT Area doesn't have scalability issues since page table page number is small; no ownership check during memory access, but the overhead of mapping maintenance is larger, however the overall overhead is smaller

### 4.2 scalable memory integrity protection

Mountable Merkle Tree: stable tree depth; minimal integrity metadata; can protect up to 512GiB secure memory

challenge: large-scale memory->deep tree->large node loading bandwidth overhead; need to pre-allocate all the tree nodes even if the secure memory is not complete; state-of-the-art: only support fixed memory area, not flexible, hard to scale out, *cannot controlled by SW*

---

on-chip: root tree root used for integrity check; **mount table:** tag, index, subtree root/address;

RAM areas: non-secure memory; secure memory; subtree nodes; MMT meta-zone(subtree root, root tree nodes, **only it is fixed**)

victim policy: mount table can only hold 32 entries simultaneously; inactive->MMT meta-zone

allocation of the secure memory and subtree node: by host OS but managed by the secure monitor(2 interfaces: `ALLOC_SECURE_MEM`, `REVOKE_SECURE_MEM`) 

boot: boot ROM, configure MMT meta-zone range, allocate subtree nodes to protect the secure monitor

subtree: 4KB x32=128KB x32=4MB x64=256MB subtree root=1GB 

global/local counter

> supply-1
>
> memory attacks: cold boot/replay attacks/dumping the memory content(tamper-resistant)/snooping the bus traffic
>
> the CPU-DRAM traffic should also be protected
>
> SGX: EPC capacity limitation(all enclave pages), which is 128MB->frequent EPC page swaps(each takes 40K CPU cycles); increasing EPC size also increases integrity tree depth which affects the cache utilization and the space overhead
>
> ---
>
> supply-2(in 2007, before TEE emerged, so the author wanted to encrypt all address spaces)
>
> core mechanism: memory encryption(for passive attacks which silently steal the sensitive information)/memory integrity verification(by computing and verifying MACs, for active attacks which invalidate the integrity guarantee)
>
> motivation: current design is not compatible with advanced HW features such as virtual memory and IPC
>
> memory encryption(current design): why do we need counters: hide the crypto latency on the critical path{an independent seed --apply a block cipher on it--> crypto pad, then we use this pad to encrypt/decrypt the memory block, **pad can be generated before/during the memory access**}; how to ensure the uniqueness of the pad(it should be varied across memory blocks and changes from time to time, that is, spatial and temporal uniqueness): we use a **counter** for each block which increases after a block write, thus block address and the counter should be seed components; however either physical address or virtual address should not be a component of the seed since it will break the spatial uniqueness of the pad
>
> memory integrity verification(current design): using Merkle tree, MAC per block; problem: cannot only protect memory reads, cannot protect swapped memory on disk, only 1 Merkle tree at a time, huge storage overhead, do not need to verify all nodes on a memory access but it still occupies 50% L2 cache;
>
> memory encryption(contribution): use *logical identifiers* instead of paddr/vaddr;
>
> memory integrity verification(contribution): support pages that are swapped out to the disk; **BMT which takes advantages of counter-mode encryption**, it is built upon counters rather than data MACs, which makes the Merkle tree smaller;
>
> memory encryption details: the first attempt: use a global counter which is incremented each time a block whatever it is is written back from the cache to the memory, trade-off{global counter width<->its on-chip cache capacity}, **I guess that we should store the value of the global counter when a block is written back to the memory for every block, and this value is not encrypted**; the second attempt: seed=per-block counter+block address+chunk id, smaller counter width->lower cache overhead, **but the block address should not be used for security schemes since it has been used in the underlying memory management system, and this can trigger many issues(see section 4.2)**
>
> memory integrity verification details:
>
> ---
>
> supply-3(2018, reducing paging overhead of SGX, efficient integrity verification)
>
> CIA guarantee = Confidentiality+Integrity+Authenticity
>
> "Integrity: the memory system correctly returns the last-written block of data at any address"
>
> EPC only stores recently accessed enclave pages since its capacity is limited to 128MiB
>
> SGX is based on an enhancement of the memory controller called MEE(memory encryption engine), but it incurs a large overhead(OS context switch on a EPC page miss; moving data between EPC and non-EPC; integrity tree maintenance), hit(200 cycles) versus miss(40K cycles)
>
> why can't we just increase the EPC size? one problem: the integrity tree and MACs are also stored in EPC(32MiB out of 128MiB)
>
> VAULT: more arity->smaller depth, more compacted; SMC: reduce storage overhead and memory bandwidth of MAC
>
> put it all together: EPC can be as large as the whole physical memory
>
> ---
>
> Memory Integrity Verification Paper(Caches and Hash Trees for Efficient Memory Integrity Verification,  2003)
>
> Why do we need to check a chain of MACs when we want to load a block from memory? What does it mean by "the parent protects its children"? How about replay attacks?
>
> **This is because the integrity tree nodes(except for the root) are also stored in the untrusted memory. Therefore, for the first question, the attacker can both modify the encrypted data and its parent node on the integrity tree.**
>
> ---
>
> SGX MEE paper

The paper did not mention that how the secure memory is encrypted and how the hash is calculated.

One detail: integrity check enabling(hole registers)

One important point: the secure memory and corresponding subtree nodes can be allocated dynamically on demand!

### 4.3 fast initialization with shadow enclaves

### 4.4 on-demand cache line locking(for side-channel attacks)

