import collections
import threading
import time
from heapq import *
from collections import *
from typing import List
import random


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []

        for n, start, end in trips:
            heappush(heap, (start, n))
            heappush(heap, (end, -n))

        passenger = 0

        while heap:
            _, n = heappop(heap)
            passenger += n
            if passenger > capacity:
                return False

        return True
