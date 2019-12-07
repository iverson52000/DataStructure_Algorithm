"""
!354. Russian Doll Envelopes
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One 
envelope can fit into another if and only if both the width and height of one envelope is greater 
than the width and height of the other envelope.
What is the maximum number of envelopes can you Russian doll? (put one inside other)
"""

#sort then binary search

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes: return 0
        tmp = []
        envelopes.sort(key=lambda x: (x[0], -x[1]))        
        for i in range(len(envelopes)):
            left = 0; right = len(tmp)-1
            height = envelopes[i][1]
            while left <= right:
                mid = (left+right)//2
                if height > tmp[mid]: left = mid+1
                else: right = mid-1
            if left >= len(tmp): tmp.append(height)
            else: tmp[left] = height        
        return len(tmp)
