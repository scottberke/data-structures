import pdb
import unittest

import sys
sys.path.append('../../basic_composites/linked_lists')
from remove_dups import *
from linked_list import *

class RemoveDupsTest(unittest.TestCase):
    # Helpers
    def create_linked_list(*data):
        linked_list = LinkedList()
        if type(data[1]) is list:
            for value in data[1]:
                linked_list.append(value)
        else:
            for value in data[1:]:
                linked_list.append(value)
        return linked_list

    # Tests
    def test_remove_dups_when_there_are_none(self):
        node_data = "tacos cheese burrito tequila picante".split()
        linked_list = self.create_linked_list(node_data)

        dedupped = remove_dups(linked_list)

        dedupped_data = []
        for item in dedupped.items():
            dedupped_data.append(item.data)

        self.assertEqual(
            dedupped_data, node_data
        )

    def test_remove_dups(self):
        node_data = "tacos cheese burrito tacos tequila cheese picante".split()
        linked_list = self.create_linked_list(node_data)

        dedupped = remove_dups(linked_list)

        expected = "tacos cheese burrito tequila picante".split()
        dedupped_data = []
        for item in dedupped.items():
            dedupped_data.append(item.data)

        self.assertEqual(
            dedupped_data, expected
        )

    def test_remove_dups_at_end(self):
        node_data = "tacos cheese burrito tacos tequila cheese picante picante".split()
        linked_list = self.create_linked_list(node_data)

        dedupped = remove_dups(linked_list)
        
        expected = "tacos cheese burrito tequila picante".split()
        dedupped_data = []
        for item in dedupped.items():
            dedupped_data.append(item.data)

        self.assertEqual(
            dedupped_data, expected
        )


if __name__ == '__main__':
    unittest.main()
