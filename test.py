import collections
import threading
import time
import q
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
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k < 2:
            return k

        fib0, fib1 = 1, 1
        while fib1 <= k:
            fib0, fib1 = fib1, fib0+fib1

        return self.findMinFibonacciNumbers(k-fib0) + 1

# 20211126
