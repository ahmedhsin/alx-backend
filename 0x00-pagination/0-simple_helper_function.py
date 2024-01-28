#!/usr/bin/env python3
"""this is a script for learning pagination"""


def index_range(page: int, page_size: int) -> tuple:
    """return a tuble with start index and end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
