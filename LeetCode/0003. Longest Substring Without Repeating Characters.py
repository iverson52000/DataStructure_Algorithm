"""
*3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.
"""

# Sliding window


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = -1
        n = len(s)
        m = {}
        for i in range(n):
            if s[i] in m and m[s[i]] > left:
                left = m[s[i]]
            m[s[i]] = i
            res = max(res, i-left)
        return res
