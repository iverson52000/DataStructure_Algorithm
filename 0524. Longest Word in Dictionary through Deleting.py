"""
524. Longest Word in Dictionary through Deleting
Given a string and a string dictionary, find the longest string in the dictionary that can be formed 
by deleting some characters of the given string. If there are more than one possible results, return 
the longest word with the smallest lexicographical order. If there is no possible result, return the 
empty string.
"""

#sort and traverse. two pointers

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            i_word = 0
            for c in s:
                if i_word < len(word) and word[i_word] == c: i_word += 1
            if i == len(word): return word
        return ""

