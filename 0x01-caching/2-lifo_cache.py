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
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the item if key exists but don’t modify the queue
                self.cache_data[key] = item
            else:
                # Add the item and update last_key
                self.cache_data[key] = item
                self.queue.append(key)

                # Check if we need to remove the most recent item added
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    last_key = self.queue.pop()
                    del self.cache_data[last_key]
                    print("DISCARD:", last_key)

    def get(self, key):
        """Gets an item from the cache by key"""
        return self.cache_data.get(key, None)
