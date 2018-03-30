import unittest
import random
from int_to_binary import *

class IntToBinaryTest(unittest.TestCase):
    def test_in_to_binary_1(self):
        int = 1
        binary = '1'
        self.assertEqual(
            int_to_binary(int),
            binary
        )

    def test_in_to_binary_2(self):
        int = 2
        binary = '10'
        self.assertEqual(
            int_to_binary(int),
            binary
        )

    def test_in_to_binary_3(self):
        int = 3
        binary = '11'
        self.assertEqual(
            int_to_binary(int),
            binary
        )


    def test_in_to_binary_4(self):
        int = 4
        binary = '100'
        self.assertEqual(
            int_to_binary(int),
            binary
        )


    def test_in_to_binary_random(self):
        int = random.randint(0,1000)
        binary = bin(int)[2:]
        self.assertEqual(
            int_to_binary(int),
            binary
        )


if __name__ == "__main__":
    unittest.main()
