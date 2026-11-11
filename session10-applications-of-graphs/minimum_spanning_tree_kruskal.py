# Easy: paths.easy, the spanning-tree half of MAIN, with Find.
def kruskal(
    num_nodes: int, edges: list[tuple[int, int, int]]
) -> list[tuple[int, int, int]]:
    """
    >>> kruskal(4, [(0, 1, 3), (1, 2, 5), (2, 3, 1)])
    [(2, 3, 1), (0, 1, 3), (1, 2, 5)]

    >>> kruskal(4, [(0, 1, 3), (1, 2, 5), (2, 3, 1), (0, 2, 1), (0, 3, 2)])
    [(2, 3, 1), (0, 2, 1), (0, 1, 3)]

    >>> kruskal(4, [(0, 1, 3), (1, 2, 5), (2, 3, 1), (0, 2, 1), (0, 3, 2),
    ... (2, 1, 1)])
    [(2, 3, 1), (0, 2, 1), (2, 1, 1)]
    """
    # Easy MAIN: the edges are listed in increasing cost: 1, 2, then 9
    edges = sorted(edges, key=lambda edge: edge[2])

    # Easy MAIN: parent(1) <- 1; parent(2) <- 2; parent(3) <- 3
    parent = list(range(num_nodes))

    # Easy Find: while parent(x) != x do x <- parent(x); return(x).
    # This one recurses and flattens the path on the way back.
    def find_parent(i):
        if i != parent[i]:
            parent[i] = find_parent(parent[i])
        return parent[i]

    # Easy MAIN: total <- 0
    minimum_spanning_tree_cost = 0
    minimum_spanning_tree = []

    # Easy MAIN: one block per edge, in that order
    for edge in edges:
        # Easy MAIN: a <- Find(parent, ...); b <- Find(parent, ...)
        parent_a = find_parent(edge[0])
        parent_b = find_parent(edge[1])
        # Easy MAIN: if a != b then [ parent(b) <- a; total <- total + w ]
        if parent_a != parent_b:
            minimum_spanning_tree_cost += edge[2]
            minimum_spanning_tree.append(edge)
            # Python points a at b. Easy points b at a. Either joins the trees.
            parent[parent_a] = parent_b

    # Easy MAIN: output total. Python returns the kept edges instead.
    return minimum_spanning_tree


if __name__ == "__main__":  # pragma: no cover
    num_nodes, num_edges = list(map(int, input().strip().split()))
    edges = []

    for _ in range(num_edges):
        node1, node2, cost = (int(x) for x in input().strip().split())
        edges.append((node1, node2, cost))

    kruskal(num_nodes, edges)
