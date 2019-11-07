#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:14:28 2019

@author: alberthsu
"""

"""
301. Remove Invalid Parentheses
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
"""

#bfs
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        q = collections.deque()
        q.append(s)
        visited = set()
        found = False
        
        while q:
            cur = q.popleft()
            if self.isValid(cur):
                res.append(cur)
                found = True
            if found: continue
            for i in range(len(cur)):
                if cur[i] not in ['(', ')']: continue
                next_s = cur[:i]+cur[i+1:]
                if next_s not in visited:
                    q.append(next_s)
                    visited.add(next_s)
        return res
                
    def isValid(self, cur):
        left = 0
        for i in range(len(cur)):
            if cur[i] == '(': left += 1
            if cur[i] == ')': left -= 1
            if left < 0: return False
        return left == 0