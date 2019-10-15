#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:14:54 2019

@author: alberthsu
"""

"""
54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        res = []
        left = 0; right = len(matrix[0])-1
        top = 0; bottom = len(matrix)-1
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1
            
            if left > right or top > bottom: break
                
            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
