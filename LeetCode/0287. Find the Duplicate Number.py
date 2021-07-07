"""
*287. Find the Duplicate Number
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
"""

# binary search


class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)
        while left <= right:
            mid = (left + right) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid - 1
        return left
