"""
31. Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Use two-pointers: two pointers start from back
        # first pointer smaller stop at descending point
        # second pointer i stop at value > nums[j]
        # swap and sort rest
        if not nums: return None
        index = len(nums)-1
        smaller = -1 # smaller is set to -1 for case `4321`, so need to reverse all in following step
        while index > 0:
            if nums[index-1] < nums[index]: # first one violates the trend
              smaller = index-1
              break
            index -= 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[smaller]: # 
                nums[i], nums[smaller] = nums[smaller], nums[i] # swap position
                nums[smaller+1:] = sorted(nums[smaller+1:]) # sort rest
                return
        
        