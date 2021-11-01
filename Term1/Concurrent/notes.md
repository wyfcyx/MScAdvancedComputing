## syntax

$u,v,...$ are identifiers, $a,b,c,...$ are names, $x,y,z,...$ are variables, $P,Q,...$ are processes

$P,Q::=0$, nil processes

$P,Q::=P|Q$, parallel composition of $P$ and $Q$

$P,Q::=(\nu\ a)P$, generation of $a$ with scope $P$, where $a$ is a *local variable* defined in the righthand side scope

$P,Q::=!P$, replication or infinite parallel composition of $P$, which is $P|P|P|...$

$P,Q::=\bar{u}\langle v\rangle$, output of $v$ on channel $v$

$P,Q:=u(x).P$, input of *distinct* variables $x$ on $u$, with continuation $P$

## free variables and free names

$f_v(x)=\{x\},f_n(x)=\empty$

$f_v(a)=\empty,f_n(a)=\{a\}$

$f_v(0)=f_n(0)=\empty$

$f_v(P|Q)=f_v(P)\cup f_v(Q),f_n(P|Q)=f_n(P)\cup f_n(Q)$

$f_v((\nu\ a)P)=f_v(P),f_n((\nu\ a)P)=f_n(P)\backslash\{a\}$

$f_v(!P)=f_v(P),f_n(!P)=f_n(P)$

$f_v(\bar{u}\langle v\rangle)=f_v(u)\cup f_v(v),f_n(\bar{u}\langle v\rangle)=f_n(u)\cup f_n(v)$

$f_v(u(x).P)=f_v(u)\cup(f_v(P)\backslash\{x\}),f_n(u(x).P)=f_n(u)\cup f_n(P)$

$(\nu\ -)$ and $u(-)$ are called **binders**.

If no free variables, closed; open otherwise.

binding occurrences(in the binders) & bounds

## $\alpha$-conversion

renaming the bound names or variable consistently without any name clashes.

If $P$ is obtained from $Q$ by $\alpha$-conversion, we say that $P$ and $Q$ are $\alpha$-equivalent, or $P=_{\alpha}Q$

## substitution

$P\{a/x\}$ replaces all $x$ in $P$ with $a$.

## structural congruence(1)

$P\equiv Q$ means that $P$ and $Q$ are structurally congruent, intuitively means that $P$ and $Q$ are completely interchangeable

Structural congruence contains $\alpha$-conversion.

$P\equiv P$ (Eq Reflexivity)

$P\equiv Q\Rightarrow Q\equiv P$ (Eq Symmetry)

$P\equiv R\ \and R\equiv Q\Rightarrow P\equiv Q$ (Eq Transitivity)

$P\equiv Q\Rightarrow P|R\equiv Q|R$ (Cong Par)

$P\equiv Q\Rightarrow(\nu\ a)P\equiv(\nu\ a)Q$(Cong Res)

$P\equiv Q\Rightarrow u(x).P\equiv u(x).Q$(Cong In)

$P\equiv Q\Rightarrow !P\equiv!Q$(Cong Rep)

$P=_{\alpha}Q\Rightarrow P\equiv Q$($\alpha$-equivalence)

## structural congruence(2)

