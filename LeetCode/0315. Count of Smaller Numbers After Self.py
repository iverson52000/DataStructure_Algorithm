"""
315. Count of Smaller Numbers After Self
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the 
right of nums[i].
"""

#binary search

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums: return None
        res = [0]*len(nums)
        tmp = []
        for i in range(len(nums)-1, -1, -1):
            left = 0; right = len(tmp)-1
            while left <= right:
                mid = (left+right)//2
                if nums[i] > tmp[mid]: left = mid+1
                else: right = mid-1
            res[i] = left
            tmp.insert(left, nums[i])
        return res