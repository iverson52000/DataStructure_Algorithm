#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:07:16 2019

@author: alberthsu
"""

"""
$253. Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] 
(si < ei), find the minimum number of conference rooms 
"""

#scanning line

import collections

def minMeetingRooms(self, intervals):
    m = collections.defaultdict(int)
    for interval in intervals:
        m[interval[0]] += 1
        m[interval[1]] -= 1
    room, res = 0
    for time in sorted(m):
        room += m[time]
        res = max(res, room)
    return res

#heap
    
from heapq import *

def minMeetingRooms(self, intervals):
    intervals.sort(key = lambda x: x[0])
    heap = []
    for interval in intervals:
        if heap and interval[0] >= heap[0]: heappop(heap)
        heappush(heap, interval[1])
    return len(heap)
        