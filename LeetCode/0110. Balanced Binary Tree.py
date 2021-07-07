"""
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

#dfs

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if root is None: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1 or abs(left-right) > 1: return -1
            return max(left, right) + 1
        return dfs(root) != -1
