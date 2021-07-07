"""
168. Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
"""

class Solution:
    def convertToTitle(self, n: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        res = []
        while n > 0:
            res.append(capitals[(n-1)%26])
            n = (n-1)//26
        res = res[::-1]
        return ''.join(res)
