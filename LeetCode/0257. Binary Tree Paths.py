"""
257. Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.
"""

# preorder dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        path = ''
        res = []
        self.dfs(root, path, res)
        return res

    def dfs(self, root, path, res):
        if not root:
            return
        path = path + str(root.val)
        if not root.left and not root.right:
            res.append(path)
            return
        self.dfs(root.left, path + '->', res)
        self.dfs(root.right, path + '->', res)

# Iteration

class Solution:
    def binaryTreePaths1(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path + str(node.val))
            if node.right:
                stack.append((node.right, path + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, path + str(node.val) + "->"))
        return res
