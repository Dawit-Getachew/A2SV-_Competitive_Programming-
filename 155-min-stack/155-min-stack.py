class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            if val <= self.minStack[-1]:
                self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            temp = self.stack.pop()
            if self.minStack[-1] == temp:
                self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
    def getMin(self) -> int:
        if self.stack:
            temp = self.minStack[-1]
            if self.minStack[-1] == temp:
                if temp in self.stack:
                    return temp
                

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()