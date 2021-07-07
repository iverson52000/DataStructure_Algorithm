#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:05:54 2019

@author: alberthsu
"""

"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
"""

class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda x: x[0])
        for i in range(1, len(intervals)):
            if interval[i][0] > interval[i-1][1]: return False
        return True
