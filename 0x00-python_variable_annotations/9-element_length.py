#!/usr/bin/env python3
"""Script defines a function to calculate the length of each element in a list
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input list

    Args:
        lst (Iterable[Sequence]): The input list of sequences

    Returns:
        List of tuples, each contains a sequence and its length as an integer
    """
    return [(i, len(i)) for i in lst]