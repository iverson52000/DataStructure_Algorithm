"""
1145. Binary Tree Coloring Game
Two players play a turn based game on a binary tree.  We are given the root of this binary tree, and the number of nodes n in the tree.  n is odd, and each node has a distinct value from 1 to n.
Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x.  The first player colors the node with value x red, and the second player colors the node with value y blue.
Then, the players take turns starting with the first player.  In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)
If (and only if) a player cannot choose such a node in this way, they must pass their turn.  If both players pass their turn, the game ends, and the winner is the player that colored more nodes.
You are the second player.  If it is possible to choose such a y to ensure you win the game, return true.  If it is not possible, return false.
"""

#dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        l_r = [0, 0]
        def dfs(node):
            if not node: return 0
            l, r = dfs(node.left), dfs(node.right)
            if node.val == x:
                l_r[0], l_r[1] = l, r
            return l+r+1
        dfs(root)
        p = n-sum(l_r)-1
        return dfs(root)/2 < max(max(l_r), p)
