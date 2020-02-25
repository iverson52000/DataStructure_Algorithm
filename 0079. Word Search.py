"""
79. Word Search
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells 
are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

#dfs

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]: return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(board, word, r, c):
                    return True
        return False   
        
    def dfs(self, board, word, r, c):
        if len(word) == 0: return True
        if r >= len(board) or r < 0 or c >= len(board[0]) or c < 0 or board[r][c] != word[0]: 
            return False
        tmp = board[r][c]
        board[r][c] = '#'
        res = self.dfs(board, word[1:], r+1, c) or \
        self.dfs(board, word[1:], r-1, c) or \
        self.dfs(board, word[1:], r, c+1) or \
        self.dfs(board, word[1:], r, c-1)
        board[r][c] = tmp
        return res
