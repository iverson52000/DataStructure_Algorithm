"""
207. Course Schedule
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
"""

#bfs

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = collections.defaultdict(set)
        indegree = {i:0 for i in range(numCourses)}
        
        for edge in prerequisites:
            out = edge[1]; inn = edge[0]
            if inn not in g[out]:
                g[out].add(inn)
                indegree[inn] += 1
        
        return self.bfs(g, indegree, numCourses)
    
    def bfs(self, g, indegree, numCourses) -> bool:
        q = collections.deque()
        visited = set()
        for inn in indegree.keys():
            if indegree[inn] == 0:
                q.append(inn)
        while q:
            out = q.popleft()
            visited.add(out)
            for inn in g[out]:
                indegree[inn] -= 1
                if indegree[inn] == 0: q.append(inn)
        return len(visited) == numCourses

#dfs

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = collections.defaultdict(set)
        visited = [0 for i in range(numCourses)]
        
        for edge in prerequisites:
            out = edge[1]; inn = edge[0]
            g[out].add(inn)
        for i in range(numCourses):
            if not self.dfs(g, visited, i):
                return False
        return True
    
    def dfs(self, graph, visited, i) -> bool:
        if visited[i] == -1: return False   #has been visited and has ring
        if visited[i] == 1: return True     #has been visited but no ring
        visited[i] = -1 	#visiting
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        visited[i] = 1      #done visited all neighbors
        return True
