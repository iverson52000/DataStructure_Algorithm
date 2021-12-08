import collections
import threading
import time
from heapq import *
from collections import *
from typing import *
import random


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node) -> Tuple[int, TreeNode]:
            if not node:
                return 0, None
            leftRes, rightRes = dfs(node.left), dfs(node.right)

            if leftRes[0] > rightRes[0]:
                return leftRes[0]+1, leftRes[1]
            elif leftRes[0] < rightRes[0]:
                return rightRes[0]+1, rightRes[1]
            else:
                return rightRes[0]+1, node

        return dfs(root)[1]

# 20211207
