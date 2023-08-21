#!/usr/bin/env python3
"""
function index_range that takes
page and page size then returns
the start and end index for that
page.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    returns the start and end index for that page.
    """
    end: int = page * page_size
    start: int
    if page == 1:
        start = 0
    else:
        start = end - page_size

    return_tuple = (start, end)

    return return_tuple
