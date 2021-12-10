import collections
import threading
import time
from heapq import *
from collections import *
from typing import *
import random


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        if not isConnected:
            return 0

        visited = set()
        res = 0

        for i in range(len(isConnected)):
            if i not in visited:
                q = collections.deque([i])
                while q:
                    p = q.popleft()
                    if p not in visited:
                        visited.add(p)
                        q += [k for k,
                              adj in enumerate(isConnected[p]) if adj and (k not in visited)]
                res += 1

        return res

# 20211209
