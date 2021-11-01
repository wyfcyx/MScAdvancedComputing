java security: sandboxing/code signing/class loaders/verifiers and rt tests/security manager(if requests are allowed)

security manager methods

stack inspection, check permission from down to top on the call stack, problem: multi-threads how to manage

java is safe based on vm based on C/C++, flaws after years, deprecated in many places due to bugs in jre

paper analyzing java exploits,

java isn't used on browsers anymore



back to native code C/C++

buffer overflow on stack/heap, can be solved by OS

solution1: DEP, stack/heap not X, but can load code to exist X positions

modifying `EIP` on the stack to jump to a arbitrary addr after ret

solution: address space layout randomization

ret2libc, the basic of return-oriented-programming

what to call **after** calling `add`, valuable instruction set including pop/pop/ret,

ROP design principles: gadgets, simple operations, ends with ret, chain with the next gadget

typical EIP code: EIP+, ESP fluctuates(push/pop); ROP code: ESP+(only pop and jump to the next addr), EIP fluctuates

gadget dictionary(mostly found in epilogues of  functions): load/store registers, or calling functions;

how to find gadgets, see paper

gadget compilers: see ROP gadget on github



malware

* virus: try to make copies, insert copies into other programs
* worm: copy through network
* spyware
* trojan: a backdoor
* drive-by-download: website or e-mail

increases as time goes, also the cybersecurity market is increasing

virus: infect other programs, may evolve, wait for users to execute an infected file

antivirus: find a signature(should be updated), a specific sequence of instructions or data, by scanning all files, which is a bottleneck

virus: place at the entry point/smaller virus; antivirus: entry point scanning/exploration until no more instructions can be found

virus: encryption, decryption into memory(also can used in JS), use a different key to infect new files; antivirus: generate signatures for encryption routines

virus: use encryption and decryption pairs; antivirus: run the code in emulation, disk/mem scanning

emulation challenges: virus can padding or sleep 

antivirus: static tech for signatures; dynamic tech for emulations, also hybrid methods

problem: false positive, innocent files are wrongly deleted by AV

gap between virus are founded and signatures are generated

limitations of AV: respond time/users should fetch recent updates!



IDS: intrusion detection systems, differentiate normal and abnormal behaviors

host-based IDS(investigate system call history) and network-based IDS(merged into the network components such as firewall)