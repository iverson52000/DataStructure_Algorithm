"""
Given a string containing just the characters '(' and ')', find the length of the longest valid 
(well-formed) parentheses substring.
"""

#stack+two pointers

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        stack = []
        res = 0
        left = -1
        for i in range(len(s)):
            if s[i] == '(': stack.append(i)
            elif not stack: left = i
            else:
                stack.pop()
                if not stack: res = max(res, i-left)
                else: res = max(res, i-stack[-1])
        return res