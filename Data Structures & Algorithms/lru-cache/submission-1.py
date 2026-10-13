class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.least, self.most = Node(0, 0), Node(0, 0)

        self.least.next, self.most.prev = self.most, self.least
    
    def insert(self, node):
        prv, nxt = self.most.prev, self.most
        prv.next, nxt.prev = node, node
        node.prev, node.next = prv, nxt

    def remove(self, node):
        prv, nxt = node.prev, node.next
        node.prev = None
        node.next = None
        prv.next, nxt.prev = nxt, prv

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.least.next
            self.remove(lru)
            del self.cache[lru.key]
        
