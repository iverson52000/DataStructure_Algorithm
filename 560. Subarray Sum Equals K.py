"""
560. Subarray Sum Equals K
Given an array of integers and an integer k, you need to find the total number of continuous 
subarrays whose sum equals to k.
"""

#prefix sum+hashmap

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        m = {0: 1}
        res = 0; summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            res += m.get(summ-k, 0)
            m[summ] = m.get(summ, 0)+1
        return res