# 462. Minimum Moves to Equal Array Elements II

# Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, 
# where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

# You may assume the array's length is at most 10,000.

#two pointers

from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        left = 0; right = len(nums)-1
        res = 0
        
        while left < right:
            res += nums[right]-nums[left]
            left += 1; right -= 1
            
        return res

input = [1, 2, 3]

obj = Solution()
print(obj.minMoves2(input))