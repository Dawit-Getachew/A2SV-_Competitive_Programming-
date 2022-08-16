class Solution:
    def __init__(self):
        self.stack = []
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        if self.stack:
            self.stack.pop()
    def peak(self):
        if self.stack:
            return self.stack[-1]
    def removeDuplicates(self, s: str) -> str:
        for char in s:
            if char != self.peak():
                self.push(char)
            else:
                self.pop()
        return "".join(self.stack)
        