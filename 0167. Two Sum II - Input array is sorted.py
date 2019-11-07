#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 11:12:40 2019

@author: alberthsu
"""

"""
167. Two Sum II - Input array is sorted
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers: return []
        left = 0; right = len(numbers)-1
        while left < right:
            if numbers[left]+numbers[right] == target: return [left+1, right+1]
            elif numbers[left]+numbers[right] > target: right -= 1
            else: left += 1
