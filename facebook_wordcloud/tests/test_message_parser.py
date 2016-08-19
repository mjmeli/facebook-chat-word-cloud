import os
from bs4 import BeautifulSoup
from unittest import TestCase

import facebook_wordcloud

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "messages_sample.htm")

class TestTest(TestCase):
    def setUp(self):
        with open(TESTDATA_FILENAME, 'r') as f:
            self.testdata = f.read()

    def test_testdata(self):
        # Should be a string right now
        self.assertTrue(isinstance(self.testdata, str))

        # Should be able to convert to HTML. If this fails, the test fails.
        soup = BeautifulSoup(self.testdata, "html.parser")

    def test_parser(self):
        self.assertTrue(True)
