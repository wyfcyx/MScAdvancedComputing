GPU TEEs->some side-channel issues, "get the classification result only relying on the timing of the GPU kernel execution"

## 1 Introduction

Graviton and HIX composed of host TEE and device-side TEE, and it cannot handle side-channel attacks

issue: GPU applications EE: user-level library+user/kernel-level GPU driver/GPU kernel, and the data and code on the GPU can be visible to the driver code in a side-channel way(for example, how much time the classification model runs on GPU), if the platform provider is compromised, 

**make the communication with GPU independent to the secret data in the GPU(called data obliviousness)**

contribution: Telekine: a data-oblivious channel between trusted client machines and untrusted cloud machines which take advantages of GPU TEEs to ensure the isolation about GPU enclaves

idea: local GPU->remote GPU, API provided by LibTelekine; based on API remoting which was used for GPU virtualization but has not been used for security; now, user library->local trusted client machine, CPU-side control code->"relay" on remote cloud machine which is untrusted, GPU kernel->executed on GPUs of remote cloud machines; **briefly, it is almost a remote GPU API relay**, which is implemented as a cryptographically secure channel

new interface: client GPU API calls->network(including the server-side relay), **data-oblivious streams which are similar to constant time defenses**->cloud GPUs

How to achieve data obliviousness? **fixed size/rate communication**

**no need for CPU TEEs** due to the lack of the side-channel attacks in their threat models

## 2 Threat model

## 3 GPU Background(*)

## 4 Example side-channel attack

## 5 Design

### 5.1 Data-oblivious stream construction

### 5.2 Telekine operation

### 5.3 Data movement example

## 6 Implementation

## 7 Evaluation

## 8 Related work

* enclave-based security(*): utilize SGX(for example) to protect some legacy applications,
* GPU TEEs: Graviton&HIX: side-channel attacks!
* about Trusted I/O paths
  * Tolerating Malicious Device Drivers in Linux.
  * SGXIO: Generic Trusted I/O Path for Intel SGX.
  * Building Verifiable Trusted Path on Commodity x86 Computers.

