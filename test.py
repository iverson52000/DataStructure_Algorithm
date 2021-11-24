import collections
import threading
import time
import queue
from collections import *
from typing import List
import random

# Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents the set of real numbers x such that a <= x < b.
# We remove the intersections between any interval in intervals and the interval toBeRemoved.

intervals = [[0, 2], [3, 4], [5, 7]]
toBeRemoved = [1, 6]

# Output: [[0,1],[6,7]]


def removeInterval(intervals, toBeRemoved):
    res = []

    for interval in intervals:
        if interval[1] <= toBeRemoved[0] or interval[0] >= toBeRemoved[1]:
            res.append(interval)
        else:
            if interval[0] < toBeRemoved[0]:
                res.append([interval[0], toBeRemoved[0]])
            if interval[1] > toBeRemoved[1]:
                res.append([toBeRemoved[1], interval[1]])

    return res


print(removeInterval(intervals, toBeRemoved))
