# Trees
## Description
A tree data structure simulates the structure or hierarchy of a tree. Trees contain a topmost node thats called a **root** along with subelements that are called **children**. Children nodes have **parent** nodes that are above them in the tree. When you reach a child node without additional children nodes, the node would be referred to as a **leaf**. When a group of nodes has the same parent, they are called **siblings**.

Trees can be defined recursively where each node is comprised of a value and a list of references to other nodes. Nodes contain references to their children but not their parents.

Trees are often used when data fits into a natural hierarchy. An example of this might be a file system or directory structure. Trees often make information easy to search when they are ordered.

Trees come in a variety of flavors:
- Binary Trees: A tree where each node has up to two children
- Binary Search Trees: A binary tree where every nodes is specifically ordered
- Balanced Trees: A tree where left and right subtrees differ in heigh by at most one

### Additional Terms Related To Trees
- Branch: Node with at least one child
- Edge: Connection between two nodes
- Path: A sequence of nodes and edges connecting nodes to descendants
- Tree Height: How many levels up to the root node
- Depth: Number of edges from root to the node in question

## Implementation
[Binary Tree - Python](./tree.py)
[Binary Tree Test Cases - Python](./tree_test.py)

## Types of Trees
### Binary Trees
Binary Trees allow for each node to have up to two children.
#### Subtypes
- Full Binary Tree: Every node has 0 or 2 children
- Complete Binary Tree: Every level is totally filled. Last level and furthest right can be empty as an exception
- Perfect Binary Tree: Every node has two children and all leaves are the same level
- Balanced Binary Tree: A tree with the minimum possible depth for the leaf nodes

#### Properties
- The maximum number of nodes at the nth level of the tree is **2^(n - 1)**
```
    1  
  /   \
 2     3  

level = 2
(2^level- 1) = 2 <- max nodes at level 2
```
- The maximum number of nodes of a binary tree with height n is **(2^n) - 1**
  ```
      1  
    /   \
   2     3  

  height = 2
  (2^height) - 1 = 3 <- max nodes with a height of 2
  ```
- The minimum height of a binary tree with n nodes is **log(n + 1)**
```
    1  
  /   \
 2     3  

nodes = 3
log(3 + 1 ) =
2^x = 4
x = 2 <- min height is 2 when there's 3 nodes
```
- The minimum height of a binary tree with n leaves is **log(n) + 1**
```
    1  
  /   \
 2     3  

leaves = 2
log(2) + 1  =
2^x = 2
x = 1
1 + 1 = 2 <- min height is 2 when there's 2 leaves
```
