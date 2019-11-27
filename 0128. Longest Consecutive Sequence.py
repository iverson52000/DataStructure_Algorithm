"""
128. Longest Consecutive Sequence
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.
"""

#hashset+two pointers

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)
        for num in nums:
            if num not in s: continue
            s.remove(num)
            pre = num-1; nxt = num+1
            while pre in s: 
                s.remove(pre)
                pre-=1
            while nxt in s: 
                s.remove(nxt)
                nxt+=1
            res = max(res, nxt-pre-1)
        return res
