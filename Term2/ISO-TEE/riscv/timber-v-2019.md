## abstract

use tagged-memory to provide efficient and flexible(that is, fine-grained, without a high management overhead) memory isolation

## 1 introduction

tagged memory: every memory block is **transparently** marked with extra metadata(like shadow memory in ASAN?)

How can we use it for isolated execution?

stack interleaving->dynamic memory management; inter-enclave communication by shared memory;

## 2 background

isolated execution which exclude the privilege software from TCB: SGX/TrustZone

SGX-related instructions are very complex

## 3 threat model and design goals

OS is fully untrusted; trust crypto primitives; do not consider physical attacks; TCB includes the HW, M mode, a trust manager  called TagRoot in S mode; do not consider side-channel attacks

design goals:

* security: secure memory isolation/entry points/communication/attestation and sealing(encrypting enclaves' state)
* flexibility: fine-grained and **dynamically reconfigurable** memory isolation
* compatibility/low overhead/real-time

## 4 design

isolated execution

N-normal domain; T-trusted domain;

trusted domain is protected by **tag isolation**; processes and enclaves are protected by **MPU isolation**, on every memory access **they are both checked**(**a huge overhead since they are checked so frequently**) 

tag isolation: 2-bit tag for every 32-bit memory word: TU(Trusted User), TS(Trusted Supervisor), TC(Trusted Callable, used for secure entry points), can be applied to peripherals

> Where are the memory tags stored?

MPU isolation: per process(including an possible enclave and untrusted parts)

fast domain transitions: Trusted domain entry points must be marked with the TC tag. When CPU fetches this memory block, it automatically enters into the trusted domain. fetch N-tag memory->back to the normal domain; **horizontal domain transition is fast** since the RV privilege is not changed unlike TrustZone; vertical domain transition: normal/trusted system call

MPU sharing: mixed(normal & enclave) process support

---

dynamic memory management

**dedicated tag instructions for dynamic memory management**, new instructions which can access memory **only if** the memory tag equals to a given and programmable tag(**more strict** than normal memory access check), **every memory access is checked irrespective whether a tag is provided**

tag update: cannot elevate the domain, more flexible(for sure?)

dynamic memory interleaving: based on tag updates, claim memory(for example, enclave, N->TU) during runtime, **reduce the TCB size**

code hardening transformation: for code-reuse attacks, e.g., leak secrets to untrusted domain, use more **checked instructions**, obviously leading to a higher overhead

---

trusted services

Tag Root(executed in the TS domain): provide trusted OS services to the untrusted OS; enclave services to enclaves

highlight: fast inter-enclave communication without data copying

enclave management: created within a user process; enclave measurement; sealing(save) the enclave states across reboots;

possible extension: trusted I/O(**not yet**), trusted scheduling services

## 9 evaluation

