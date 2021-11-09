job precedencies: DAGs

focus on some DAG topologies: in-tree/out-tree(out from root node)/opposing forest(many in-trees and out-trees)

> actually not tree, they're DAGs!

Hu's critical path algorithm: $P|i.t.,p_j=1|C_{\max}$ on an in-tree, greedy, prioritize the job in the ready list whose $\alpha_j$, length of the critical path (longest path) between exit node and it on in-tree, $\text{if}\ j\rightarrow\text{exit node} $, is the largest

how many machines to achieve best $C_{\max}$, if wish to complete in time $t=L+\Delta$ where $\Delta$ is an integer, then the number of  needed machine $m$ satisfies $m=\lfloor\max_q\{\frac{1}{q+\Delta}\sum_{j=1}^q\mathcal{l}(L+1-j)\}\rfloor+1$

Hu's also works for $P|o.t.,p_j=1|C_{\max}$(change orientations of i.t to o.t then reverse the order) and disjoint i.t or o.t(and a dummy root node)



Muntz-coffman algorithm: general DAG, preemptive, 2 machines, very easy algorithm, look back again...

each step choose at least 2 jobs to be in a new subset if possible(enough available jobs) to fill all the machines

optimal for $2|pmtn,prec,p_j=1|C_{\max},P|pmtn,i.t.,p_j=1|C_{\max},P|pmtn,o.t.,p_j=1|C_{\max}$

worst-case ratio of $P|pmtn,prec|C_{\max}=2-\frac{2}{m}$

