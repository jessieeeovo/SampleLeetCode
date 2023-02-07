class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = dict()
        # initialize a doubly linked list
        # use dummy nodes both at head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self._remove(node)
            self._add(node)
            return node.v
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self._remove(self.d[key])
        node = Node(key, value)
        # store NODE in the dict!!!
        self.d[key] = node
        self._add(node)
        if len(self.d) > self.capacity:
            head = self.head.next
            del self.d[head.k]
            self._remove(head)
    
    def _remove(self, node):
        # remove the node given
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def _add(self, node):
        # add to the tail (before the dummy node)
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)