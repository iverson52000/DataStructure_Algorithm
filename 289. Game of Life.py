"""
289. Game of Life
"""

#matrix

"""
cells nearby	change	state
	<2			 1->0	  2
	2, 3		 1->1	  1
	>3			 1->0	  2
	3			 0->1	  3
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        n_r = len(board); n_c = len(board[0])
        for r in range(n_r):
            for c in range(n_c):
                cells = 0
                for r_next in range(max(0, r-1), min(r+2, n_r)):
                    for c_next in range(max(0, c-1), min(c+2, n_c)):
                        if (r_next, c_next) != (r, c) and board[r_next][c_next] in (1, 2):
                            cells += 1
                if board[r][c] == 0:
                    if cells == 3:
                        board[r][c] = 3
                else:
                    if cells < 2 or cells > 3:
                        board[r][c] = 2

        for r in range(n_r):
            for c in range(n_c):
                if board[r][c] == 2: board[r][c] = 0
                elif board[r][c] == 3: board[r][c] = 1
