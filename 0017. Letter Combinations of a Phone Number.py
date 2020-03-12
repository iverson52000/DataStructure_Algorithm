"""
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent.
"""

# dfs


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        self.letters = ["", "", "abc", "def", "ghi",
                        "jkl", "mno", "pqrs", "tuv", "wxyz"]
        level = 0
        path = ''
        self.dfs(digits, level, path, res)
        return res

    def dfs(self, digits, level, path, res):
        if level == len(digits):
            res.append(path)
            return
        candidates = self.letters[int(digits[level])]
        for candidate in candidates:
            self.dfs(digits, level + 1, path + candidate, res)
