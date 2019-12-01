"""
!297. Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
"""

#preorder dfs

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []
        def dfs(root):
            if root == None:
                res.append(‘#’)
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)        
        dfs(root)
        return ‘,’.join(res)

data = '1, 2, 3, #'

    def deserialize(self, data):
        idx = [0]
        data = data.split(',')
        def dfs() -> TreeNode:
            if data[idx[0]] == ‘#’:
                idx[0] += 1
                return None
            root = TreeNode(data[idx[0]])
            idx[0] += 1
            root.left = dfs()
            root.right = dfs()
            return root       
        return dfs()
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
