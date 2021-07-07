"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.
"""

#dfs

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = ''
        left = right = n
        self.dfs(res, path, left, right)
        return res
    
    def dfs(self, res, path, left, right):
        if left > right: return
        if left == 0 and right == 0: res.append(path)
        if left > 0: self.dfs(res, path+'(', left-1, right)
        if right > 0: self.dfs(res, path+')', left, right-1)    
        
        