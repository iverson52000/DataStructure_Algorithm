#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:44:37 2019

@author: alberthsu
"""

"""
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
"""

class Solution:
    def search(self, nums, target):
        if not nums: return -1
        left = 0; right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target: return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]: right = mid-1
                else: left = mid+1
            else:
                if nums[mid] < target <= nums[right]: left = mid+1
                else: right = mid-1
        return -1


