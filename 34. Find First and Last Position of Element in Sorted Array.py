#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:24:50 2019

@author: alberthsu
"""

"""
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
"""

#binary search

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchLeft(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] >= target: right = mid-1	#target is in the left. Search left boundary
                elif nums[mid] < target: left = mid+1
            return left

        def binarySearchRight(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] > target: right = mid-1	#target is in the left. Search right boundary
                elif nums[mid] <= target: left = mid+1
            return right
        
        left_pos, right_pos = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left_pos, right_pos) if left_pos <= right_pos else [-1, -1]
