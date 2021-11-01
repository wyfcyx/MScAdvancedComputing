user is the weakest link

scared number about passwds

passwords->81% of breaches

data integrity: sh1/one way hash?/CRC/md5(example: file integrity check)

accountability: log

99.999% availability(5 nines uptime; <6min downtime per year), solution: redundancy

how to handle DoS? captcha/cloudflare(they are all depending on the platform); [other approaches](https://www.usenix.org/system/files/sec21fall-nakatsuka.pdf), how relieve users from captchas

non-repudiation, evidence of communication, like transactional? solution: trusted third party or blockchain when bank cannot be relied on



principles:

1. least privilege(qmail story, C bugs, less is more, main answer(eliminating trusted code): least privilege)
2. defense-in-depth: multiple methods for one mechanism such as passwd(different layers)
3. securing the weakest link, social engineering hack(employees can be the weakest part), back doors, 
4. fail-safe stance i.e. plan for failure(when lifts are powered off)
5. through obscurity: hiding internal mechanisms
6. security by default

code of design published by the government

a summary(slice 33)



vulnerabilities of PL

C++: manual mem alloc/pointer arithmetic/focus on speed and hardware control

Java: auto mem management/type safety such as array bound checks/perf suffers



Java security basics

compiler->byte code-> JVM which cross-platform, gives Java portability

byte code was used by pascal/smalltalk

trade-off between safety and perf

java memory areas: native method stacks?

inside JVM: class loader(important)/linker/verifier(bytecode may be from attackers), valid instruction has many features, so verifier is complicated, verifier issues CVE-2012-1723, slide 43

how java maintains mem safety: array bounds check, check cast-type safe, non-null check when using pointers or references, check array references, GC

java native interactions: call methods from C++/dll, C# can also do this

java security mechanisms of rt, sandboxing, code signing(encrypt class file), loader(namespace isolation), verifier and rt checks, security manager such as stack inspection which java is famous for







