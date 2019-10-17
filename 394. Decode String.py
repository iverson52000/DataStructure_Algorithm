#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:52:21 2019

@author: alberthsu
"""

"""
*394. Decode String
Given an encoded string, return it's decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
"""

#Stack

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []; cur_num = 0; cur_str = ''
        for c in s:
            if c.isdigit():
                cur_num = cur_num*10 + int(c)
            elif c == '[':
               stack.append((cur_num, cur_str))                
               cur_str = ''
               cur_num = 0
            elif c == ']':
                pre_num, pre_str = stack.pop()
                cur_str = pre_str+pre_num*cur_str
            else:
                cur_str += c
        return cur_str
