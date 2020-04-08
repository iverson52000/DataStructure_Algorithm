"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by 
its upper left corner (row1, col1) and lower right corner (row2, col2)."""

# dp


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        self.dp = [[0 for c in range(len(matrix[0]) + 1)]
                   for r in range(len(matrix) + 1)]
        for r in range(1, len(matrix) + 1):
            for c in range(1, len(matrix[0]) + 1):
                self.dp[r][c] = self.dp[r][c - 1] + self.dp[r - 1][c] - \
                    self.dp[r - 1][c - 1] + matrix[r - 1][c - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]
