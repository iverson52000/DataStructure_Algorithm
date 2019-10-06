#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 10:35:13 2019

@author: alberthsu
"""

"""
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
"""

#stack

class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        stack = []
        for char in s:
            if char in ('(', '[', '{'): stack.append(char)
            else:
                if stack: cur = stack.pop()
                else: return False
                if char == ')' and cur != '(': return False
                if char == ']' and cur != '[': return False
                if char == '}' and cur != '{': return False
        return len(stack) == 0 