class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, value):
        new_node = Node(value)
        current = self.head
        if current is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.head = new_node
            new_node.next = current
            self.size += 1
    # memorize this method, know this method
    def includes(self, value):
        current = self.head
        while current is not None:
            print(f"checking node value: {current.value}")
            if current.value == value:
                return True
            current = current.next
        print("reached the end of the linkList")
        return False

    def __str__(self):
        str = ""
        current = self.head
        while current is not None:
            str += f"{{ {current.value} }} -> "
            current = current.next
        str += f"NULL"
        return str




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
