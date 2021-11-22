potential game: if a function $\Phi:\mathcal{X}\rightarrow\mathbb{R}$ s.t.

$J_i(x_i,x_{-i})-J_i(y_i,x_{-i})=\Phi(x_i,x_{-i})-\Phi(y_i,x_{-i})$

idea: combine the cost functions, reduce the dimensions;

for potential games: pure NE exists, and best response algorithm converges in a finite number of steps



congestion games: Set of resources $\mathcal{R}$, resources cost $l_{r}(\cdot)$ where $r\in\mathcal{R}$ is a resource, $l_r(\cdot)$ means that different positions in the queue accessing this resource leads to different costs. Set of players $\{1,...,N\}$, player feasible set $x_i\subseteq \mathcal{R}$, player $i$ cost $J_i(x)=\sum_{r\in x_i}l_r(|x|_r)$, $|x|_r$ how many players select this resource

proof: CG are potential: easy to prove

how quick is the convergence: special cases(singleton CG, every player can only choose one resource, convergent in O(n^2m) with n players and m resources) quick; bad cases slow

proof of O(n^2m) singleton CG convergence: sort all $l_{r,k}$ values(all n\*m values) and reconstruct them to 1~n\*m(maybe lower than n\*m since some values may occur multiple times), then $\Phi\leq n^2m$(how to prove this?) also we need to prove that the new game is equivalent to the original one to some extent(a single better step in the new game also means that it is better in the original game)

