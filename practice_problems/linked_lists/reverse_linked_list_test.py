import unittest
import random
from reverse_linked_list import *


class ReverseLinkedListTest(unittest.TestCase):
    # Helpers
    def create_linked_list_from_arr(self, arr):
        ll = LinkedList()
        for item in arr:
            ll.append(item)
        return ll

    # Tests
    def test_reverse_linked_list_single_element(self):
        arr = ['tacos']
        linked_list = self.create_linked_list_from_arr(arr)
        linked_list = reverse_linked_list(linked_list)
        self.assertEqual(
            linked_list.head.data,
            arr[0]
        )


    def test_reverse_linked_list_two_elements(self):
        arr = ['tacos', 'tequila']
        linked_list = self.create_linked_list_from_arr(arr)
        linked_list = reverse_linked_list(linked_list)
        self.assertEqual(
            linked_list.head.data,
            arr[1]
        )

        self.assertEqual(
            linked_list.head.next.data,
            arr[0]
        )

    def test_reverse_linked_list_multi_elements(self):
        arr = ['tacos', 'tequila', 'whiskey', 'burritos']
        linked_list = self.create_linked_list_from_arr(arr)
        linked_list = reverse_linked_list(linked_list)

        current_node = linked_list.head
        for item in arr[::-1]:
            self.assertEqual(
                current_node.data,
                item
            )
            current_node = current_node.next


    def test_reverse_linked_list_many_elements(self):
        # Random array with 100 elements for the linked list
        arr = random.sample(range(100), 100)
        linked_list = self.create_linked_list_from_arr(arr)
        linked_list = reverse_linked_list(linked_list)
        pdb.set_trace()
        current_node = linked_list.head
        for item in arr[::-1]:
            self.assertEqual(
                current_node.data,
                item
            )
            current_node = current_node.next


if __name__ == "__main__":
    unittest.main()
