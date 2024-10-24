#!/usr/bin/env python3
"""
This module contains a type-annotated function named 'index_range' that takes
two int arguments 'page' & 'page_size'. It returns a tuple of size two
containing a start index & an end index, corresponding to the range of indexes
to return in a list for those particular pagination parameters.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Takes two int arguments and returns a tuple of size 2 containing a start
    index & end index, corresponding to the range of indexes to return in a
    list for those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
