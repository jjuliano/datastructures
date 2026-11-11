"""
Disjoint set.
Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""

from dataclasses import dataclass


# Easy: union_find.easy, array parent(1:3). Each Node carries its
# own parent cell. rank belongs to the weighting rule for union.
@dataclass
class Node:
    data: int
    rank: int = 0
    parent: Node | None = None


# Easy MAIN: parent(1) <- 1, and the same for 2 and 3.
def make_set(x: Node) -> None:
    """
    Make x as a set.

    >>> node = Node(1)
    >>> make_set(node)
    >>> node.parent == node
    True
    >>> node.rank
    0
    >>> node.data
    1
    """
    # rank is the distance from x to its' parent
    # root's rank is 0
    x.rank = 0
    # Easy MAIN: parent(x) <- x
    x.parent = x


# Easy: union_find.easy, procedure Unite(parent, a, b).
def union_set(x: Node, y: Node) -> None:
    """
    Union of two sets.
    set with bigger rank should be parent, so that the
    disjoint set tree will be more flat.

    >>> node1 = Node(1)
    >>> node2 = Node(2)
    >>> make_set(node1)
    >>> make_set(node2)
    >>> union_set(node1, node2)
    >>> find_set(node1) == find_set(node2)
    True
    >>> # Test union of already connected nodes
    >>> node3 = Node(3)
    >>> make_set(node3)
    >>> union_set(node1, node3)
    >>> find_set(node1) == find_set(node3)
    True
    >>> find_set(node2) == find_set(node3)
    True
    """
    # Easy Unite: ra <- Find(parent, a); rb <- Find(parent, b)
    x, y = find_set(x), find_set(y)
    # Easy Unite: if ra != rb then ..., so equal roots do nothing
    if x == y:
        return

    # Easy Unite: parent(rb) <- ra. Python makes the root with the
    # larger rank the parent, the weighting rule Easy leaves out.
    elif x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


# Easy: union_find.easy, procedure Find(parent, x).
def find_set(x: Node) -> Node:
    """
    Return the parent of x

    >>> node = Node(1)
    >>> make_set(node)
    >>> find_set(node) == node
    True
    >>> node1 = Node(1)
    >>> node2 = Node(2)
    >>> make_set(node1)
    >>> make_set(node2)
    >>> union_set(node1, node2)
    >>> find_set(node1) == find_set(node2)
    True
    >>> # Test path compression
    >>> node3 = Node(3)
    >>> make_set(node3)
    >>> union_set(node1, node3)
    >>> find_set(node1) == find_set(node3)
    True
    """
    # Easy Find: while parent(x) != x do x <- parent(x)
    # Python recurses, and the assignment flattens the path.
    if x != x.parent:
        x.parent = find_set(x.parent)
    # Easy Find: return(x), the root
    return x.parent


def find_python_set(node: Node) -> set:
    """
    Return a Python Standard Library set that contains i.

    >>> node = Node(1)
    >>> find_python_set(node)
    {0, 1, 2}
    >>> node = Node(4)
    >>> find_python_set(node)
    {3, 4, 5}
    >>> node = Node(6)
    >>> find_python_set(node)
    Traceback (most recent call last):
       ...
    ValueError: 6 is not in ({0, 1, 2}, {3, 4, 5})
    """
    sets = ({0, 1, 2}, {3, 4, 5})
    for s in sets:
        if node.data in s:
            return s
    msg = f"{node.data} is not in {sets}"
    raise ValueError(msg)


def test_disjoint_set() -> None:
    """
    Test the disjoint set operations with a comprehensive example.
    Creates two disjoint sets: {0, 1, 2} and {3, 4, 5}

    >>> test_disjoint_set()
    """
    vertex = [Node(i) for i in range(6)]
    for v in vertex:
        make_set(v)

    union_set(vertex[0], vertex[1])
    union_set(vertex[1], vertex[2])
    union_set(vertex[3], vertex[4])
    union_set(vertex[3], vertex[5])

    for node0 in vertex:
        for node1 in vertex:
            if find_python_set(node0).isdisjoint(find_python_set(node1)):
                assert find_set(node0) != find_set(node1)
            else:
                assert find_set(node0) == find_set(node1)


if __name__ == "__main__":
    test_disjoint_set()
