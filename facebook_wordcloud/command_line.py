import facebook_wordcloud
from message_parser import *
import word_counter
import tuple_helper

import os

def main():
    print "Alpha Development"

    print "Loading file..."
    TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "tmp/messages.htm")
    with open(TESTDATA_FILENAME, 'r') as f:
        testdata = f.read()

    # Parse the HTML (may take a long time)
    print "Building HTML tree..."
    parser = MessageParser(testdata)

    # Extract messages from the parsed HTML
    print "Parsing messages..."
    thread = parser.parse_thread("Kylie Geller")
    messages = thread.get_messages_contents()

    # Get top frequencies of each word
    freq_tuple = word_counter.get_occurrences_tuple(messages)

    # Get top 200 of those
    freq_top = tuple_helper.get_nlargest_tuples(freq_tuple, 200, 1)
