"""
947. Most Stones Removed with Same Row or Column
On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.
Now, a move consists of removing a stone that shares a column or row with another stone on the grid.
What is the largest possible number of moves we can make?
"""

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        g = collections.defaultdict(set)
        for i in range(len(stones)):
            x1, y1 = stones[i]
            for j in range(i+1,len(stones)):
                x2, y2=stones[j]
                if x1 == x2 or y1 == y2:
                    g[i].add(j)
                    g[j].add(i)
        n_g = 0
        visited = set()
        for i in range(len(stones)):
            if i not in visited:
                self.dfs(i, visited, g)
                n_g += 1
        return len(stones)-n_g
                
    def dfs(self, i, visited, g):
        visited.add(i)
        for j in g[i]:
            if j not in visited:
                self.dfs(j, visited, g)
