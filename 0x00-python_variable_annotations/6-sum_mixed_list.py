#!/usr/bin/env python3
"""
This module contains a function that takes a list of integers and floats,
and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a mixed list of integers and floats and returns their
    sum as float"""
    return sum(mxd_lst)
