"""
222. Count Complete Tree Nodes
Given a complete binary tree, count the number of nodes.
Note:
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and 
all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes 
inclusive at the last level h.
"""

#Brute force

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        return self.countNodes(root.left)+self.countNodes(root.right)+1

#Optimized

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        h_left = 0; h_right = 0
        node_left = root; node_right = root
        while node_left:
            h_left += 1
            node_left = node_left.left
        while node_right:
            h_right += 1
            node_right = node_right.right
        if  h_left == h_right: return 2**h_left-1
        return self.countNodes(root.left)+self.countNodes(root.right)+1
