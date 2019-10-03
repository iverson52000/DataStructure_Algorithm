#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:02:47 2019

@author: alberthsu
"""

"""
!4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
"""

#Binary search

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): return self.findMedianSortedArrays(nums2, nums1)
        
        n1 = len(nums1); n2 = len(nums2)
        left = 0; right = n1
        while left <= right:
            mid1 = (left+right)//2
            mid2 = (n1+n2+1)//2-mid1
            
            max_left_1 = nums1[mid1-1] if mid1 > 0 else float('-inf')
            max_left_2 = nums2[mid2-1] if mid2 > 0 else float('-inf')
            min_right_1 = nums1[mid1] if mid1 < n1 else float('inf')
            min_right_2 = nums2[mid2] if mid2 < n2 else float('inf')
            
            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                if (n1+n2)%2 == 0:
                    return (max(max_left_1, max_left_2)+min(min_right_1, min_right_2))/2
                else:
                    return max(max_left_1, max_left_2)
            elif max_left_1 > min_right_2: right = mid1-1
            else: left = mid1+1                

