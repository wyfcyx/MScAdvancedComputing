## Basics

### security considerations

* confidentiality/integrity of the data
* integrity/confidentiality(optional) of the code
* secure boot
* trust(static/dynamic), the root of trust can evaluate the trusted score of the system, and an interface is provided to the application without any privilege to check the status of trust

## Hardware architecture

### armv8 TrustZone

### armv9 RME, Realm Management Extension

### Intel SGX, Software Guard Extensions

will be deprecated...

### Intel TDX, Trusted Domain Extensions

### RISC-V PMP, Physical Memory Protection

## Software stack

SW stack(that is, TEE) of the trusted world: trusted firmware/secure monitors->trusted partition manager->trusted OS->trusted services

### firmware/secure monitor

there are many open-source implementations

### something between trusted OS and the firmware

### trusted OS

### trusted services

## Application examples

## Known attacks

