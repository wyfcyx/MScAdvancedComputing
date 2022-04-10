across the boundary of privileges

# system call tampering attacks

overshadow: protect user applications from malicious OS by encrypting memory. secrecy and integrity of the user applications are protected.

however, if the OS has been compromised, the OS can implement the system calls in a malicious way which doesn't follow the spec. target: protecting the control flow integrity of the application from a malicious OS **since we don't want to modify the applications**.

a new system call protection model that only considers the safety properties

secrecy by encryption

(integrity: )how to check: **verify** the safety properties after the OS has executed it

pure-software, it is orthogonal to TEE methods?

based on **a trusted VMM**

# Iago attacks

the kernel and applications are peers which communicate with each other via RPCs

trusted supervisory HW modules such as XOM and hypervisors like Over Shadow are not effective under the Iago attacks

a important consideration: the system call APIs must be carefully designed and somehow limited

> however, a versatile system call may improve the overall performance

Iago attacks: only rely on system call return values (scalar) rather than any other OS secure properties

attack target: making applications misbehave or leak secrets

takeaway: system call APIs design is critical even if the kernel is assumed to be an fully untrusted peer in the threat model

---

hacking SSL module of Apache: the kernel provide the same `getpid` and `time` results to another child process, since they are the only sources of randomness, leading to replay attacks

underlying reason: **SSL use PID as a nonrepeating nonce!**

takeaways: system call APIs are not designed to be secure RPC APIs which assumes that the kernels may be untrusted, however system calls are used everywhere; the gap between verification(by a supervisor) and implementation(by the kernel) is **not as large as** it was imagined before

trend: protect special-purpose tasks rather than general-purpose tasks

# exokernel

application-level physical resource management, expose all physical resources to **untrusted LibOSes**

advantage: application-specific resource management

> difference from microkernel?

critical point: **near-application flexible abstraction**

