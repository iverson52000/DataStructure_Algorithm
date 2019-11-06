"""
410. Split Array Largest Sum
Given an array which consists of non-negative integers and an integer m, you can split the array into mnon-empty continuous subarrays. Write an algorithm to minimize the largest sum among these msubarrays.
Note:
If n is the length of array, assume the following constraints are satisfied:
•	1 ≤ n ≤ 1000
•	1 ≤ m ≤ min(50, n)
"""

#binary search

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if not nums: return 0
        left = max(nums); right = sum(nums)
        while left <= right:
            mid = (left+right)//2
            if self.minSub(mid, nums) > m: left = mid+1
            else: right = mid-1
        return left
    
    def minSub(self, mid, nums) -> int:
        cur_sum = 0; n_sub = 1
        for num in nums:
            cur_sum += num
            if cur_sum > mid:
                cur_sum = num
                n_sub += 1
        return n_sub

#dp

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        sums = [0]*(n+1)
        dp = [[float('inf')]*(n+1) for i in range(m+1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            sums[i] = sums[i-1]+nums[i-1]
        
        for m_tmp in range(1, m+1):
            for n_tmp in range(1, n+1):
                for k in range(m_tmp-1, n_tmp):
                    cur_max = max(dp[m_tmp-1][k], sums[n_tmp]-sums[k])
                    dp[m_tmp][n_tmp] = min(dp[m_tmp][n_tmp], cur_max)
        return dp[m][n]
