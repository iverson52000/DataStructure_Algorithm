"""
$314. Binary Tree Vertical Order Traversal
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.
"""

#dfs

import collections
res = []
if not root: return res
m = {}
q = collections.deque()
q.append((0, root))
while q:
    idx, node = q.popleft()
    m[idx] = m.get(idx, []) + [node.val]
    if node.left: q.append((idx-1, node.left))
    if node.right: q.append((idx+1, node.right))
m.sort()
for key, val in m: res.append(val)
return res
