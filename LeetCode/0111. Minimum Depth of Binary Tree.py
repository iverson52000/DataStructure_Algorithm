"""
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
"""

#dfs

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if (not root.left) and (not root.right): return 1 #if root is leaf

        if (not root.left): return self.minDepth(root.right)+1  
        elif (not root.right): return self.minDepth(root.left)+1
        else: return min(self.minDepth(root.left), self.minDepth(root.right))+1 


#bfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        q = collections.deque()
        q.append((root, 1))
        while q:
            node, depth = q.popleft()
            if not node.left and not node.right: return depth
            if node.left: q.append((node.left, depth+1))
            if node.right: q.append((node.right, depth+1))    

