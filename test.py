from heap import *


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pre, cur = 0, 0
        i = 0
        n = len(nums)
        while cur < n-1:
            while i <= pre:
                cur = max(i+nums[i], cur)
                i += 1
            if pre == cur:
                return False
            pre = cur
        return True if cur >= n-1 else False


# 20210321
