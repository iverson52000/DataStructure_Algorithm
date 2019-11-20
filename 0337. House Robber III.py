"""
337. House Robber III
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without alerting the police.
"""

#dfs+memo

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        self.memo = {}
        return self.dfs(root)
    
    def dfs(self, root) -> int:
        if not root: return 0
        if root in self.memo: return self.memo[root]
        res = root.val
        if root.left: res += self.dfs(root.left.left)+self.dfs(root.left.right)
        if root.right: res += self.dfs(root.right.left)+self.dfs(root.right.right)
        res = max(res, self.dfs(root.left)+self.dfs(root.right))
        self.memo[root] = res
        return res


