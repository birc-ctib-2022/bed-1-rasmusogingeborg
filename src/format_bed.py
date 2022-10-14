"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from typing import TextIO
from bed import (
    parse_line, print_line
)


def default(input):
    """Read lines from input, and prints tab-separated lines to stdout.
    >>> default(open('data/test_input.bed')) 
    chr1    20100    20101    foo
    chr3    0    1    bar
    """ 
    for line in input.readlines():
        elements = line.split()
        new_line = '    '.join(elements)
        print(new_line)

def convert_from_files(inp, outp='<stdout>'):
    """
    >>> convert_from_files(open('data/test_input.bed', 'r'))
    chr1    20100    20101    foo
    chr3    0    1    bar
    >>> convert_from_files(open('data/test_input.bed', 'r'), open('data/test_output.bed', 'w'))
    open(data/test_output.bed, 'w') # Virker ikke, men funktionen returnerer jo
    # også None. 
    """
    if outp == '<stdout>':
        for line in inp.readlines(): # f.readlines is a list of strings.
            elements = line.split()
            new_line = '    '.join(elements)
            print(new_line)
    else: 
        for line in inp.readlines():
            elements = line.split()
            new_line = '    '.join(elements)
            print(new_line, file=outp)

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


    if args.infile.name != '<stdin>' and args.outfile.name != '<stdout>':
        input = open(args.infile.name, 'r')
        output = open(args.outfile.name, 'w')
        for line in input.readlines(): # f.readlines is a list of strings.
            elements = line.split()
            new_line = '    '.join(elements)
            print(new_line, file=output)
        return

    if args.infile.name != '<stdin>': # and args.outfile.name == <stdout>. 
        input = open(args.infile.name, 'r')
        for line in input.readlines():
            elements = line.split()
            new_line = '    '.join(elements)
            print(new_line)
        return

    default(sys.stdin)
    return


if __name__ == '__main__':
    main()
