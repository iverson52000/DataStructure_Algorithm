"""
684. Redundant Connection
In this problem, a tree is an undirected graph that is connected and has no cycles.
The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.
Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.
"""

#Union find

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        roots = [-1]*(len(edges)+1)
        for edge in edges:
            node1 = self.findRoot(roots, edge[0]); node2 = self.findRoot(roots, edge[1])
            if node1 == node2: return edge
            roots[node1] = node2
        return []
    
    def findRoot(self, roots, v):
        if roots[v] == -1: return v
        else:
            roots[v] = self.findRoot(roots, roots[v]) 
            return roots[v]
