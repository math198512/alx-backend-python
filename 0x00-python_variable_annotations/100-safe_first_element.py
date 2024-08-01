#!/usr/bin/env python3
"""
This module
"""
from typing import List, TypeVar, Optional

T = TypeVar('T')  # Declare a generic type variable

def safe_first_element(lst: List[T]) -> Optional[T]:
    """
    """
    if lst:
        return lst[0]
    else:
        return None