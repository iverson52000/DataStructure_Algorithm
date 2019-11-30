"""
*127. Word Ladder
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
1.	Only one letter can be changed at a time.
2.	Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
"""

#bfs

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        q = collections.deque()
        q.append((beginWord, 1))
        visited = set()
        chars = string.ascii_lowercase
        while q:
            word, level = q.popleft()
            if word == endWord: return level
            for i in range(len(word)):
                for char in chars:
                    next_word = word[:i]+char+word[i+1:]
                    if next_word in wordList and next_word not in visited:
                        q.append((next_word, level+1))
                        visited.add(next_word)
        return 0
