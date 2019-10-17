#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:11:58 2019

@author: alberthsu
"""

"""
!224. Basic Calculator
Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
"""

#stack

class Solution:
    def calculate(self, s: str) -> int:
        pre_num = cur_num = 0
        sign = 1
        stack = []
        for c in s:
            if c.isdigit():
                cur_num = cur_num*10+int(c)
            elif c in ('-', '+'):
                pre_num += sign*cur_num
                cur_num = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                stack.append((sign, pre_num))
                sign = 1
                pre_num = 0
            elif c == ')':
                pop_sign, pop_num =stack.pop() 
                pre_num += sign*cur_num
                pre_num *= pop_sign
                pre_num += pop_num
                cur_num = 0
        return pre_num+sign*cur_num
