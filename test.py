import collections
import threading
import time
import queue
from collections import *
from typing import List
import random


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        m = collections.defaultdict(list)

        for i, v in enumerate(colors):
            m[v].append(i)

        res = []
        for i, c in queries:
            if c in m:
                # search where the element can be inserted
                index = bisect.bisect_left(m[c], i)
                if index == 0:
                    res.append(abs(i-m[c][0]))
                elif index >= len(m[c]):
                    res.append(i-m[c][-1])
                else:
                    res.append(min(abs(i-m[c][index-1]), abs(m[c][index]-i)))
            else:
                res.append(-1)

        return res
