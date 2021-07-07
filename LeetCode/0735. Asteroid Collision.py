# 735. Asteroid Collision
# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

#stack

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pos = []
        neg = []
        
        for asteroid in asteroids:
            if asteroid > 0:
                pos.append(asteroid)
            else:
                while pos and pos[-1] < abs(asteroid):
                    pos.pop()
                if not pos:
                    neg.append(asteroid)
                elif pos[-1] == abs(asteroid):
                    pos.pop()
                
        return neg+pos