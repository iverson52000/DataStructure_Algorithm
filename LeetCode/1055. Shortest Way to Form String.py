"""
1055. Shortest Way to Form String
From any string, we can form a subsequence of that string by deleting some number of characters 
(possibly no deletions).
Given two strings source and target, return the minimum number of subsequences of source such that 
their concatenation equals target. If the task is impossible, return -1.
"""

#two pointer

source = "abc"; target = "acdbc"

res = 0
i_target = 0
while i_target < len(target):
    exist = False
    for i_source in range(len(source)):
        if i_target < len(target) and source[i_source] == target[i_target]:
            exist = True
            i_target += 1
    if not exist: 
        res =  -1
        break
    res += 1
