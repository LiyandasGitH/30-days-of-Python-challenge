import unittest 
from reverse import reverse_string


class TestReverseString(unittest.TestCase):
    def test_regular_string(self):
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_empty_string(self):
        self.assertEqual(reverse_string(""),"")

    def test_palidrome(self):
        self.assertEqual(reverse_string("level"), "level")

if __name__ == "__main__":
    unittest.main()