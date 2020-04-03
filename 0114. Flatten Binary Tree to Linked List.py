"""
114. Flatten Binary Tree to Linked List
Given a binary tree, flatten it to a linked list in-place.
"""

#preverse preorder

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre = None
        self.dfs(root)
    
    def dfs(self, root):
        if not root: return
        self.dfs(root.right)
        self.dfs(root.left)
        root.right = self.pre
        root.left = None
        self.pre = root
