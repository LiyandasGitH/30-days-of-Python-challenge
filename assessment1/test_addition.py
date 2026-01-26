import unittest
from assessment1.addition import add

class TestAddFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_negative_numbers(self):
        self.assertEqual(add(-4, -6), -10)

    def test_mixed_numbers(self):
        self.assertEqual(add(-2, 7), 5)

if __name__ == "__main__":
    unittest.main()