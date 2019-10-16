#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:49:58 2019

@author: alberthsu
"""

"""
!37. Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
1.	Each of the digits 1-9 must occur exactly once in each row.
2.	Each of the digits 1-9 must occur exactly once in each column.
3.	Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.
"""

#dfs

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) != 9 or len(board[0]) != 9: return
        self.dfs(board, 0, 0)
    
    def dfs(self, board, r, c) -> bool:
        if r >= 9: return True
        if c >= 9: return self.dfs(board, r+1, 0)
        if board[r][c] == '.':
            for num in range(1, 10):
                board[r][c] = str(num)
                if self.isValid(board, r, c): 
                    if self.dfs(board, r, c+1): return True
                board[r][c] = '.'
        else: return self.dfs(board, r, c+1)
        return False
    
    def isValid(self, board, r, c) -> bool:
        for r_next in range(9):
            if r_next != r and board[r][c] == board[r_next][c]: return False
        for c_next in range(9):
            if c_next != c and board[r][c] == board[r][c_next]: return False
        for r_next in range(r//3*3, r//3*3+3):
            for c_next in range(c//3*3, c//3*3+3):
                if (r_next != r or c_next != c) and board[r][c] == board[r_next][c_next]: return False
        return True   
