"""
!76. Minimum Window Substring
Given a string S and a string T, find the minimum window in S which will contain all the characters 
in T in complexity O(n).
"""

# Two pointer+hashmap


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        missing = len(t)
        m = collections.Counter(t)
        left = left_min = right_min = 0
        for i in range(len(s)):
            if m[s[i]] > 0:
                missing -= 1
            m[s[i]] -= 1
            if missing == 0:
                while left < i and m[s[left]] < 0:
                    m[s[left]] += 1
                    left += 1
                m[s[left]] += 1
                missing += 1
                if right_min == 0 or i + 1 - left < right_min - left_min:
                    right_min, left_min = i + 1, left
                left += 1
        return s[left_min:right_min]
