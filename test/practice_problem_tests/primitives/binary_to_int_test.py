import unittest
import random
from practice_problems.primitives.binary_to_int import *

class BinaryToIntTest(unittest.TestCase):
    def test_binary_to_int_1(self):
        integer = 1
        binary = '1'
        self.assertEqual(
            binary_to_int(binary),
            integer
        )

    def test_binary_to_int_2(self):
        integer = 2
        binary = '10'
        self.assertEqual(
            binary_to_int(binary),
            integer
        )

    def test_binary_to_int_3(self):
        integer = 3
        binary = '11'
        self.assertEqual(
            binary_to_int(binary),
            integer
        )


    def test_binary_to_int_4(self):
        integer = 4
        binary = '100'
        self.assertEqual(
            binary_to_int(binary),
            integer
        )


    def test_binary_to_int_random(self):
        integer = random.randint(0,1000)
        binary = bin(integer)[2:]
        self.assertEqual(
            binary_to_int(binary),
            integer
        )


if __name__ == "__main__":
    unittest.main()
