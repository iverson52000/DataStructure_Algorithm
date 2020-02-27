
"""
301. Remove Invalid Parentheses
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
"""

# bfs


class Solution:

    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        q = collections.deque()
        q.append(s)
        visited = set()
        found = False
        while q:
            s_pop = q.popleft()
            if self.isValid(s_pop):
                res.append(s_pop)
                found = True
            if found:
                continue
            for i in range(len(s_pop)):
                if s_pop[i] not in ('(', ')'):
                    continue
                s_next = s_pop[:i] + s_pop[i + 1:]
                if s_next not in visited:
                    q.append(s_next)
                    visited.add(s_next)
        return res

    def isValid(self, s) -> bool:
        left = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                left -= 1
            if left < 0:
                return False
        return left == 0
