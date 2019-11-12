"""
1110. Delete Nodes And Return Forest
Given the root of a binary tree, each node in the tree has a distinct value.
After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
Return the roots of the trees in the remaining forest.  You may return the result in any order.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.to_delete = set(to_delete)
        self.res = []
        self.dfs(root, False)
        return self.res
    
    def dfs(self, root, parent_exist) -> TreeNode:
        if not root: return None
        if root.val in self.to_delete:
            root.left = self.dfs(root.left, False)
            root.right = self.dfs(root.right, False)
            return None
        else:
            if not parent_exist: self.res.append(root)
            root.left = self.dfs(root.left, True)
            root.right = self.dfs(root.right, True)    
            return root