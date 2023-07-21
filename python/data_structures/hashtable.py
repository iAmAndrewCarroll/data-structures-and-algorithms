class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def display(self):
        return [self.key, self.value]

class Hashtable:
    """
    Paramaters: Key, Value
    Returns: Nothing
    """

    def __init__(self, size=1024):
        self.size = size
        self.buckets = size * [None]

    def set(self, key, value):
        """
        Arguments: key, value
        Returns: nothing
        """
        # hash the key
        index = self.hash(key)
        # determine index and go there
        if self.buckets[index] is None:
        # if there is nothing there, add a new node
            self.buckets[index] = Node(key, value)
        # if there is a node, check if the key is the same
        else:
            current = self.buckets[index]
            while current:
                if current.key == key:
        # if the key is the same, update the value
                    current.value = value
                    return
                # if current.next is None:
                #     break
                current = current.next
        # if the key is different, add a new node
            # current.next = Node(key, value)
            new_node = Node(key, value)
            new_node.next = self.buckets[index]
            self.buckets[index] = new_node

    # define the get method of the hashtable class. Takes a key as an argument and returns the associated value if the key is found in the hashtable. If the key is not found, return None.
    def get(self, key):
        """
        Arguments: key
        Returns: value
        """
        # hash the key
        index = self.hash(key)
        # check if there is no data (node) at the index in the hashtable (self.buckets). If index is empty, the key is not present in the hashtable, and the method should return None.
        if self.buckets[index] is None:
            return None
        # if there is at least one node present at the index, there is the possibility of a collision. Traverse the linked list at that index to find the key/value pair.
        else:
            # create current variable and initialize it to the first node in the linked list at the index. This allows traversal of the linked list from the head node to find the key/value match.
            current = self.buckets[index]
            # while loop that iterates as long as there is a valid (current) node in the linked list.  Used to traverse through the linked list and check if the key exists.
            while current:
                # check if the current node's key matches the key that was passed into the get method. If so, return the value.
                if current.key == key:
                    return current.value
                current = current.next

    def has(self, key):
        """
        Arguments: key
        Return: boolean
        """
        # hash the key
        index = self.hash(key)
        # check if there is no data (node) at the index in the hashtable (self.buckets). If index is empty, the key is not present in the hashtable, and the method should return None.
        if self.buckets[index] is None:
            return False
        # if there is at least one node present at the index, there is the possibility of a collision. Traverse the linked list at that index to find the key/value pair.
        else:
            # create current variable and initialize it to the first node in the linked list at the index. This allows traversal of the linked list from the head node to find the key/value match.
            current = self.buckets[index]
            # while loop that iterates as long as there is a valid (current) node in the linked list.  Used to traverse through the linked list and check if the key exists.
            while current:
                # check if the current node's key matches the key that was passed into the get method. If so, return the value.
                if current.key == key:
                    return True
                current = current.next
            return False

    def keys(self):
        """
        Returns: collection of keys
        """
        # create an empty list
        unique_keys = []
        # loop through the hashtable
        for bucket in self.buckets:
            # if there is a node, add the key to the list
            if bucket:
                current = bucket
                while current:
                    unique_keys.add(current.key)
                    current = current.next
        # return the list
        return list(unique_keys)

    def hash(self, key):
        """
        hash
        Arguments: key
        Returns: Index in the collection for that key
        :return:
        """
        # super
        #     ^
        # jump
        # 106 + 117 + 109 + 112 = 446
        # total = 0 + 115 + 117 + 112 + 101 + 114 = 560 * 11 = 10640
        # ['super: 100', None, None, None, None, None, 'jump: 734', None, None, None]
        total = 0
        for ch in key:
            total += ord(ch)
        primed = total * 19
        index = primed % self.size
        return index

if __name__ == '__main__':

    hash1 =  Hashtable()
    print(hash1.size)
    print(hash1.hash('super'))

