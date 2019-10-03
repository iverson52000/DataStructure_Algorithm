#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:53:54 2019

@author: alberthsu
"""

"""
122. Best Time to Buy and Sell Stock II
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]: res += (prices[i]-prices[i-1])
        return res
                                            