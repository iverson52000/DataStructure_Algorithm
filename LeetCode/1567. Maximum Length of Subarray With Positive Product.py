"""
1567. Maximum Length of Subarray With Positive Product

Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.
"""

# dp


class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)

        pos, neg = [0] * n, [0] * n
        if nums[0] > 0:
            pos[0] = 1
        if nums[0] < 0:
            neg[0] = 1

        res = pos[0]

        for i in range(1, n):
            # if nums[i] == 0, pos[i] won't be updated
            if nums[i] > 0:
                pos[i] = 1 + pos[i - 1]
                neg[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
            elif nums[i] < 0:
                pos[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
                neg[i] = 1 + pos[i - 1]
            res = max(res, pos[i])

        return res
