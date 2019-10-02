#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 09:52:47 2019

@author: alberthsu
"""

"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        memo = {}
        return self.copyNode(head, memo)
    
    def copyNode(self, cur, memo):       
        if not cur: return None
        if cur in memo: return m[cur]
        
        copy = Node(cur.val, None, None)
        memo[cur] = copy
        copy.next = self.copyNode(cur.next, m)
        copy.random = self.copyNode(cur.random, m)      
        return copy
