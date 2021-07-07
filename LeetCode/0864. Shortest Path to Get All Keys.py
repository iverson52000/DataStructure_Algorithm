"""
864. Shortest Path to Get All Keys
We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks.
We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can't walk over a lock unless we have the corresponding key.
For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.
Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.
"""

#bfs

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n_r, n_c = len(grid), len(grid[0])
        n_keys = 0
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]     
        
        for r in range(n_r):
            for c in range(n_c):
                if grid[r][c] == '@':
                    r_start = r
                    c_start = c
                elif grid[r][c] in "abcdef":
                    n_keys += 1
        
        q = collections.deque()
        q.append([r_start, c_start, 0, ".@abcdef", 0])
        visited = set()
        
        while q:
            r_pop, c_pop, moves, keys, n_collect = q.popleft()
            if grid[r_pop][c_pop] in "abcdef" and grid[r_pop][c_pop].upper() not in keys:
                keys += grid[r_pop][c_pop].upper()
                n_collect += 1     
            if n_collect == n_keys: return moves
            for dir0, dir1 in dirs:
                r = r_pop+dir0
                c = c_pop+dir1
                if 0 <= r < n_r and 0 <= c < n_c and grid[r][c] in keys:
                    if (r, c, keys) not in visited:
                        visited.add((r, c, keys))
                        q.append([r, c, moves+1, keys, n_collect])
        return -1
