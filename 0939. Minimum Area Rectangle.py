"""
939. Minimum Area Rectangle
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.
If there isn't any rectangle, return 0.
"""

#traverse

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points: return 0
        res = float('inf')
        points_set = set()
        for x, y in points:
            points_set.add((x, y))
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 > x2 and y1 > y2:
                    if (x1, y2) in points_set and (x2, y1) in points_set:
                        area = abs(x2-x1)*abs(y2-y1)
                        if area != 0: res = min(res, area)
        return 0 if res == float('inf') else res
