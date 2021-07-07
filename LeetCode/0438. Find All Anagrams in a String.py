"""
438. Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.
"""

# hash


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        n_s, n_p, S, P, res = len(s), len(p), 0, 0, []
        if n_p > n_s:
            return res
        for i in range(n_p):
            S, P = S + hash(s[i]), P + hash(p[i])
        if S == P:
            res.append(0)
        for i in range(n_p, n_s):
            S += hash(s[i]) - hash(s[i - n_p])
            if S == P:
                res.append(i - n_p + 1)
        return res
