"""
659. Split Array into Consecutive Subsequences
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3. 
"""

#Greedy+hashmap

class Solution:
    def isPossible(self, nums) -> bool:
            freq = collections.Counter(nums)
            need = collections.Counter()
            for num in nums:
                if freq[num] == 0: continue
                freq[num] -= 1
                if need[num] > 0:
                    need[num] -= 1
                    need[num+1] += 1
                elif freq[num+1] != 0 and freq[num+2] != 0:
                    freq[num+1] -= 1
                    freq[num+2] -= 1
                    need[num+3] += 1
                else:
                    return False
            return True
