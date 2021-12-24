import collections
import threading
import time
from heapq import *
from collections import *
from typing import *
# import random


from collections import Counter


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        cnts_1, cnts_2 = Counter(s1), Counter(s2[:len(s1)])

        for start in range(len(s1), len(s2)):
            if cnts_1 == cnts_2:
                return True
            cnts_2[s2[start]] += 1
            cnts_2[s2[start-len(s1)]] -= 1
            if cnts_2[s2[start-len(s1)]] == 0:
                del cnts_2[s2[start-len(s1)]]

        return cnts_1 == cnts_2

# 20211224
