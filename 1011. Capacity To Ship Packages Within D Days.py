"""
1011. Capacity To Ship Packages Within D Days
A conveyor belt has packages that must be shipped from one port to another within D days.
The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with 
packages on the conveyor belt (in the order given by weights). We may not load more weight than the 
maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor 
belt being shipped within D days.
"""

#binary search

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if not weights: return 0
        left = max(weights); right = sum(weights)
        while left <= right:
            mid = (left+right)//2
            group = self.minSub(weights, mid)
            if group > D: left = mid+1
            else: right = mid-1
        return left
    
    def minSub(self, weights, mid) -> int:
        cur_sum = 0; group = 1
        for weight in weights:
            cur_sum += weight
            if cur_sum > mid: 
                group += 1
                cur_sum = weight
        return group
