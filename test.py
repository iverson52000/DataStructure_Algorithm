import collections
import threading
import time
from heapq import *
from collections import *
from typing import *
import random


class Solution:
    def __init__(self):
        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                           "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty",
                     "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        res = ''

        def dfs(num) -> str:
            if num == 0:
                return ""
            elif num < 20:
                return self.lessThan20[num] + " "
            elif num < 100:
                return self.tens[num//10] + " " + dfs(num % 10)
            else:
                return self.lessThan20[num//100] + " Hundred " + dfs(num % 100)

        while num > 0:
            if num % 1000 != 0:
                res = self.helper(num % 1000)+self.thousands[i]+' '+res
            num //= 1000
            i += 1

        return res.strip()

# 20211215
