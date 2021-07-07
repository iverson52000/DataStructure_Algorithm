"""
1277. Count Square Submatrices with All Ones
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
"""

# dp


class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        n_r = len(matrix)
        n_c = len(matrix[0])
        dp = [[0 if matrix[r][c] == 0 else 1 for c in range(
            n_c)] for r in range(n_r)]
        for r in range(1, n_r):
            for c in range(1, n_c):
                if matrix[r][c] == 1:
                    dp[r][c] = min(dp[r - 1][c], dp[r][c - 1],
                                   dp[r - 1][c - 1]) + 1
                else:
                    dp[r][c] = 0
        return sum(sum(row) for row in dp)
