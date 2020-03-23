"""
!124. Binary Tree Maximum Path Sum
Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
"""

# dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = float('-inf')
        self.dfs(root)
        return self.res

    def dfs(self, root) -> int:
        if not root:
            return 0
        left_val = max(self.dfs(root.left), 0)
        right_val = max(self.dfs(root.right), 0)
        self.res = max(self.res, root.val + left_val + right_val)
        return max(left_val, right_val) + root.val
