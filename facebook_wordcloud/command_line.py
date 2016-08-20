import facebook_wordcloud
from message_parser import *
import word_counter

import os

def main():
    print "Alpha Development"

    print "Loading file..."
    TESTDATA_FILENAME = "/Users/Meli/Downloads/facebook-michaelmeli/html/messages.htm"
    with open(TESTDATA_FILENAME, 'r') as f:
        testdata = f.read()

    # Parse the message thread
    print "Parsing file..."
    parser = MessageParser(testdata)
    thread = parser.parse_thread("Foo Bar")
    messages = thread.get_messages_contents()

    # Get occurrences
    print word_counter.get_occurrences(messages)
