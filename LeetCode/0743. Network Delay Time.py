"""
743. Network Delay Time
There are N network nodes, labelled 1 to N.
Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source 
node, v is the target node, and w is the time it takes for a signal to travel from source to target.
Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
"""

#dijkstra bfs

from heapq import *

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        g = collections.defaultdict(list) 
        for u, v, w in times: g[u].append((w, v))
        dist = {} 
        heap = [(0, K)]
        while heap:
            if len(dist) == N: break
            d, node = heappop(heap)
            if node in dist: continue
            dist[node] = d
            for w, v in g[node]:
                if v not in dist: heappush(heap, (d+w, v))
        return max(dist.values()) if len(dist) == N else -1