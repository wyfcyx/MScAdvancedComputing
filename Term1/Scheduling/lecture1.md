# before the class

I didn't do anything...

# during class

gantt chart which illustrate the status of scheduling

$C_j$ means completion time, if $C_j$ increases, metric $f({C_j})$ , which is called regular measures, also increases thus becomes worse

makespan: $\max{\{C_j\}}$, about load balance

$\alpha$ -> machines, $\beta$ -> job features, $\gamma$ -> optimality criterion, $\alpha|\beta|\gamma$ -> scheduling case

complexity classes...

* P, solvable in poly time
* NP, verifiable in poly time
* weak NP-hard: guarantee a approximation in poly time
* strict NP-hard: on guarantee

most scheduling are NP-hard, so we'll use search methods

single machine scheduling: release time $r_j=0$, process time has been determined, no preemption, single machine, no gaps are needed, machine won't idle either

> hint: preemption has costs!

$\sum\{C_j\}$ won't be improved on single machine using preemption, if $\exist_{j} r_j\neq0$, then it can be improved

$1||\sum C_j$, optimal: shortest processing time

$1||\sum w_jC_j$, optimal: sort by $\frac{p_j}{w_j}$, prove: switch two adjacent that not follow the rule

$1|chains|\sum w_jC_j$,job chains: allow interleaving or not allow

can interrupt: greedy, choose a initial chain which has the smallest ratio everytime