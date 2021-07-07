
"""
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if 
the input string is valid.
"""

# stack


class Solution:

    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            else:
                if not stack:
                    return False
                elif char == ')' and stack.pop() != '(':
                    return False
                elif char == ']' and stack.pop() != '[':
                    return False
                elif char == '}' and stack.pop() != '{':
                    return False
        return len(stack) == 0
