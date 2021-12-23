import collections
import threading
import time
from heapq import *
from collections import *
from typing import *
# import random


class Player:
    member = True

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def run(self) -> int:
        print("running")
        return 1


class VIP(Player):
    def __init__(self, name: str, age: int, tier: str):
        super().__init__(name, age)
        self.tier = tier

    def run(self) -> int:
        # Player.run(self)
        print(f"running like VIP({self.tier})")
        return 1

    def fly(self):
        print('flying')


player = Player('Albert', 30)
vip = VIP('Bryan', 20, 'Gold')


def doRun(char):
    char.run()  # polymorphism


playerRunning = doRun(player)
vipRunning = doRun(vip)

# 20211221
