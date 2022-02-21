class MinStack:

    def __init__(self):
        self.L = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.L.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)
        

    def pop(self) -> None:
        if self.L:
            temp = self.L.pop()
            if self.min_stack:
                if self.min_stack[-1] == temp:
                    self.min_stack.pop()
            return temp

    def top(self) -> int:
        if self.L:
            return self.L[-1]

    def getMin(self) -> int:
        if self.min_stack:
            temp = self.min_stack[-1]
            if self.L:
                if temp in self.L:
                    return temp
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()