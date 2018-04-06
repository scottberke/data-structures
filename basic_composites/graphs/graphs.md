# Graphs
## Description
Graphs are similar to trees in that they contain a set of nodes or vertices. Graphs can either be **directed** or **undirected**. Directed graphs can be thought of as having vertices that are connected by one-way streets while undirected graphs would have two-way streets.

A pair of two vertices `(i, j)` is called an edge. The preceding edge can be thought of as an edge existing between node `i` and node `j`. The **degree** of a vertex or node is is the number of edges connected to the vertex. A graph is considered **weighted** if edges in the graph have values representing a weight or cost/time between the vertices. A graph is colored when colors are assigned to the vertices in the graph where no adjacent vertices have the same color.

If a path exists between each pair of nodes then the graph would be considered connected. A connected graph means that there are no unreachable nodes in the graph.

A cyclic graph is a graph that has a cycle, meaning that a number of nodes create a chain that can be cycled through. A graph must have at least one cycle to be considered a cyclical graph.

A common representation of a graph is that of an Adjacency Matrix. An adjacency matrix is a 2D array consisting of nodes in the graph and the weights between each node. For example:
```
      0  1  2  3  4
  0 [[0, 1, 2, 1, 6],   <- Node 0 has a weight of 6 to reach Node 4
  1  [1, 0, 1, 1, 1],   <- Node 1 has a weight of 1 to reach Node 0
  2  [1, 3, 0, 1, 1],   <- Node 2 has a weight of 3 to reach Node 1
  3  [1, 1, 2, 0, 1],   <- Node 3 has a weight of 2 to reach Node 2
  4  [1, 1, 1, 1, 0]]   <- Node 4 has a weight of 1 to reach Node 3
```

### Additional Terms Related To Graphs

## Implementation
- [Graph - Python](./graph.py)
- [Graph Test Cases - Python](./graph_test.py)
- [Adjacency Matrix - Python](./adjacency_matrix_graph.py)
- [Adjacency Matrix Test Cases - Python](./adjacency_matrix_graph_test.py)


## Practice Problems
- [Route Between Nodes](../../practice_problems/graphs/practice_problems.md#route-between-nodes)
