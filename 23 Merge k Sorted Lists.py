#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:35:20 2019

@author: alberthsu
"""

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

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
        l_list = self.mergeKLists(lists[:mid])
        r_list = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(l_list, r_list)
    
    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1      
        if l1.val<l2.val:
            l1.next =self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next =self.mergeTwoLists(l1, l2.next)
            return l2

#Heap

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pre = cur = ListNode(0)         
        heap = []
        for i in range(len(lists)):
            if lists[i]: 
                heapq.heappush(heap, (lists[i].val, i, lists[i]))             
        while heap:
            val, idx, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next       
            if cur.next:
                heapq.heappush(heap, (cur.next.val, idx, cur.next))
        return pre.next
