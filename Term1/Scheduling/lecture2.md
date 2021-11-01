release time $r_j$, start time of job $j$ should $\geq r_j$

**forced idleness**: no jobs are available now!

non-preemptive: $1|r_j|\max C_j$ can be easily done(random or FIFO), $1|r_j|\sum w_jC_j$ is NP-hard

$1|r_j|\sum C_j$ 2 SPT variants but neither of them are optimal: SPT-A(wait for the next shortest job) and SPT-B(SPT for ready jobs)

$1|r_j,pmtn|\sum C_j$: SRPT(shortest remaining processing time) scheduling, proof? when to change running job?->release time of a new job/completion of the current job

approx of $1|r_j|\sum C_j$ inspired by SRPT, $R$-approx means that for any job set $S$, $\frac{f(S_A)}{f(S_{OPT})}\leq R$, for example 2-approximation

convert-preemptive schedule approx: schedule the job in the order of completion time in $1|r_j,pmtn|\sum C_j$, wait if no jobs are available, it can be proven to be 2-approximation

proof? good but I need to review it



due date $d_j$, it's soft, so we just need to minimize the variations

lateness $L_j=C_j-d_j$, tardiness $T_j=\max(0,L_j)$ only have penalty if late

$1|d_j|\sum w_jL_j$ is the same problem as $1||\sum C_j$  

$1||L_{max}$ and $1||T_{max}$: earliest due date(EDD)-> nondecreasing $d_j$ order, proof: adjacent switch

$1||\sum T_j$ is NP-hard, but if $p_i\geq p_j\rightarrow d_i\geq d_j$, then EDD sequencing with ties broken by SPT(if several tasks have the same $d_j$)

$1||\sum U_j$ where $U_j$ is $1$ if $C_j>d_j$ otherwise $0$, Moore-Hodgson's algorithm, EDD until a late job is found, remove the job whose $p_j$ is the largest, then try to add other jobs still as EDD. finally add all the previously deleted jobs. $1||\sum w_jU_j$ is NP-hard.