$P|(Q|Q')\equiv (P|Q)|Q'$(Associativity)

$P|Q\equiv Q|P$(Commutativity)

$P|0\equiv P$(Zero)

$!P\equiv P|!P$(Rep)

## structural congruence(3)

$(\nu\ a)0\equiv 0$ (Res Nil)

$(\nu\ a)(\nu\ b)P\equiv (\nu\ b)(\nu\ a)P$ (Res Res)

$P|(\nu\ a)Q\equiv (\nu\ a)(P|Q)$ if $a\notin f_n(P)$ (Res Par)

## reduction relation

$\bar{a}\langle b\rangle|a(x).P\rightarrow P\{b/x\}$ (Comm)

$P\rightarrow P'\Leftrightarrow P|Q\rightarrow P'|Q$(Par)

$P\rightarrow P'\Leftrightarrow (\nu\ a)P\rightarrow(\nu\ a)P'$(Res)

$P\equiv Q\rightarrow Q\equiv P'\Leftrightarrow P\rightarrow P'$(Struct)

examples:

* communication: switcher $a(x).\bar{x}\langle c\rangle$, $a(x).\bar{x}\langle c\rangle|\bar{a}\langle b\rangle\rightarrow \bar{b}\langle c\rangle$
* scope extrusion: forwarder $a(x).\bar{b}\langle x\rangle$, $(\nu\ b)\bar{a}\langle b\rangle|a(x).\bar{c}\langle x\rangle\rightarrow(\nu\ b)\bar{c}\langle b\rangle$
* identity agent: $!a(x).\bar{a}\langle x\rangle$
* nondeterminism: $\bar{a}\langle d\rangle|\bar{a}\langle b\rangle|a(x).\bar{c}\langle x\rangle\rightarrow\bar{c}\langle d\rangle\text{or}\ \bar{c}\langle b\rangle$

## small agents

* forwarder $FW(a,b)\stackrel{\text{def}}{=}a(z).\bar{b}\langle z\rangle$
* duplicator $D(a,b,c)\stackrel{\text{def}}{=}a(z).(\bar{b}\langle z\rangle|\bar{c}\langle z\rangle)$
* killer $K(a)\stackrel{\text{def}}{=}a(z).0$
* identity receptor $I(a)\stackrel{\text{def}}{=}!FW\langle a,a\rangle$
* equator $EQ(a,b)\stackrel{\text{def}}{=}!FW\langle a,b\rangle|!FW\langle b,a\rangle$
* Omega $\Omega\stackrel{\text{def}}{=}(\nu\ a)(!FW\langle a,a\rangle|\bar{a}\langle a\rangle)$
* new name generator $NN(a)\stackrel{\text{def}}{=}!a(x).(\nu\ b)\bar{x}\langle b\rangle$

## Full $\pi$-calculus

above is async monadic which has limitations including:

* no continuation on the output, $\bar{u}\langle v\rangle.P$ is not supported
* only one value is communicated, $\bar{u}\langle v\rangle$

add continuation on output, then sync communication: $\bar{a}\langle b\rangle.P|a(x).Q\rightarrow P|Q\{b/x\}$

**how can we simulate sync using async?**

basic encoding definition: $[P]=Q$ is a function from $P$(full) to $Q$(async-monadic):

* $[0]=0$
* $[P|Q]=[P]|[Q]$
* $[(\nu\ a)P]=(\nu\ a)[P]$
* $[!P]=![P]$

from sync to async: $[\bar{u}\langle v\rangle.P]=(\nu\ c)(\bar{u}\langle c\rangle|c(y).(\bar{y}\langle v\rangle|[P]))$, where $y\notin f_v(P),c\notin f_n(P)$

$[u(x).P]=u(y).(\nu\ d)(\bar{y}\langle d\rangle|d(x).[P])$, where $y\notin f_v(P),d\notin f_n(P)$

$[P]$ represents the formal notation for the encoding of $P$

example: $[\bar{b}\langle e\rangle.P]|[b(x).Q]$

$\rightarrow (\nu\ c)(\bar{b}\langle c\rangle|c(y).(\bar{y}\langle e\rangle|[P]))|b(y).(\nu\ d)(\bar{y}\langle d\rangle|d(x).[Q])$

$\rightarrow (\nu\ c)(c(y).(\bar{y}\langle e\rangle|[P])|(\nu\ d)(\bar{c}\langle d\rangle|d(x).[Q]))$

$\rightarrow (\nu\ d)(\bar{d}\langle e\rangle|[P]|d(x).[Q])$

$\rightarrow [P]|[Q]\{e/x\}$

**simulation ended!**

Polyadic: $P::=u(x_1,...,x_n).P$ or $P::=\bar{u}\langle x_1,...,x_n\rangle.P$

reduction rule: $\bar{a}\langle c_1,...,c_n\rangle.P|a(x_1,...,x_n).Q\rightarrow P|Q\{\tilde{c}/\tilde{x}\}$

**simulate polyadic using monadic**

wrong: $[u(x_1,...,x_n).P]=u(x_1).u(x_2)...u(x_n).[P]$ because $\tilde{c}$ can be received by different receivers!

using private channel!

$[u(x_1,...,x_n).P]=u(z).z(x_1)...z(x_n).[P]$

$[\bar{u}\langle x_1,...,x_n\rangle.P]=(\nu\ c)(\bar{u}\langle c\rangle.\bar{c}\langle x_1\rangle...\bar{c}\langle x_n\rangle).[P]$



internal nondeterminism $P\oplus Q\stackrel{\text{def}}{=}(\nu\ a)(\bar{a}|a.P|a.Q)$, which can reduce to either $P|(\nu\ a)a.Q$ or $Q|(\nu\ a)a.P$

branching... stop here





---

quick access:

\bar{x}\langle c\rangle









