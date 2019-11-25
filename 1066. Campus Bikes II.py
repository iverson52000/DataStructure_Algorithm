"""
1066.Campus Bikes II
On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and 
bike is a 2D coordinate on this grid.
We assign one unique bike to each worker so that the sum of the Manhattan distances between each 
worker and their assigned bike is minimized.
The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.
"""

#dfs+backtracking

workers = [[0,0],[2,1]]; bikes = [[1,2],[3,3]]

res = float('-inf')
n_bikes = len(bikes)
occupied = [False]*n_bikes
dfs(0, workers, bikes, 0, assigned)

def dfs(i_worker, workers, bikes, summ, assigned):
	if i_worker == len(workers):
		res = min(res, summ)
		return
	if summ > res: return
	for i in range(len(bikes)):
		if not assigned[i]:
			assigned[i] = True
			dfs(i_worker+1, workers, bikes, summ+getDist(workers[i_worker]), bike[i], assigned)
			assigned[i] = False

def getDist(worker, bike):
    return abs(worker[0]-bike[0])+abs(worker[1]-bike[1])



