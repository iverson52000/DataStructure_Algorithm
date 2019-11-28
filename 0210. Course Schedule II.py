"""
210. Course Schedule II
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
"""

#topological sort dfs

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = collections.defaultdict(set)
        self.res = []
        visited = [0]*numCourses
        for edge in prerequisites:
            out = edge[1]; inn = edge[0]
            g[inn].add(out)     
        for i in range(numCourses):
            if not self.dfs(g, visited, i): return []      
        return self.res
    
    def dfs(self, graph, visited, i) -> bool:
        if visited[i] == -1: return False   #is being visited
        if visited[i] == 1: return True     #has been visited but no ring
        visited[i] = -1 	#visiting
        for j in graph[i]:
            if not self.dfs(graph, visited, j): return False
        visited[i] = 1      #done visited all neighbors
        self.res.append(i)
        return True
