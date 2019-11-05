"""
1007. Minimum Domino Rotations For Equal Row
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
We may rotate the i-th domino, so that A[i] and B[i] swap values.
Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.
If it cannot be done, return -1.
"""

#Traverse

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        A_swap = B_swap = 0
        for i in range(n):
            if A[i] == A[0] or B[i] == A[0]:
                if A[i] != A[0]: A_swap += 1
                if B[i] != A[0]: B_swap += 1
            else: break
        if i == n-1: return min(A_swap, B_swap)
        
        A_swap = B_swap = 0
        for i in range(n):
            if A[i] == B[0] or B[i] == B[0]:
                if A[i] != B[0]: A_swap += 1
                if B[i] != B[0]: B_swap += 1
            else: break
        if i == n-1: return min(A_swap, B_swap)
        return -1

