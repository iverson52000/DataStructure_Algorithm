"""
96. Unique Binary Search Trees
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
"""

#dp

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]
