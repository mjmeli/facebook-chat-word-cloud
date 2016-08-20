import facebook_wordcloud
from message_parser import *
import word_counter

import os

def main():
    print "Alpha Development"

    TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "tests/messages_sample.htm")
    with open(TESTDATA_FILENAME, 'r') as f:
        testdata = f.read()

    # Parse the message thread
    parser = MessageParser(testdata)
    thread = parser.parse_thread("Foo Bar")
    messages = [message.contents for message in thread.messages]

    # Get occurrences
    print word_counter.get_occurrences(messages)
