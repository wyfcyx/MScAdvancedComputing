## local search methods

cannot guarantee find globally optimal; or time given is not enough;

similar to hill climbing but for discrete problems; neighborhood $\mathcal{N}(S)$ from $S$ by adjacent pairwise interchange(maybe there're some constraints); until we find a local optima, but sometimes it isn't a global optima, depend on start point/direction/path

**Randomized**: simulated annealing(SA), random walk, can escape from a local optima, the tendency to escape reduces by means of *temperature*(it's difficult to escape under a low temperature) which helps for convergent

$x_k$, find a neighbor $y$, $\Delta=g(x_k)-g(y)$, if $\Delta\geq 0$ or with probability $e^{\Delta/T_k}$ $x_{k+1}:=y$ otherwise $x_{k+1}:=x_k$ where $T_k=\alpha^{k}T_0$ where $0<\alpha<1$

**Deterministic**: Tabu search, find only one proper neighbor list SA, accept $\Delta<0$  but $\Delta>-\gamma$, Tabu list $\mathcal{T}$ records last $L$ interchanges unordered pair $(i,j)$ to avoid loop(cannot handle very long loops), exception: if $g(y)$ is the best solution yet, then $y$ can be accepted even if the interchange this time can be found in Tabu list

## parallel machine scheduling

assumption: machines are identical; $P||C_{\max}$ (makespan) no longer trivial since we need consider *load-balancing*

total completion time $P||\sum C_j$ on $m$ machines, sort tasks according to $p_j$, $m$ smallest on $m$ machines, $m$ smaller on $m$ machines, ...

WSPT is an approximation of $P||\sum w_jC_j$ with ratio $R=1.21$

makespan lowerbound $M^*=\max\{\max p_j, \sum p_j/m\}$

$P|\text{pmtn}|C_{\max}$: McNaughtson's rule($M^*$-oriented scheduling), schedule tasks on machine 1 until total p reaches $M^*$, possibly interrupt here, after task do the same things on machine 2 etc. Since $M^*\geq p_{\max}$ we can guarantee that every task works on only one machine at a time.

$P|C_{\max}$ is NP-hard(has poly-time approximations) even $P=2$.

List scheduling(LS): a priority list of jobs, wait for an idle machine and send the first job, worst-case ratio is $2-\frac{1}{m}$

proof: last scheduled job $k$ starts at time $t_k=C_{\max}^{LS}-p_k$, before this point of time all machines are busy $\sum p_j-p_k\geq mt_k$, rearranging: $C_{\max}^{LS}\leq\sum_j\frac{p_j}{m}+\frac{(m-1)p_k}{m}$, given that $C_{\max}^{OPT}\geq M^*$, so $C_{\max}^{OPT}\geq\frac{\sum p_j}{m}$ and $p_k\leq p_{\max}\leq C_{\max}^{OPT}$, substitution ...

LS with longest processing time(LPT) which prioritizes jobs whose processing time is larger give a better worse-case ratio $\frac{4}{3}-\frac{1}{3m}$, worse-case construction: $n=2m+1$ and $p=\{2m-1,2m-1,2m-2,2m-2,...,m+1,m+1,m,m,m\}$







