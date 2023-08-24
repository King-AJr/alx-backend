#!/usr/bin/env python3
"""
inherits BasicCaching and
is a caching system that
implements LRU
"""
from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    class to implement LRU caching
    algorithm
    """
    cache = OrderedDict()

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache
        while implementing LRU algorithm
        for eviction"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            # If key already exists, move it to the end and update the value
            self.cache_data.pop(key)
        elif len(self.cache_data) == self.MAX_ITEMS:
            # If cache is full, remove the first (least recently used) item
            discarded_key, discarded_value = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(discarded_key))
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value  # Move the accessed item to the beginning
            self.cache_data = self.cache_data
            return key
        
        return None
