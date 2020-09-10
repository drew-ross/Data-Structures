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
        s = self.storage
        if len(s) > 0:
            print('HEAP ', s)
            s[0], s[-1] = s[-1], s[0]
            deleted = s.pop()
            self._sift_down(0)
            print('DELETED ', deleted)
            return deleted

    def get_max(self):
        if len(self.storage) > 0:
            return self.storage[0]
        else:
            return None

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        s = self.storage
        node = s[index]
        parent = s[(self._get_parent_index(index))]
        if node > parent:
            s[index] = parent
            s[(self._get_parent_index(index))] = node
            index = self._get_parent_index(index)
            self._bubble_up(index)

    def _sift_down(self, index):
        s = self.storage
        if len(s) > 0:
            node = s[index]
            left = s[self._get_left_index(index)]
            right = s[self._get_right_index(index)]
            max_child = max(left, right)
            max_i = self._get_left_index(index) if max_child == left else self._get_right_index(index)
            if node < max_child and max_i != index:
                s[index] = max_child
                s[max_i] = node
                self._sift_down(max_i)

    def _get_parent_index(self, index):
        parent_index = math.floor((index - 1) / 2)
        if parent_index < 0:
            parent_index = 0
        return parent_index

    def _get_left_index(self, index):
        li = 2 * index + 1
        if li > len(self.storage) - 1:
            li = index
        return li

    def _get_right_index(self, index):
        ri = 2 * index + 2
        if ri > len(self.storage) - 1:
            ri = index
        return ri