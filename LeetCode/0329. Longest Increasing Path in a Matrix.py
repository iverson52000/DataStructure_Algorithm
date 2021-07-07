"""
329. Longest Increasing Path in a Matrix
Given an integer matrix, find the length of the longest increasing path.
From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
"""

#dfs
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        res = 0
        memo = collections.defaultdict(int)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res = max(res, self.dfs(matrix, memo, r, c))                
        return res
    
    def dfs(self, matrix, memo, r, c) -> int:
        if (r, c) in memo: return memo[(r, c)]           
        maxx = 1; path = 0     
        for dir0, dir1 in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            r_next = r+dir0; c_next = c+dir1
            if r_next < 0 or r_next >= len(matrix) or c_next < 0 or c_next >= len(matrix[0]) or matrix[r_next][c_next] <= matrix[r][c]: continue
            path = 1+self.dfs(matrix, memo, r_next, c_next)
            maxx = max(maxx, path)
        memo[(r, c)] = maxx 
        return maxx
