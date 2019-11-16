"""
221. Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
"""

#dp

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        n_r = len(matrix); n_c = len(matrix[0])
        dp = [[0]*n_c for i in range(n_r)]
        
        for r in range(n_r): dp[r][0] = 1 if matrix[r][0] == '1' else 0
        for c in range(n_c): dp[0][c] = 1 if matrix[0][c] == '1' else 0
        
        for r in range(1, n_r):
            for c in range(1, n_c):
                if matrix[r][c] == '1':
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])+1
                else:
                    dp[r][c] = 0
        
        res = max(max(row) for row in dp)
        return res**2
                