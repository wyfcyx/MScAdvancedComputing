# CW1

## problem 1

### a

$P=(\nu\ c)(\bar{b}\langle c\rangle|b(x).P_1)$

$f_n(P)=f_n(\bar{b}\langle c\rangle|b(x).P_1)\backslash\{c\}$

$=(\{b,c\}\cup\{b\}\cup f_n(P_1))\backslash\{c\}$

$=\{b\}\cup f_n(P_1)\backslash\{c\}$



$f_v(P)=f_v(\bar{b}\langle c\rangle|b(x).P_1)$

$=\empty\cup f_v(b(x).P_1)$

$=\{x\}\cup f_v(P_1)$

### b

$Q=(\nu\ b)(b(x).Q_1|\bar{b}\langle c\rangle|x(y).Q_2)$

$f_n(Q)=fn(b(x).Q_1|\bar{b}\langle c\rangle|x(y).Q_2)\backslash\{b\}$

$=(\{b\}\cup f_n(Q_1)\cup\{b,c\}\cup f_n(Q_2))\backslash\{b\}$

$=\{c\}\cup((f_n(Q_1)\cup f_n(Q_2))\backslash\{b\})$



$f_v(Q)=f_v(b(x).Q_1|\bar{b}\langle c\rangle|x(y).Q_2)$

$=(f_v(Q_1)\backslash\{x\})\cup\empty\cup(\{x\}\cup(f_v(Q_2)\backslash\{y\}))$

$=(f_v(Q_1)\backslash\{x\})\cup(\{x\}\cup(f_v(Q_2)\backslash\{y\}))$

$=f_v(Q_1)\cup(f_v(Q_2)\backslash\{y\})$

### c

$R=(\nu\ a)(!a(x).\bar{c}\langle y\rangle|a(x).R_1|b(y).0)$

$f_n(R)=f_n(!a(x).\bar{c}\langle y\rangle|a(x).R_1|b(y).0)\backslash\{a\}$

$=(\{a,c\}\cup\{a\}\cup f_n(R_1)\cup\{b\})\backslash\{a\}$

$=\{b,c\}\cup(f_n(R_1)\backslash\{a\})$



$f_v(R)=f_v(!a(x).\bar{c}\langle y\rangle|a(x).R_1|b(y).0)$

$=f_v(!a(x).\bar{c}\langle y\rangle)\cup(f_v(R_1)\backslash\{x\})\cup\{y\}$

$=\{y\}\cup(f_v(R_1)\backslash\{x\})\cup\{y\}$

$=(f_v(R_1)\backslash\{x\})\cup\{y\}$

## problem 2

### a

$((\nu\ a,b)(!\bar{b}\langle x\rangle|\bar{b}\langle a\rangle|!(\nu\ c)b(y).P))\{b/x,a/y\}$

$=((\nu\ a,b')(!\bar{b'}\langle x\rangle|\bar{b'}\langle a\rangle|!(\nu\ c)b'(y).P))\{b/x,a/y\}$

$=((\nu\ a,b')(!\bar{b'}\langle b\rangle|\bar{b'}\langle a\rangle|!(\nu\ c)b'(y).P\{b/x\}))\{a/y\}$

$=((\nu\ a,b')(!\bar{b'}\langle b\rangle|\bar{b'}\langle a\rangle|!(\nu\ c)b'(y).P\{b/x\}))$

### b

The substitution is not correct.

$((\nu\ a)(\bar{x}\langle x\rangle|a(x).(\nu\ a)\bar{y}\langle a\rangle))\{a/x,b/y\}$

$=((\nu\ a')(\bar{x}\langle x\rangle|a'(x).(\nu\ a)\bar{y}\langle a\rangle))\{a/x,b/y\}$

$=((\nu\ a')(\bar{a}\langle a\rangle|a'(a).(\nu\ a)\bar{y}\langle a\rangle))\{b/y\}$

$=((\nu\ a')(\bar{a}\langle a\rangle|a'(a).(\nu\ a)\bar{b}\langle a\rangle))$

The righthand side given in the question is $((\nu\ a)(\bar{a}\langle a\rangle|a(a).(\nu\ a)\bar{b}\langle a\rangle))$. It not correct since $a$ clashes.

## problem 3

### a

if $a\notin f_n(P)$, then:

lefthandside $(\nu\ a)Q|P|!(P|(\nu\ a)Q)$

$\equiv (\nu\ a)(P|Q)|!((\nu\ a)(P|Q))$, which is equal to the right hand side.

But $a\notin f_n(P)$ is not given, so they are not structurally congruent.

### b

The left hand side is $(\nu\ a)\bar{c}\langle a\rangle|(!(\bar{a}\langle x\rangle|b(y).0))$

