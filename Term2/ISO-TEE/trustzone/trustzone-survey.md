# 2 TrustZone HW & platforms

## 2.1 Application processors(ARM-A)

`SCR_EL3.NS`, switch between S/NS world: SMC/IRQ/FIQ

extended memory infrastructure: TrustZone Address Space Controller(TZASC), partition memory regions as S/NS, only SW in S world can modify it; TrustZone Memory Adaptor(a kind of monitor?) which manages off-chip ROM or SRAM; MMU: page table per world

protect system devices: TrustZone Protection Controller(TZPC), NS is not allowed to access some resources, for example: TTC0, GIC(prioritize FIQ for S world over IRQ for NS world)

## 2.2 Micro-controllers(ARM-M)

the mechanism of ARM-M is different from ARM-A since ARM-M is optimized for interrupt latency/real-time scheduling/low power consumption/faster context switch/and so on, so ARM-M is not just a reuse of ARM-A

S/NS state automatically switching when accessing different type of memory(based on memory-map)

do not need secure monitor; state-transition instructions: Secure Gateway(NS->S), BXNS/BLXNS(S->NS)

control registers are banked across S/NS world, for example: physical SP, VTOR from SCB,

extending Nested Vectored Intr Controller,

## 2.3 TrustZone-enabled HW platforms



# 3. TrustZone-assisted TEE

## 3.1 TrustZone

guarantee the confidentiality and integrity of the computation inside the container

isolated execution: based on privilege(linear relationship)/based on other types of protection(S/NS world, memory, interrupt, I/O)

how to build trust:

* runtime: secure provisioning: for example, remote attestation which is used to establish a trusted channel between the secure container and the remote users
* boot time: secure boot, secure world SW - load -> Rich OS

an exception will be triggered and handled by the Secure Monition if NS world code want to access secure memory under the case that the OS has been compromised

providing end-to-end security which means that no one except for the sender and recipient of the messages including the service provider can read or modify the messages: trusted I/O paths, secure storage, remote attestation, 

TEE kernel: multiplex TEE instances; TEE service: implement a specific function, do not rely on OS for memory management or communication, only one service can be deployed on a device at a time;

## 3.2 Trusted kernels

TEE standardization: Open Mobile Terminal Platform defined a set of security requirements(OMTP, 2009); Global Platform(GP) defined: TEE internal APIs between trusted applications and the trusted kernel, TEE client APIs: communication interfaces between trusted applications and rich OS SW(client applications) maintained by the trusted kernel; device spec including  TEE user interface APIs, for example, PIN or screen and so on

> Summary: GP provides TEE internal/client APIs and device specs

Rich TEE: Samsung KNOX, several layers of data protection including secure boot, integrity attestation and SE Android support; encapsulate a secure container; cons: rich application in the secure world->larger TCB, more likely to be compromised

Small TEE: On-board Credentials(ObC), Trusted Language Runtime(TLR), OP-TEE, TLK, Open-TEE

unconventional trusted kernels: TrustICE, part of trusted code runs in normal world, which reduces the size of TCB; real-time support for IoT devices

## 3.3 Trusted services

special-purpose, no need for an underlying OS, small TCB, 

* trusted storage: DroidVault based on Sierra TEE, data owner can have a strong control over the sensitive data on an untrusted Android platform, a tiny trusted engine with a minimal TCB, always store encrypted data to untrusted storage medium
* authentication and crypto functions: Android Key Store, TrustOTP, and so on...
* rich OS introspection and control: enhancing some functions of OS using TrustZone, Restricted Spaces; TrustDump; and so on
* Trusted UI(secure I/O channels to the UI): TrustUI, divide the device drivers in the normal world into 2 parts: frontend in the secure world and backend in the normal world, which communicate with each other using proxy modules

## 3.4 cloud systems

client side: DFCLoud, provide secure access to cloud storage services such as Dropbox or Amazon S3 on Android services, it manages crypto keys which are used to decrypt data stored on cloud,

backend: TEE-protected privacy proxy for Zookeeper(only store encrypted data); Darkroom, secure image processing, decrypt image->transformation->encrypt image in a secure container on the server side 

## 3.5 Alternative TEE HW

protection ring(**which level the TEE is built upon**): 3->user applications; 0->kernel;  -1->hypervisor; -2->special system maintenance functions; -3->coprocessor or off-chip hardware

ring3: SGX/Sanctum

ring0: AEGIS

ring-1: rely on a trusted hypervisor, Bastion/AMD SEV(Secure Encrypted Virtualization)

ring-2: TrustZone, x86 SMM('90s, System Management Mode)

ring-3: TPM(Trusted Platform Module, specified by Trusted Computing Group, TCG): main purpose: secure boot, 

## 3.6 discussions

trusted kernel or service; 

reducing TCB(logically or physically): provide trusted services(or, trusted client APIs) instead of trusted kernels, since only minimal necessary modules are needed; ultimate solution: formal verification

# 4. TrustZone-assisted Virtualization

# 5 SW issues and HW vulnerabilities

