"""
!140. Word Break II
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
"""

#dfs

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        memo = {}
        return self.dfs(s, wordDict, memo)

    def dfs(self, s, wordDict, memo) -> list:
        if s in memo: return memo[s]
        if not s: return []
        res = []
        for word in wordDict:
            if s[:len(word)] != word: continue
            if word == s: res.append(word)
            else:
                res_rest = self.dfs(s[len(word):], wordDict, memo)
                for sentence_rest in res_rest:
                    sentence = word+' '+ sentence_rest
                    res.append(sentence)
        memo[s] = res
        return res
