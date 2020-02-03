"""
!84. Largest Rectangle in Histogram
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        s = [-1]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[s[-1]]:
                h = heights[s.pop()]
                w = i-s[-1]-1
                res = max(res, h*w)
            s.append(i)
        #heights.pop()
        return res 
