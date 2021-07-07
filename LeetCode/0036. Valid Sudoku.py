"""
36. Valid Sudoku
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
"""

#hashset


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False
        flag = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != '.':
                    num = board[r][c]
                    if (r, num) in flag or (num, c) in flag or (r // 3, c // 3, num) in flag:
                        return False
                    flag.add((r, num))
                    flag.add((num, c))
                    flag.add((r // 3, c // 3, num))
        return True
