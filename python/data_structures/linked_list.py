class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next

class LinkedList:
  def __init__(self, head=None, values=None, insert=None):
    self.head = None

  def insert (self, value):
    newNode = Node(value)
    newNode._next = self.head
    self.head = newNode

  def append(self, value):
    newNode = Node(value)
    if self.head is None:
      self.head = newNode
    else:
      current = self.head
      while current._next is not None:
        current = current._next
      current._next = newNode

  def insert_before(self, value, new_value):
      current = self.head
      previous = None
      if current is None:
        raise ValueError(f"Value {value} not found in linked list")

      while current is not None and current.value != value:
        previous = current
        current = current._next

      if current is None:
        raise ValueError(f"Value {value} not found in linked list")

      newNode = Node(new_value)
      newNode._next = current
      if previous is None:
        self.head = newNode
      else:
        previous._next = newNode

  def insert_after(self, value, new_value):
      current = self.head
      while current is not None and current.value != value:
        current = current._next

      if current is None:
        raise ValueError(f"Value {value} not found in linked list")
      newNode = Node(new_value)
      newNode._next = current._next
      current._next = newNode

  def __str__(self):
    if self.head == None:
      return "NULL"
    else:
      current = self.head
    output = ""
    while current:
      output += f"{{ {current.value} }} -> "
      current = current._next
    output += "NULL"
    return output

  def includes(self, value):
    current = self.head
    while current:
      if current.value == value:
          return True
      current = current._next
    return False

  def kth_from_end(self, k):
    current = self.head
    count = 0
    while current:
      count += 1
      current = current._next
    if k < 0 or k >= count:
      raise TargetError("Target not found")
    current = self.head
    for i in range(count - k - 1):
      current = current._next
    return current.value

class TargetError(Exception):
  pass















# if __name__ == '__main__':
#     node1 = Node(1)
#     node2 = Node(2, node1)
#     # [2] -> [1] -> None
#     print(node1.value)
#     node1.value = 4
#     print(node1.value)



# Code Challenge 06
# CD into code_challenges
# Pytest test_linked_list_insertions.py
# pytest-watch-k version_1 < this will watch for any changes to your file


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0

#     def insert(self, value):
#         new_node = Node(value)
#         current = self.head
#         if current is None:
#             self.head = new_node
#             self.tail = new_node
#             self.size += 1
#         else:
#             self.head = new_node
#             new_node.next = current
#             self.size += 1

# This is my original insert function from Code Challeng 5
# def insert(self, value):
#         new_node = Node(value)
#         current = self.head
#         if current is None:
#             self.head = new_node
#             self.tail = new_node
#             self.size += 1
#         else:
#             self.head = new_node
#             new_node.next = current
#             self.size += 1
    # memorize this method, know this method
    # def includes(self, value):
    #     current = self.head
    #     while current is not None:
    #         print(f"checking node value: {current.value}")
    #         if current.value == value:
    #             return True
    #         current = current.next
    #     print("reached the end of the linkList")
    #     return False

    # def __str__(self):
    #     str = ""
    #     current = self.head
    #     while current is not None:
    #         str += f"{{ {current.value} }} -> "
    #         current = current.next
    #     str += f"NULL"
    #     return str




#     def delete_node(self, data):
#         if self.head is None:
#             return

#         current_node = self.head
#         while current_node is not None and current_node.value != value:
#             current_node = current_node.next

#         if current_node is None:
#             return

#         if current_node == self.head:
#             self.head = current_node.next
#         else:
#             previous_node = current_node.prev
#             previous_node.next = current_node.next

#         self.size -= 1
# pass
    # def __str__(self):
    #     if self.head is None:
    #         return "NULL"
    #     else:
    #         sb = ""
    #         current_node = self.head
    #         while current_node is not None:
    #             sb += str(current_node.value) + ","
    #             current_node = current_node.next

    #         return sb[:-1]

# pass


# class TargetError:
#     pass
