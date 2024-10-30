#!/usr/bin/python3
"""
This module contains a class BasicCache that inherits from BaseCaching and
is a caching system.
This caching system doesn't have limit.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A caching system that Inherits from BasicCaching and has no limit
    """
    def __init__(self):
        """Initializes an empty cache_data dictionary"""
        super().__init__()

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
            self.cache_data[key] = item

    def get(self, key):
        """Returns an item from the cache by key"""
        return self.cache_data.get(key, None)
