#!/usr/bin/env python3
"""lru cache system using dict'"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """basic lru cache is just a simple dict"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """put function"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]

        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            first = next(iter(self.cache_data))
            del self.cache_data[first]
            print(f'DISCARD: {first}')

        self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key is None or key not in self.cache_data:
            return
        val = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = val
        return val
