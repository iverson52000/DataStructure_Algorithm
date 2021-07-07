"""
844. Backspace String Compare
Given two strings S and T, return if they are equal when both are typed into empty text editors. 
# means a backspace character.
"""

#stack

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        res1 = self.stack(S, [])
        res2 = self.stack(T, [])
        return res1 == res2      
    
    def stack(self, S, stack) -> list:
        for char in S:
            if char is not "#":
                stack.append(char)
            else:
                if not stack: continue
                stack.pop()
        return stack


#two pointer

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        n1 = len(S)-1; n2 = len(T)-1  
        while n1 >= 0 or n2 >= 0:
            char1 = char2 = ""
            if n1 >= 0: char1, n1 = self.getChar(S, n1)
            if n2 >= 0: char2, n2 = self.getChar(T, n2)
            if char1 != char2: return False
        return True
           
    def getChar(self, s , n) -> (str, int):
        char, sign = '', 0
        while n >= 0 and not char:
            if s[n] == '#': sign += 1
            elif sign == 0: char = s[n]
            else: sign -= 1
            n -= 1
        return char, n
