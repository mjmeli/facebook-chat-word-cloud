"""
    arghelper
    Intended to provide some helper functions for parsing arguments.
"""
import os

CONFIGURATION_ARGS = ["font_path", "width", "height", "prefer_horizontal",
                      "mask", "scale", "max_words", "stopwords",
                      "background_color", "max_font_size", "min_font_size",
                      "font_step", "mode", "relative_scaling"]

# Checks whether an argument is a valid file
# Source: http://codereview.stackexchange.com/questions/28608/checking-if-cli-arguments-are-valid-files-directories-in-python
def is_valid_file(parser, arg):
    if not os.path.isfile(arg):
        parser.error('The file {} does not exist!'.format(arg))
    else:
        # File exists so return the filename
        return arg

def generate_argparse(parser):
    # Required
    parser.add_argument("messages_file",
                        help="path to your Facebook generated messages file",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("users",
                        help="command separated string containing the user(s) the desired conversation is with (i.e. \"Foo Bar\" or \"Foo Bar,John Smith\")")

    # Optional
    parser.add_argument("-c", "--config-file",
                        help="path to json formatted configuration file",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-font", "--font-path",
                        help="font path to the font that will be used")
    parser.add_argument("-w", "--width",
                        help="width of the canvas",
                        type=int)
    parser.add_argument("-ht", "--height",
                        help="height of the canvas",
                        type=int)
    parser.add_argument("-ph", "--prefer-horizontal",
                        help="the ratio of times to try horizontal fitting as opposed to vertical",
                        type=float)
    parser.add_argument("-m", "--mask",
                        help="gives a binary mask on where to draw words; ignores width and height",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-s", "--scale",
                        help="scaling between computation and drawing",
                        type=float)
    parser.add_argument("-max", "--max-words",
                        help="the maximum number of words",
                        type=int)
    parser.add_argument("-stop", "--stopwords",
                        help="a string of space separated strings that will be eliminated beyond traditional stopwords",
                        nargs='+')
    parser.add_argument("-bg", "--background-color",
                        help="background color for the image")
    parser.add_argument("-maxf", "--max-font-size",
                        help="maximum font size for the largest word; defaults to height",
                        type=int)
    parser.add_argument("-minf", "--min-font-size",
                        help="smallest font size to use",
                        type=int)
    parser.add_argument("-step", "--font-step",
                        help="step size for the font",
                        type=int)
    parser.add_argument("-mode", "--mode",
                        help="transparent background is generated with RGBA when background-color is null")
    parser.add_argument("-rs", "--relative-scaling",
                        help="importance of relative word frequencies for font size",
                        type=float)

# Load args that were provided into a dictionary
def load_args(args, store):
    args_dict = vars(args)
    for config_arg in CONFIGURATION_ARGS:
        if config_arg == "stopwords" and args_dict["stopwords"] is not None:
            stopwords = "".join(args_dict["stopwords"]).split(" ")
            store["wordcloud_configuration"]["stopwords"] = stopwords
        elif args_dict[config_arg] is not None:
            store["wordcloud_configuration"][config_arg] = args_dict[config_arg]
