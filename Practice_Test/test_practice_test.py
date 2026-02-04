import unittest
from practice_test import (
    square_number,
    even_or_odd,
    get_highest,
    sum_of_list,
    first_and_last_letter,
    count_letter,
    every_other_letter,
    strict_string
)

class TestFunctions(unittest.TestCase):

    # --------------------
    # Tests for square_number
    # --------------------
    def test_square_number(self):
        self.assertEqual(square_number(3), 9)
        self.assertEqual(square_number(-4), 16)
        self.assertEqual(square_number(0), 0)

    def test_square_number_more(self):
        self.assertEqual(square_number(1), 1)
        self.assertEqual(square_number(-1), 1)
        self.assertEqual(square_number(10), 100)
        self.assertEqual(square_number(999), 998001)

    # --------------------
    # Tests for even_or_odd
    # --------------------
    def test_even_or_odd(self):
        self.assertEqual(even_or_odd(4), "even")
        self.assertEqual(even_or_odd(7), "odd")
        self.assertEqual(even_or_odd(0), "even")

    def test_even_or_odd_more(self):
        self.assertEqual(even_or_odd(-2), "even")
        self.assertEqual(even_or_odd(-3), "odd")
        self.assertEqual(even_or_odd(1000000), "even")

    # --------------------
    # Tests for get_highest
    # --------------------
    def test_get_highest(self):
        self.assertEqual(get_highest([1, 5, 3, 2]), 5)
        self.assertEqual(get_highest([-10, -3, -50]), -3)
        self.assertEqual(get_highest([42]), 42)

    def test_get_highest_more(self):
        self.assertEqual(get_highest([5, 5, 5]), 5)
        self.assertEqual(get_highest([2, 3]), 3)
        self.assertEqual(get_highest([-1]), -1)
        self.assertEqual(get_highest([0, -1, -100]), 0)

    # --------------------
    # Tests for sum_of_list
    # --------------------
    def test_sum_of_list(self):
        self.assertEqual(sum_of_list([1, 2, 3]), 6)
        self.assertEqual(sum_of_list([-1, -1, -1]), -3)
        self.assertEqual(sum_of_list([100]), 100)
        self.assertEqual(sum_of_list([]), 0)


    def test_sum_of_list_more(self):
        self.assertEqual(sum_of_list([0, 0, 0]), 0)
        self.assertEqual(sum_of_list([10, -10, 5]), 5)
        self.assertEqual(sum_of_list([50, 50, 50]), 150)
        self.assertEqual(sum_of_list([-5, 5]), 0)

    # --------------------
    # Tests for first_and_last_letter
    # --------------------
    def test_first_and_last_letter(self):
        self.assertEqual(first_and_last_letter("hello"), "ho")
        self.assertEqual(first_and_last_letter("a"), "aa")
        self.assertEqual(first_and_last_letter("cat"), "ct")

    def test_first_and_last_letter_more(self):
        self.assertEqual(first_and_last_letter("zzzz"), "zz")
        self.assertEqual(first_and_last_letter("hi"), "hi")
        self.assertEqual(first_and_last_letter("python"), "pn")
        self.assertEqual(first_and_last_letter("x"), "xx")

    # --------------------
    # Tests for count_letter
    # --------------------
    def test_count_letter(self):
        self.assertEqual(count_letter("hello", "l"), 2)
        self.assertEqual(count_letter("banana", "a"), 3)
        self.assertEqual(count_letter("test", "z"), 0)

    def test_count_letter_more(self):
        self.assertEqual(count_letter("mississippi", "s"), 4)
        self.assertEqual(count_letter("aaaaaa", "a"), 6)
        self.assertEqual(count_letter("123abc123", "1"), 2)
        self.assertEqual(count_letter("", "a"), 0)

    # --------------------
    # Tests for every_other_letter
    # --------------------
    def test_every_other_letter(self):
        self.assertEqual(every_other_letter("runner"), "unr")
        self.assertEqual(every_other_letter("abcdef"), "bdf")
        self.assertEqual(every_other_letter("x"), "")

    def test_every_other_letter_more(self):
        self.assertEqual(every_other_letter("aaaaaa"), "aaa")
        self.assertEqual(every_other_letter("xy"), "y")
        self.assertEqual(every_other_letter("xyz"), "y")
        self.assertEqual(every_other_letter("python"), "yhn")
        self.assertEqual(every_other_letter(""), "")

    # --------------------
    # Tests for strict_string
    # --------------------
    def test_strict_string(self):
        # Valid case
        self.assertTrue(strict_string("chease"))

        # Too short
        self.assertFalse(strict_string("tree"))

        # Contains digit
        self.assertFalse(strict_string("app1e"))

        # Contains space
        self.assertFalse(strict_string("hello world"))

        # Missing 'a' or 'e'
        self.assertFalse(strict_string("string"))
        self.assertFalse(strict_string("banana"))

        # Starts with vowel
        self.assertFalse(strict_string("applee"))

        # Ends with consonant
        self.assertFalse(strict_string("cheesed"))

        # No repeated letters
        self.assertFalse(strict_string("planeti"))

    def test_strict_string_more(self):
        # Valid examples
        self.assertTrue(strict_string("beatle"))
        self.assertTrue(strict_string("chease"))

        # No repeated letters
        self.assertFalse(strict_string("planeti"))

        # Ends with uppercase vowel → should be false
        self.assertFalse(strict_string("cheesE"))

        # Starts with vowel
        self.assertFalse(strict_string("elephant"))

        # Missing 'a' or 'e'
        self.assertFalse(strict_string("coffee"))
        self.assertFalse(strict_string("banana"))

        # Ends with consonant
        self.assertFalse(strict_string("digger"))

        # Contains digit
        self.assertFalse(strict_string("che3se"))

        # Too short
        self.assertFalse(strict_string("chees"))

        # Contains punctuation
        self.assertFalse(strict_string("chease!"))

if __name__ == "__main__":
    unittest.main()
