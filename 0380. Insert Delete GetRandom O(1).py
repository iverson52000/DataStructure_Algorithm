"""
380. Insert Delete GetRandom O(1)
Design a data structure that supports all following operations in average O(1) time.
1.	insert(val): Inserts an item val to the set if not already present.
2.	remove(val): Removes an item val from the set if present.
3.	getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
"""

#Array+Hashmap

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.m = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.m: return False
        self.nums.append(val)
        self.m[val] = len(self.nums)-1
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.m: return False
        last_val = self.nums[-1]
        self.nums[self.m[val]], self.nums[-1] = self.nums[-1], self.nums[self.m[val]]
        self.m[last_val] = self.m[val]
        self.nums.pop()
        self.m.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
