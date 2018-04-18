import unittest
from atoi import *
from io import StringIO
from contextlib import *

class AtoiTest(unittest.TestCase):
    def test_atoi(self):
        string = "1234"
        self.assertEqual(
            atoi(string),
            int(string)
        )

    def test_atoi_large_string(self):
        string = "12366456789"
        self.assertEqual(
            atoi(string),
            int(string)
        )

    def test_atoi_negative(self):
        string = "-1234"
        self.assertEqual(
            atoi(string),
            int(string)
        )

    def test_atoi_invalid_input(self):
        string = "123a4"
        with self.assertRaises(AttributeError) as error:
            atoi(string)

        self.assertEqual(
            str(error.exception),
            "Invalid Input: a"
        )

if __name__ == "__main__":
    unittest.main()
