"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
from singly_linked_list import LinkedList
# Linked List Stack
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __str__(self):
        if self.storage.length == 0:
            return 'the Stack is empty'
        n = self.storage.head
        output = ''
        while n is not None:
            output += f'\n[{n.value}]'
            n = n.next
        return output

    def __len__(self):
        return self.storage.getLength()

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        if self.storage.length == 0:
            return None
        value = self.storage.tail.value
        self.storage.remove_tail()
        return value
