"""
1458. Max Dot Product of Two Subsequences
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.
"""

# 2d dp


class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * (n2) for i in range(n1)]
        for i in range(n1):
            for j in range(n2):
                dp[i][j] = nums1[i] * nums2[j]
                if i != 0 and j != 0:
                    dp[i][j] += max(dp[i - 1][j - 1], 0)
                if i != 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j != 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])
        return dp[-1][-1]
