"""Preorder and height, the Python twin of walks.easy.

Original, written for The Data Structures Notebook. MIT, copyright (c)
2026 Joel Bryan Juliano. See LICENSE-EASY.md.

The sample tree: 1 has children 2 and 3, and 2 has children 4 and 5.
Height counts nodes, so this tree's height is 3.

>>> root = sample_tree()
>>> pre(root)
[1, 2, 4, 5, 3]
>>> height(root)
3
"""

from __future__ import annotations

from dataclasses import dataclass


# Easy: walks.easy, node(info, left, right).
@dataclass
class Node:
    info: int
    left: Node | None = None
    right: Node | None = None


# Easy: walks.easy, procedure Make(x, l, r).
def make(x: int, left: Node | None, right: Node | None) -> Node:
    # Easy Make: call GETNODE(p); info(p) <- x
    # Easy Make: left(p) <- l; right(p) <- r; return(p)
    return Node(x, left, right)


# Easy: walks.easy, procedure Pre(p, order, k).
# The list is order, and its length plays the part of k.
def pre(p: Node | None, order: list[int] | None = None) -> list[int]:
    if order is None:
        order = []
    # Easy Pre: if p = nil then return
    if p is None:
        return order
    # Easy Pre: k <- k + 1; order(k) <- info(p)
    order.append(p.info)
    # Easy Pre: call Pre(left(p), order, k)
    pre(p.left, order)
    # Easy Pre: call Pre(right(p), order, k)
    pre(p.right, order)
    return order


# Easy: walks.easy, procedure Height(p, lh, rh).
def height(p: Node | None) -> int:
    # Easy Height: if p = nil then return(0)
    if p is None:
        return 0
    # Easy Height: lh <- Height(left(p), 0, 0)
    lh = height(p.left)
    # Easy Height: rh <- Height(right(p), 0, 0)
    rh = height(p.right)
    # Easy Height: if lh > rh then return(lh + 1)
    if lh > rh:
        return lh + 1
    # Easy Height: else return(rh + 1)
    return rh + 1


# Easy: walks.easy, the tree built at the top of MAIN.
def sample_tree() -> Node:
    # Easy MAIN: d <- Make(4, nil, nil); e <- Make(5, nil, nil)
    d = make(4, None, None)
    e = make(5, None, None)
    # Easy MAIN: b <- Make(2, d, e); c <- Make(3, nil, nil)
    b = make(2, d, e)
    c = make(3, None, None)
    # Easy MAIN: a <- Make(1, b, c)
    return make(1, b, c)


# Easy: walks.easy, procedure MAIN.
if __name__ == "__main__":
    root = sample_tree()
    # Easy MAIN: call Pre(a, order, k); output order(1) ... order(5)
    print(*pre(root))
    # Easy MAIN: output Height(a, 0, 0)
    print(height(root))
