# Given a prefix, return all words, that start with that prefix.
import collections
from typing import *

# Doggy day care centers help care for pet dogs while their owners might be busy at work.
# However, dogs can be unhappy if they are too crowded, and so each dog needs a certain amount of space.
# In addition, each dog also needs a certain amount of food.
# Please write a reservation system to allow pet owners to reserve a space for their pet at the day care.


class Dog:
    def __init__(self, size: int, foodRequired: int):
        pass


class ReservationSystem:
    def __init__(self, space: int, food: int):
        dates = ['2021113', '2021114']
        self.m = collections.defaultdict(List)

        for date in dates:
            self.m[date] = [space, food]


def reserverSpace(self, dog, date: str) -> bool:
    # m{date: [space, food]}
    space, food = self.m[date]
    size = dog.size
    foodRequired = dog.foodRequired

    if size > space:
        return False

    if foodRequired > food:
        return False

    space -= size
    food -= foodRequired

    self.m[date] = [space, food]

    return True


reservationSystem = ReservationSystem(100, 100)

# test
