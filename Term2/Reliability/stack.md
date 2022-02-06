(optimization-)unstable code: fragment that is only reachable when a input which will trigger UB is given, thus it is eliminate by the compiler since the language standard assume that no UB will happen

c does not insert inherent checks, it believes that programmers will never trigger any UB, it even eliminate some checks from the programmers

well-defined program: $R_e(x)$ is true IFF for an input $x$, code fragment $e$ is reachable; $U_e(x)$ is true IFF for an input $x$, code fragment $e$ triggers UB, assuming C semantics; $\Delta(x)$ means that a program is well-defined on input $x$, that is, $\Delta(x)=\land_{e\in\mathcal{p}}R_e(x)\rightarrow\neg U_e(x)$

---

eliminating unreachable code

code fragment $e$ can be eliminated if $\not\exist x:\Delta(x)\and R_e(x)$

> for a code fragment $e$, if $\exist x:\Delta(x)\and R_e(x)$, then $x$ cannot be eliminated

---

simplifying unnecessary computation

expression $e$ can be simplified with $e'$ if $\exist e'\not\exist x:e(x)\not=e'(x)\and R_e(x)\and \Delta(x)$

simplification: Boolean/algebra oracle

---

STACK inserts UB condition function `bug_on` in order to calculate $\and_{d\in dom(e)}\neg U_d(x)$, it also can be used to find a minimal UB set for understandable bug reporting



