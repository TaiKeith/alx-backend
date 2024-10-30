#!/usr/bin/python3
"""
This module contains a class LIFOCache that inherits from BaseCaching and
is a caching system.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A caching system that inherits from BaseCaching
    """
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.queue = []  # To track insertion order for LIFO removal algo

    def put(self, key, item):
        """
        Adds an item in the cache

        Args:
            key: Key to be used as an index
            item: Item to be stored
        Returns:
            nothing if the key and item is none
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.queue.pop()
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from the cache by key"""
        return self.cache_data.get(key, None)
