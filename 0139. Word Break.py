"""
 *139. Word Break
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine 
if s can be segmented into a space-separated sequence of one or more dictionary words.
"""

#dfs
class Solution(object):
    def wordBreak(self, s, wordDict):
        memo = {}
        wordDict = set(wordDict)
        return self.dfs(s, wordDict, memo)
    
    def dfs(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if s in wordDict:
            memo[s] = True
            return True
        for i in range(1, len(s)):
            if s[:i] in wordDict and self.dfs(s[i:], wordDict, memo):
                memo[s] = True
                return True
        memo[s] = False
        return False

#bfs
class Solution(object):
    def wordBreak(self, s, wordDict):
        visited = {}
        return self.bfs(s, wordDict, visited)
    
    def bfs(self, s, wordDict, visited):
        if s in wordDict: return True
        q = collections.deque([s])
        while q:
            cur_s = q.pop()
            if cur_s in wordDict: return True
            for i in range(1, len(cur_s)):
                if cur_s[:i] in wordDict and cur_s[i:] not in visited:
                    q.append(cur_s[i:])
                    visited[cur_s[i:]] = True
        return False

#dp
class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n+1):
            for left in range(i):
                if dp[left] and s[left:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]
