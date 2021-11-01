import threading
import time
import queue
from collections import *


def dfs(i):
            visited[i] = True
            neigh_depths = []
            for j in adj_lst[i]:
                if not visited[j]:
                    neigh_depths.append(dfs(j))
            neigh_depths.sort(reverse=True)
            if not neigh_depths:
                return 1
            else:
                diameter[0] = max(diameter[0], sum(neigh_depths[:2]))
                return 1 + neigh_depths[0]

        if not edges:
            return 0
        n = len(edges)
        adj_lst = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)
        diameter = [0]
        visited = (n + 1) * [False]
        for i in range(n + 1):
            if not visited[i]:
                dfs(i)
        return diameter[0]
