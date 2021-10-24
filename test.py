import threading
import time
import queue


# 20211023
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)

            inc, dec = 1, 1
            l_inc, l_dec = dfs(node.left)
            r_inc, r_dec = dfs(node.right)

            if node.left:
                if node.left.val == node.val + 1:
                    inc = max(inc, 1 + l_inc)
                if node.left.val == node.val - 1:
                    dec = max(dec, 1 + l_dec)
            if node.right:
                if node.right.val == node.val + 1:
                    inc = max(inc, 1 + r_inc)
                if node.right.val == node.val - 1:
                    dec = max(dec, 1 + r_dec)
            res[0] = max(res[0], inc + dec - 1)
            return (inc, dec)

        res = [0]
        dfs(root)

        return res[0]
