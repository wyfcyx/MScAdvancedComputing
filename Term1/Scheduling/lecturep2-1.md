multiple decision makers

game theory=analysis/design of multiagent decision making

players $1\leq i\leq N$, actions $x_i\in\mathcal{X}_i$, cost $J_i(x_i,x_{-i})$ which means that actions of players other than player i

Nash Equilibrium; what's the outcome of a game?

Pure NE: no players can reduce their cost only by changing their own action

best response, when $x_{-i}$ is fixed, we can find a best $x_i$ for player i in set $\mathcal{X}_i$

best response algorithm: best response for $i$, and then $i=(i+1)\%N$ until we reaches a NE

mixed NE: randomize decisions, players aim to minimize the expected cost

$C_i(\sigma_1,...,\sigma_N)=\mathbb{E}_{x\sim\sigma}[J_i(x)]$

mixed NE: $(\sigma_1,...,\sigma_N)$ that satisfies that any player i won't reduce their cost if substitute $\sigma_i$ with $x_i\in\mathcal{X}_i$



 

