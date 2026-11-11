"""Insert and height, the Python twin of bst.easy.

Original, written for The Data Structures Notebook. MIT, copyright (c)
2026 Joel Bryan Juliano. See LICENSE-EASY.md.

Height counts nodes on the longest path. A leaf has height 1.

>>> height(grow(1, 2, 3))
3
>>> height(grow(2, 1, 3))
2
"""

from __future__ import annotations

from dataclasses import dataclass


# Easy: bst.easy, node(info, left, right).
@dataclass
class Node:
    info: int
    left: Node | None = None
    right: Node | None = None


# Easy: bst.easy, procedure Insert(root, x).
# Easy writes into the link it was handed. Python returns the subtree,
# and the caller stores it back into that link.
def insert(root: Node | None, x: int) -> Node:
    # Easy Insert: if root = nil then [ call GETNODE(p); info(p) <- x
    # Easy Insert:   left(p) <- nil; right(p) <- nil; root <- p ]
    if root is None:
        return Node(x, None, None)
    # Easy Insert: else if x < info(root) then call Insert(left(root), x)
    if x < root.info:
        root.left = insert(root.left, x)
    # Easy Insert: else call Insert(right(root), x)
    else:
        root.right = insert(root.right, x)
    return root


# Easy: bst.easy, procedure Height(p, lh, rh).
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


# Easy: bst.easy, procedure Grow(root, x, y, z).
def grow(x: int, y: int, z: int) -> Node:
    # Easy Grow: root <- nil
    root = None
    # Easy Grow: call Insert(root, x); Insert(root, y); Insert(root, z)
    root = insert(root, x)
    root = insert(root, y)
    root = insert(root, z)
    return root


# Easy: bst.easy, procedure MAIN.
if __name__ == "__main__":
    # Easy MAIN: call Grow(root, 1, 2, 3); output Height(root, 0, 0)
    print(height(grow(1, 2, 3)))
    # Easy MAIN: call Grow(root, 2, 1, 3); output Height(root, 0, 0)
    print(height(grow(2, 1, 3)))
