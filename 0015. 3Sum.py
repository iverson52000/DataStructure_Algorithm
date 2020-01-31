"""
15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0 
Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
"""

#Two pointers

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            left = i+1; right = n-1
            while left < right:
                summ = nums[i]+nums[left]+nums[right]
                if summ == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1; right -= 1
                elif summ > 0: right -= 1
                else: left += 1
        return  list(set(map(tuple, res)))

