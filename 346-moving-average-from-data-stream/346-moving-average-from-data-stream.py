class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.data = []
    def next(self, val: int) -> float:
        self.data.append(val)
        if len(self.data) <= self.size:
            return mean(self.data)
        else:
            return mean(self.data[-self.size:])


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)