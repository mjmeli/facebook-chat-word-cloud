from unittest import TestCase

from facebook_wordcloud.tuple_helper import *

class TestTupleHelper(TestCase):
    # Test with n=3 on a list of size 4
    def test_nlargest_smaller(self):
        n_largest = 3
        k_column = 1
        input_tuple = [
            ("apple", 1),
            ("pie", 2),
            ("cake", 4),
            ("bananas", 3)
        ]
        expected_output = [
            ("cake", 4),
            ("bananas", 3),
            ("pie", 2)
        ]
        self.assertEquals(get_nlargest_tuples(input_tuple, n_largest, k_column), expected_output)

    # Test with n=3 on a list of size 3
    def test_nlargest_equal(self):
        n_largest = 3
        k_column = 1
        input_tuple = [
            ("apple", 1),
            ("pie", 2),
            ("cake", 4)
        ]
        expected_output = [
            ("cake", 4),
            ("pie", 2),
            ("apple", 1)
        ]
        self.assertEquals(get_nlargest_tuples(input_tuple, n_largest, k_column), expected_output)

    # Test with n=4 on a list of size 3
    def test_nlargest_larger(self):
        n_largest = 4
        k_column = 1
        input_tuple = [
            ("apple", 1),
            ("pie", 2),
            ("cake", 4)
        ]
        expected_output = [
            ("cake", 4),
            ("pie", 2),
            ("apple", 1)
        ]
        self.assertEquals(get_nlargest_tuples(input_tuple, n_largest, k_column), expected_output)

    # Test with positions flipped
    def test_nlargest_flipped(self):
        n_largest = 3
        k_column = 0
        input_tuple = [
            (1, "apple"),
            (2, "pie"),
            (4, "cake"),
            (3, "bananas")
        ]
        expected_output = [
            (4, "cake"),
            (3, "bananas"),
            (2, "pie")
        ]
        self.assertEquals(get_nlargest_tuples(input_tuple, n_largest, k_column), expected_output)

    # Test with a tuple of width greater than 2
    def test_nlargest_three_columns(self):
        n_largest = 3
        k_column = 2
        input_tuple = [
            ("apple", "pie", 1),
            ("pie", "crust", 2),
            ("cake", "frosting", 4),
            ("bananas", "monkeys", 3)
        ]
        expected_output = [
            ("cake", "frosting", 4),
            ("bananas", "monkeys", 3),
            ("pie", "crust", 2)
        ]
        self.assertEquals(get_nlargest_tuples(input_tuple, n_largest, k_column), expected_output)
