"""
46. Permutation
Given a collection of distinct integers, return all possible permutations.
"""

#dfs

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = []
        path = []
        visited = [False]*len(nums)
        self.dfs(nums, res, path, visited)
        return res

    def dfs(self, nums, res, path, visited):
    	if len(path) == len(nums):
    		res.append(path.copy())
    		return
    	for i in range(len(nums)):
    		if visited[i]: continue
    		visited[i] = True
    		path.append(nums[i])
    		self.dfs(nums, res, path, visited)
			visited[i] = False
    		path.pop()