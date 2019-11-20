"""
133. Clone Graph
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
"""

#hashmap+graph dfs

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        node_copy = Node(node.val, [])
        m = collections.defaultdict()
        m[node] = node_copy
        self.dfs(node, m)
        return node_copy
    
    def dfs(self, node, m) -> 'Node':
        if not node: return None
        for neighbor  in node.neighbors:
            if neighbor not in m:
                neighbor_copy = Node(neighbor.val, [])
                m[neighbor] = neighbor_copy
                m[node].neighbors.append(neighbor_copy)
                self.dfs(neighbor, m)
            else:
                m[node].neighbors.append(m[neighbor])


