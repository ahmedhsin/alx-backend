#!/usr/bin/env python3
"""fifo cache system using dict'"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """basic fifo cache is just a simple dict"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """put function"""
        if key is None or item is None:
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            first = next(iter(self.cache_data))
            del self.cache_data[first]
            print(f'DISCARD: {first}')

        self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
