import facebook_wordcloud
from message_parser import *

import os

def main():
    print "Alpha Development"

    TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "tests/messages_sample.htm")
    with open(TESTDATA_FILENAME, 'r') as f:
        testdata = f.read()

    parser = MessageParser(testdata)

    parser.parse_thread("Foo Bar")
