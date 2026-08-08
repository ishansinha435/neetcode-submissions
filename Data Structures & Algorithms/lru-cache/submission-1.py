class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key, self.val = key, val
        self.prev, self.next = prev, next

class LRUCache:

    def __init__(self, capacity: int):
        self.lru, self.mru = Node(None, None), Node(None, None)
        self.lru.next, self.mru.prev = self.mru, self.lru
        self.hmap, self.capacity = {}, capacity

    def remove(self, key):
        node = self.hmap[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.hmap.pop(key)

    def insert(self, key, value):
        node = Node(key, value)
        node.next, node.prev = self.mru, self.mru.prev
        self.mru.prev.next = self.mru.prev = node
        self.hmap[key] = node

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        val = self.hmap[key].val
        self.remove(key)
        self.insert(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.remove(key)
        self.insert(key, value)
        if len(self.hmap) > self.capacity:
            self.remove(self.lru.next.key)
        
