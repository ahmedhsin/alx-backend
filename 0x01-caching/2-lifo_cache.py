#!/usr/bin/env python3
"""lifo cache system using dict'"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """basic lifo cache is just a simple dict"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """put function"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            first = self.cache_data.popitem()[0]
            print(f'DISCARD: {first}')

        self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
