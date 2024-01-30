#!/usr/bin/env python3
"""lfu cache system using dict'"""


BaseCaching = __import__('base_caching').BaseCaching


def get_victim(tracker):
    """get victim with least calls"""
    mn = 999999
    print(str(tracker))
    val = None
    for k, v in tracker.items():
        if v < mn:
            mn = v
            val = k
    return val


class LFUCache(BaseCaching):
    """basic lfu cache is just a simple dict"""
    def __init__(self):
        self.tracker = {}
        super().__init__()

    def put(self, key, item):
        """put function"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.tracker[key]
            del self.cache_data[key]

        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            first = get_victim(self.tracker)
            del self.cache_data[first]
            del self.tracker[first]
            print(f'DISCARD: {first}')

        self.tracker[key] = 0
        self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key is None or key not in self.cache_data:
            return
        val = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = val
        self.tracker[key] += 1
        return val
