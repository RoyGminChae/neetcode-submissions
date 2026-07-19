class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        self.hashMap = dict()
        self.nodeToKey = dict()
        
        self.dummy1 = Node(None)
        self.dummy2 = Node(None)
        self.dummy1.next = self.dummy2
        self.dummy2.prev = self.dummy1


    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        
        node = self.hashMap[key]
        self.nodeToKey[node] = key
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.dummy2.prev
        node.next = self.dummy2 
        self.dummy2.prev.next = node
        self.dummy2.prev = node

        return node.val


    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.hashMap:
            node = self.hashMap[key]
            self.nodeToKey[node] = key
            node.val = value

            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node = Node(value)
            self.hashMap[key] = node
            self.nodeToKey[node] = key
            self.size += 1
        
        node.prev = self.dummy2.prev
        node.next = self.dummy2 
        self.dummy2.prev.next = node
        self.dummy2.prev = node

        if self.size > self.capacity: 
            self.hashMap.pop(self.nodeToKey[self.dummy1.next])
            self.nodeToKey.pop(self.dummy1.next)

            self.dummy1.next = self.dummy1.next.next
            self.dummy1.next.prev = self.dummy1
            self.size -= 1
            

class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev