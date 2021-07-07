"""
753. Cracking the Safe
There is a box protected by a password. The password is a sequence of n digits where each digit can be one of the first k digits 0, 1, ..., k-1.
While entering a password, the last n digits entered will automatically be matched against the correct password.
For example, assuming the correct password is "345", if you type "012345", the box will open because the correct password matches the suffix of the entered password.
Return any password of minimum length that is guaranteed to open the box at some point of entering it.
"""

#dfs

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        self.k = k
        self.n = n
        return self.dfs("0"*n, set(["0"*n]), k**n)
        
    def dfs(self, cur_str, visited, total):
        if len(visited) == total: return cur_str
        for i in range(self.k):
            next_str = cur_str[-(self.n-1):]+str(i) if self.n!=1 else str(i)
            if next_str not in visited:
                visited.add(next_str)
                res = self.dfs(cur_str+str(i), visited, total)
                if res: return res
                visited.remove(next_str)
