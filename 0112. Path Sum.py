"""
112. Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
"""

#dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        return self.dfs(root, sum)
    
    def dfs(self, root, sum) -> bool:
        if not root: return False
        if not root.left and not root.right and root.val == sum: return True
        return self.dfs(root.left, sum-root.val) or self.dfs(root.right, sum-root.val)
