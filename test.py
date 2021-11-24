import collections
import threading
import time
import q
from collections import *
from typing import List
import random


def snakesAndLadders(self, board: List[List[int]]) -> int:
    n = len(board)

    def label_to_position(label):
        r, c = divmod(label-1, n)
        if r % 2 == 0:
            return n-1-r, c
        else:
            return n-1-r, n-1-c

    visited = set()
    q = collections.deque()
    q.append((1, 0))

    while q:
        label, step = q.popleft()
        r, c = label_to_position(label)
        if board[r][c] != -1:
            label = board[r][c]
        if label == n*n:
            return step
        for x in range(1, 7):
            new_label = label + x
            if new_label <= n*n and new_label not in visited:
                visited.add(new_label)
                q.append((new_label, step+1))

    return -1
