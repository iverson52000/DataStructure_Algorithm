#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:39:19 2019

@author: alberthsu
"""

"""
269. Alien Dictionary
There is a new alien language which uses the latin alphabet. However, the order among letters 
are unknown to you. You receive a list of non-empty words from the dictionary, where words are 
sorted lexicographically by the rules of this new language. Derive the order of letters in this 
language.

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"

"""

#directed graph+bfs

import collections
words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

res = []
indegree = collections.defaultdict(int)
g = collections.defaultdict(set)
buildGraph(g, words, indegree)
bfs(res, g, indegree)

def buildGraph(g, words, indegree):
    for word in words:
       for char in word:
           g[char] = set()
    for i in range(1, len(words)):
        first = words[i-1]
        second = words[i]
        length = min(len(first), len(second))
        for j in range(length):
            if first[j] != second[j]:
                out = first[j]
                inn = second[j]
                if inn not in g[out]:
                    g[out].add(inn)
                    indegree[inn] += 1
                    break

def bfs(res, g, indegree) -> str:
    q = collections.deque()
    for out in g.keys():
        if indegree[out] == 0:
            res.append(out)
            q.append(out)
    while q:
        out = q.popleft()
        if g[out] == None or len(g[out]) == 0: continue
        for inn in g[out]:
            indegree[inn] -= 1
            if indegree[inn] == 0:
                q.append(inn)
                res.append(inn)
    return ''.join(res) if len(res) == len(g) else ''
