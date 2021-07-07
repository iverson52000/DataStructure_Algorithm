"""
63. Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
"""

#2/12

#dp

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1: return 0
        n_r = len(obstacleGrid); n_c = len(obstacleGrid[0]) 
        dp = [[0]*(n_c+1) for i in range(n_r+1)]
        dp[0][1] = 1
        for r in range(1, n_r+1):
            for c in range(1, n_c+1):
                if obstacleGrid[r-1][c-1] != 1:
                    dp[r][c] = dp[r][c-1]+dp[r-1][c]
                else:
                    dp[r][c] = 0
        return dp[-1][-1]

#1d dp

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1: return 0
        
        n_r = len(obstacleGrid); n_c = len(obstacleGrid[0])
        dp = [0 for i in range(n_c+1)]
        dp[1]= 1
        for r in range(1, n_r+1):
            for c in range(1, n_c+1):
                if obstacleGrid[r-1][c-1] == 1: 
                    dp[c] = 0   #needed for 1D dp!
                    continue
                dp[c] += dp[c-1]
        return dp[n_c]

