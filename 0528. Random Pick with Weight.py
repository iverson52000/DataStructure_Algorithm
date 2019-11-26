"""
528. Random Pick with Weight
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.
"""

#prefixSum and binary search

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.n = len(w)
        for i in range(1, self.n):
            w[i] += w[i-1]

    def pickIndex(self) -> int:
        num = random.randint(1, self.w[-1])
        left = 0; right = self.n-1
        while left <= right:
            mid = (left+right)//2
            if num == self.w[mid]: return mid
            elif num < self.w[mid]: right = mid-1
            else: left = mid+1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
