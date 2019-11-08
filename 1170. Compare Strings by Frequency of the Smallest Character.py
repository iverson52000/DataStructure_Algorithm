"""
1170. Compare Strings by Frequency of the Smallest Character

Let's define a function f(s) over a non-empty string s, which calculates the frequency of the 
smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character 
is "c" and its frequency is 2.
Now, given string arrays queries and words, return an integer array answer, where each answer[i] 
is the number of words such that f(queries[i]) < f(W), where W is a word in words.
"""

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words_cnt = sorted([w.count(min(w)) for w in words])
        res = []
        for query in queries:
            cnt = query.count(min(query))
            idx = bisect.bisect(words_cnt, cnt)
            res.append(len(words)-idx)
        return res
