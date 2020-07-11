"""
78. Subset
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
"""

# dfs


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        path = []
        level = 0
        self.dfs(res, path, level, nums)
        return res

    def dfs(self, res, path, level, nums):
        if level > len(nums):
            return
        res.append(path.copy())
        for i in range(level, len(nums)):
            path.append(nums[i])
            self.dfs(res, path, i + 1, nums)
            path.pop()
