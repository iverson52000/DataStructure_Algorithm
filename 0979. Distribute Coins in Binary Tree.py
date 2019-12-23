"""
979. Distribute Coins in Binary Tree
Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.
In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)
Return the number of moves required to make every node have exactly one coin.
"""

#post order

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, root) -> int:
        if not root: return 0
        left_res = self.dfs(root.left)
        right_res = self.dfs(root.right)
        self.res += abs(left_res)+abs(right_res)
        return root.val-1+left_res+right_res
