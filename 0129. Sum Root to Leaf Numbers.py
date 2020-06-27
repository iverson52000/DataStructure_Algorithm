"""
129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.
"""

# dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def sumNumbers(self, root: TreeNode) -> int:
        total = 0
        return self.dfs(root, total)

    def dfs(self, root, total) -> int:
        if not root:
            return 0
        total = total * 10 + root.val
        if (not root.left) and (not root.right):
            return total
        return self.dfs(root.left, total) + self.dfs(root.right, total)
