"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
"""

# iteration


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return
        carry = 0
        pre = l3 = ListNode(-1)
        while l1 or l2 or carry != 0:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, v3 = divmod(v1 + v2 + carry, 10)
            l3.next = ListNode(v3)
            l3 = l3.next
        return pre.next
