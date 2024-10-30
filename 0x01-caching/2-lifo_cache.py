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
        self.last_key = None  # To track the last item added

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
                # Add the item and update last_key
                self.cache_data[key] = item
                self.last_key = key

                # Check if we need to remove the most recent item added
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    del self.cache_data[self.last_key]
                    print("DISCARD:", self.last_key)

                    # Update the last key to the current key
                    self.last_key = key

    def get(self, key):
        """Gets an item from the cache by key"""
        return self.cache_data.get(key, None)
