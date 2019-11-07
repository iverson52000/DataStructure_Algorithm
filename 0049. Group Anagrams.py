"""
49. Group Anagrams
Given an array of strings, group anagrams together.
"""

#hashmap+sort

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []
        m = {}
        for word in strs:
            key = tuple(sorted(word))
            m[key] = m.get(key, [])+[word]
        return m.values()