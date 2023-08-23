#!/usr/bin/env python3
"""
inherits BasicCaching and
is a caching system that
implements LIFO
"""

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    class to implement LRU caching
    algorithm
    """
    temp_key = 0
    freq_score = {0: 'zero',
                  1: 'one',
                  2: 'two',
                  3: 'three'}

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache using the LRU algorithm for eviction"""
        if key is None or item is None:
            pass  # Skip if key or item is None

        if len(self.cache_data) == 0:
            self.freq_score[0] = key  # Initialize frequency score if cache is empty

        if len(self.cache_data) != 0 and len(self.cache_data) < self.MAX_ITEMS:
            temp = len(self.cache_data)
            self.freq_score[temp] = key  # Set frequency score for the new item

        if len(self.cache_data) == self.MAX_ITEMS and key not in self.cache_data.keys():
            # Evict the least recently used item if cache is full and the key is new
            print("DISCARD: {}".format(self.freq_score[0]))
            self.cache_data.pop(self.freq_score[0])
            self.freq_score[0] = self.freq_score[1]
            self.freq_score[1] = self.freq_score[2]
            self.freq_score[2] = self.freq_score[3]
            self.freq_score[3] = key  # Update frequency scores

        if len(self.cache_data) == self.MAX_ITEMS and key in self.cache_data.keys():
            # If the key already exists, adjust frequency scores to indicate recent usage
            for k, v in self.freq_score.items():
                if v == key:
                    self.temp_key = k  # Store the key's frequency score
            for i in range(2):
                temp = self.freq_score[self.temp_key - i]
                self.freq_score[self.temp_key - i] = self.freq_score[3 - i]
                self.freq_score[3 - i] = temp  # Update frequency scores

        self.cache_data[key] = item  # Add the new item to the cache






    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data.keys():
            pass

        return self.cache_data.get(key)
