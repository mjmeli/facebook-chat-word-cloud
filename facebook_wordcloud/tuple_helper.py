"""
    tuple_helper
    Provides helper functions for manipulating tuples.
"""
import operator

# Get the n largest tuples from a list of tuples based on the kth value of the
# tuple, 0-indexed.
def get_nlargest_tuples(tuples, n, k):
    # Sort the list of tuples
    tuples.sort(key=operator.itemgetter(k), reverse=True)

    # Get the first n values. If n is larger than the length of the list, just
    # return the list.
    if n > len(tuples):
        return tuples
    else:
        return tuples[:n]
