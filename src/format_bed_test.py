# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from format_bed import to_tab_separated

def test_to_tab_separated():
    assert to_tab_separated('chr1 20100  20101 foo') == 'chr1    20100    20101    foo'