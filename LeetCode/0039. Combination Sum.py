"""
39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        level = 0
        self.dfs(candidates, res, path, level, target)
        return res
    
    def dfs(self, candidates, res, path, level, target):
        if target < 0: return
        if target == 0:
            res.append(path.copy())
            return
        for i in range(level, len(candidates)):
            path.append(candidates[i])
            self.dfs(candidates, res, path, i, target-candidates[i])
            path.pop()
    