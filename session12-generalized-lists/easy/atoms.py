"""Atoms of a pure list, the Python twin of atoms.easy.

Original, written for The Data Structures Notebook. MIT, copyright (c)
2026 Joel Bryan Juliano. See LICENSE-EASY.md.

A list node has tag 1 and two links. An atom has tag 0 and a value.

>>> atoms(cons(atom("oak"), cons(atom("ash"), None)))
oak
ash
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


# Easy: atoms.easy, node(tag, info, head, tail).
@dataclass
class Node:
    tag: int
    info: Any = None
    head: Node | None = None
    tail: Node | None = None


# Easy: atoms.easy, procedure Atom(x).
def atom(x: Any) -> Node:
    # Easy Atom: call GETNODE(p); tag(p) <- 0; info(p) <- x
    # Easy Atom: head(p) <- nil; tail(p) <- nil; return(p)
    return Node(0, x, None, None)


# Easy: atoms.easy, procedure Cons(a, b).
def cons(a: Node | None, b: Node | None) -> Node:
    # Easy Cons: call GETNODE(p); tag(p) <- 1; info(p) <- nil
    # Easy Cons: head(p) <- a; tail(p) <- b; return(p)
    return Node(1, None, a, b)


# Easy: atoms.easy, procedure Atoms(p).
def atoms(p: Node | None) -> None:
    # Easy Atoms: if p = nil then return
    if p is None:
        return
    # Easy Atoms: if tag(p) = 0 then output info(p)
    if p.tag == 0:
        print(p.info)
    # Easy Atoms: else [ call Atoms(head(p)); call Atoms(tail(p)) ]
    else:
        atoms(p.head)
        atoms(p.tail)


# Easy: atoms.easy, procedure MAIN.
if __name__ == "__main__":
    # Easy MAIN: row <- Cons(Atom("oak"), Cons(Atom("ash"), nil))
    row = cons(atom("oak"), cons(atom("ash"), None))
    # Easy MAIN: call Atoms(row)
    atoms(row)
