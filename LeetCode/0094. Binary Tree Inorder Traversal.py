"""
94. Binary Tree Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values.
"""

#iteration

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        res, s = [], []
        while s or root:
            if root:
                s.append(root)
                root = root.left
            else:
                node = s.pop()
                res.append(node.val)
                root = node.right
        return res


#dfs

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res
        
    def dfs(self, root, res): 
        if root is None: return
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right,res)
