import unittest
from io import StringIO
from contextlib import *

from linked_list import *

class LinkedListTest(unittest.TestCase):
    # Helpers
    def create_linked_list(*data):
        linked_list = LinkedList()
        for value in data[1:]:
            linked_list.append(value)
        return linked_list

    # Tests
    def test_create_new_linked_list(self):
        linked_list = LinkedList()
        self.assertEqual(
            type(linked_list),
            LinkedList)

    def test_append_to_linked_list(self):
        data = 'tacos'
        linked_list = self.create_linked_list(data)
        self.assertEqual(
            linked_list.head.data,
            data)

    def test_append_mult_to_linked_list(self):
        head_data = 'tacos'
        tail_data = 'burritos'
        linked_list = self.create_linked_list(head_data, tail_data)
        tail = linked_list.head.next

        self.assertEqual(
            tail.data,
            tail_data)

    def test_get_node(self):
        head_data = 'tacos'
        tail_data = 'burritos'
        linked_list = self.create_linked_list(head_data, tail_data)

        node = linked_list.get(head_data)
        self.assertEqual(
            node.data,
            head_data
        )

    def test_delete_node_middle(self):
        head_data = 'tacos'
        mid_data = 'whiskey'
        tail_data = 'burritos'

        linked_list = self.create_linked_list(head_data, mid_data, tail_data)
        linked_list.delete_node(mid_data)

        self.assertEqual(
            linked_list.head.data,
            head_data
        )

        self.assertEqual(
            linked_list.head.next.data,
            tail_data
        )

    def test_delete_node_head(self):
        head_data = 'tacos'
        mid_data = 'whiskey'
        tail_data = 'burritos'

        linked_list = self.create_linked_list(head_data, mid_data, tail_data)
        linked_list.delete_node(head_data)

        self.assertEqual(
            linked_list.head.data,
            mid_data
        )

    def test_get_nonexistent_node(self):
        head_data = 'tacos'
        tail_data = 'burritos'
        linked_list = self.create_linked_list(head_data, tail_data)

        node = linked_list.get('whiskey')
        self.assertEqual(
            node,
            False
        )

    def test_print_linked_list(self):
        head_data = 'tacos'
        tail_data = 'burritos'

        linked_list = self.create_linked_list(head_data, tail_data)
        out = StringIO()
        with redirect_stdout(out):
            linked_list.print_list()
        self.assertEqual(
            out.getvalue(),
            'tacos\nburritos\n')


    def test_insert_after(self):
        head_data = 'tacos'
        tail_data = 'burritos'
        linked_list = self.create_linked_list(head_data, tail_data)
        insert_data = 'tequila'

        linked_list.insert_after(head_data, insert_data)

        self.assertEqual(
            linked_list.head.next.data,
            insert_data)

    def test_linked_list_as_iterable(self):
        head_data = 'tacos'
        tail_data = 'burritos'
        linked_list = self.create_linked_list(head_data, tail_data)

        for node in linked_list.items():
            self.assertTrue(
                node.data in [head_data, tail_data]
            )

if __name__ == '__main__':
    unittest.main()
