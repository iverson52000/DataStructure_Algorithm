"""
257. Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.
"""

#preorder dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        path = ''
        res = []
        self.dfs(root, path, res)
        return res
    
    def dfs(self, root, path, res):
        if not root: return
        path = path+str(root.val)
        if not root.left and not root.right:
            res.append(path)
            return
        self.dfs(root.left, path+'->', res)
        self.dfs(root.right, path+'->', res)
