import unittest
from hash_table import *
import random

class HashTableTest(unittest.TestCase):
    def test_hash_table_create(self):
        hash_table = HashTable()
        self.assertTrue(
            type(hash_table) == HashTable
        )

    # These two tests are the same. Probably a better test here is needed
    def test_hash_table_set_value(self):
        hash_table = HashTable()
        val = random.randint(0,100)
        hash_table['tacos'] = val
        self.assertEqual(
            hash_table['tacos'],
            val
        )

    def test_hash_table_get_value(self):
        hash_table = HashTable()
        val = random.randint(0,100)
        hash_table['tacos'] = val
        retrieved_val = hash_table['tacos']
        self.assertEqual(
            val,
            retrieved_val
        )



if __name__ == "__main__":
    unittest.main()
