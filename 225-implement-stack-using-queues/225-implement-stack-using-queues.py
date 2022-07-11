class MyStack:

    def __init__(self):
        self.sin = deque()
        self.sout = deque()

    def push(self, x: int) -> None:
        self.sin.append(x)

    def pop(self) -> int:
        for i in range(len(self.sin) - 1):
            self.sout.append(self.sin.popleft())
        self.sin, self.sout = self.sout, self.sin
        return self.sout.pop()

    def top(self) -> int:
        if not self.sin:
            return None
        else:
            return self.sin[-1]

    def empty(self) -> bool:
        return not self.sin 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()