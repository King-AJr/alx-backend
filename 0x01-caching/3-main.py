#!/usr/bin/python3
"""
Test
"""
import sys

try:
    LRUCache = __import__("3-lru_cache").LRUCache
    from base_caching import BaseCaching

    BaseCaching.MAX_ITEMS = 1
    LRUCache.MAX_ITEMS = 1
    my_cache = LRUCache()
    my_cache.MAX_ITEMS = 1
    prev_key = None

    for i in range(5):
        key = "key-{}".format(i)
        value = "value-{}".format(i)
        if prev_key is not None:
            my_cache.get(prev_key)
        prev_key = key
        my_cache.put(key, value)
        my_cache.print_cache()

except:
    print(sys.exc_info()[1])
