import collections
import threading
import time
from heapq import *
from collections import *
from typing import *
import random


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        stack = []  # non-decreasing
        arr = [float('-inf')] + arr + [float('-inf')]

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                cur = stack.pop()
                res += arr[cur] * (i - cur) * (cur - stack[-1])
            stack.append(i)

        return res % (10**9 + 7)

# 20211210
