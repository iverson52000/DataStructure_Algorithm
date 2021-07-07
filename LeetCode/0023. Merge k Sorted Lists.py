
"""
23. Merge k Sorted Lists
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

#Heap
#Time: O(nlog(k)) Space: O(k). n: number of total elements. k: len of lists

from heapq import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pre = cur = ListNode(-1)         
        heap = []
        for i in range(len(lists)):
            if lists[i]: 
                heapq.heappush(heap, (lists[i].val, i, lists[i]))             
        while heap:
            val, idx, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next       
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        return pre.next

#Merge Sort

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return 
        if len(lists) == 1: return lists[0]
        mid = len(lists)//2
        left_list = self.mergeKLists(lists[:mid])
        right_list = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left_list, right_list)
    
    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1      
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2