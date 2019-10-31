#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 11:30:00 2019

@author: alberthsu
"""

"""
15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0 
Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
"""

#Two pointer

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if not nums or nums[0] > 0 or nums[-1] < 0: return []
        res = []
        for i in range(len(nums)-2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue
            left = i+1; right = len(nums)-1
            while left < right:
                summ = nums[i]+nums[left]+nums[right]
                if summ == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]: left += 1
                    while left < right and nums[right] == nums[right-1]: right -= 1
                    left += 1; right -= 1
                elif summ < 0: left += 1
                else: right -= 1
        return res 

