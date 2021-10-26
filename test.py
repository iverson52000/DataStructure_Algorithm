import threading
import time
import queue


# 20211025
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [[float('inf')]*(m+1) for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[j-1] == s2[i-1]:
                    if i == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = dp[i][j-1]+1

        res = min(dp[-1])

        if res == float('inf'):
            return ''

        for i in range(1, m+1):
            if dp[-1][i] == res:
                return s1[i-res:i]
