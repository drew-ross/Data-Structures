class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.storage = []
        self.last_read = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def __str__(self):
        return f"{self.storage}"

    def get(self, key):
        s = self.storage
        try:
            for i, item in enumerate(s):
                if key in item.keys():
                    self.last_read = i
                    s.pop(i)
                    s.append(item)
                    return item[key]
        except:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        s = self.storage
        entry = self.get(key)
        if entry:
            s[self.last_read] = { key: value }
        elif len(s) < self.limit:
            s.append({ key: value })
        else:
            s.pop(0)
            s.append({ key: value })

