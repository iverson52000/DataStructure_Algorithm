"""
460. LFU Cache
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.
Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.
"""

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
        self.freq = 1

class DLinkedList:
    def __init__(self):
        self.dummy_head = ListNode(0, 0)
        self.dummy_tail = ListNode(0, 0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.size = 0

    def __len__(self):
        return self.size
    
    def append(self, node):
        tail = self.dummy_tail.prev
        tail.next = node
        node.prev = tail
        node.next = self.dummy_tail
        self.dummy_tail.prev = node
        self.size += 1
    
    def remove(self, node):
        pre = node.prev
        nxt = node.next
        pre.next = nxt
        nxt.prev = pre
        self.size -= 1
        
class LFUCache:
    def __init__(self, capacity: int):
        self.m = {}
        self.capacity = capacity       
        self.m_freq = collections.defaultdict(DLinkedList)
        self.min_freq = 0
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.m: return -1
        node = self.m[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        
        if key in self.m: 
            node = self.m[key]
            self.update(node)
            node.val = value
        else:
            if self.size == self.capacity:
                node = self.m_freq[self.min_freq].dummy_head.next
                self.m_freq[self.min_freq].remove(node)
                self.m.pop(node.key)
                self.size -= 1
            node = ListNode(key, value)
            self.m[key] = node  
            self.m_freq[1].append(node)
            self.min_freq = 1
            self.size += 1

    def update(self, node):
        freq = node.freq        
        self.m_freq[freq].remove(node)
        if self.min_freq == freq and not self.m_freq[freq]:
            self.min_freq += 1   
        node.freq += 1
        freq = node.freq
        self.m_freq[freq].append(node)
    

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
