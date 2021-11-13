import collections
import threading
import time
import queue
from collections import *
from typing import List
import random


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.cnt_p = 0
        self.cnt_q = 0

        def dfs(self, root, p, q) -> TreeNoder:
            if not root:
                return None

            leftRes = self.dfs(root.left, p, q)
            rightRes = self.dfs(root.right, p, q)

            if root.val == p.val:
                self.countp += 1
                return root
            if root.val == q.val:
                self.cnt_q += 1
                return root
            if leftRes and rightRes:
                return root

        return leftRes or rightRes

        res = self.dfs(root, p, q)

        if not self.countp or not self.cnt_q:
            return None

        return res
