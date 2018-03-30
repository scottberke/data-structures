import unittest
import random
from binary_min_heap import *

class BinaryMinHeapTest(unittest.TestCase):
    # Helpers
    def create_heap(self, num_of_nodes):
        # ex:
        #        0
        #      /   \
        #     1    2
        # => [0, 1, 2]
        random_nodes = random.sample(range(100), num_of_nodes)
        heap = MinHeap()

        for node in random_nodes:
            heap.insert(node)

        return heap

    def check_balanced_heap(self, heap):
        for node_index in range(len(heap)):
            child_index_1 = 2*node_index + 1
            child_index_2 = 2*node_index + 2

            if heap[child_index_1] and heap[node_index] > heap[child_index_1]:
                return False
            if heap[child_index_2] and heap[node_index] > heap[child_index_2]:
                return False
        return True

    # Tests
    def test_create_min_heap(self):
        heap = MinHeap()
        self.assertIsInstance(
            heap,
            MinHeap
        )

    def test_min_heap_peek(self):
        heap = MinHeap()
        root = 1
        other_node = 2
        heap.append(root)
        heap.append(other_node)
        self.assertEqual(
            heap.peek(),
            root
        )

    def test_min_heap_children_indices(self):
         heap = self.create_heap(3)
         node_to_check = 0
         self.assertEqual(
            heap.children(0),
            [ 2*node_to_check + 1, 2*node_to_check + 2 ]
        )

    def test_min_heap_children_leaf_indices(self):
        heap = self.create_heap(3)
        node_to_check = 2
        self.assertEqual(
            heap.children(node_to_check),
            []
        )

    def test_min_heap_children_one_indices(self):
        heap = self.create_heap(2)
        node_to_check = 0

        self.assertEqual(
            heap.children(node_to_check),
            [ (2*node_to_check + 1) ]
        )

    def test_min_heap_insert(self):
        heap = self.create_heap(10)
        heap.insert(random.randint(0,100))
        self.assertTrue(
            self.check_balanced_heap(heap)
        )

    def test_min_heap_insert_larger(self):
        heap = self.create_heap(100)
        heap.insert(random.randint(0,100))
        self.assertTrue(
            self.check_balanced_heap(heap)
        )

    def test_min_heap_poll(self):
        heap = self.create_heap(10)
        root = heap[0]
        polled = heap.poll()

        self.assertTrue(
            root == polled and self.check_balanced_heap(heap)
        )

if __name__ == "__main__":
    unittest.main()
