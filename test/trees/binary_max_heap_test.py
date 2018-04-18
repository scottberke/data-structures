import unittest
import random
from data_structures.basic_composites.trees.binary_max_heap import *

class BinaryMaxHeapTest(unittest.TestCase):
    # Helpers
    def create_heap(self, num_of_nodes):
        # ex:
        #        2
        #      /   \
        #     1    0
        # => [0, 1, 2]
        random_nodes = random.sample(range(100), num_of_nodes)
        heap = MaxHeap()

        for node in random_nodes:
            heap.insert(node)

        return heap

    def check_balanced_heap(self, heap):
        for node_index in range(len(heap)):
            child_index_1 = 2*node_index + 1
            child_index_2 = 2*node_index + 2

            if heap[child_index_1] and heap[node_index] < heap[child_index_1]:
                return False
            if heap[child_index_2] and heap[node_index] < heap[child_index_2]:
                return False
        return True

    # Tests
    def test_create_max_heap(self):
        heap = MaxHeap()
        self.assertIsInstance(
            heap,
            MaxHeap
        )

    def test_max_heap_peek(self):
        heap = MaxHeap()
        root = 2
        other_node = 1
        heap.append(root)
        heap.append(other_node)
        self.assertEqual(
            heap.peek(),
            root
        )

    def test_max_heap_peek_empty(self):
        heap = MaxHeap()
        self.assertEqual(
            heap.peek(),
            None
        )

    def test_max_heap_children_indices(self):
         heap = self.create_heap(3)
         node_to_check = 0
         self.assertEqual(
            heap.children(0),
            [ 2*node_to_check + 1, 2*node_to_check + 2 ]
        )

    def test_max_heap_children_leaf_indices(self):
        heap = self.create_heap(3)
        node_to_check = 2
        self.assertEqual(
            heap.children(node_to_check),
            []
        )

    def test_max_heap_children_one_indices(self):
        heap = self.create_heap(2)
        node_to_check = 0

        self.assertEqual(
            heap.children(node_to_check),
            [ (2*node_to_check + 1) ]
        )

    def test_max_heap_insert(self):
        heap = self.create_heap(10)
        heap.insert(random.randint(0,100))
        self.assertTrue(
            self.check_balanced_heap(heap)
        )

    def test_max_heap_insert_larger(self):
        heap = self.create_heap(100)
        heap.insert(random.randint(0,100))
        self.assertFalse(
            self.check_balanced_heap(heap)
        )

    def test_max_heap_poll(self):
        heap = self.create_heap(10)
        root = heap[0]
        polled = heap.poll()
        self.assertTrue(
            root == polled and self.check_balanced_heap(heap)
        )

    def test_max_heap_size(self):
        size = random.randint(0,100)
        heap = self.create_heap(size)

        self.assertEqual(
            heap.size(),
            size
        )

    def test_max_heap_heapify(self):
        size = random.randint(0,100)
        random_nodes_arr = random.sample(range(100), size)
        heap = MaxHeap()
        heap.heapify(random_nodes_arr)

        self.assertTrue(
            heap.size() == size and self.check_balanced_heap(heap)
        )

    def test_max_heap_heapify_w_existing_heap(self):
        # Create heap with 10 nodes
        heap = self.create_heap(10)
        # Create some random sized nodes array
        size = random.randint(0,100)
        random_nodes_arr = random.sample(range(100), size)
        # Heapify random nodes array
        heap.heapify(random_nodes_arr)
        self.assertTrue(
            heap.size() == 10 + size and self.check_balanced_heap(heap)
        )

    def test_max_heap_find(self):
        size = random.randint(0,100)
        random_nodes_arr = random.sample(range(100), size)

        heap = MaxHeap()
        heap.heapify(random_nodes_arr)

        value_to_find = random_nodes_arr[size//2]
        index_of_values = [ index for index, val in enumerate(heap) if val == value_to_find ]

        self.assertEqual(
            heap.find(value_to_find),
            index_of_values
        )

    def test_max_heap_is_empty_w_empty(self):
        heap = MaxHeap()
        self.assertTrue(
            heap.is_empty()
        )

    def test_max_heap_is_empty_w_not_empty(self):
        heap = self.create_heap(10)
        self.assertFalse(
            heap.is_empty()
        )

if __name__ == "__main__":
    unittest.main()
