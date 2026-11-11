#!/usr/bin/python

"""Author: OMKAR PATHAK"""

from __future__ import annotations

from queue import Queue


class Graph:
    def __init__(self) -> None:
        self.vertices: dict[int, list[int]] = {}

    def print_graph(self) -> None:
        """
        prints adjacency list representation of graaph
        >>> g = Graph()
        >>> g.print_graph()
        >>> g.add_edge(0, 1)
        >>> g.print_graph()
        0  :  1
        """
        for i in self.vertices:
            print(i, " : ", " -> ".join([str(j) for j in self.vertices[i]]))

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        """
        adding the edge between two vertices
        >>> g = Graph()
        >>> g.print_graph()
        >>> g.add_edge(0, 1)
        >>> g.print_graph()
        0  :  1
        """
        if from_vertex in self.vertices:
            self.vertices[from_vertex].append(to_vertex)
        else:
            self.vertices[from_vertex] = [to_vertex]

    # Easy: walks.easy (session 9), procedure Breadth. Python keeps the
    # set of visited vertices, not the order(k) list.
    def bfs(self, start_vertex: int) -> set[int]:
        """
        >>> g = Graph()
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(2, 0)
        >>> g.add_edge(2, 3)
        >>> g.add_edge(3, 3)
        >>> sorted(g.bfs(2))
        [0, 1, 2, 3]
        """
        # initialize set for storing already visited vertices
        # Easy Breadth: seen(u) is u in visited
        visited = set()

        # create a first in first out queue to store all the vertices for BFS
        # Easy Breadth: array q(1:5); qh <- 1; qt <- 1
        queue: Queue = Queue()

        # mark the source node as visited and enqueue it
        # Easy Breadth: q(1) <- v; seen(v) <- true
        visited.add(start_vertex)
        queue.put(start_vertex)

        # Easy Breadth: while qh <= qt do
        while not queue.empty():
            # Easy Breadth: here <- q(qh); qh <- qh + 1
            vertex = queue.get()

            # loop through all adjacent vertex and enqueue it if not yet visited
            # Easy Breadth: while i <= deg(here) do u <- adj(here, i)
            for adjacent_vertex in self.vertices[vertex]:
                # Easy Breadth: if seen(u) = false then
                if adjacent_vertex not in visited:
                    # Easy Breadth: qt <- qt + 1; q(qt) <- u
                    queue.put(adjacent_vertex)
                    # Easy Breadth: seen(u) <- true
                    visited.add(adjacent_vertex)
        return visited


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.print_graph()
    # 0  :  1 -> 2
    # 1  :  2
    # 2  :  0 -> 3
    # 3  :  3

    assert sorted(g.bfs(2)) == [0, 1, 2, 3]
