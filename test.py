import collections
import threading
import time
import queue
from collections import *
from typing import List
import random


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n_r, n_c = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = collections.deque([(0, 0, 0)])
        dp = {}

        while q:
            r, c, cost = q.popleft()
            while 0 <= r < n_r and 0 <= c < n_c and (r, c) not in dp:
                dp[(r, c)] = cost
                q += [(r+dir0, c+dir1, cost+1) for dir0, dir1 in dirs]
                dir0, dir1 = dirs[grid[r][c]-1]
                r, c = r+dir0, c+dir1

        return dp[n_r-1, n_c-1]

# 20211117
