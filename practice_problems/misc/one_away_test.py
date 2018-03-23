import unittest
from one_away import *

class OneAwayTest(unittest.TestCase):
    def test_one_away_change_char(self):
        string = "pale"
        string_perm = "bale"
        self.assertTrue(
            one_away(string, string_perm)
        )

    def test_one_away_change_two_char(self):
        string = "pale"
        string_perm = "bake"
        self.assertFalse(
            one_away(string, string_perm)
        )

    def test_one_away_add_char(self):
        string = "pale"
        string_perm = "pales"
        self.assertTrue(
            one_away(string, string_perm)
        )


    def test_one_away_add_char_diff_order(self):
        string = "pales"
        string_perm = "pale"
        self.assertTrue(
            one_away(string, string_perm)
        )

    def test_one_away_add_char_diff_location(self):
        string = "pasle"
        string_perm = "pale"
        self.assertTrue(
            one_away(string, string_perm)
        )

    def test_one_away_add_two_char(self):
        string = "pale"
        string_perm = "paless"
        self.assertFalse(
            one_away(string, string_perm)
        )


    def test_one_away_remove_char(self):
        string = "pale"
        string_perm = "ple"
        self.assertTrue(
            one_away(string, string_perm)
        )

    def test_one_away_reomve_two_char(self):
        string = "pale"
        string_perm = "pa"
        self.assertFalse(
            one_away(string, string_perm)
        )


if __name__ == "__main__":
    unittest.main()
