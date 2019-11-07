#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 11:02:18 2019

@author: alberthsu
"""

"""
332. Reconstruct Itinerary
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
"""

#directed graph+dfs

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = collections.defaultdict(list)
        res = []
        self.buildGraph(g, tickets)
        self.dfs(g, res, 'JFK')
        return res[::-1]
    
    def buildGraph(self, g, tickets):
        for start, end in tickets:
            g[start].append(end)
        for key in g:
            g[key].sort(reverse = True)
    
    def dfs(self, g, res, start):
        if not start: return
        while g[start]: self.dfs(g, res, g[start].pop())
        res.append(start)
