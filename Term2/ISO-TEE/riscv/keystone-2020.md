can run on unmodified RISC-V HW
## 1 Introduction

current TEE HW support(SGX/TrustZone/AMD SEV) has many platform-specific details, and it is hard to port applications. Also, the application design is limited. Flexibility! e.g. fixed enclave size on SGX.

Our contribution: highly customizable TEE leveraging RISC-V's primitives.

SM(Secure Manager): the boundary between the secure and non-secure world;RT: each enclave has its own S-Mode Runtime, which manage the virtual memory of the enclave

> RT is analogous to a library OS since it only supports 1 EAPP to run

Idea: expose more general APIs to SW

**tailor the TEE design according to the requirements**

big picture: SM(machine mode)/untrusted OS+Application(S+U modes)/enclaves(RT in S mode+EAPP in U mode)

## 2 A Common base for diverse TEEs

### 2.1 Commercial TEEs

current TEE designs are limited by a small design space; SGX: a large SW stack; SEV: VM with a huge TCB; TrustZone: flexible, support secure I/O like edge-computing sensors, but only 1 isolated domain(the secure world) and we need to multiplex it

developers have to compromise their requirements according to the platform they select

a recent trend: a **thin** secure software layer(a secure monitor like a *reference monitor* in the kernel design); pros: lower TCB and greater compatibility

### 2.2 Customizable TEEs

different applications have different security requirements(different threat models) even based on the same HW platform

> a very good example analysis, on an IoT sensor platform, here are the requirements:
>
> 1. "sign measurements for authenticity guarantees"
> 2. cache-occupancy side-channel attacks should be included in the threat model
>
> Then, how can we customize the enclave?
>
> sensor driver needs runtime memory integrity(specific, I guess it means code integrity); the signing process requires memory integrity+confidentiality
>
> Thus, the configuration: crypto library, private cache partition enclave, authenticated communication between 2 enclaves is support by the SM

target: achieve a higher utilization of all the available resources, **flexible TEE configuration and composition**

SGX and TrustZone do not allow flexible configurations to some extent, while RISC-V is more extendable?

Keystone's HW primitive requirements: **a device-specific key** can only be accessed by the **trusted boot process**, and a HW source of randomness

### 2.3 Entities in TEE lifecycle

- HW manufacturer(HW support of trusted boot)
- keystone platform provider(SM provider)
- keystone programmer(develop SM/RT/EAPPs)
- keystone user(instantiate an enclave with a suitable RT+EAPP configuration)
- EAPP(enclave user-mode application) user(interact with an EAPP)

> It is somehow like the TrustZone picture but there is not a world partition here, instead it is a classical linear privilege relationship

## 3 Overview

keystone will(?) support H Mode **in the future**

### 3.1 design principles

* SM: programmable by platform providers/minimal privilege/interrupt and exception delegation/PMP support
* separation of resource management and security guarantee: SM for security guarantees; RT and EAPP work in the same address space isolated from untrusted OS/APPs; RT is responsible for some management tasks
* modular layers: that is, SM+RT+EAPPs, which is flexible
* fine-grained TCB configuration: **TCB includes SM+RT+EAPP, which is relatively large, thus we need formal verification...**

### 3.2 enclave workflow

SM can be instantiated by the platform provider with some security extensions such as cache partitioning

developer -> keystone developer framework -> EAPP bin/RT bin/measurement

platform provider -> keystone framework -> SM bin/something useful for remote attestation

### 3.3 writing EAPPs

3 types, maybe not important?

### 3.4 threat model

TCB: PMP spec and implementation

chain of trust: root of trust->SM->RT->EAPP

protect **integrity and confidentiality of all the code and data of created enclave**

four classes of attacks are:

- physical attacker $A_{phy}$, monitor signals which move from/to the package
- software attacker $A_{SW}$, control all untrusted SW
- side-channel attacker, probe trusted execution from untrusted execution, cache $A_{cache}$, timing $A_{Time}$, controlled channel $A_{cntrl}$

- DoS attacker

scope: **keystone cannot defend speculative execution attacks**, cannot support (a part of) side-channel attacks **natively** since **they are orthogonal to this paper**, ...

## 4 SM

### 4.1 memory isolation

> possible limitation of PMP: only supports continuous memory allocation; number of PMP entries is limited to 32/64(but you have to rely on it)

highest(used by keystone) versus lower priority(used by OS) of `pmpcfg`

