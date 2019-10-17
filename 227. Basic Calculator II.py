#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:45:30 2019

@author: alberthsu
"""

"""
227. Basic Calculator II
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
"""

class Solution:
    def calculate(self, s: str) -> int:
        s += '+0'   #for the last num
        stack = []; cur_num = 0; sign = "+"
        for c in s:
            if c.isdigit(): cur_num = cur_num*10 + int(c)
            elif not c.isspace():
                if   sign == "+": stack.append(cur_num)
                elif sign == "-": stack.append(-cur_num)
                elif sign == "*": stack.append(stack.pop()*cur_num)
                elif sign == '/': stack.append(int(stack.pop()/cur_num))                
                sign = c; cur_num = 0
        return sum(stack) 
