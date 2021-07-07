"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
"""

#Trie+dfs

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        self.res = []
        path = ''
        node = trie.root
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.dfs(board, node, r, c, path)
        return self.res
    
    def dfs(self, board, node, r, c, path):
        if node.isWord:
            self.res.append(path)
            node.isWord = False
            return
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]): return 
        tmp = board[r][c]
        node = node.children.get(tmp)
        if not node: return
        board[r][c] = '#'
        self.dfs(board, node, r+1, c, path+tmp)
        self.dfs(board, node, r-1, c, path+tmp)
        self.dfs(board, node, r, c+1, path+tmp)
        self.dfs(board, node, r, c-1, path+tmp)
        board[r][c] = tmp
        