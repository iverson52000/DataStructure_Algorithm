import collections
import threading
import time
import queue
from collections import *


graph = collections.defaultdict(list)
   for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    # init variables
    m = len(targetPath)
    dp = [[m] * n for _ in range(m)]
    prev = [[0] * n for _ in range(m)]

    # populate dp
    for v in range(n):
        dp[0][v] = (names[v] != targetPath[0])
    for i in range(1, m):
        for v in range(n):
            for u in graph[v]:
                if dp[i-1][u] < dp[i][v]:
                    dp[i][v] = dp[i-1][u]
                    prev[i][v] = u
            dp[i][v] += (names[v] != targetPath[i])

    # re-construct path
    path, min_dist = [0], m
    for v in range(n):
        if dp[-1][v] < min_dist:
            min_dist = dp[-1][v]
            path[0] = v
    for i in range(m - 1, 0, -1):
        u = prev[i][path[-1]]
        path.append(u)

    return path[::-1]
