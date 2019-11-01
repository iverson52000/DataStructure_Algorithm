"""
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order 
of characters. No two characters may map to the same character but a character may map to itself.
"""

#hashmap

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1, m2 = {}, {}
        for i, val in enumerate(s):
            m1[val] = m1.get(val, [])+[i]
        for i, val in enumerate(t):
            m2[val] = m2.get(val, [])+[i]
        return sorted(m1.values()) == sorted(m2.values())

