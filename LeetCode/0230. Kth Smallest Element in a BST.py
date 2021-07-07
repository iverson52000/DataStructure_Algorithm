"""
230. Kth Smallest Element in a BST
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""

#recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root: return    
        self.dfs(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.dfs(root.right)
