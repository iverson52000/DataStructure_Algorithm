"""
282. Expression Add Operators
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
"""

# dfs


class Solution:

    def addOperators(self, num: str, target: int) -> List[str]:
        self.res = []
        diff = 0
        cur_num = 0
        path = ''
        self.dfs(num, target, diff, cur_num, path)
        return self.res

    def dfs(self, num, target, diff, cur_num, path):
        if len(num) == 0 and cur_num == target:
            self.res.append(path)
            return
        for i in range(1, len(num) + 1):
            cur = num[:i]
            if len(cur) > 1 and cur[0] == '0':  # prevent "00"
                return
            nxt = num[i:]
            if len(path) == 0:
                self.dfs(nxt, target, int(cur), int(cur), cur)  # prevent +123
            else:
                self.dfs(nxt, target, int(cur), cur_num +
                         int(cur), path + '+' + cur)
                self.dfs(nxt, target, -int(cur), cur_num -
                         int(cur), path + '-' + cur)
                self.dfs(nxt, target, diff * int(cur), (cur_num -
                                                        diff) + diff * int(cur), path + '*' + cur)
