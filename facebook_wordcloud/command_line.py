import facebook_wordcloud
from message_parser import *
import word_counter
import tuple_helper
from wordcloud import WordCloud

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
    thread = parser.parse_thread("Staton Grimes")
    messages = thread.get_messages_contents()

    # Get top frequencies of each word
    print "Analyzing messages for word frequencies..."
    freq_tuple = word_counter.get_frequencies_tuple(messages)

    # Filter out stop words
    print "Filtering out stop words..."
    freq_tuple_filtered = word_counter.filter_stopwords(freq_tuple)

    # Get top 200 of those
    print "Getting top words..."
    freq_top = tuple_helper.get_nlargest_tuples(freq_tuple_filtered, 200, 1)

    # Parameters for word cloud
    # http://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html#wordcloud.WordCloud
    # TODO: Implement these as command line parameters
    wordcloud_args = {}
    wordcloud_args["font_path"] = None
    wordcloud_args["width"] = 400
    wordcloud_args["height"] = 200
    wordcloud_args["ranks_only"] = False
    wordcloud_args["prefer_horizontal"] = 0.90
    wordcloud_args["mask"] = None
    wordcloud_args["scale"] = 1.0
    wordcloud_args["max_words"] = 200
    wordcloud_args["stopwords"] = None
    wordcloud_args["background_color"] = "black"
    wordcloud_args["max_font_size"] = None
    wordcloud_args["min_font_size"] = 4
    wordcloud_args["font_step"] = 1
    wordcloud_args["mode"] = "RGB"
    wordcloud_args["relative_scaling"] = 0.5

    # Generate the word cloud and show
    wordcloud = WordCloud(**wordcloud_args).generate_from_frequencies(freq_top)
    image = wordcloud.to_image()
    image.show()

    # Output to a file for now
    TEMP_FILENAME = os.path.join(os.path.dirname(__file__), "tmp/cloud.png")
    image.save(TEMP_FILENAME, 'PNG')
