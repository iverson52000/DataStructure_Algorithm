"""
818. Race Car
Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)
Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).
When you get an instruction "A", your car does the following: position += speed, speed *= 2.
When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)
For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.
Now for some target position, say the length of the shortest sequence of instructions to get there.
"""

#brute force bfs

class Solution:
    def racecar(self, target: int) -> int:
        q = collections.deque()
        q.append((0, 1))
        visited = set([(0, 1)])
        res = 0
        while q:
            for i in range(len(q)):
                pos, speed = q.popleft()
                if pos == target:
                    return res
                if not (pos+speed, speed*2) in visited:
                    q.append((pos+speed, speed*2))
                    visited.add((pos+speed, speed*2))
                if not (pos, -1 if speed > 0 else 1) in visited:
                    q.append((pos, -1 if speed > 0 else 1))
                    visited.add((pos, -1 if speed > 0 else 1))
            res += 1 
