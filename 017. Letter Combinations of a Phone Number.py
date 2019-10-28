"""
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent.
"""

#dfs

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return ''
        res = []
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        path = ''
        level = 0
        self.dfs(digits, res, letters, path, level)
        return res
    
    def dfs(self, digits, res, letters, path, level):
        if level == len(digits):
            res.append(path)
            return
        candidate = letters[int(digits[level])]
        for i in range(len(candidate)):
            self.dfs(digits, res, letters, path+candidate[i], level+1)