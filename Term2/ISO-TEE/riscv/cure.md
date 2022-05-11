problem of current designs: only one fixed type of enclave; do not support MLaaS(machine learning), which means that **they cannot expand the security boundary to include accelerators or multicores**; cannot effective defense side-channel attacks

contribution: multiple types of enclaves: sub-space/user-space/self-contained; **enclaves can access system resources exclusively**; 15% performance overhead

## 1 Intro

SGX: adaptation cost(we want to keep the applications intact!);

about secure I/O: It said that: "SGX/SEV/Sanctum do not provide secure I/O at all, Keystone and Graviton do, but with some costs"; if accelerator itself should be modified, that's not good; and we want to **bind peripherals directly to enclaves**

about side-channel attacks: aren't in the threat model of SGX/TrustZone; either Sanctum or SEV cannot do it well

contribution: 3 types of enclaves; **bind peripherals to enclaves exclusively**; side-channel protection(only cache-based?)

challenges: new HW primitives are needed; minimal HW modification; minimal enclave management overhead; should consider transient execution and side-channel attacks

## 2 System assumptions

modern high performance multi-core microarchitecture

system bus->a fixed set of hardwired peripheral controllers->peripherals; MMIO-based: CPU->parent, peripherals->children; DMA-based: DMA->children, devices->parents; system bus needs some scheduling mechanisms

secure boot on reset; 

## 3 Threat model

**SW-only** strong adversary which can compromise **all SW components** except for TCB

TCB is responsible for enclave management and the adversary can maliciously call these APIs

other attacks: memory integrity attacks or DMA attacks

do not consider: HW flaws; physical attacks; DoS; assume that **enclave code is trusted**

## 4 Requirements

### 4.1 Security requirements

enclave protection: code integrity, data integrity/confidentiality, code inaccessibility, protected from all other SW including other enclaves and DMA

protected by HW components only can be controlled by TCB; minimal TCB; side-channel attacks(cache, controlled channel, transient execution)

### 4.2 functionality requirements

dynamic enclave boundaries(across privilege levels: self-sustained enclaves); enclave-to-peripheral binding; minimal HW modifications(**no invasive CPU changes** for compatibility); reasonable performance overhead; configurable protection mechanisms

## 5 Cure architecture design

**enclave ID**-based access control, that is, per-enclave resource mapping including memory and peripherals

### 5.1 Cure ecosystem

CURE ecosystem: CURE-compatible device vendors; device users and service providers

implementation of sensitive services: 1) an enclave + an host APP 2) embedded the APP into an enclave

per enclave: a configuration provided by the service provider, which includes **resource requirements, version number and an enclave number $L_{encl}$**, which is unique in the app store

deployed bundle: configuration file, **enclave binary**, host APP

service provide should sign the configuration file and the enclave binary using a private key

device vendor also need to sign a certificate, what content?

### 5.2 customizable and resilient enclaves

#### 5.2.1 enclave management

type1: user-space; type2: kernel-space; type3: user + kernel space; type4: firmware or secure manager

enclave management: SM(security monitor) itself is a type4 enclave which manage other enclaves, reboot?



enclave installation: when deploying a new enclave->SM verifies its signature->create enclave meta-data structure $D_{encl}$, including enclave state structure $S_{encl}$(persistently store sensitive enclave data) and a $K_{encl}$ which is used to encrypt $S_{encl}$

initially, $S_{encl}$ contains another key $K_{com}$ created by SM which is used when the enclave is communicating with untrusted OS

based on counters which can prevent rollback attacks



enclave setup and teardown: SM verifies the binary and allocate(and isolate) the resources **exclusively** to the enclave according to the configuration file(**kernel-space enclave** should be allowed to control the **MMU** since it needs to execute the privileged code); then configure other HW primitives(for example, peripheral caches); then **load or restore the encrypted enclave state from the disk** after verification

SM controls all interrupts thus all context switches(assuming that HW hyperthreading is disabled during enclave runtime)

teardown: SM stores the encrypted enclave state on the disk->increases counter->clear processor states



enclave execution: enclave can access services provided by SM such as expanding memory or proves its integrity to the remote service provider before the provider send secrets to the enclave; enclave can access I/O provided by untrusted OS, this communication should be protected by $K_{com}$; enclave can implement their own crypto algorithms

**on a context switch**: flush all **core-exclusive** caches(What about shared caches?)

#### 5.2.2 user-space enclaves

user-process model which utilize system calls, tightly integrated into the OS, exception: context switch is intercepted by the SM; **small binary**

defensing controlled side-channel attacks(gain information by observing enclave's usage of the resource such as page tables): move enclave page tables into enclave memory; **secure interrupt** by providing handlers

limitation: cannot execute high privilege code like drivers->secrecy of data sent to peripherals; unable to protect sensitive services **accessing devices(sensors or GPUs)**, but is suitable to protect short-living services **relying on data encryption**(OTP, payment services, digital key services)

#### 5.2.3 kernel-space enclaves

a lightweight OS(itself or with a user-space part) which is called a RT(runtime), can access devices using drivers embedded into it, **flush peripheral's internal memory when its ownership is transferred**

as a virtual machine: VM page tables->enclave memory, SM instead of a hypervisor

limitation: higher binary size/memory consumption/development effort/high scheduling overhead since core is bound to kernel-space enclaves

scenario: **when secure I/O is required**

#### 5.2.4 sub-space enclaves

isolating SM from M-mode firmware->SM doesn't trust the firmware, **shrinking the TCB**, **HW countermeasure** prevents the firmware from accessing the SM data

### 5.3 HW security primitives

enhanced CPU components: register file per CPU core; system bus; shared cache

#### 5.3.1 Enclave Execution Context

#### 5.3.2 Access control on the system bus

#### 5.3.3 on-demand cache partitioning

## 6 Cure Prototyping

### 6.1 SW Cure enclaves

### 6.2 HW security primitives

## 7 Security Considerations

## 8 Evaluation

## 9 Related work

**a very useful comparison table!**

TrustZone: itself only supports 1 enclave, thus many extensions are designed to support multiplexing the enclaves, but they all have some shortcomings

## 10 Conclusion







