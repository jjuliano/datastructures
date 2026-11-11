"""Non recursive implementation of a DFS algorithm."""

from __future__ import annotations


# Easy: walks.easy (session 9), procedure Visit. Easy recurses and
# keeps the visit order in order(k). This version keeps a stack and
# returns the set it reached, so the order is not kept.
def depth_first_search(graph: dict, start: str) -> set[str]:
    """Depth First Search on Graph
    :param graph: directed graph in dictionary format
    :param start: starting vertex as a string
    :returns: the trace of the search
    >>> input_G = { "A": ["B", "C", "D"], "B": ["A", "D", "E"],
    ... "C": ["A", "F"], "D": ["B", "D"], "E": ["B", "F"],
    ... "F": ["C", "E", "G"], "G": ["F"] }
    >>> output_G = list({'A', 'B', 'C', 'D', 'E', 'F', 'G'})
    >>> all(x in output_G for x in list(depth_first_search(input_G, "A")))
    True
    >>> all(x in output_G for x in list(depth_first_search(input_G, "G")))
    True
    """
    # Easy Visit: seen(start) <- true, and a pile of vertices to visit
    explored, stack = set(start), [start]

    # Easy Visit: each pop stands for one recursive call
    while stack:
        v = stack.pop()
        # Easy Visit: seen(v) <- true
        explored.add(v)
        # Differences from BFS:
        # 1) pop last element instead of first one
        # 2) add adjacent elements to stack without exploring them
        # Easy Visit: while step <= deg(v) do nxt <- adj(v, step). Reversed,
        # so the first neighbor comes off the stack first.
        for adj in reversed(graph[v]):
            # Easy Visit: if seen(nxt) = false then call Visit(..., nxt, 0)
            if adj not in explored:
                stack.append(adj)
    # Easy MAIN reads order(1) ... order(5). Python returns the set.
    return explored


G = {
    "A": ["B", "C", "D"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "D"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
}

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(depth_first_search(G, "A"))
