"""
889. Construct Binary Tree from Preorder and Postorder Traversal
Return any binary tree that matches the given preorder and postorder traversals.
Values in the traversals pre and post are distinct positive integers.
"""

#divide and conquer

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre: return
        root = TreeNode(pre[0])
        pre, post = pre[1:], post[:-1]
        if not pre: return root
        i = post.index(pre[0])
        root.left = self.constructFromPrePost(pre[:i+1], post[:i+1])
        root.right = self.constructFromPrePost(pre[i+1:], post[i+1:])
        return root
