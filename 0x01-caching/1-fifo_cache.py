#!/usr/bin/env python3
"""
inherits BasicCaching and
is a caching system that
implements FIFO
"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    class to implement FIFO caching
    algorithm
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache
        while implementing FIFO algorithm
        for eviction"""
        if key is None or item is None:
            return

        if len(self.cache_data) == self.MAX_ITEMS\
                and key not in self.cache_data.keys():
            first_key = next(iter(self.cache_data))
            print("DISCARD: {}".format(first_key))
            self.cache_data.pop(first_key)

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data.keys():
            pass

        return self.cache_data.get(key)
