import unittest 
from multiply import multiply 

class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(2, 5), 10)
    
    def test_negative_numbers(self):
        self.assertEqual(multiply(-2, -4), 8)

    def test_mixed_numbers(self):
        self.assertEqual(multiply(-3, 4), -12)
    
if __name__ == "__main__":
    unittest.main()