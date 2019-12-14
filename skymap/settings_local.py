"""
Define a common command-line interface which is shared between all the scripts.
"""

import argparse


def fetch_command_line_arguments(default_filename=''):
    """
    Read input parameters from the command line

    :return:
        Dictionary of command-line arguments
    """

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--latitude', dest='latitude', type=int, default=52,
                        help="The latitude to create a planisphere for.")
    parser.add_argument('--format', dest='img_format', choices=["pdf", "png", "svg"], default="png",
                        help="The image format to create.")
    parser.add_argument('--output', dest='filename', default=default_filename,
                        help="Filename for output, without a file type suffix.")
    parser.add_argument('--theme', dest='theme', choices=["light", "light"], default="light",
                        help="Color theme to be used in the planisphere.")
    args = parser.parse_args()

    return {
        "latitude": args.latitude,
        "img_format": args.img_format,
        "filename": args.filename,
        "theme": args.theme
    }
