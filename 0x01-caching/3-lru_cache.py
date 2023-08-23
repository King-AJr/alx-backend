#!/usr/bin/env python3
"""
inherits BasicCaching and
is a caching system that
implements LIFO
"""
from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    class to implement LRU caching
    algorithm
    """

    capacity = 4
    cache = OrderedDict()

    def __init__(self):
        super().__init__()

    def put(self, key, value):
        if key in self.cache:
            # If key already exists, move it to the end and update the value
            self.cache.pop(key)
        elif len(self.cache) >= self.MAX_ITEMS:
            # If cache is full, remove the first (least recently used) item
            discarded_key, discarded_value = self.cache.popitem(last=False)
            print("DISCARD: {}".format(discarded_key))
        self.cache[key] = value
        self.cache_data = self.cache



    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data.keys():
            pass

        return self.cache_data.get(key)
