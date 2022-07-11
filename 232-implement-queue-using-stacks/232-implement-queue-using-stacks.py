class MyQueue:

    def __init__(self):
        self.sin = []
        self.sout = []

    def push(self, x: int) -> None:
        self.sin.append(x)

    def pop(self) -> int:
        if self.sout:
            return self.sout.pop()
        else:
            for i in range(len(self.sin)):
                self.sout.append(self.sin.pop())
            return self.sout.pop()

    def peek(self) -> int:
        if self.sout:
            ans = self.sout.pop()
            self.sout.append(ans)
            return ans 
        else:
            for i in range(len(self.sin)):
                self.sout.append(self.sin.pop())
            ans = self.sout.pop()
            self.sout.append(ans)
            return ans                    

    def empty(self) -> bool:
        return not (self.sin or self.sout)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()