#!/usr/bin/env python3
"""
inherit methods from
BaseCaching
"""

BaseCache = __import__("base_caching").BaseCaching


class BasicCache(BaseCache):
    """inherits from BaseCaching
    and is a caching system"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            pass

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data.keys():
            pass

        return self.cache_data.get(key)
