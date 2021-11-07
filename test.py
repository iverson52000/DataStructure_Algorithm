import collections
import threading
import time
import queue
from collections import *
from typing import List


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0

        res = 0
        dp = collections.defaultdict(int)

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c]:
                    dp[(r, c, 0)] = dp[(r, c - 1, 0)] + 1
                    dp[(r, c, 1)] = dp[(r - 1, c, 1)] + 1
                    dp[(r, c, 2)] = dp[(r - 1, c - 1, 2)] + 1
                    dp[(r, c, 3)] = dp[(r - 1, c + 1, 3)] + 1
                    res = max(res, dp[(r, c, 0)], dp[(r, c, 1)],
                              dp[(r, c, 2)], dp[(r, c, 3)])

        return res
