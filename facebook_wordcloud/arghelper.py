"""
    arghelper
    Intended to provide some helper functions for parsing arguments.
"""
import os

# Checks whether an argument is a valid file
# Source: http://codereview.stackexchange.com/questions/28608/checking-if-cli-arguments-are-valid-files-directories-in-python
def is_valid_file(parser, arg):
    if not os.path.isfile(arg):
        parser.error('The file {} does not exist!'.format(arg))
    else:
        # File exists so return the filename
        return arg
