# Trees
## Description
A tree data structure simulates the structure or hierarchy of a tree. Trees contain a topmost node thats called a **root** along with subelements that are called **children**. Children nodes have **parent** nodes that are above them in the tree. When you reach a child node without additional children nodes, the node would be referred to as a **leaf**. When a group of nodes has the same parent, they are called **siblings**.

Trees can be defined recursively where each node is comprised of a value and a list of references to other nodes. Nodes contain references to their children but not their parents.

Trees are often used when data fits into a natural hierarchy. An example of this might be a file system or directory structure. Trees often make information easy to search when they are ordered.

### Types Of Trees
- [Binary Tree](#binary-trees)
- [Binary Search Tree](#binary-search-trees)
- [Balanced Binary Search Tree](#balanced-binary-search-tree)
- [Binary Heap](#binary-heap)
- [AVL Tree](#avl-tree)

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
Trees are typically traversed in-order, pre-order or post-order.
In-order traversal hits/touches all left nodes recursively before hitting all right nodes. Pre-order traversal hits/touches a node, hits its left child then its right child. Post-order traversal hits left children, followed by right children before hitting itself. Examples of each are outlined in the code.  
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

### Balanced Binary Search Tree
These trees have the same properties as a binary search tree, however, the difference between the two is that a balanced binary search tree will self balance itself to maintain it's lowest possible height in relation to the number or nodes it contains. This enables optimal speed operations on the tree.

These trees maintain a balanced state by using 'tree rotations'. A tree rotation takes place after an operation leaves a tree in an unbalanced state. Rotations take place in either right or left directions. After a rotation, a balanced tree is the result.


### Binary Heap
A Binary Heap is a specific type of Binary Tree that is not sorted however, it does conform to a particular order. Binary heaps are complete in that all levels, except for the last level, are full. They can either be **min heaps** or **max heaps**. A min heap has the lowest value in the tree at the root while the max heap has the largest possible value at the root of the tree. A heap is commonly implemented as an array.

A heap is an efficient example of a priority queue. Heaps are used in Dijkstra's algorithm.

Items are inserted into a binary heap by adding them to the next open spot in the tree and then 'bubbling up' to the correct position depending on whether the heap is a min or max heap. The element moves upward, swapping with parent nodes that are in violation of the heap property.

Removing from binary heaps usually takes place at the root since thats typically the node of interest or highest/smallest priority. Removing the root is called polling. To perform polling, we take the root node and swap with the last element in the tree. After the swap, we 'bubble down' by swapping the new root with the next smallest value of the children. When the children nodes are equal, we default to the left node.

Removing a non-root node requires we first find the non-root node. We then swap the found non-root node with the last element in the tree, then remove the last node. We then 'bubble up' to place the swapped node belongs.


### Red Black Trees
TODO

### AVL Trees
An AVL tree is a type of balanced binary search tree. A balanced tree is a tree that has the property where the height of a subtree can only be off by at most one. One that property is violated, the tree is rebalanced to adhere to this property.

The result of balancing ensures that all operations on the tree take place at O(log n) time where n is the number of nodes in the tree. Balancing is done by rotating the tree.

A AVL tree has a balance factor which is the height of the right sub-tree minus the height of the left subtree. This balance factor, when having a balanced tree property, will be in [-1, 0, 1].

Various combinations of unbalanced trees can exist. In the 'left left' unbalanced case, the tree has multiple, unbalanced left child nodes resulting in a -2 balance factor. This fixed with a right rotation.

In the 'left right' unbalanced case, the tree has a left child and a right unbalanced child off of that. This also results in a -2 balance factor. Fixing this case requires a left rotation to create the 'left left' case followed by a right rotation to balance the tree.

The right cases mirror the left cases. In a 'right right' case you have two right children and a balance factor of 2. This is fixed with a left rotation.

The 'right left' case has a right child and a left child off of that one. This also has a balance factor of 2 and is fixed with a right rotation followed by a left rotation to balance the tree.

Nodes in AVL trees carry additional information: The value being stored, the balance factor of the node, the height of the node and the left and right children
