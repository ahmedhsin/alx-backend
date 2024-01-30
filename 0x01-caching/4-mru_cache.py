#!/usr/bin/env python3
"""mru cache system using dict'"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """basic mru cache is just a simple dict"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """put function"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]

        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            des = list(self.cache_data.keys())[-1]
            del self.cache_data[des]
            print(f'DISCARD: {des}')

        self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key is None or key not in self.cache_data:
            return
        val = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = val
        return val
