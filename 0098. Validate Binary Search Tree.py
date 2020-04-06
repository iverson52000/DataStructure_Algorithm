"""
*98. Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
•	The left subtree of a node contains only nodes with keys less than the node's key.
•	The right subtree of a node contains only nodes with keys greater than the node's key.
•	Both the left and right subtrees must also be binary search trees.
"""

#4/6
#dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        min_val = float('-inf')
        max_val = float('inf')
        return self.dfs(root, min_val, max_val)
    
    def dfs(self, root, min_val, max_val) -> bool:
        if not root: return True
        if root.val >= max_val or root.val <= min_val: return False
        left_bool = self.dfs(root.left, min_val, root.val)
        right_bool = self.dfs(root.right, root.val, max_val)
        return left_bool and right_bool

#iteration

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        pre = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if pre and node.val <= pre.val: return False
                pre = node
                root = node.right
        return True
