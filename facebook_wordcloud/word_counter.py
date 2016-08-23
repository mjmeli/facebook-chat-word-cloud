"""
    word_counter
    Provides helper functions for word counts.
"""
import os
import re
from collections import Counter

STOPWORDS_FILE = os.path.join(os.path.dirname(__file__), "STOPWORDS")

# Get the frequencies of each word as a dictionary.
# strings = a list of strings, can be strings of any length/number of words
def get_frequencies(strings):
    # Ensure users array is a list
    if type(strings) is not list:
        strings = [strings]

    # Use a Counter to do this easily
    counts = Counter()

    # Use a regular expression to easily remove punctuation
    words = re.compile(r'[\w\'-]+')

    # Split each string/sentence into individual words, make them all lowercase,
    # then add them to the counter
    for sentence in strings:
        counts.update(words.findall(sentence.lower()))

    return dict(counts)

# Get the frequencies of each word as a tuple.
# strings = a list of strings, can be strings of any length/number of words
def get_frequencies_tuple(strings):
    return get_frequencies(strings).items()

# Load stopwords from file, if it exists
def load_stopwords():
    if os.path.isfile(STOPWORDS_FILE):
        return set([x.strip() for x in open(STOPWORDS_FILE).read().split('\n')])
    else:
        return set()


# Filter out stopworks from a frequencies dict or tuple
def filter_stopwords(frequencies, additional_stopwords=None):
    # Convert to tuples for easy of development if dictionary
    is_dict = False
    if type(frequencies) is dict:
        is_dict = True
        frequencies = frequencies.items()

    # Load stopwords from file
    stopwords = load_stopwords()

    # Add in additional stopwords
    if additional_stopwords is not None:
        for word in additional_stopwords:
            stopwords.add(word)

    # Filter out words that are stopwords
    filtered = []
    for word in frequencies:
        if not word[0] in stopwords:
            filtered.append(word)

    # Convert back to original form
    if is_dict:
        return dict(filtered)
    else:
        return filtered
