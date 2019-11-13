"""
679. 24 Game
You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.
"""

#dfs

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1 and abs(nums[0] - 24) <= 0.001: return True
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    others = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    if self.judgePoint24(others+[nums[i]+nums[j]]): return True
                    if self.judgePoint24(others+[nums[i]*nums[j]]): return True
                    if self.judgePoint24(others+[nums[i]-nums[j]]): return True
                    if self.judgePoint24(others+[nums[j]-nums[i]]): return True
                    if nums[j] != 0 and self.judgePoint24(others+[nums[i]/nums[j]]): return True
                    if nums[i] != 0 and self.judgePoint24(others+[nums[j]/nums[i]]): return True
        return False
