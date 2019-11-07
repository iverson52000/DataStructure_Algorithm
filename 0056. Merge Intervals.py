#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:42:15 2019

@author: alberthsu
"""

"""
56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort(key = lambda x: x[0])	#nedd to sort first!
        res = [intervals[0]]	#list of list
        for interval in intervals[1:]:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else: res.append(interval)
        return res 
