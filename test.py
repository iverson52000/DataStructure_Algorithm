import threading
import time
import queue


# 20211028
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        def find(city) -> int:
            if parents[city] != city:
                parents[city] = find(parents[city])

            return parents[city]

        def union(c1, c2) -> bool:
            root1, root2 = find(c1), find(c2)
            if root1 == root2:
                return False
            parents[root2] = root1

            return True

        parents = {city: city for city in range(1, n+1)}
        connections.sort(key=lambda x: x[2])
        total = 0

        for city1, city2, cost in connections:
            if union(city1, city2):
                total += cost

        root = find(n)

        return total if all(root == find(city) for city in range(1, n+1)) else -1
