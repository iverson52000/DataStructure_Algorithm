"""
155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
•	push(x) -- Push element x onto stack.
•	pop() -- Removes the element on top of the stack.
•	top() -- Get the top element.
•	getMin() -- Retrieve the minimum element in the stack.
"""

#Two stack

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min or x <= self.min[-1]: self.min.append(x)

    def pop(self) -> None:
        num = self.stack.pop()
        if self.min[-1] == num: self.min.pop()
        
    def top(self) -> int:
        if len(self.stack) == 0: return None
        else: return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min) == 0: return None
        else: return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin() 

#One stack
        
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        cur_min = self.getMin()
        if cur_min == None or x <= cur_min: cur_min = x            
        self.stack.append((x, cur_min))


    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0: return None
        else: return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0: return None
        else: return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

