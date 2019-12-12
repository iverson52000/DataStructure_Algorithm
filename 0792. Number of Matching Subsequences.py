"""
792. Number of Matching Subsequences
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.
"""

#hashmap+binary search+recursion

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        m_idx = collections.defaultdict(list)
        for i in range(len(S)):
            m_idx[S[i]].append(i)
        return sum(self.isMatch(word, m_idx, 0, 0) for word in words)
            
    def isMatch(self, word, m_idx, i_word, i_S) -> bool:
            if i_word == len(word): return True
            indices = m_idx[word[i_word]]
            if len(indices) == 0 or i_S > indices[-1]: return False
            i = indices[bisect.bisect_left(indices, i_S)]
            return self.isMatch(word, m_idx, i_word+1, i+1)
