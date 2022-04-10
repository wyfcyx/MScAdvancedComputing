# On the performance of Intel SGX

## SGX programming mode

possible overhead: memory encryption on every secure memory access; frequent privilege transition via `ECALL` or `OCALL`;

## experiments

ECALL/OCALL->7000 cycles while a simple system call only takes 200 cycles

for memory accesses: lower memory copy throughput; higher dynamic memory allocation overhead;

## conclusion

more adaption effort should be spent using SGX... For example, there are large SW such as Apache or...

# performance of SGX on the cloud

when running in enclave mode, threads are not allowed to trigger SW interrupts or use system calls

concurrency: one TCS(Thread Control Structure) per thread(or logical processor)

exit enclave mode: sync using `EEXIT` instruction; async by `AEX`, e.g. switch to OS to handle HW interrupts

DMA to PRM is prohibited by the HW

MEE: encrypt and decrypt at the CPU package boundary, that is, after the LLC

**maximum PRM size is only 128MiB**->high swapping frequency thus high overhead

EPC pages cannot be shared across enclaves

**up to 16 page evictions at a time**

SGX version 2: page allocation after an enclave has been initialized?

SECS controls the lifecycle of an enclave; TCS per logical processor; EPCM->like a page table?

---

experimental setup: PRM=128MiB, observation: "more iterations didn't yield a low deviation"

`RDTSC` instruction cannot be executed natively in an enclave. Therefore, we can only record how much time is spent in the enclave.

state transition cost:  increases almost linearly (**when the buffer size is larger than 64KiB** used for arguments?)as the buffer size increases

> Question: I guess that we don't need to copy the memory buffer on normal state transitions?

paging: when workload size is larger than PRM size, page fault handled by the OS, AEX/IPI if there are multiple threads

attestation(provisioning): increases if concurrent number of enclaves or enclave workload size increase

---

recommendation: partition the enclaves so that every enclave doesn't exceed 64KiB; pre-provision the enclave if we can predict the usage of the enclave to hide the enclave creation latency

# on the performance of TrustZone

based on OP-TEE framework(I want to smile in silence? here)

GP APIs includes: secure storage/memory access/cryptographic operations

**TAs must be fitted in on-chip memory, which is limited to 3-5MiB in terms of size**

FIQs are used exclusively by the secure world. For example, the **secure clock** is critical to ensure the security of the secure world.

TA concurrency: on a **core** basis. Surprisingly, ARM supports hyperthreading!

> How to ensure the secrecy of the data given that it is send back and forth across the world boundary?

secure storage: data stored on untrusted disk is encrypted, an eMMC(Multi Media Card) device is used to prevent replay attacks

