import collections
import threading
import time
import q
from collections import *
from typing import List
import random


class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()  # split(sep=None) will discard empty strings.
        n_words = len(words)
        n_space = text.count(' ')
        gap = 0 if n_words == 1 else n_space // (n_words - 1)
        n_trailing = n_space - gap * (n_words - 1)  # credit to @madno

        return (' ' * gap).join(words) + ' ' * n_trailing
