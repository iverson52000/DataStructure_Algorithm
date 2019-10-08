#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:18:27 2019

@author: alberthsu
"""

"""
*300. Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing subsequence.
"""

#dp

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

#Binary search
        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = []
        for i in range(len(nums)):
            left = 0; right = len(dp)-1
            while left <= right:
                mid = (left+right)//2
                if nums[i] > dp[mid]: left = mid+1
                else: right = mid-1
            if left >= len(dp): dp.append(nums[i])
            else: dp[left] = nums[i]
        return len(dp)
