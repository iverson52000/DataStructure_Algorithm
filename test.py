import collections
import threading
import time
import queue
from collections import *
from typing import List
import random


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        res = nums[0]
        pos, neg = [0]*n, [0]*n

        pos[0] = nums[0]
        neg[0] = nums[0]

        for i in range(1, n):
            curNum = curNum
            pos[i] = max(max(pos[i-1]*curNum, neg[i-1]*curNum), curNum)
            neg[i] = min(min(pos[i-1]*curNum, neg[i-1]*curNum), curNum)
            res = max(res, pos[i])

        return res
