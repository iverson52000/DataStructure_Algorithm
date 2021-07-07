"""
72. Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""

# 2d dp


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for i in range(n1 + 1)]
        for i in range(1, n1 + 1):
            dp[i][0] = i
        for i in range(1, n2 + 1):
            dp[0][i] = i
        for i1 in range(1, n1 + 1):
            for i2 in range(1, n2 + 1):
                if word1[i1 - 1] == word2[i2 - 1]:
                    dp[i1][i2] = dp[i1 - 1][i2 - 1]
                else:
                    dp[i1][i2] = min(dp[i1 - 1][i2], dp[i1]
                                     [i2 - 1], dp[i1 - 1][i2 - 1]) + 1
        return dp[n1][n2]
