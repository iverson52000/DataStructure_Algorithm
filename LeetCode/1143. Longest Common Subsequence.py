"""
1143. Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest 
common subsequence.
"""

# 2d dp


class Solution:

    def longestCommonSubsequence(self, A: List[int], B: List[int]) -> int:
        n_A = len(A)
        n_B = len(B)
        dp = [[0] * (n_B + 1) for i in range(n_A + 1)]
        for i in range(1, n_A + 1):
            for j in range(1, n_B + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n_A][n_B]
