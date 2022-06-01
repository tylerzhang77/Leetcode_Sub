class TwoSum:

    def __init__(self):
        self.val = []
                

    def add(self, number):
        val = self.val
        val.append(number)

    def find(self, value):
        val = self.val
        if len(val)<2:
            return False
        val.sort()
        left = 0
        right = len(val)-1
        while (left < right):
            if val[left] + val[right] < value:
                left += 1
            elif val[left] + val[right] > value:
                right -= 1
            else:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)