class MyQueue:

    def __init__(self):
        self.data = []

    def push(self, x) -> None:
        self.data = [x] + self.data
    def pop(self) -> int:
        if len(self.data) == 0:
            return
        return self.data.pop()

    def peek(self) -> int:
        return self.data[-1]
        
    def empty(self) -> bool:
        return len(self.data) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()