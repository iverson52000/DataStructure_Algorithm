"""
*347. Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.
"""

# hashmap+heap

from heapq import *


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        res = []
        m = collections.Counter(nums)
        heap = [(-val, key) for key, val in m.items()]
        heapify(heap)
        for i in range(k):
            res.append(heappop(heap)[1])
        return res
