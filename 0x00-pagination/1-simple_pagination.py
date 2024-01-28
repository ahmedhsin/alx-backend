#!/usr/bin/env python3
"""this is a script for learning pagination"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """return a tuble with start index and end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


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
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get ranged dataset"""
        assert (type(page) == int and type(page_size) == int)
        assert (page > 0 and page_size > 0)
        ac_range = index_range(page, page_size)
        start = ac_range[0]
        end = ac_range[1]
        data = self.dataset()
        if start > end or end > len(data) - 1:
            return []
        return data[start:end]
