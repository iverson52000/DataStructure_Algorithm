"""
!552. Student Attendance Record II
Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.
A student attendance record is a string that only contains the following three characters:
1.	'A' : Absent.
2.	'L' : Late.
3.	'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
"""

#dp

class Solution(object):
    def checkRecord(self, n):
        M = 1000000007
        if n == 0: return 0
        if n == 1: return 3
        dp = [1, 1, 2]
        i = 2
        while i < n:
            dp.append((dp[i] + dp[i-1] + dp[i-2])%M)
            i += 1
        res = (dp[n] + dp[n-1] + dp[n-2])%M
        for i in range(n):
            res += dp[i+1]*dp[n-i]%M
            res %= M
        return res
