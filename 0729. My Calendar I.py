"""
729. My Calendar I
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.
Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)
For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
"""

#bst

class TreeNode:
    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.left = None
        self.right = None

    def insert(self, start, end) -> bool:
        if end <= self.s:
            if self.left is None:
                self.left = TreeNode(start, end)
                return True
            else:
                return self.left.insert(start, end)
        elif start >= self.e:
            if self.right is None:
                self.right = TreeNode(start, end)
                return True
            else:
                return self.right.insert(start, end)
        else:
            return False

class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = TreeNode(start, end)
            return True
        else:
            return self.root.insert(start, end)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
