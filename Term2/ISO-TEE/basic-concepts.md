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

---

taxonomy version 1:

core of trust: remote attestation/isolated execution/root of trust

critical techniques: trusted storage(data safety)/secure boot(build a chain of trust)/TEE/measurement and verification or attestation/

basic methods: cryptography(certificate authorities, secure hashing algorithms, secret key exchanging algorithm)/formal verification

---

taxonomy version 2:

> threat model: what we trust throughout the whole process(TCB including a root of trust)
>
> by the way, there are also some untrusted HW or SW in the system, we should not rely on their status.
>
> system quality(per strategy, and finally put them all together): security(confidentiality/integrity); performance(latency/throughput/parallelism); reliability(availability/vulnerabilities/more...); maybe scalability?; 
>
> > [ref](https://syndicode.com/blog/12-software-architecture-quality-attributes/#:~:text=Availability%20is%20part%20of%20reliability,to%20the%20total%20working%20time.&text=Scalability%20is%20the%20ability%20of,to%20rapidly%20increase%20the%20load.)
> >
> > performance; interoperability; usability; reliability; availability; security; maintainability; modifiability; testability; scalability; reusability; supportability
>
> for each application, given its requirements(for example, performance, data sensitivity, ...), in the perspective of the programmers, we should determine a combination of answers of the following questions: How many machines should we use? How do these machines interconnect with each other? How many processors/cores are on each machine? Which HW platform should we use(X86, AMD, ARM, RISC-V)? Which SW stack(framework/SDK) should we use? How should we develop our application?
>
> For each question, we may have multiple choices like different rows in a table from a database. And we should evaluate these choices in terms of these system quality aspects.
>
> For a single aspect, it can be further divided into subtopics. {effect, overhead, there are still some known attacks}
>
> How do we evaluate a solution? For each attribute, we should evaluate all methods which may effect this attribute. Another idea which is more achievable: For each method, evaluate which attributes(also overheads) it can provide. 
>
> We should focus on the TCB! We do not need to concern the SW stack outside of TCB, but there may be some structural problems. **In the perspective of the applications**
>
> So: step1: per method(problem: why do we need a specific method, for example, remote attestation?); step2: summary for this whole strategy/implementation
>
> but performance??? We need more data!

end-to-end security solution, reducing TCB(trusted services instead of trusted kernels), eliminate vulnerabilities(static program analysis, formal verification), confidentiality&integrity, isolated execution(privilege, memory, I/O, interrupts)&context switch, crypto-based verification(create a trusted channel, local/remote attestation)

main target: building an end-to-end security solution which guaranteeing the confidentiality and integrity of the secret code & data

where is **trust**? What's trust?(also threat model)

At first we trust some parts of the whole system, and based on it we want to provide an end-to-end security solution which can guarantee the confidentiality and integrity(maybe also availability) of the secret code and data.

root of trust and a chain of trust(in the ways of certification or  key derivation)

2 core techniques:

1. isolated execution(a type of access control)

   privilege or something which is not a linear relationship

2. cryptograph-base methods(encryption&decryption)

How to attack? Compromise the TCB will break the TEE. Thus how can we do it?

1. find SW vulnerabilities(solution: reducing the size of TCB/using formal verification/static program analysis/fuzzing/symbolic execution/dynamic or static instrumentation/etc)
2. conduct microarchitectural attacks(improve the circuit design/come up with a more precise threat model)
3. more...

What can cryptography provide?(integrity, confidentiality, authenticity, so on and so forth)
