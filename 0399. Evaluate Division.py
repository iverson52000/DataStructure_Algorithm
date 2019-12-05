"""
399. Evaluate Division
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.
Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].
"""

#graph+bfs

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        g = collections.defaultdict(list)
        self.buildGraph(g, equations, values)
        for query in queries: self.bfs(res, g, query)
        return res
    
    def buildGraph(self, g, equations, values):       
        for vertices, value in zip(equations, values):
            nom, denom = vertices
            g[nom] += [(denom, value)]
            g[denom] += [(nom, 1/value)]
            
    def bfs(self, res, g, query):
        nom, denom = query
        if nom not in g or denom not in g:
            res.append(-1.0)
            return
        q = collections.deque()
        q.append((nom, 1.0))
        visited = set()
        while q:
            nom_pop, value_pop = q.popleft()
            if nom_pop == denom:
                res.append(value_pop)
                return
            visited.add(nom)
            for denom_g, value in g[nom_pop]:
                if denom_g not in visited:
                    q.append((denom_g, value_pop*value))
        res.append(-1.0)

