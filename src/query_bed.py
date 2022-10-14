"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from bed import (
    parse_line, parse_line2, print_line
)
from query import Table
# Necessary to import Bedline from Bed?
from bed import BedLine, BedLine2

def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(
        description="Extract regions from a BED file")
    argparser.add_argument('bed', type=argparse.FileType('r'))
    argparser.add_argument('query', type=argparse.FileType('r'))

    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument('-o', '--outfile',  # use an option to specify this
                           metavar='output',  # name used in help text
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # Open input- and query files. Both are mandatory.
    input = open(args.bed.name, 'r') # could e.g., be 'data/input2.bed'
    query = open(args.query.name, 'r') # could e.g., be 'data/query2.txt'
         
    # Examine whether output file passed as argument or not. Open if yes.
    if args.outfile.name != '<stdout>':
        output = open(args.outfile.name, 'w') # could e.g., be 
        #'data/output2.bed'. 
    else: 
        output = sys.stdout

    # Initiate list to store BedLines from input-file in. 
    lst = []

    # Read strings in input file and convert to BedLines (4 columns). 
    # Add BedLines to table.
    for line in input.readlines():
        parsed_input_line = parse_line(line) # Returns e.g., BedLine(
        # chrom='chr1', chrom_start=20100, chrom_end=20101, name='foo')
        lst.append(parsed_input_line)

    # Read strings in query file and convert to BedLines (3 columns).
    for line in query.readlines():
        parsed_query_line = parse_line2(line)
        # Compare BedLine2 from query with each BedLine1 in list. 
        # Print BedLine1 to output file, if chrom, chrom_start and 
        # chrom_end are identical. 
        for parsed_input_line in lst:
            if parsed_input_line.chrom == parsed_query_line.chrom and parsed_input_line.chrom_start == parsed_query_line.chrom_start and parsed_input_line.chrom_end == parsed_query_line.chrom_end:
                print_line(parsed_input_line, f=output)

if __name__ == '__main__':
    main()
