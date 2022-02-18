depend on where the security modules are: secure processor(on-chip)/coprocessor/accelerator(inside devices)/monitor(between processors and devices)

linear relationship: Every software layer trust all software below it in normal computer architecture.

**TEE**: guarantee confidentiality/integrity/availability, but not reliability since we focus on deliberate attacks rather than random errors

**TCB**(trusted computing base): underlying SW/HW of TEE, normally we trust it, but if there are vulnerabilities in the TCB, TEE will not provide any guarantees, thus TCB should be as small as possible to reduce attack surfaces

non-linear relationship: for example, SGX: only applications are trusted among applications/OS/Hypervisors while SMM&SecE below hypervisors are always trusted

protect protected SW's state(e.g. memory/IO/other modules) from untrusted SW/HW, ideal case: execute protected SW without side-effects which means that all modifications of shared states are erased across context switches

protected SW are also trusted

---

we should monitor TCB's code execution to ensure its trustworthiness(code authentication/isolation or protection)

**Root of trust**: security of the whole system is derived from it, which is a secret such as a crypto key, only accessible to TCB modules

derived keys from the root of trust: signing/verification keys, application: remote attestation which users use to check what SW is running in TEE

---

way of attacking memory: processor(untrusted SW)/bus(other devices snooping on the bus)/memory/DMA etc.

main idea: trust on-chip memory and off-chip memory is untrusted

confidentiality: encryption: CPU -> encrypt data -> memory -> decrypt data -> CPU

integrity: Merkle tree: hash nodes are stored in untrusted memory; should consider which memory region to protect at which granularity, for example, whole memory, a part of memory, or including external storage

when NVRAM comes in: ignored now...











