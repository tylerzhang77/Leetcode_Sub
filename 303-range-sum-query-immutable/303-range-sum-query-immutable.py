class NumArray:

    def __init__(self, nums: List[int]):
        self.data = nums

    def sumRange(self, left: int, right: int) -> int:
        sub = self.data[left:right+1]
        return sum(sub)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)