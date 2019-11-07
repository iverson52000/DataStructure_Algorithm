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
            
            left_max_1 = nums1[mid1-1] if mid1 > 0 else float('-inf')
            left_max_2 = nums2[mid2-1] if mid2 > 0 else float('-inf')
            right_min_1 = nums1[mid1] if mid1 < n1 else float('inf')
            right_min_2 = nums2[mid2] if mid2 < n2 else float('inf')
            
            if left_max_1 <= right_min_2 and left_max_2 <= right_min_1:
                if (n1+n2)%2 == 0:
                    return (max(left_max_1, left_max_2)+min(right_min_1, right_min_2))/2
                else:
                    return max(left_max_1, left_max_2)
            elif left_max_1 > right_min_2: right = mid1-1
            else: left = mid1+1                
             

