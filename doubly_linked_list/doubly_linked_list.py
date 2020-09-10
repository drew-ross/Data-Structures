"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.head:
            old_head = self.head
            self.head = ListNode(value)
            old_head.prev = self.head
            self.head.prev = None
            self.head.next = old_head
        else:
            self.head = ListNode(value)
            self.tail = self.head
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head:
            old_head = self.head
            self.head = self.head.next
            #If None, the old head was also the tail, remove tail
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.length -= 1
            return old_head.value
        else:
            return None
            
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if not self.tail:
            self.tail = ListNode(value)
            self.head = self.tail
        else:
            old_tail = self.tail
            self.tail = ListNode(value)
            self.tail.prev = old_tail
            old_tail.next = self.tail
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail:
            old_tail = self.tail
            self.tail = self.tail.prev
            #If None, the old tail was also the head, remove head
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            self.length -= 1
            return old_tail.value
        else:
            return None
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head is not node:
            prev_node = node.prev
            prev_node.next = node.next
            if node.next:
                node.next.prev = prev_node
            old_head = self.head
            self.head = node
            node.next = old_head
            node.prev = None
            old_head.prev = self.head
            if self.head is self.tail:
                self.tail = prev_node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.tail is not node:
            next_node = node.next
            next_node.prev = node.prev
            if node.prev:
                node.prev.next = next_node
            old_tail = self.tail
            self.tail = node
            node.prev = old_tail
            node.next = None
            old_tail.next = self.tail
            if self.head is self.tail:
                self.head = next_node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max = self.head.value
        current = self.head
        for i in range(self.length):
            if current.value > max:
                max = current.value
            current = current.next
        return max