#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 09:50:17 2019

@author: alberthsu
"""

"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
"""

#dfs

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit(): return [int(input)]
        res = []
        memo = []
        if input in memo: return memo[input]
        for i in range(len(input)):
            if input[i] in '+-*':
                left_input = self.diffWaysToCompute(input[:i])
                right_input = self.diffWaysToCompute(input[i+1:])
                for left in left_input:
                    for right in right_input:
                        res.append(self.ops(left, right, input[i]))
        memo[input] = res
        return res
    
    def ops(self, left, right, op) -> int:
        if op == '+': return left+right
        if op == '-': return left-right
        if op == '*': return left*right
            