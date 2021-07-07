"""
261.Graph Valid Tree
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
"""

#union find

class Solution:
    def validTree(self, n, edges):
        roots = [-1 for i in range(n)]
        for edge in edges:
            root1 = self.findRoot(roots, edge[0])
            root2 = self.findRoot(roots, edge[1])
            if root1 == root2: return False
            else: roots[root1] = root2
        return len(edges) == n-1
         
    def findRoot(self, roots, v):
        if roots[v] == -1: return v
        else:
            roots[v] = self.findRoot(roots, roots[v])
            return roots[v]

obj = Solution()
obj.validTree(n, edges)
