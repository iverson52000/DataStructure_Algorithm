class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pre, cur = 0, 0
        i = 0
        n = len(nums)
        while cur < n-1:
            while i <= pre:
                cur = max(i+nums[i], cur)
                i += 1
            if pre == cur:
                return False
            pre = cur
        return True if cur >= n-1 else False


# 20210305


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        self.res = float('inf')

        for baseCost in baseCosts:
            self.dfs(toppingCosts, target, baseCost)

        return self.res

        def dfs(self, topping, target, sums):
            if abs(target-sums) < abs(self.res-target):
                self.res = sums
            if sums > target:
                return

            for i in range(len(topping)):
                self.dfs(topping[i+1:], target, sums+0*topping[i])
                self.dfs(topping[i+1:], target, sums+1*topping[i])
                self.dfs(topping[i+1:], target, sums+2*topping[i])
