"""
395. Longest Substring with At Least K Repeating Characters
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.
"""

#divide and conquer

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        m = collections.Counter(s)
        for char in m:
            if m[char] < k:
                return max(self.longestSubstring(sub_s, k) for sub_s in s.split(char))
        return len(s) 
