## Trusted kernels

[Sierra TEE](https://www.sierraware.com/open-source-ARM-TrustZone.html), trusted OS, based on GP APIs

[OP-TEE](https://optee.readthedocs.io/en/latest/index.html), trusted OS, based on GP APIs

[Open-TEE](https://open-tee.github.io/), virtual TEE for secure application developers, based on GP APIs

[base-hw based on Genode OS framework](https://genode.org/documentation/articles/trustzone), experimental trusted microkernel, TCB = 20KLOC, 

[Andix OS](https://ieeexplore.ieee.org/abstract/document/7281715/?casa_token=q3CdiozRLdEAAAAA:vRIbrzjp-shomgORC-7bZcBKNLxHBW7Cz1u8BG8SoQQWnMYERwPheK8wN9NZVPusoiFHpRLLHQ), designed for Industrial Control Systems, trusted OS, support Linux/Android as a normal world OS, multitasking, based on GP APIs

> be able to restore the state of the normal world if it has been compromised/subverted
>
> TCB: HW, bootloader, and Andix kernel
>
> isolation: isolated address spaces of trusted application and the trusted kernel
>
> trusted services are invoked by executing the SMC(secure monitor call) instruction
>
> I/O reuse: TA tells the app: plz read the data from a file and return it back!

[On-board Credentials](https://aaltodoc.aalto.fi/bitstream/handle/123456789/3568/isbn9789526045986.pdf?sequence=1)

> multiple hardware credentials since each of them is not for general purpose
>
> create credentials flexibly, decentralized

[Trusted Language Runtime](https://dl.acm.org/doi/abs/10.1145/2541940.2541949?casa_token=Ed2wL8QoMw4AAAAA:oZUEvW-gubaZA1d-htv72WWekRjxpsXmFvMnJxI9AqTGcWzfJxRr0mOQ8hSYNJGNvW-PcJuYeswy0A), be like SGX SDK on x86 but it supports .NET, guarantee the confidentiality and integrity of the .NET mobile applications, separate secure/non-secure parts of the applications such as e-wallet or e-health, interpreting bytecode in a secure environment

[T6](https://www.trustkernel.com/uploads/datasheets/T6_TEE_datasheet.pdf): small TCB since operations which are not sensitive are relayed to the normal OS; can switch between working OS(safer) and entertainment OS as a hypervisor;

[Trusted Little Kernel by NVIDIA](https://www.w3.org/2012/webcrypto/webcrypto-next-workshop/papers/webcrypto2014_submission_25.pdf), small TCB, GP APIs, secure storage as a TA, 

> by the way, another 3 security attributes: secure I/O path/interrupt handling/storage/UI

[Samsung KNOX](https://images.samsung.com/is/content/samsung/p5/ch/business/enterprise-edition/Samsung_Knox_Whitepaper.pdf); featured: Real-Time Kernel Protection; perform integrity checks before executing trusted code based on digital signatures; secure storage based on Knox workspaces; support hardware-based root of trust, secure boot and attestation; 1TA corresponds to 1 RoT; continue later with RKP... 

[TrustICE](https://ieeexplore.ieee.org/abstract/document/7266865/?casa_token=BUBkt6_elmwAAAAA:bfP5ae4LuCyzAPsnuleHK4uzJzpLBw53GD7tZsTEsfRSu_XP5W90-m2w__Yo-Vu3JlQkWvROoQ); create isolated computing env **in the normal world** rather than the secure world; no hypervisor; TCB: only a Boot ROM and a trusted domain controller(<300LOC) which is responsible for the switching between ICE and the rich OS; only one ICE or the rich OS can be active at a time, a suspended ICE's data is protected by HW(watermark technique, no encryption/decryption)

> by the way, ARM defined an TZAPI for TruzeZone?
>
> by the way: 3 core mechanism: access control; isolated computing environment(coprocessor); cryptography-based
>
> TrustZone itself supports: CPU state/memory(MMU; TZASC, address space controller, secure/non-secure DRAM areas)/IO isolation(HW interrupt[non-secure: IRQ only, FIQ is excluded] by GIC & DMA isolation)/device privilege by TZPC, protection controller
>
> briefly, a secure hypervisor which manages non-secure OSs
>
> if the rich OS has been compromised, then the Trusted Domain controller can be bypassed

## Trusted services

[TrustOTP](https://dl.acm.org/doi/abs/10.1145/2810103.2813692?casa_token=-nGXeMQvo98AAAAA:gXkeqACaXbsAOg-C2ZLNv6ee-_56jIsPo04XSVL7XnyfBPBbg9P3NC4r70FQo5POnJVHIXVYiRn3Bw); 

> extra HW modules may work together with TrustZone(you're not alone!) See section 2.2
>
> NMI->into TrustOTP->show OTP on the secure screen->switch back to the normal OS

[TrustDump](https://doi.org/10.1007/978-3-319-11203-9_12); facilitate dynamic malware analysis; reliable memory acquisition, suspicious->user presses HW button->NMI interrupt->TrustDump

> OEM: original equipment manufacturer

