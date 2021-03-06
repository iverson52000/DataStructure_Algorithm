"""
146. LRU Cache
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the 
following operations: get and put.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, 
otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached 
its capacity, it should invalidate the least recently used item before inserting a new item.
"""

#OrderedDict O(1)

class LRUCache:

    def __init__(self, capacity: int):
        self.m = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.m: return -1
        val = self.m.pop(key)
        self.m[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.m: self.m.pop(key)
        self.m[key] = value
        if len(self.m) > self.capacity:
            self.m.popitem(last = False)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


#Deque + Hashmap O(n)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = {}
        self.q = collections.deque()

    def get(self, key: int) -> int:
        if key not in self.m: return -1
        self.q.remove(key)
        self.q.append(key)
        return self.m[key]

    def put(self, key: int, value: int) -> None:
        if key in self.m: self.q.remove(key)	#O(n) Shift
        self.m[key] = value
        self.q.append(key)	#O(1)
        if len(self.m) > self.capacity:
            key_pop = self.q.popleft()
            self.m.pop(key_pop)

#DLinkedList + Hashmap O(1)
            
class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class DLinkedList:
    
    def __init__(self):
        self.dummy_head = Node(0, 0)
        self.dummy_tail = Node(0, 0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
    
    def append(self, node):
        tail = self.dummy_tail.prev
        tail.next = node
        node.prev = tail
        node.next = self.dummy_tail        
        self.dummy_tail.prev = node
        
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = {}     
        self.q = DLinkedList()
        
    def get(self, key: int) -> int:
        if key not in self.m: return -1
        node = self.m[key]
        self.q.remove(node)
        self.q.append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.m: self.q.remove(self.m[key])
        node = Node(key, value)
        self.q.append(node)
        self.m[key] = node
        if len(self.m) > self.capacity:
            head = self.q.dummy_head.next
            self.q.remove(head)
            self.m.pop(head.key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
