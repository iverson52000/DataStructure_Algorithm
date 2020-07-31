"""
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
"""

# dp. Space: O(n) 


class Solution:

    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

# dp. Space: O(1) 


class Solution:

    def climbStairs(self, n: int) -> int:
        dp1 = dp2 = 1
        for i in range(n):
            dp1, dp2 = dp2, dp1 + dp2
        return dp1
