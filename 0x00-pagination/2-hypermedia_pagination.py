#!/usr/bin/env python3
"""
function index_range that takes
page and page size then returns
the start and end index for that
page.
"""
import csv
import math
from typing import Tuple, List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return data for a given page"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        indexes: Tuple = index_range(page, page_size)
        start: int = indexes[0]
        end: int = indexes[1]
        self.dataset()
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """return data for a given page and other informations
        associated with the page"""
        next_page: int
        prev_page: int
        data = self.get_page(page, page_size)
        total_pages: int = math.ceil(len(self.dataset()) / page_size)
        if page < total_pages:
            next_page = page + 1
        else:
            next_page = None

        if page != 1:
            prev_page = page - 1
        else:
            prev_page = None

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }


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
