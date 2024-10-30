#!/usr/bin/python3
"""
This module contains a class LFUCache that inherits from BaseCaching and
is a caching system.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    A caching system that inherits from BaseCaching with LFU eviction.
    """
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.freq = {}  # Tracks frequency of access for each key
        self.order = []  # Tracks order of access for LRU among same-freq items

    def put(self, key, item):
        """
        Adds an item in the cache

        Args:
            key: Key to be used as an index
            item: Item to be stored
        """
        if key is None or item is None:
            return

        # If key already exists, update the item and increase its frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.order.remove(key)
            self.order.append(key)
        else:
            # If cache is at max capacity apply LFU & LRU policy to remove item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the lowest frequency among items
                min_freq = min(self.freq.values())
                # Find items with the minimum frequency
                candidates = [k for k,
                              freq in self.freq.items() if freq == min_freq]

                # If multiple candidates, use the LRU policy
                if len(candidates) > 1:
                    for candidate in self.order:
                        if candidate in candidates:
                            discard = candidate
                            break
                else:
                    discard = candidates[0]

                # Discard the selected item
                del self.cache_data[discard]
                del self.freq[discard]
                self.order.remove(discard)
                print("DISCARD:", discard)

            # Add the new key and item, with frequency set to 1
            self.cache_data[key] = item
            self.freq[key] = 1
            self.order.append(key)

    def get(self, key):
        """Gets an item from the cache by key, updating frequency for LFU"""
        if key in self.cache_data:
            # Increase frequency & update order for LRU among same-freq items
            self.freq[key] += 1
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
