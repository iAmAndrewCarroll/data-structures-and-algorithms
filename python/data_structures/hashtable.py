class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def _hash(self, key):
        total = 0
        for ch in key:
            total += ord(ch)
        primed = total * 19
        index = primed % self.size
        return index

    def set(self, key, value):
        index = self._hash(key)

        if self._buckets[index] is None:
            self._buckets[index] = Node(key, value)
        else:
            current = self._buckets[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next

            new_node = Node(key, value)
            new_node.next = self._buckets[index]
            self._buckets[index] = new_node

    def get(self, key):
        index = self._hash(key)

        if self._buckets[index] is None:
            return None
        else:
            current = self._buckets[index]
            while current:
                if current.key == key:
                    return current.value
                current = current.next

        return None

    def has(self, key):
        index = self._hash(key)

        if self._buckets[index] is None:
            return False
        else:
            current = self._buckets[index]
            while current:
                if current.key == key:
                    return True
                current = current.next
            return False

    def keys(self):
        unique_keys = []
        for bucket in self._buckets:
            if bucket:
                current = bucket
                while current:
                    unique_keys.append(current.key)
                    current = current.next
        return unique_keys
