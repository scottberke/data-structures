import unittest

from reverse_message_string import *

class ReverseMessageStringsTest(unittest.TestCase):
    def test_reverse_message_string_simple(self):
        message = ['t', 'a', 'c', 'o', 's']
        self.assertEqual(
            reverse_message(message),
            'tacos'
        )

    def test_reverse_message_string_complex(self):
        message = ['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l']
        self.assertEqual(
            reverse_message(message),
            'steal pound cake'
        )

if __name__ == "__main__":
    unittest.main()
