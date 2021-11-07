import collections
import threading
import time
import queue
from collections import *
from typing import List
import random


class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}

        def dfs(l, r) -> int:
            if l > r:
                return 0
            if (l, r) not in memo:
                res = dfs(l+1, r) + 1
                for k in range(l+1, r+1):
                    if s[k] == s[l]:
                        res = min(res, dfs(l, k-1) + dfs(k+1, r))
                memo[(l, r)] = res
            return memo[(l, r)]

        return dfs(0, len(s) - 1)


random.ra
