"""
325.Maximum Size Subarray Sum Equals k
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
"""

# prefix sum+hashmap

nums = [1, -1, 5, -2, 3], k = 3

summ = 0
res = 0
m = {}
for i in range(len(nums)):
    summ += nums[i]
    if summ == k:
        res = i + 1
    elif summ - k in m:
        res = max(res, i - m[summ - k])
    if summ not in m:
        m[summ] = i
return res
