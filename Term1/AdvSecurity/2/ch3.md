safety design principles

## the principle of the least privilege

the least amount of privilege should be given to users so that they can complete their tasks

## defense in depth(redundancy)

rely on a combination of multiple mechanism to achieve safety

prevent(bank guards)/manage or contain(sandboxes)/recover(trace to robbers through a special kind of dye)/insurance

only prevention and detection are not enough, since attacks are facts rather than exceptions; plans during emergency(minimize the impact of the attack),

take password as an example: strong password is required, limit IP or address which is used to login

## diversity-in-defense

multiple heterogeneous systems do the same thing, e.g. use multiple OS in order to mitigate the impact of viruses

but: expensive, hard to deploy?

## securing the weakest link

weak password of some careless user, people in a company that cannot follow the safety policies, programmers themselves are malicious(review is good, but programmers may collude),

vulnerabilities(inappropriate use of encryption function), mixing of data and control such as SQL injection or buffer overflow

## fail-safe stance

(like something in distributed system)even if some components of the systems failed, there're still some levels of safety can be guaranteed

software should be designed with expectation that some other components may be fail

example: send a file(such as /dev/random which returns a random number of bits) whose length is infinite to the server to make the server run out its memory

solution1: check the file length(in fact, check whether the current runtime has enough memory to store the whole file in a buffer). but: the file length of /dev/random is zero from OS!

solution2: send as it reads(don't store the file entirely in memory), but if the server is not multi-threaded, it can never handle request from other users if /dev/random is sent

solution3: impose a download limit in terms of bytes, downside: it's difficult to choose the LIMIT so that it isn't too low or too high

## secure by default

many software are deployed with all features by default, which makes the software more vulnerable

good practice: only enable 20% features used by 80% users by default

hardening the OS: turn off unnecessary services by default(such as Microsoft's IIS)

## simplicity

make the software simpler, remove unnecessary functions, -> less vulnerabilities

less is more

## usability

## security features do not imply security

