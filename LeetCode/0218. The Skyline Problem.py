#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:10:40 2019

@author: alberthsu
"""

"""
218. The Skyline Problem
"""

from heapq import *

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = [(L, R, -H) for L, R, H in buildings]
        events += [(R, 0, 0) for _, R, _ in buildings]
        events.sort(key = lambda x: (x[0], x[2]))
        res = [[0, 0]]  #(L, H)
        heap = [(0, float('inf'))] #(negH, R)
        for L, R, negH in events:
            if negH != 0: heappush(heap, (negH, R))
            while L >= heap[0][1]: heappop(heap)
            if res[-1][1] != -heap[0][0]: res += [[L, -heap[0][0]]]
        return res[1:]