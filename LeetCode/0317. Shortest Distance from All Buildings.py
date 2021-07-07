#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:18:08 2019

@author: alberthsu
"""

"""
$!317. Shortest Distance from All Buildings
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
•	Each 0 marks an empty land which you can pass by freely.
•	Each 1 marks a building which you cannot pass through.
•	Each 2 marks an obstacle which you cannot pass through.
"""

# bfs

import collections
test code:
grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]


def shortestDistance(self, grid) -> int:
    if not grid or len(grid) == 0:
        return -1
    res = float('inf')
    n_r = len(grid)
    n_c = len(grid[0])
    n_can_reach = [[0] * n_c for i in range(n_r)]
    dist = [[0] * n_c for i in range(n_r)]
    n_building = 0
    for r in range(n_r):
        for c in range(n_c):
            if grid[r][c] == 1:
                n_building += 1
                self.bfs(grid, r, c, dist, n_can_reach)
    for r in range(n_r):
        for c in range(n_c):
            if n_can_reach[r][c] == n_building:
                res = min(res, dist[r][c])
    return -1 if res == float('inf') else res


def bfs(self, grid, r, c, dist, n_can_reach):
    n_r = len(grid)
    n_c = len(grid[0])
    visited = [[False] * n_c for i in range(n_r)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = collections.deque()
    q.append((r, c))
    visited[r][c] = True
    distance = 0
    while q:
        distance += 1
        for i in range(len(q)):
            r, c = q.popleft()
            for dirr in dirs:
                r_next = dirr[0] + r
                c_next = dirr[1] + c
                if self.isValid(grid, r_next, c_next, visited):
                    dist[r_next][c_next] += distance
                    n_can_reach[r_next][c_next] += 1
                    q.append((r_next, c_next))
                    visited[r_next][c_next] = True


def isValid(self, grid, r_next, c_next, visited) -> bool:
    if r_next >= len(grid) or r_next < 0 or c_next >= len(grid[0]) or c_next < 0:
        return False
    if visited[r_next][c_next]:
        return False
    if grid[r_next][c_next] != 0:
        return False
    return True
