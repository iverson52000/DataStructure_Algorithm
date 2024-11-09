import collections


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = collections.deque()
        l, r = 0, len(nums)-1

        while l <= r:
            num_left, num_right = abs(nums[l]), abs(nums[r])
            if num_left > num_right:
                result.appendleft(num_left*num_left)
                l += 1
            else:
                result.appendleft(num_right*num_right)
                r -= 1

        return list(result)

# 20241109
