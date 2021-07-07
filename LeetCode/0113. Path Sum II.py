"""
113. Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
"""

#recursion

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        res = []
        path = []
        self.dfs(root, sum, res, path)
        return res
    
    def dfs(self, root, sum, res, path):
        if not root: return
        path.append(root.val)
        if not root.left and not root.right and root.val == sum:
            res.append(path.copy())
        self.dfs(root.left, sum-root.val, res, path)
        self.dfs(root.right, sum-root.val, res, path)
        path.pop()
