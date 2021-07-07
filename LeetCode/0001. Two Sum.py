
"""
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a 
specific target.
You may assume that each input would have exactly one solution, and you may not use the 
same element twice.
"""

#hashmap

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return []
        m = {}
        
        for i in range(len(nums)):
            if nums[i] in m: return [m[nums[i]], i]
            else: m[target-nums[i]] = i
