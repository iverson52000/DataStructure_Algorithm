"""
450. Delete Node in a BST
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
1.  Search for a node to remove.
2.  If the node is found, delete the node.
Note: Time complexity should be O(height of tree).
"""

#recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        if root.val > key: root.left = self.deleteNode(root.left, key)
        elif root.val < key: root.right= self.deleteNode(root.right, key)
        else: 
            if not root.right: return root.left
            if not root.left: return root.right        
            temp = root.right
            minn = temp.val
            while temp.left:
                temp = temp.left
                minn = temp.val
            root.val = minn
            root.right = self.deleteNode(root.right, root.val)
        return root 
