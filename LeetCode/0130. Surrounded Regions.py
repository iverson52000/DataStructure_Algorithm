"""
130. Surrounded Regions
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""

# dfs


class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        n_r = len(board)
        n_c = len(board[0])

        for r in range(n_r):
            if board[r][0] == 'O':
                self.dfs(board, r, 0)
            if board[r][n_c - 1] == 'O':
                self.dfs(board, r, n_c - 1)
        for c in range(n_c):
            if board[0][c] == 'O':
                self.dfs(board, 0, c)
            if board[n_r - 1][c] == 'O':
                self.dfs(board, n_r - 1, c)

        for r in range(n_r):
            for c in range(n_c):
                if board[r][c] == 'S':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'

    def dfs(self, board, r, c):
        n_r = len(board)
        n_c = len(board[0])
        if r < 0 or r >= n_r or c < 0 or c >= n_c or board[r][c] != 'O':
            return
        board[r][c] = 'S'
        self.dfs(board, r + 1, c)
        self.dfs(board, r - 1, c)
        self.dfs(board, r, c + 1)
        self.dfs(board, r, c - 1)
