"""
91. Decode Ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
"""

class Solution:
    def numDecodings(self, s) -> int:
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, n+1):
            oneDigit = int(s[i-1:i])  #dp(2226) = dp(222)+6 and dp(22)+26
            twoDigit = int(s[i-2:i])
            if 0 < oneDigit <= 9: dp[i] += dp[i-1]
            if 10 <= twoDigit <= 26: dp[i] += dp[i-2]
        return dp[n]
