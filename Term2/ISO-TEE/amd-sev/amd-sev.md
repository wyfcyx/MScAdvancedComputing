# [introduction1](https://developer.amd.com/wp-content/resources/HelpingSecuretheCloudwithAMDEPYCSEV.pdf)

SME(Secure Memory Encryption): should be enabled in BIOS, only store encrypted data in memory based on an AES-128 engine embedded in the memory controller, 

SEV(Secure Encrypted Virtualization): one key per virtual machine, 

# [about AMD memory encryption](https://www.amd.com/system/files/documents/cloud-security-epyc-hardware-memory-encryption.pdf)

date categorization: data in flight(or data in transition)/data at rest(on persistent storage, 3 methods: individual file/filesystem/disk encryption)/date in use

SME: single key encryption, the key is generated at boot time, 

SEV: many key protection(key-based isolation): when the hypervisor and a VM are compromised, other VM's data cannot be accessed since it requires the cooperation between the hypervisor and the VM otherwise only encrypted data can be seen