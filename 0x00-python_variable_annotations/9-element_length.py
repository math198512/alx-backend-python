#!/usr/bin/env python3
"""
This module
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with the length of each element"""
    return [(i, len(i)) for i in lst]
