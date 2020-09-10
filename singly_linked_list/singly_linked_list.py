class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_tail(self, value):
        new_tail = Node(value)
        if not self.tail:
            self.head = new_tail
            self.tail = new_tail
        else:
            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail
        self.length += 1
        return new_tail

    def remove_tail(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            old_tail = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return old_tail.value
        elif self.head.next == self.tail:
            old_tail = self.tail
            self.tail = self.head
            self.head.next = None
            return old_tail.value
        else:
            current_node = self.head
            for i in range(self.length - 2):
                current_node = current_node.next
            old_tail = current_node.next
            current_node.next = None
            self.tail = current_node
            self.length -= 1
            return self.tail.value

    def remove_head(self):
        if not self.head:
            return None
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return current_head.value
        else:
            current_head = self.head
            self.head = current_head.next
            self.length -= 1
            return current_head.value