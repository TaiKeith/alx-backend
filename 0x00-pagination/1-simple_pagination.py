#!/usr/bin/env python3
"""
This module contains a type-annotated function named 'index_range' that takes
two int arguments 'page' & 'page_size'. It returns a tuple of size two
containing a start index & an end index, corresponding to the range of indexes
to return in a list for those particular pagination parameters.
"""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple:
    """
    Takes two int arguments and returns a tuple of size 2 containing a start
    index & end index, corresponding to the range of indexes to return in a
    list for those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset"""
        # Check if the arguments are valid integers greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Get the start and end index for the pagination
        start_idx, end_idx = index_range(page, page_size)

        # Get the data
        data = self.dataset()

        # If the start index is out of range, return an empty list
        if start_idx >= len(data):
            return []

        # Return the slice of the dataset for the requested page
        return data[start_idx:end_idx]
