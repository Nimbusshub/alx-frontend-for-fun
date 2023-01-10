#!/usr/bin/python3
import sys
from os.path import exists

"""A markdown to html file
    Args:
        Arg 1: Markdown file
        Arg 2: output file name (HTML)
    """
if __name__ == 'main':

    """Check if number of arguments == 2"""

    if sys.argv != 2:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        exit(1)

    """Check if input file is a correct markdown file"""
    if "." in sys.argv[0]:
        newArr = sys.argv[0].split('.')
        if len(newArr) != 2:
            sys.stderr.write('Bad Markdown file')
            exit(1)
        if newArr[1] != ".md":
            sys.stderr.write('First argument must a markdown file')

    """Check if markdown file exist"""
    if exists(sys.argv[0]) == False:
        sys.stderr.write('Missing {}'.format(sys.argv[0]))
        exit(1)

    exit(0)
