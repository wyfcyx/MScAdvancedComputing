2018 by Microsoft

changes are limited to the GPU's command processors; CUDA runtime extension which enable the secure data copy between CPU and GPU; 17-33% overhead with encryption/decryption support

## 1 Introduction

why TEE support for accelerators is challenging: **device driver** has full control of the devices; microarchitecture of the devices for high throughput(many cores, high bandwidth memory) and it's difficult to implement security policies such as memory confidentiality since it will bring an unacceptable performance overhead

rely on device drivers->large attack surface; difference between the design of CPU & GPU, hard to snoop or monitor between the GPU and stacked memory

what is TEE in Graviton: a secure context, "a set of GPU resources(memory, command queue, register)" which is bound to a crypto key pair(the private key is more important, and **it is protected by the CPU TEE**)

threat model: do not trust all host SWs and other GPU contexts

other 2 primitives: attestation like SGX/dynamic secure memory management(it's the driver's responsibility) like Penglai

implementation: the command processor serves as a proxy between GPU sensitive resources and the driver, the main access control policy is implemented inside it(mention again the difference of the design between CPU&GPU)

**assumption that GPU on-package memory is trusted**, thus all HW changes are the command processor and the PCIe controller; benchmarks are based on emulations; the overhead is dominated by the encryption/decryption

**its threat model covers the whole host HW stack**, but **it trust part of the GPU HW** including the on-package memory

> How can you identify an enclave among multiple enclaves if you want to support running enclaves concurrently?

## 2 background

### 2.1 GPU

GPU stack: GPU user runtime(like CUDA)->GPU driver->PCI bus->GPU

command processor manages channels each of which is a command queue

### 2.2 SGX

## 3 Threat Model

## 4 Overview

## 5 Graviton Architecture

### 5.1 Remote attestation

### 5.2 Secure Context Management

### 5.3 Secure Context Isolation

## 6 SW stack

## 7 Evaluation

## 8 Related Work

why is SGX widely used? Because it can provide protection for both client CPUs and public cloud servers. 

development of this field: trusted I/O path which trusts a host component->Graviton which put the entire SW stack in the threat model

## 9 Conclusion

future work: support multiple GPUs/on-demand allocation/remove host TEE dependencies/support FPGAs