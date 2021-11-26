import collections
import threading
import time
import q
from collections import *
from typing import List
import random


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(self.w)):
            w[i] += w[i-1]

    def pickIndex(self) -> int:
        num = random.randint(1, self.w[-1])
        l = 0
        r = len(self.w)-1

        while l <= r:
            mid = (l+r)//2
            if self.w[mid] == num:
                return mid
            elif self.w[mid] > num:
                r = mid-1
            else:
                l = mid+1

        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# 20211126
