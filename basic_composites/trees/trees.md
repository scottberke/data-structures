# Trees
## Description
A tree data structure simulates the structure or hierarchy of a tree. Trees contain a topmost node thats called a **root** along with subelements that are called **children**. Children nodes have **parent** nodes that are above them in the tree. When you reach a child node without additional children nodes, the node would be referred to as a **leaf**. When a group of nodes has the same parent, they are called **siblings**.

Trees can be defined recursively where each node is comprised of a value and a list of references to other nodes. Nodes contain references to their children but not their parents.

Trees are often used when data fits into a natural hierarchy. An example of this might be a file system or directory structure. Trees often make information easy to search when they are ordered.

### Types Of Trees
- [Binary Tree](#binary-trees)
- [Binary Search Tree](#binary-search-trees)
- [Binary Heap](#binary-heap)

### Additional Terms Related To Trees
- Branch: Node with at least one child
- Edge: Connection between two nodes
- Path: A sequence of nodes and edges connecting nodes to descendants
- Tree Height: How many levels up to the root node
- Depth: Number of edges from root to the node in question
- Height: Number of edges between the root and the leafs

## Implementation
- [Binary Tree - Python](./tree.py)
- [Binary Tree Test Cases - Python](./tree_test.py)
- [Binary Search Tree - Python](./binary_search_tree.py)
- [Binary Search Tree Test Cases - Python](./binary_search_tree_test.py)
- [Binary Min Heap](./binary_min_heap.py)
- [Binary Min Heap Test Cases](./binary_min_heap.py)

### Binary Trees
Binary Trees allow for each node to have up to two children.
#### Subtypes
- Full Binary Tree: Every node has 0 or 2 children
- Complete Binary Tree: Every level is totally filled. Last level and furthest right can be empty as an exception
- Perfect Binary Tree: Every node has two children and all leaves are the same level
- Balanced Binary Tree: A tree with the minimum possible depth for the leaf nodes

#### Tree Traversal
- [Traversal - Python](./binary_tree_traversal.py)
- [Traversal Test Cases - Python](./binary_tree_traversal_test.py)

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


### Binary Search Trees
A Binary Search Tree is a ordered or sorted binary tree. These trees enable fast lookup and binary search. Typically, binary search trees will be sorted such that subtrees left of the root node are nodes with values less than the root and subtrees right of the root node are greater in value than the root node.

Search and insertion into a BST is O(h) where h is the height of the BST.

### Binary Heap
A Binary Heap is a specific type of Binary Tree that is not sorted however, it does conform to a particular order. Binary heaps are complete in that all levels, except for the last level, are full. They can either be **min heaps** or **max heaps**. A min heap has the lowest value in the tree at the root while the max heap has the largest possible value at the root of the tree. A heap is commonly implemented as an array.

A heap is an efficient example of a priority queue. Heaps are used in Dijkstra's algorithm.

Items are inserted into a binary heap by adding them to the next open spot in the tree and then 'bubbling up' to the correct position depending on whether the heap is a min or max heap. The element moves upward, swapping with parent nodes that are in violation of the heap property.

Removing from binary heaps usually takes place at the root since thats typically the node of interest or highest/smallest priority. Removing the root is called polling. To perform polling, we take the root node and swap with the last element in the tree. After the swap, we 'bubble down' by swapping the new root with the next smallest value of the children. When the children nodes are equal, we default to the left node.

Removing a non-root node requires we first find the non-root node. We then swap the found non-root node with the last element in the tree, then remove the last node. We then 'bubble up' to place the swapped node belongs.


### Red Black Trees
TODO

### AVL Trees
TODO
