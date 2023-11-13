# ReasoningSolvers
CSP (Constraint Satisfaction Problem) Solvers in Z3, Or-Tools, and Prolog

# Tools

## Z3
Written in .txt and .py files with z3 imported (https://github.com/Z3Prover/z3).

## OrTools
Written in .py files with ortools imported (https://developers.google.com/optimization/install/).

## Prolog
Written in .pl files with prolog installed, with provided commands to execute (https://www.swi-prolog.org/download/stable).

# Solvers

## General
1. $A \oplus B$
2. $A \lor \neg B$
3. $(A \lor \neg B \lor \neg C) \land B \land C$
4. $((A \supset B) \equiv (A \land B)) \land \neg B$
5. $(x + y < 10) \land (x > 8)$
6. $(x > 1) \land (x \mid 3) \land (x \mid 7)$

## Special

### blocks
* $OnTop(a, b)$
* $OnTop(b, c)$
* $Green(a)$
* $\neg Green(c)$
* $\forall x \forall y . OnTop(x, y) \land Green(x) \land \neg Green(y)$

### barberParadox
* $barber \in People$
* $\forall x \in People \mid \neg Shaves(x, x) \Rightarrow Shaves(barber, x)$
* $\forall x \in People \mid Shaves(barber, x) \Rightarrow \neg Shaves(x, x)$

### houseWindsor
* mother of child: made child
* father of child: made child
* parent of child: either a mother or father of child
* sibling of child: mother and father of child made sibling, sibling not child
* spouse of person: other parent who made child with person
* aunt or uncle of nephew: siblings of parents who made nephew
* cousin of child: children made by siblings of the parents of child