request chain: application to OS: want to create an enclave! then, OS to SM: want to create a `pmpcfg`

control transfer between enclave and non-enclave: enable/disable some `pmpcfg`(some details here but not important)

PMP synchronization among cores using IPI during the construction/destruction of an enclave

limited concurrency of enclaves: virtualizing PMP by H mode in the future?

### 4.2 post-creation in-enclave page management

every enclave has its own page table managed by its RT after the page table is created by the host OS

### 4.3 interrupts and exceptions

do not trust enclaves completely: set a machine timer before entering into an enclave to avoid denial-of-service attacks(although unintentionally)

### 4.4 Enclave lifecycle

* creation: virtual memory(allocated by untrusted OS, verified by the SM) layout measurement by SM

* execution: SM set PMP entries before transferring control to the enclave
* destruction

### 4.5 TEE primitives

* secure boot: what the root-of-trust does is that it generates SM measurement and an attestation key, then it signs them using a hardware-visible secret
* secure source of randomness: from SBI call `random`
* remote attestation
* other primitives...

### 4.6 platform-specific extensions

example: FU540

* secure on-chip memory: each enclave is assigned with a secure on-chip memory up to 2MiB **exclusively** for its entire lifecycle
* cache partitioning(avoiding shared cache): L2 controller's *waymasking* primitive; use PMP to way-partition the L2 cache;(i am not sure TAT)
* dynamic resizing: enclave want to expand the address space->host OS allocate the memory->SBI call to SM to update the PMP entries

## 5 Modular RT

### 5.1 MM modules

a contagious memory allocated by the host OS, not flexible for legacy applications, thus we need some extensions

* free memory: dynamically map VA to unmapped PA while the available memory region is fixed
* in-enclave self paging: handling page fault, page swapping(virtual memory)
* protecting the page content leaving the enclave: before copying the evicted pages to non-secure storage(non-secure DRAM regions or disk), method: SW(as a RT component) or HW encryption(like Intel MEE), target: confidentiality(adversary cannot understand the encrypted content) and integrity(adversary cannot change the encrypted content in silence)

### 5.2 functionality modules

* edge call interface: enclave are not allowed to access non-enclave memory directly, thus edge call(with function ID and parameters)->RT->host OS->handled by host applications

  RT and host OS share a buffer which they can use it to communicate

  further extension: syscalls/IPC/inter-enclave communication

  in the other direction: host applications->EAPP(mention **Iago attack**, what's this?)

  in-enclave syscalls: host applications->host OS->RT->SM

* multi-threading: RT for thread management, do not support multicore yet

## 6 Security Analysis

### 6.1 enclave protection

$A_{SW}$: access enclave memory(data/code of enclave/RT): we have PMP!

* mapping attacks: RT checks the validity of the mapping if it is going to be changed by the enclave
* syscall tampering attacks: there are RT modules that can defend syscall tampering or Iago attacks
* side-channel attacks: SM flush the shared states(TLB, registers, L1 cache, etc) between enclaves and non-enclaves during a context switch; mention that we also take advantage of the cache partition method

### 6.2 host OS protection

SW flush shared states; enclaves cannot access memory which belongs to host OS/processes nor modify the page table of them

### 6.3 SM protection

PMP protection of SM address space; well-define SBI interface; SM is only a special-purpose reference monitor

### 6.4 protection against physical attackers

on-chip memory(trusted, called scratchpad) --full, evicted--> DRAM

for enclave, PMP region only stores encrypted pages

for the SM, it is executed on the on-chip memory entirely

## 7 Evaluation

questions: modularity/TCB/performance/expressiveness of real-world applications

how can the host OS communicate with the enclaves: **Linux kernel driver**, that is, `/dev/keystone`

Linux launches and manages the enclaves

high I/O throughput loss due to syscall proxy

## 8 Related work

* TEE Architecture & extensions: SGX/TrustZone/Sanctum(SM/MMU/cache partitioning)
* TEE modularity: SW/HW
* versus trusted hypervisor: "more analogous to a reference monitor than a trusted hypervisor", reason: not memory management/scheduling/...
* TEE enhancement: SM layer/hypervisor layer(multiplex the secure isolation)/RT layer/EAPP layer
* enhancement of TEE security
* formal verification
* how it can guide OS designs: it is microkernel-like(SM for isolation and RT for functionality); RT modularity is like a exokernel

## 9 Conclusion

