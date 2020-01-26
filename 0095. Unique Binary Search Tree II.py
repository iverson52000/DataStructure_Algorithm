"""
95. Unique Binary Search Trees II
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 
1, 2 ... n.
"""

#1/26/20

#dfs+memo

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        memo = {}
        return self.dfs(1, n, memo)

    def dfs(self, left_num, right_num, memo) -> List[TreeNode]:
        if left_num > right_num: return [None]
        res = []
        if (left_num, right_num) in memo: return memo[(left, right)]
        for i in range(left_num, right_num +1):
            left_res = self.dfs(left_num, i-1, memo)    #divide
            right_res = self.dfs(i+1, right_num, memo)
            for left_node in left_res:         #conquer
                for right_node in right_res:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    res.append(root)
        memo[(left_num, right_num)] = res
        return res
