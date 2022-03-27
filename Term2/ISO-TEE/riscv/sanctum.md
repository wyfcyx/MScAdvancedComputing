same promise as SGX(thus it is also a ring3 TEE); eliminate the entire attack surfaces through isolation instead of adding to it; secure but not cryptographic ops;

problems of SGX: SW isolation guarantees are weak, for example, cannot defense side-channel attacks; HW implementation are hidden; 

Sanctum=HW modifications+SW security monitor; SW-only threat model; 

> cache timing attacks; memory access pattern attacks;

encrypted input->enclave->encrypted output

## 4 Implementation

SGX microcode(what's this?)->RV secure monitor(M, a part of TCB?);

DRAM(secure/non-secure partition by OS)/CPU management isn't prioritized, untrusted SW's responsibility

every enclave has its own page table which is stored in the DRAM area reserved for it(a part of secure memory), the page table cannot be accessed by the OS which might be compromised

outside EVRANGE: translation using the page table set up by OS

> brief summary:
>
> enclave PT inside enclave memory can only point to enclave memory
>
> other PT inside non-enclave memory can only point to non-enclave memory

 enclave threads run in User privilege;

enclave metadata region(like EPCM in SGX, another mystery: where is it stored in?)

enter enclave using SMC which locks a thread state data->exit enclave after unlocking the thread state data

enclaves are aware of the interrupts so that they can implement some security policies

enclaves also have their own trap handlers!

flush L1/TLB during context switching; LLC isolation based on the HW

guarantee: all computation inside an enclave which only access data in the enclave memory is protected from the outside SW(runtime can copy data into the enclave memory ahead. Additionally, all communication with the outside world should not bypass the proxy in the runtime)

the application requests the OS to create an enclave from `.so` or `.dll`

supports attestation by sending a piece of message to a privileged attestation enclave which can access the attestation key of the secure monitor

## 5 HW modifications

### 5.1 LLC

### 5.2 Page Walker Input

### 5.3 Page Walker Memory Access

### 5.4 DMA Transfer Filtering

 ## 6 SW

we trust: measurement root(ROM)/secure monitor(firmware, **so, what makes it a ring-3 TEE?**)/signing enclave(untrusted storage)

a special-purpose signing enclave, the security monitor send *private key* to it after checking its measurement 

support local attestation by providing a mechanism called mailbox
