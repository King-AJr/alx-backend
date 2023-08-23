#!/usr/bin/env python3
"""
inherits BasicCaching and
is a caching system that
implements MRU
"""

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    class to implement LRU caching
    algorithm
    """

    # cache_data = OrderedDict()

    def __init__(self):
        super().__init__()

    def put(self, key, value):
        """Add an item in the cache
        while implementing MRU algorithm
        for eviction"""
        if key in self.cache_data:
            # If key already exists, move it to the end and update the value
            self.cache_data.pop(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # If cache is full, remove the first (least recently used) item
            discarded_key, discarded_value = self.cache_data.popitem(last=True)
            print("DISCARD: {}".format(discarded_key))
        self.cache_data[key] = value

    def get(self, key):
        if key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value  # Move the accessed item to the end
            return value
        return None
