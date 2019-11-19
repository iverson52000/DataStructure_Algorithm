"""
$1057.Campus Bikes
On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. 
Each worker and bike is a 2D coordinate on this grid.
Our goal is to assign a bike to each worker. Among the available bikes and workers, 
we choose the (worker, bike) pair with the shortest Manhattan distance between each other, 
and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the same 
shortest Manhattan distance, we choose the pair with the smallest worker index; if there are 
multiple ways to do that, we choose the pair with the smallest bike index). We repeat this 
process until there are no available workers.
"""

#bucket sort

import collections

workers = [[0,0],[1,1],[2,0]]; bikes = [[1,0],[2,2],[2,1]]

def assignBikes(workers, bikes) -> list:
	n_workers = len(workers)
	n_bikes = len(bikes)
	res = [-1]*n_workers
	assigned = [False]*n_workers
	occupied = [False]*n_bikes
	bucket = collections.defaultdict()
	for w in len(n_workers):
		for b in len(n_bikes):
			dist = getDist(workers[w], bikes[b])
			if dist not in bucket: bucket[dist] = [[w, b]]
			else: bucket[dist] += [[w,b]]

	for dist in sorted(bucket):
		n_pair = len(bucket[dist])
		for pair in range(n_pair):
			w = bucket[dist][pair][0]
			b = bucket[dist][pair][1]
			if not assigned[w] and not occupied[b]:
				res[w] = b
				assigned[w] = True
				occupied[b]  =True
	return res


def getDist(worker, bike) -> int:
	return abs(worker[0]-bike[0])+abs(worker[1]-bike[1])