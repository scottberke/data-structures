# Graphs
## Description
Graphs are similar to trees in that they contain a set of nodes or vertices. Graphs can either be **directed** or **undirected**. Directed graphs can be thought of as having vertices that are connected by one-way streets while undirected graphs would have two-way streets.

A pair of two vertices `(i, j)` is called an edge. The preceding representation of an edge can be thought of as an edge existing between node `i` and node `j`. The **degree** of a vertex or node is is the number of edges connected to the vertex. A graph is considered **weighted** if edges in the graph have values representing a weight or cost/time between the vertices. A graph is colored when colors are assigned to the vertices in the graph where no adjacent vertices have the same color. A graph can be colored with `d+1` colors where `d` is the max degrees in the graph. So, if `d = 3` that means that at least one node in the graph has 3 edges and will need at least 4 colors (1 for each neighbor plus one for itself) to legally color the graph.

If a path exists between each pair of nodes then the graph would be considered connected. A connected graph means that there are no unreachable nodes in the graph.

A cyclic graph is a graph that has a cycle, meaning that a number of nodes create a chain that can be cycled through. A graph must have at least one cycle to be considered a cyclical graph.

A common representation of a graph is that of an Adjacency Matrix. An adjacency matrix is a 2D array consisting of nodes in the graph and the weights between each node. For example:
```
      0  1  2  3  4     Examples:
  0 [[0, 1, 2, 1, 6],   <- Node 0 has a weight of 6 to reach Node 4
  1  [1, 0, 1, 1, 1],   <- Node 1 has a weight of 1 to reach Node 0
  2  [1, 3, 0, 1, 1],   <- Node 2 has a weight of 3 to reach Node 1
  3  [1, 1, 2, 0, 1],   <- Node 3 has a weight of 2 to reach Node 2
  4  [1, 1, 1, 1, 0]]   <- Node 4 has a weight of 1 to reach Node 3
```

Another common representation of a graph is an Adjacency List. Similar to an adjacency matrix, an adjacency list stores nodes and their adjacent nodes:

```
                  Examples:
  0:  [1, 2, 4]   <- Node 0 is connected to 1, 2 and 4
  1:  [0, 2]      <- Node 1 is connected to 0 and 2
  2:  [1, 3]      <- Node 2 is connected to 1 and 3
  3:  [0, 2]      <- Node 3 is connected to 0 and 2
  4:  [1]         <- Node 4 is connected to 1
```

### Additional Terms Related To Graphs

## Implementation
- [Graph - Python](./graph.py)
- [Graph Test Cases - Python](../../test/graphs/graph_test.py)
- [Adjacency Matrix - Python](./adjacency_matrix_graph.py)
- [Adjacency Matrix Test Cases - Python](../../test/graphs/adjacency_matrix_graph_test.py)

- [Graph - Ruby](./graph.rb)
- [Graph Test Cases - Ruby](../../spec/basic_composites/graphs/graph_spec.rb)
- [Adjacency Matrix - Ruby](./adjacency_matrix_graph.rb)
- [Adjacency Matrix Test Cases - Ruby](../../spec/basic_composites/graphs/adjacency_matrix_graph_spec.rb)

## Practice Problems
- [Route Between Nodes](../../practice_problems/graphs/practice_problems.md#route-between-nodes)
