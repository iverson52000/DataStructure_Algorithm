import threading
import time
import queue


def fn(nums):
    has_pos = False
    has_neg = False
    for num in nums:
        has_pos = num > 0
        has_neg = num < 0
    return (has_pos, has_neg)


print(fn([0, 1, 2]))

# 20210819
