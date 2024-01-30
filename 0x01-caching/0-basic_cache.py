#!/usr/bin/env python3
"""simple cache system using dict 'not limit'"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """basic cache is just a simple dict"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """put function"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
