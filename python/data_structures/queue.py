from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    """
    Put docstring here...Okay
    """

    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.back = new_node
        if self.back:
            self.back.next = new_node
            self.back = new_node
        else:
            current = self.front
            while current.next:
                current = current.next
            current.next = new_node
            self.back = current.next


    def dequeue(self):
        if not self.front:
            raise InvalidOperationError
        else:
            current = self.front
            self.front = self.front.next
            current.next = None
            return current.value

    def peek(self):
        if self.front:
            return self.front.value
        else:
            raise InvalidOperationError

    def is_empty(self):
        if not self.front:
            return True
        else:
            return False

