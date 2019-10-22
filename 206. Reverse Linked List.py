#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:00:50 2019

@author: alberthsu
"""

"""
206. Reverse Linked List
Reverse a singly linked list.
"""

#Iteration

class Solution:
    def reverseList(self, head):
        if not head: return None
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

#Recursion

class Solution:
    def reverseList(self, head) -> ListNode:
        if not head or not head.next: return head
        new_head = self.reverseList(head.next)
        nxt = head.next
        nxt.next = head
        head.next = None
        return new_head

