"""
310. Minimum Height Trees
For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.
"""

#graph bfs

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0] 
        g = collections.defaultdict(list)
        for v1, v2 in edges:
            g[v1].append(v2)
            g[v2].append(v1)

        leaves = [i for i in range(n) if len(g[i]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                v_pop = g[leaf].pop()
                g[v_pop].remove(leaf)
                if len(g[v_pop]) == 1: new_leaves.append(v_pop)
            leaves = new_leaves
            
        return leaves
