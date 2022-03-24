# Definitions

## General conceptions

* Trusted Computing Base(TCB)
* Trusted Execution Environment(TEE)
* Trust

## Security attributes

* integrity
* confidentiality
* attestation
* secure boot
* TCB size

## Core mechanism 1: hardware access control

* protection ring(for example, privilege level on x86 and exception level on ARM)
* isolated execution

## Core mechanism 2: cryptographical methods

* Root of trust, chain of trust

# List of properties

## Security attributes

* code/data integrity
* data confidentiality
* code confidentiality
* secure boot
* local/remote attestation
* TCB size
* availability

## Implementation

* (minimum) protection ring level of the TEE
* instruction set architecture(or vendor)
* software stack

## Overhead(side effects)

* scalability
* usability
* 

# Table Rows

## Divided by HW

SGX(Intel x86_64, ring 3)

Sanctum(RISC-V, ring 3)

AMD SEV(AMD x86_64, ring -1)

ARM TrustZone(ARM, ring -2)

