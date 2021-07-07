"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which 
has the largest sum and return its sum.
"""

#dp

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0

        res = float('-inf'); cur_sum = 0
        
        for num in nums:
            cur_sum = max(cur_sum+num, num)
            res = max(res, cur_sum)
            
        return res