$\equiv (\nu\ a')\bar{c}\langle a'\rangle|(!(\bar{a'}\langle x\rangle|b(y).0))$

$\equiv (\nu\ a')\bar{a}\langle a'\rangle|(!(\bar{a'}\langle x\rangle|b(y).0))$

$\equiv (\nu\ c)\bar{a}\langle c\rangle|(!(\bar{c}\langle x\rangle|b(y).0))$

The right hand side is $\bar{a}\langle c\rangle|(\nu\ c)(!(\bar{c}\langle x\rangle|b(y).0))$

The only difference between them is the position of the restriction. Therefore, they are not structurally congruent.

### c

They are not structurally congruent. On the left hand side, $a$ in $a(x).\bar{a}\langle a\rangle$ is bounded, but on the right hand side, $b$ in  $b(x).\bar{b}\langle b\rangle$ is a free name.

## problem 4

### a

$(\nu\ b)(a(x).\bar{x}\langle b\rangle)|!(\bar{a}\langle b\rangle|b(x).0)$

$\equiv (\nu\ b)(a(x).\bar{x}\langle b\rangle)|(\bar{a}\langle b\rangle|b(x).0)|!(\bar{a}\langle b\rangle|b(x).0)$

$\equiv (\nu\ b)(a(x).\bar{x}\langle b\rangle)|\bar{a}\langle b\rangle|b(x).0|!(\bar{a}\langle b\rangle|b(x).0)$

$\equiv (\nu\ c)(a(x).\bar{x}\langle c\rangle)|\bar{a}\langle b\rangle|b(x).0|!(\bar{a}\langle b\rangle|b(x).0)$

$\rightarrow(\nu\ c)\bar{b}\langle c\rangle|b(x).0|!(\bar{a}\langle b\rangle|b(x).0)$

$\rightarrow 0|!(\bar{a}\langle b\rangle|b(x).0)$

$\equiv !(\bar{a}\langle b\rangle|b(x).0)$

### b

$!a(x).(\bar{b}\langle x\rangle|\bar{c}\langle x\rangle)|!b(y).(\bar{a}\langle y\rangle|c(y).0)|\bar{a}\langle e\rangle$

$\equiv a(x).(\bar{b}\langle x\rangle|\bar{c}\langle x\rangle)|!b(y).(\bar{a}\langle y\rangle|c(y).0)|\bar{a}\langle e\rangle|!a(x).(\bar{b}\langle x\rangle|\bar{c}\langle x\rangle)$

$\rightarrow \bar{b}\langle e\rangle|\bar{c}\langle e\rangle|!b(y).(\bar{a}\langle y\rangle|c(y).0)|!a(x).(\bar{b}\langle x\rangle|\bar{c}\langle x\rangle)$

$\equiv a(x).(\bar{b}\langle x\rangle|\bar{c}\langle x\rangle)|!b(y).(\bar{a}\langle y\rangle|c(y).0)|\bar{a}\langle e\rangle|!a(x).(\bar{b}\langle x\rangle|\bar{c}\langle x\rangle)$

$\equiv \bar{b}\langle e\rangle|\bar{c}\langle e\rangle|b(y).(\bar{a}\langle y\rangle|c(y).0)|!a(x).(\bar{b}\langle x\rangle|\bar{c}\langle x\rangle)|!b(y).(\bar{a}\langle y\rangle|c(y).0)$

$\rightarrow \bar{c}\langle e\rangle|\bar{a}\langle e\rangle|c(e).0|!a(x).(\bar{b}\langle x\rangle|\bar{c}\langle x\rangle)|!b(y).(\bar{a}\langle y\rangle|c(y).0)$

$\equiv !a(x).(\bar{b}\langle x\rangle|\bar{c}\langle x\rangle)|!b(y).(\bar{a}\langle y\rangle|c(y).0)|\bar{a}\langle e\rangle$

### c

$\bar{a}\langle a,b,c\rangle|!a(x,y,z).\bar{y}\langle x,z,y\rangle|!b(x,z,y).\bar{x}\langle x,z,y\rangle$

$\rightarrow \bar{b}\langle a,c,b\rangle|!b(x,z,y).\bar{x}\langle x,z,y\rangle|!a(x,y,z).\bar{y}\langle x,z,y\rangle$

$\rightarrow \bar{a}\langle a,c,b\rangle|!a(x,y,z).\bar{y}\langle x,z,y\rangle|!b(x,z,y).\bar{x}\langle x,z,y\rangle$

### d

$\bar{a}\langle c\rangle|\bar{a}\langle d\rangle|\bar{a}\langle e\rangle|\bar{a}\langle f\rangle|!a(x).(\nu\ b)\bar{x}\langle b\rangle$

$\equiv \bar{a}\langle c\rangle|\bar{a}\langle d\rangle|\bar{a}\langle e\rangle|\bar{a}\langle f\rangle|a(x).(\nu\ b)\bar{x}\langle b\rangle|!a(x).(\nu\ b)\bar{x}\langle b\rangle$

$\rightarrow (\nu\ b)\bar{c}\langle b\rangle|\bar{a}\langle d\rangle|\bar{a}\langle e\rangle|\bar{a}\langle f\rangle|!a(x).(\nu\ b)\bar{x}\langle b\rangle$

$\rightarrow (\nu\ b)\bar{c}\langle b\rangle|(\nu\ b)\bar{d}\langle b\rangle|\bar{a}\langle e\rangle|\bar{a}\langle f\rangle|!a(x).(\nu\ b)\bar{x}\langle b\rangle$

$\rightarrow (\nu\ b)\bar{c}\langle b\rangle|(\nu\ b)\bar{d}\langle b\rangle|(\nu\ b)\bar{e}\langle b\rangle|\bar{a}\langle f\rangle|!a(x).(\nu\ b)\bar{x}\langle b\rangle$

$\rightarrow (\nu\ b)\bar{c}\langle b\rangle|(\nu\ b)\bar{d}\langle b\rangle|(\nu\ b)\bar{e}\langle b\rangle|(\nu\ b)\bar{f}\langle b\rangle|!a(x).(\nu\ b)\bar{x}\langle b\rangle$

$\equiv (\nu\ b)\bar{c}\langle b\rangle|(\nu\ b)\bar{d}\langle b\rangle|(\nu\ b)\bar{e}\langle b\rangle|(\nu\ b)\bar{f}\langle b\rangle|\text{NN}(a)$

