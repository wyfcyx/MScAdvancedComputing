## effciency of equilibria

social cost: SC:$\mathcal{X}\rightarrow\mathbb{R}$ quality of allocation for the whole players, for example total routing time $SC(x)=\sum_x J_i(x)$ or makespan $SC(x)=\max_i J_i(x)$

PoA(Price of anarchy)=the ratio of SC of the worst PNE and the SC of the best allocation which minimize the SC. It is larger than 1 due to selfishness.

smooth game: given $\lambda>0,\mu<1$ is smooth if $\sum_i J_i(x_i',x_{-i})\leq\lambda SC(x')+\mu SC(x)$, where $x'=(x_1',...,x_n')$

in a $(\lambda,\mu)$ smooth game, $\text{PoA}\leq\frac{\lambda}{1-\mu}$

every congestion game with a affine latency(non-decreasing) is a (5/3,1/3) smooth game, thus $\text{PoA}\leq2.5$

Proof:

congestion games whose `PoA` is exactly 2.5:

PoA bound of smooth games also works for MNE(means that the worst MNE/best allocation is ...)



