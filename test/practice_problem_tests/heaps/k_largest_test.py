import unittest
from random import shuffle, sample, randint

from practice_problems.heaps.k_largest import *

class KLargestElementsTest(unittest.TestCase):
    def test_k_largest_elements_simple(self):
        arr = [1,2,3,4,5,6,7,8,9,10]
        shuffle(arr)
        k = 3
        largest = k_largest(arr, 3)
        # pdb.set_trace()
        self.assertEqual(
            largest,
            [10,9,8]
        )

    def test_k_largest_elements_empty(self):
        arr = []
        shuffle(arr)
        k = 3

        self.assertEqual(
            k_largest(arr, k),
            []
        )

    def test_k_largest_elements_in_50(self):
        arr = sample(range(100), 50)
        shuffle(arr)
        k = 3

        self.assertEqual(
            k_largest(arr, k),
            sorted(arr, reverse=True)[:k]
        )

    def test_10_largest_elements(self):
        arr = sample(range(100), 50)
        shuffle(arr)
        k = 10

        self.assertEqual(
            k_largest(arr, k),
            sorted(arr, reverse=True)[:k]
        )


    def test_k_largest_elements_random(self):
        arr = sample(range(1000), 500)
        shuffle(arr)
        k = randint(0,100)

        self.assertEqual(
            k_largest(arr, k),
            sorted(arr, reverse=True)[:k]
        )

if __name__ == "__main__":
    unittest.main()
