import unittest
from kth_to_last import *

class KthToLastTest(unittest.TestCase):
    # Helpers
    def create_linked_list(*data):
        linked_list = LinkedList()
        if type(data[1]) is list:
            for value in data[1]:
                linked_list.append(value)
        return linked_list

    # Tests
    def test_2nd_to_last(self):
        node_data = "tacos cheese burrito tequila picante salsa".split()
        linked_list = self.create_linked_list(node_data)
        kth = find_kth(linked_list, 2)

        self.assertTrue(
            kth == 'picante'
        )

    def test_last_node(self):
        node_data = "tacos cheese burrito tequila picante salsa".split()
        linked_list = self.create_linked_list(node_data)
        kth = find_kth(linked_list, 1)

        self.assertTrue(
            kth == 'salsa'
        )

if __name__ == "__main__":
    unittest.main()
