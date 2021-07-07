"""
797. All Paths From Source to Target
Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them 
in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for 
which the edge (i, j) exists.
"""

# dfs+backtracking


class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(cur, path):
            if cur == len(graph) - 1:
                res.append(path.copy())
            else:
                for i in graph[cur]:
                    path.append(i)
                    dfs(i, path)
                    path.pop()
        res = []
        dfs(0, [0])
        return res
