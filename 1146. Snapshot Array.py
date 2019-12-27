"""
1146. Snapshot Array
Implement a SnapshotArray that supports the following interface:
•   SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
•   void set(index, val) sets the element at the given index to be equal to val.
•   int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
•   int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
"""

#list of list and binary search

class SnapshotArray:

    def __init__(self, length: int):
        self.A = [[[-1, 0]] for i in range(length)]
        self.snap_id = 0

    def set(self, index, val):
        self.A[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id-1

    def get(self, index, snap_id):
        i = bisect.bisect(self.A[index], [snap_id+1])-1
        return self.A[index][i][1]
        
#nums hashmap and snap array

class SnapshotArray(object):

    def __init__(self, length):
        self.nums = {}
        self.snaps = []   

    def set(self, index, val):
        self.nums[index] = val

    def snap(self):
        self.snaps.append(self.nums.copy())
        return len(self.snaps)-1

    def get(self, index, snap_id):
        if index in self.snaps[snap_id]:
            return self.snaps[snap_id][index]
        else: return 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

