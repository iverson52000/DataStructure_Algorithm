import collections
import threading
import time
import queue
from collections import *
from typing import List
import random


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(set)
        res = [0] * n
        counts = [1] * n

        for i, j in edges:
            g[i].add(j)
            g[j].add(i)

        def dfs(root, pre):
            for i in g[root]:
                if i != pre:
                    dfs(i, root)
                    counts[root] += counts[i]
                    res[root] += res[i] + counts[i]

        def dfs2(root, pre):
            for i in g[root]:
                if i != pre:
                    res[i] = res[root] - counts[i] + n - counts[i]
                    dfs2(i, root)

        dfs(0, -1)
        dfs2(0, -1)

        return res
