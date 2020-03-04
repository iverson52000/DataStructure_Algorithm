"""
10. Regular Expression Matching
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
"""

# dp


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        n_s = len(s)
        n_p = len(p)
        dp = [[False] * (n_p + 1) for i in range(n_s + 1)]  # n_s x n_p
        dp[0][0] = True
        for i_p in range(1, n_p + 1):
            if p[i_p - 1] == '*':
                dp[0][i_p] = dp[0][i_p - 2]
        for i_s in range(1, n_s + 1):
            for i_p in range(1, n_p + 1):
                if s[i_s - 1] == p[i_p - 1] or p[i_p - 1] == '.':
                    dp[i_s][i_p] = dp[i_s - 1][i_p - 1]
                elif p[i_p - 1] == '*':
                    dp[i_s][i_p] = dp[i_s][i_p - 2]
                    if s[i_s - 1] == p[i_p - 2] or p[i_p - 2] == '.':
                        dp[i_s][i_p] = dp[i_s][i_p] or dp[i_s - 1][i_p]
        return dp[n_s][n_p]
