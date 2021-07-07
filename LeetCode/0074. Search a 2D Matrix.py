#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:03:58 2019

@author: alberthsu
"""

"""
74. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
•	Integers in each row are sorted from left to right.
•	The first integer of each row is greater than the last integer of the previous row.
"""

#binary search

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target) -> bool:
        if not matrix or not matrix[0]: return False

        n_r = len(matrix); n_c = len(matrix[0])
        left = 0; right = n_r*n_c-1

        while left <= right:
            mid = (left+right)//2
            num = matrix[mid//n_c][mid%n_c]
            if num == target: return True
            if num > target: right = mid-1
            else: left = mid+1
            
        return False
