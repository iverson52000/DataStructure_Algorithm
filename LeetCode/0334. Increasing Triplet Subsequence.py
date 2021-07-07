"""
334. Increasing Triplet Subsequence
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
"""

# small and big vars

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums: return False
        small = big = float('inf')
        for num in nums:
            if num <= small: small = num
            elif num <= big: big = num
            else: return True
        return False
