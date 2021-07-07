"""
403. Frog Jump
A frog is crossing a river. The river is divided into x units and at each unit there may or may not 
exist a stone. The frog can jump on a stone, but it must not jump into the water.
Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able 
to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume 
the first jump must be 1 unit.
If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note 
that the frog can only jump in the forward direction.
Note:
•   The number of stones is ≥ 2 and is < 1,100.
•   Each stone's position will be a non-negative integer < 231.
•   The first stone's position is always 0.
"""

#dfs

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo = set()
        target = stones[-1]
        stones = set(stones)
        return self.dfs(stones, memo, 1, 1, target)
 
    def dfs(self, stones, memo, cur, k, target) -> bool:
        if cur == target: return True         
        if cur > target or cur < 0 or k <= 0 or cur not in stones: return False  
        if (cur, k) in memo: return False
        units = [k-1, k, k+1]
        for unit in units:
            if (cur+unit) in stones:
                if self.dfs(stones, memo, cur+unit, unit, target): return True
        memo.add((cur, k))
        return False
