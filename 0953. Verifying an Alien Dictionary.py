"""
953. Verifying an Alien Dictionary
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
"""

# hashmap+array


class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ind = {c: i for i, c in enumerate(order)}
        for word1, word2 in zip(words, words[1:]):
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return False
            for c1, c2 in zip(word1, word2):
                if ind[c1] < ind[c2]:
                    break
                elif ind[c1] > ind[c2]:
                    return False
        return True
