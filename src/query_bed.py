"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from bed import (
    parse_line, parse_line2, print_line
)
from query import Table
from bed import BedLine, BedLine2

#def add(line: str) -> lst:
#    """ Append line from input file to list.
#    >>> add('chr1 20100  20101 foo')
#    [BedLine(chrom='chr1', chrom_start=20100, chrom_end=20101, name='foo')]
#    """
#    lst.append(parse_line(line))
# hvordan teste når modificere variablen lst?

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
 
    input = args.bed # could e.g., be 'data/input2.bed'
    query = args.query # could e.g., be 'data/query2.txt'
    output = args.outfile

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
            if parsed_input_line.chrom == parsed_query_line.chrom and parsed_input_line.chrom_start in [i for i in range(parsed_query_line.chrom_start, parsed_query_line.chrom_end+1)] and parsed_input_line.chrom_end in [i for i in range(parsed_query_line.chrom_start, parsed_query_line.chrom_end+1)]:
                print_line(parsed_input_line, f=output)

if __name__ == '__main__':
    main()

