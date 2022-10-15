"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from typing import TextIO
from bed import (
    parse_line, print_line
)


def to_tab_separated(line: str) -> str:
    """ Convert a space-separated line to a tab-separated line.
    >>> to_tab_separated('chr1 20100  20101 foo')
    'chr1    20100    20101    foo'
    """
    elements = line.split()
    return '    '.join(elements)


def main() -> None:
    """Run the program.    
    """
    # Create ArgumentParser-object using the argparse module. The 
    # ArgumentParser is used to store and parse the options given to 
    # the program through the command-line. 
    argparser = argparse.ArgumentParser(description="Cleans up a BED file")
    # 'infile' is either provided as an input file name or stdin
    # add_argument() used to tell the ArgumentParser, which options it can 
    # expect and which objects it should create when it receives a given 
    # option.
    argparser.add_argument('infile',                     # The name of the option passed to the program.
                           nargs='?',                    # 0 or 1 arguments
                           type=argparse.FileType('r'),  # file for reading
                           default=sys.stdin)
    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument('outfile',
                           nargs='?',                    # 0 or 1 arguments
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)
    args = argparser.parse_args()


    input = args.infile 
    output = args.outfile
    for line in input.readlines(): 
        print(to_tab_separated(line), file=output)
    return


if __name__ == '__main__':
    main()
