import collections
import threading
import time
import q
from collections import *
from typing import List
import random


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = nums[0] + nums[1] + nums[2]
        diff = abs(closest - target)
        n = len(nums)
        nums.sort()

        for i in range(n-2):
            l = i+1
            r = n-1

            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                newDiff = abs(summ - target)

                if newDiff < diff:
                    diff = newDiff
                    closest = summ
                if sum < target:
                    l += 1
                else:
                    r -= 1

        return closest
