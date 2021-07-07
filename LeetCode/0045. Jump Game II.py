"""
!45. Jump Game II
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
"""

# Greedy


class Solution:

    def jump(self, nums: List[int]) -> int:
        res = 0
        cur_end = 0
        cur_farthest = 0
        for i in range(len(nums)):
            cur_farthest = max(cur_farthest, i + nums[i])
            if i == cur_end:
                res += 1
                cur_end = cur_farthest
        return res
