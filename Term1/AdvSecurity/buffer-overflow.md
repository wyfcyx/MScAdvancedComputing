# 1intro

buf overflow->so common,easy to exploit

effective for **remove penetration attack**: can enable attackers *inject and execute code*, what is they exactly need, control, privilege(1.2)

# 2

can take control a privileged program, or just control the host

main goal: `exec(sh)` in order to get a *root* shell, two subgoals: 1) find code in addr space; 2) jump with params

## goal1: injection

inject: input a string in the buffer(no need to overflow sometimes), buffers can be everywhere(stack/heap/static)

already there: combination

## goal2: control flow

how to alter control flow: overflow a buffer->corrupt the state of an adjacent part of the program's state such as adjacent pointers(near-arbitrary means that some bytes cannot be modified)

class: kind of program state to be corrupted, and where the state is located in the mem

class1: activation records, overwrite stack frame, jump when victim returns(stack smashing attack),

class2: function pointers: easy

class3:longjmp buffers, checkpoint/rollback system in C called setjmp/longjmp, longjump(buffer) to rollback, corrupt the buffer after find a near buffer

## combination

most common: ra points to hacking code, overwrite at the same time

maybe multi-steps

# 3defences

## 3.1writing correct code

some tools may help; `grep` finding `strcpy` or `sprintf` which don't check bounds; code auditing teams, however overflows can be subtle even safer alternatives are used; fault injection tools which try to trigger overflows randomly or static analysis tools, however cannot eliminate all overflows since C semantics is too weak;

## 3.2 non-X buffers

nowadays, many depend on inserting dynamic code into program data segments to optimize, therefore not all data segments can be non-X; however stacks can be non-X, both compatibility and safety, exceptions where code is placed on stack: 1)Linux signal delivery 2) GCC trampolines, but can be disabled; cannot work when using resident code or buffer is allocated on static/heap

## 3.3 bound checking

compaq C compiler; limited; too severe and cannot assure

gcc patch for bound checking; base & other attributes; large cost!, 30x slower for MM; no mature, cannot compile all programs

Purify memory access checking: link with Purify, check all access by inserting object code; 3~5x slower;

type-safe language; but a lot of code is written in C, and this paper aims to protect existing code;btw, JVM should also be protected!

## 3.4 code pointer integrity checking

detect if a code pointer has been corrupted before it's dereferenced; but, cannot protect other program states others than code pointer from overflows; high performance and good compatibility;

snarskii: custom implementation of libc, only protect activation records inside libs;

**stackguard**: protect `ra` in activation records; a gcc patch; *place a canary word next to ra*, check this word before jump to the address that `ra` points to; critical: how to implement this, how to prevent forgeries; 1) terminator canary: can cut down the overflowed string; 2) random canary: generated at the time when the program starts; result: work for both current and future attacks; stackguarded Red Hat v5.1, almost identical function; performance: higher cost of a single function call, but do not affect ssh throughput, and apache perf;

**pointguard**: generalization of stackguard dealing with more general overflows; *place canaries next to all code pointers* including function pointers and `longjmp` buffers; issue1, when and where to allocate, not want to modify DS due to compatibility, 'special-cased'; issue2, when to check, whenever value is loaded from mem to reg, but not a variable is used due to compiler optimizations; now pointguard can protect code pointers statically allocated; to protect non-pointer variable in the future, can support it arbitrarily

conclusion about code pointer integrity checking vs. bound checking; performance: code pointer is good; implementation effort: hard to implement bound check in C since pointer and array reference are indistinguishable; compatibility: code pointer is good since bound checking tends to break part of the C semantics

## 4 effective combinations

 

