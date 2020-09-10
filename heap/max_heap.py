import math


class Heap:
    def __init__(self):
        self.storage = []

    def __str__(self):
        return f"{self.storage}"

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        node = self.storage[index]
        parent = self.storage[(self._get_parent_index(index))]
        while node > parent:
            self.storage[index] = parent
            self.storage[(self._get_parent_index(index))] = node
            index = self._get_parent_index(index)
            if index < 0:
                break
            node = self.storage[index]
            parent = self.storage[(self._get_parent_index(index))]

    def _sift_down(self, index):
        pass

    def _get_parent_index(self, index):
        parent_index = math.floor((index - 1) / 2)
        if parent_index < 0:
            parent_index = 0
        return parent_index

    def _get_left_index(self, index):
        return 2 * index + 1

    def _get_right_index(self, index):
        return 2 * index + 2
