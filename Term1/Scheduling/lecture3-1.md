enumeration methods: scheduling as an optimization problem

$g(S)=\sum_{j}g_j(S)$ e.g. $g_j(S)=\max(0,C_j-d_j)$, combinatorial optimization

3 types of main techniques: approximation/enumeration(search for all possible solutions, global optimum)/metaheuristics(quick, perf is guar through experiments, only local optimum)

## enumeration

compression DP: $G(J)=\min_{j\in J}\{G(J-j)+g_j(J)\}$, $G(\empty)=0$, $\mathcal{O}(n2^n)$, where $j$ is the last scheduled job

branch(partition) and bound(update)? maybe an illustration: as a search tree

use approximation(such as preemptive EDD) as a *lowed bound* when searching, prioritize smallest lower bound(jumptracking), if higher than lower bound do not go deeper(fathoming)

revisit the search tree???

mixed-integer linear programming(MILP) when constraints and targets are linear

$1||\sum T_j$: time-indexed MILP

* let $T=\sum p_j$, $x_{j,t}=1$ if job $j$ starts at period $t$, 0 otherwise 

* $\min \sum_j \sum_{t=1}^{T-p_j+1} \max\{0,t+p_j-1-d_j\}x_{j,t}$

* cons1: $\forall j, \sum_{t=1}^{T-p_j+1}x_{j,t}=1$

* cons2: $S_{j,t}$ are the possible start times of job $j$ is at period $t$ it is running, then $S_{j,t}=\max(1,t-p_j+1)..\min(t,T-p_j+1)$, only one job can run at a time, thus

  $\forall t,\sum_j\sum_{s\in S_{j,t}}x_{j,s}\leq 1$

$1||\sum T_j$: sequence-position MILP

* $x_{j,k}=1$ if job $j$ is the $k$-th scheduled job, or 0 otherwise
* cons1: $\forall j,\sum_{k}x_{j,k}=1$
* cons2: $\forall k,\sum_{j}x_{j,k}=1$
* let $T_k$ is tardiness of the job ranked $k$, $\min \sum_{k}T_k$, where $T_k=\sum_{j}\sum_{u=1}^{k}x_{j,k}p_j-\sum_{j}x_{j,k}d_j$

---

problem 4 of tutorial 2

