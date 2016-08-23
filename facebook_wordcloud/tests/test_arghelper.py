import os
import mock
import argparse
from unittest import TestCase

from facebook_wordcloud.arghelper import *

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "messages_sample.htm")

class TestException(Exception):
    pass

class TestArgHelper(TestCase):
    @mock.patch('argparse.ArgumentParser.error')
    def test_isfile(self, argparse_error):
        argparse_error.side_effect = TestException()
        parser = argparse.ArgumentParser()
        self.assertTrue(is_valid_file(parser, TESTDATA_FILENAME))
        self.assertTrue(is_valid_file(parser, __file__))
        self.assertRaises(TestException, is_valid_file, parser, "not a file")
        self.assertRaises(TestException, is_valid_file, parser, ";) ;) ;) ;)")
