problem of current designs: only one fixed type of enclave; do not support MLaaS(machine learning), which means that **they cannot expand the security boundary to include accelerators or multicores**; cannot effective defense side-channel attacks

contribution: multiple types of enclaves: sub-space/user-space/self-contained; **enclaves can access system resources exclusively**; 15% performance overhead

## 1 Intro

SGX: adaptation cost(we want to keep the applications intact!);

about secure I/O: It said that: "SGX/SEV/Sanctum do not provide secure I/O at all, Keystone and Graviton do, but with some costs"; if accelerator itself should be modified, that's not good; and we want to **bind peripherals directly to enclaves**

about side-channel attacks: aren't in the threat model of SGX/TrustZone; either Sanctum or SEV cannot do it well

## 2 System assumptions

## 3 Threat model

## 4 Requirements

### 4.1 Security

### 4.2 functionality

## 5 Cure architecture design

### 5.1 Cure ecosystem

### 5.2 customizable and resilient enclaves

### 5.3 HW security primitives

## 6 Cure Prototyping

### 6.1 SW Cure enclaves

### 6.2 HW security primitives

## 7 Security Considerations

## 8 Evaluation

## 9 Related work

**a very useful comparison table!**

TrustZone: itself only supports 1 enclave, thus many extensions are designed to support multiplexing the enclaves, but they all have some shortcomings

## 10 Conclusion







