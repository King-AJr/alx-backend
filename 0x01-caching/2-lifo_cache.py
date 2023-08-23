#!/usr/bin/env python3
"""
inherits BasicCaching and
is a caching system that
implements LIFO
"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    class to implement LIFO caching
    algorithm
    """
    last_key = ""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache
        while implementing LIFO algorithm
        for eviction"""
        if key is None or item is None:
            pass

        if len(self.cache_data) == self.MAX_ITEMS\
                and key not in self.cache_data.keys():
            print("DISCARD: {}".format(self.last_key))
            self.cache_data.pop(self.last_key)

        self.last_key = key
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data.keys():
            pass

        return self.cache_data.get(key)
