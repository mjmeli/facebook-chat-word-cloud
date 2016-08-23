import facebook_wordcloud
from message_parser import *
import word_counter
import tuple_helper
from wordcloud import WordCloud

import os
import sys
import json
import argparse
import arghelper

def main():
    print "Alpha Development"

    # Set up argument parser
    parser = argparse.ArgumentParser()
    arghelper.generate_argparse(parser)
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        print "For more information on word cloud options, see:\n  https://github.com/amueller/word_cloud"
        print "I recommend using a config.json file to set options!"
        sys.exit(0)

    # Parse configuration file if it was provided
    if args.config_file is not None:
        with open(args.config_file, 'r') as f:
            config = json.load(f)
        try:
            config["wordcloud_configuration"]["stopwords"] = [word.strip() for word in config["wordcloud_configuration"]["stopwords"].split(" ")]
        except KeyError:
            pass
    else:
        config = { "wordcloud_configuration": {} }

    # Parse command line arguments into configuration if provided
    arghelper.load_args(args, config)

    print "Loading file..."
    filename = args.messages_file
    with open(filename, 'r') as f:
        messages_file_data = f.read()

    # Parse the HTML (may take a long time)
    print "Building HTML tree..."
    message_parser = MessageParser(messages_file_data)

    # Extract messages from the parsed HTML
    print "Parsing messages..."
    users = [user.strip() for user in args.users.split(",") if len(user.strip()) > 0]
    thread = message_parser.parse_thread(users)
    messages = thread.get_messages_contents()

    # Get top frequencies of each word
    print "Analyzing messages for word frequencies..."
    freq_tuple = word_counter.get_frequencies_tuple(messages)

    # Filter out stop words
    print "Filtering out stop words..."
    try:
        custom_stopwords = config["wordcloud_configuration"]["stopwords"]
        freq_tuple_filtered = word_counter.filter_stopwords(freq_tuple, custom_stopwords)
    except KeyError:
        freq_tuple_filtered = word_counter.filter_stopwords(freq_tuple)

    # Get top 200 of those
    print "Getting top words..."
    freq_top = tuple_helper.get_nlargest_tuples(freq_tuple_filtered, 200, 1)

    # Parameters for word cloud
    # http://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html#wordcloud.WordCloud
    wordcloud_args = config["wordcloud_configuration"]
    wordcloud_args.pop("stopwords", None)

    # Generate the word cloud and show
    wordcloud = WordCloud(**wordcloud_args).generate_from_frequencies(freq_top)
    image = wordcloud.to_image()
    image.show()

    # Output to a file for now
    TEMP_FILENAME = os.path.join(os.path.dirname(__file__), "tmp/cloud.png")
    image.save(TEMP_FILENAME, 'PNG')
