"""Module for querying a genome.

The code in this module is, again, something we haven't seen yet, but you don't
need to understand it to use it. It gives you a table where you can insert
BedLine objects and then access them per chromosome. Create a table and insert
BED lines it like below, and when you later want to get only the lines relevant
for a given chromosome, you can use the get_chrom() method:

>>> from bed import BedLine
>>> table = Table()
>>> table.add_line(BedLine('chr1', 0, 1, 'foo'))
>>> table.add_line(BedLine('chr2', 0, 1, 'bar'))
>>> table.add_line(BedLine('chr1', 10, 11, 'baz'))
>>> table.get_chrom('chr1')
[BedLine(chrom='chr1', chrom_start=0, chrom_end=1, name='foo'), BedLine(chrom='chr1', chrom_start=10, chrom_end=11, name='baz')]
"""

from bed import BedLine
from collections import defaultdict


class Table:
    """Table containing bed-lines."""

    tbl: dict[str, list[BedLine]]

    def __init__(self) -> None:
        """Create a new table."""
        self.tbl = defaultdict(lambda: [])

    def add_line(self, line: BedLine) -> None:
        """Add line to the table."""
        self.tbl[line.chrom].append(line)

    def get_chrom(self, chrom: str) -> list[BedLine]:
        """Get all the lines that sits on chrom"""
        return self.tbl[chrom]
    
    def get_table(self): 
        """Get the table to see what it looks like"""
        return self.tbl
# Example of table:
# {'chr1': [BedLine(chrom='chr1', chrom_start=20100, chrom_end=20101, 
# name='foo'), BedLine(chrom='chr1', chrom_start=600, chrom_end=601, 
# name='baz')], 'chr3': [BedLine(chrom='chr3', chrom_start=0, 
# chrom_end=1, name='bar')], 'chr2': [BedLine(chrom='chr2', chrom_start
# =200, chrom_end=201, name='qux'), BedLine(chrom='chr2', chrom_start=
# 199, chrom_end=200, name='qax')]})
