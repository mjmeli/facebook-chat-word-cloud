import facebook_wordcloud
from message_parser import *
import word_counter

import os

def main():
    print "Alpha Development"

    print "Loading file..."
    TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "tmp/messages.htm")
    with open(TESTDATA_FILENAME, 'r') as f:
        testdata = f.read()

    # Parse the HTML (may take a long time)
    print "Parsing HTML..."
    parser = MessageParser(testdata)

    # Extract messages from the parsed HTML
    # thread = parser.parse_thread("Foo Bar")
    # messages = thread.get_messages_contents()

    # Get occurrences
    # print word_counter.get_occurrences(messages)
