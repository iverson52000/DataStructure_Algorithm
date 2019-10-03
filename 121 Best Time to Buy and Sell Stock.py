#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:47:11 2019

@author: alberthsu
"""

"""
121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        buy = float('inf'); res = 0
        for price in prices:
            buy = min(buy, price)
            res = max(res, price-buy)
        return res
        