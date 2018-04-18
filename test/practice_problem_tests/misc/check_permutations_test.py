import unittest
from check_permutations import *

class CheckPermutationsTest(unittest.TestCase):
    def test_find_true_permutation(self):
        string = "abcd"
        permutation = "dcba"
        self.assertTrue(
            check_permutations(string, permutation)
        )

    def test_find_true_permutation_w_repeats(self):
        string = "abcdd"
        permutation = "dcbda"
        self.assertTrue(
            check_permutations(string, permutation)
        )

    def test_find_false_permutation(self):
        string = "abcd"
        permutation = "cba"
        self.assertFalse(
            check_permutations(string, permutation)
        )

    def test_find_false_permutation_w_repeats(self):
        string = "abcdd"
        permutation = "dcba"
        self.assertFalse(
            check_permutations(string, permutation)
        )

    def test_find_false_perm_w_less_in_first_str(self):
        string = "abc"
        permutation = "dba"
        self.assertFalse(
            check_permutations(string, permutation)
        )

    def test_find_false_perm_w_case_sensitivity(self):
        string = "God"
        permutation = "dog"
        self.assertFalse(
            check_permutations(string, permutation)
        )

    def test_find_false_perm_w_white_space(self):
        string = "god"
        permutation = "   dog"
        self.assertFalse(
            check_permutations(string, permutation)
        )


if __name__ == "__main__":
    unittest.main()
