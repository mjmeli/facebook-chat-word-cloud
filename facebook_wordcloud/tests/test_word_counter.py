from unittest import TestCase

from facebook_wordcloud.word_counter import *

class TestWordCounter(TestCase):
    # Test individual strings
    def test_individual_strings(self):
        test_strings = ["apple", "pie", "bananas", "cake"]
        expected_counts = {
            "apple": 1,
            "pie": 1,
            "bananas": 1,
            "cake": 1
        }
        self.assertEquals(get_occurrences(test_strings), expected_counts)

    # Test duplicate individual strings
    def test_duplicate_individual_strings(self):
        test_strings = ["apple", "pie", "apple", "bananas", "cake", "pie", "pie"]
        expected_counts = {
            "apple": 2,
            "pie": 3,
            "bananas": 1,
            "cake": 1
        }
        self.assertEquals(get_occurrences(test_strings), expected_counts)

    # Test not sending in a list
    def test_nonlist_individual_string(self):
        test_strings = "apple"
        expected_counts = {
            "apple": 1
        }
        self.assertEquals(get_occurrences(test_strings), expected_counts)

    # Test not sending in a list, but sending in multiple strings
    def test_nonlist_multiple_strings(self):
        test_strings = "apple pie bananas cake"
        expected_counts = {
            "apple": 1,
            "pie": 1,
            "bananas": 1,
            "cake": 1
        }
        self.assertEquals(get_occurrences(test_strings), expected_counts)

    # Test sending in sentences with duplicate words
    def test_duplicate_multiple_strings(self):
        test_strings = ["apple", "pie is good", "apple pie is good", "bananas pie"]
        expected_counts = {
            "apple": 2,
            "pie": 3,
            "bananas": 1,
            "is": 2,
            "good": 2
        }
        self.assertEquals(get_occurrences(test_strings), expected_counts)

    # Test punctuated strings appearing as one word
    def test_punctuated_string(self):
        test_strings = ["apple-pie", "I've"]
        expected_counts = {
            "apple-pie": 1,
            "i've": 1
        }
        self.assertEquals(get_occurrences(test_strings), expected_counts)

    # Test mixed case strings
    def test_mixed_case_strings(self):
        test_strings = ["apple", "APPLE", "aPPle", "CAKE"]
        expected_counts = {
            "apple": 3,
            "cake": 1
        }
        self.assertEquals(get_occurrences(test_strings), expected_counts)
