from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.cache and\
            len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
        self.cache.move_to_end(key)
