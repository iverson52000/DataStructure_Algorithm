"""
*200. Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is 
surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""

#dfs

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        n_r = len(grid); n_c = len(grid[0])
        cnt = 0
        for r in range(n_r):
            for c in range(n_c):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    cnt += 1
        return cnt
    
    def dfs(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != '1': return
        grid[r][c] = '0'
        self.dfs(grid, r+1, c)
        self.dfs(grid, r-1, c)
        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)

#bfs

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    self.bfs(grid, r, c)
                    cnt += 1
        return cnt
    
    def bfs(self, grid, r, c):
        q = collections.deque()
        q.append((r, c))
        grid[r][c] = '0'
        dirs = [(0,1), (0,-1), (-1,0), (1,0)]
        while q:
            pop_r, pop_c = q.popleft()
            for dirr in dirs:
                r, c = pop_r + dirr[0], pop_c + dirr[1]
                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != '1': continue
                q.append((r, c))
                grid[r][c] = '0'

