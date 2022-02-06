## Materials

[Technical Overview of TEE, including SGX/TrustZone/RV PMP(Video)](https://www.youtube.com/watch?v=MREwcSo0uz4)

> Defined by CCC, 3 core properties: data confidentiality(cannot be viewed)/integrity(cannot by changed) & code integrity within TEE
>
> Here are some important aspects of TEE, but this presentation only talks about some of them
>
> ![](security-comparisons.png)
>
> other aspects: code confidentiality(maybe for intellectual property), authenticates launch(only run applications when are proved to be secure), programmability, attestability(measure the origin and current state of TEE, similar to **static/dynamic trust**?), recoverability
>
> attestation: ensure the integrity of TEE itself, usually rely on the root of trust(RoT), and it can be checked locally or remotely
>
> **Arm TrustZone**
>
> * OpenTEE
>
> * separation of normal/secure world
>
>   <img src="trustzone-1.png" style="zoom:50%;" />
>
>   <img src="trustzone-2.png" alt="good example of secure boot" style="zoom:60%;" />
>
> **Intel SGX**, too complicated...
>
> **RISC-V PMP**, can be used to create enclaves in x86, [keystone-enclave.org](https://keystone-enclave.org/), an ecosystem like OP-TEE but base on RV

[Trusted RV(Video)](https://www.youtube.com/watch?v=BuHbgefCxvM)

> Currently RV does not have a TEE specification, instead all the TEE frameworks(I guess, but at least one) that can be found are based on RV PMP, so it has not been mature yet?

[TEE Wikipedia](https://en.wikipedia.org/wiki/Trusted_execution_environment)

[A great survey about TEE](https://people.apache.org/~xli/presentations/tee.pdf)

attestation and authentication: provide *verifiable* evidence about the state or the identity of the computing device

setup the protection **from bottom up**: execute trusted code, remote attestation, isolation(sandboxing), data confidentiality/integrity

root of trust: unattested code/data provide other components trust(key for digital signature, self-verification)

> about TEE, famous groups: [TCG, trusted computing group](https://trustedcomputinggroup.org/) and [GP, global platform](https://globalplatform.org/technical-committees/trusted-execution-environment-tee-committee/), they contributed to the development of TEE

TEE: trusted code can be executed securely in it

> * based on RoT
> * uses protected memory
> * allow communication between normal and secure apps
> * allow secure apps to access system resources
> * support remote attestation/authentication([an example of remote attestation](https://seclab.stanford.edu/pcl/cs259/projects/cs259_final_lavina_jayesh/CS259_report_lavina_jayesh.pdf))

implementation 1: TPM-based, examples: Intel TXT, AMD SKINIT

implementation 2: coprocessor, individual OS and apps, communicate with the normal world, examples: Intel ME, AMD ST, Apple Secure Enclave

implementation 3: privilege modes, switch between EEs on the same processor, example: Intel SMM, ARM TrustZone

implementation 4: virtualization, secure VM isolated from the main OS, redirect system calls to the main OS(maybe not secure), take the cost of the hypervisor

implementation 5: memory encryption, 

implementation 6: user secure enclave, secure contained inside a process, address space is encrypted to/from RAM, minimal TCB(trusted computing base, a part of the system which has attack surfaces)-- only HW+enclave, example: Intel SGX, [RISC-V Sanctum](https://riscv.org/wp-content/uploads/2016/11/Tue1615-RISC-V-with-Sanctum-Enclaves-Lebedev-MIT.pdf), copy initial code without secrets to enclaves within which secret comes in after passing remote attestation from outside 
