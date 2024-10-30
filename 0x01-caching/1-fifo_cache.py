#!/usr/bin/python3
"""
This module contains a class FIFOCache that inherits from BaseCaching and
is a caching system.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A caching system that inherits from BaseCaching
    """
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.cache_order = []  # To track the order of items

    def put(self, key, item):
        """
        Adds an item in the cache

        Args:
            key: Key to be used as an index
            item: Item to be stored
        Returns:
            nothing if the key and item is none
        """
        if key is not None and item is not None:
            # If key exists, update the item but don't add to order again
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                # Add new item to the cache and order list
                self.cache_data[key] = item
                self.cache_order.append(key)

                # Check if we need to remove the oldest item
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    oldest_key = self.cache_order.pop(0)
                    del self.cache_data[oldest_key]
                    print("DISCARD:", oldest_key)

    def get(self, key):
        """Gets an item from the cache by key"""
        return self.cache_data.get(key, None)
