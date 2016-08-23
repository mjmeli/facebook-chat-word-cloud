import facebook_wordcloud
from message_parser import *
import word_counter
import tuple_helper
from wordcloud import WordCloud, ImageColorGenerator

import os
import sys
import json
import copy
import argparse
import arghelper
import numpy as np
from PIL import Image

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser()
    arghelper.generate_argparse(parser)
    args = parser.parse_args()

    # Parse configuration file if it was provided
    if args.config_file is not None:
        with open(args.config_file, 'r') as f:
            config = json.load(f)
        try:
            if config["wordcloud_config"]["stopwords"] is not None:
                config["wordcloud_config"]["stopwords"] = [word.strip() for word in config["wordcloud_config"]["stopwords"].split(" ")]
        except KeyError:
            pass
    else:
        config = { "wordcloud_config": {} }

    # Parse command line arguments into configuration if provided
    arghelper.load_args(args, config)

    print "Loading file..."
    if not args.sample:
        filename = args.messages_file
    else:
        filename = os.path.join(os.path.dirname(__file__), "messages_sample.htm")
        args.users = "Foo Bar"
    with open(filename, 'r') as f:
        messages_file_data = f.read()

    # Parse the HTML and extract messages (may take a long time)
    print "Building HTML tree..."
    message_parser = MessageParser(messages_file_data)
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
        custom_stopwords = config["wordcloud_config"]["stopwords"]
        freq_tuple_filtered = word_counter.filter_stopwords(freq_tuple, custom_stopwords)
    except KeyError:
        freq_tuple_filtered = word_counter.filter_stopwords(freq_tuple)

    # Get top n of those
    print "Getting top words..."
    try:
        if config["wordcloud_config"]["max_words"] > 200:
            max_words = config["wordcloud_config"]["max_words"]
        else:
            max_words = 200
    except:
        max_words = 200
    freq_top = tuple_helper.get_nlargest_tuples(freq_tuple_filtered, max_words, 1)

    # Create a mask if an image was provided for one
    if config["wordcloud_config"]["mask"] is not None:
        print "Generating mask image..."
        if not os.path.isfile(config["wordcloud_config"]["mask"]):
            raise IOError("Couldn't locate mask file...did you make sure to specify the URL relative to where you are running the script?")
        config["wordcloud_config"]["mask"] = np.array(Image.open(config["wordcloud_config"]["mask"]))

    # Generate the word cloud
    wordcloud_args = copy.copy(config["wordcloud_config"])
    wordcloud_args.pop("stopwords", None)
    wordcloud_args.pop("coloring", None)
    wordcloud = WordCloud(**wordcloud_args).generate_from_frequencies(freq_top)

    # If coloring is selected, recolor
    try:
        if config["wordcloud_config"]["coloring"] is True:
            print "Recoloring image..."
            image_colors = ImageColorGenerator(config["wordcloud_config"]["mask"])
            wordcloud.recolor(color_func=image_colors)
    except KeyError:
        pass

    # Show the wordcloud
    image = wordcloud.to_image()
    image.show()

    # If a output file was specified, output to there
    if args.out is not None:
        if args.out.endswith("png"):
            image.save(args.out, 'PNG')
        else:
            image.save(args.out + ".png", 'PNG')
