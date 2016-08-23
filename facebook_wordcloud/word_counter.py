"""
    word_counter
    Provides helper functions for word counts.
"""
import re
from collections import Counter

# Get the occurrences of each word as a dictionary.
# strings = a list of strings, can be strings of any length/number of words
def get_occurrences(strings):
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

# Get the occurrences of each word as a tuple.
# strings = a list of strings, can be strings of any length/number of words
def get_occurrences_tuple(strings):
    return get_occurrences(strings).items()
