import threading
import time
import queue


# 20211028
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cnts, res = Counter(changed), []

        for num in sorted(changed, key=lambda x: abs(x)):
            if cnts[num] == 0:
                continue
            if cnts[2*num] == 0:
                return []
            res += [num]
            if num == 0 and cnts[num] <= 1:
                return []
            cnts[num] -= 1
            cnts[2*num] -= 1

        return res
