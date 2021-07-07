"""
$!305. Number of Islands II
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation 
which turns the water at position (row, col) into a land. Given a list of positions to operate, count the 
number of islands after each addLand operation. An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

#Union Find

m = 3
n = 3
positions = [[0,0], [0,1], [1,2], [2,1]]

res = []
cnt = 0
roots = [-1]*m*n
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for position in positions:
    idx = n*position[0]+position[1]
    if roots[idx] == -1:
        roots[idx] = idx
        cnt += 1
    for d in dirs:
        r_next = position[0]+d[0]
        c_next = position[1]+d[1]
        idx_next = n*r_next+c_next
        if r_next < 0 or r_next >= m or c_next < 0 or c_next >= n or roots[idx_next] == -1: continue
        root_next = findRoot(roots, idx_next); root_island = findRoot(roots, idx)
        if root_next != root_island:
            roots[root_next] = root_island
            cnt -= 1
    res.append(cnt)	
    return res

def findRoot(roots, idx):
    if idx == roots[idx]: return idx
    else: return findRoot(roots, roots[idx])
