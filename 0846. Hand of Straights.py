"""
846. Hand of Straights
Alice has a hand of cards, given as an array of integers.
Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.
Return true if and only if she can.
"""

#hashmap

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        m = collections.Counter(hand)
        for num in sorted(m):
            if m[num] > 0:
                for rest in range(W-1, -1, -1):
                    m[num+rest] -= m[num]
                    if m[num+rest] < 0: return False
        return True
