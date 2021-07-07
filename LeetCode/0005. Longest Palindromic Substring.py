"""
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum 
length of s is 1000.
"""

#Two pointer

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        res = ''
        for i in range(len(s)):
            tmp = self.isPal(s, i, i)
            if len(tmp) > len(res): res = tmp
            tmp = self.isPal(s, i, i+1)
            if len(tmp) > len(res): res = tmp
        return res
    
    def isPal(self, s, left, right) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]: 
            left -= 1; right += 1
        return s[left+1:right]
    
#dp

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        res = ''
        n = len(s)
        dp = [[False]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = True
            for left in range(i, -1, -1):
                if s[left] == s[i] and (i-left < 2 or dp[left+1][i-1]):
                    dp[left][i] = True
                    if i-left+1 > len(res):
                        res = s[left:i+1]
        return res
        

