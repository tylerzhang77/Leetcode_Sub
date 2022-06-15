class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minnum = inf
        cumsum = 0
        for i in nums:
            cumsum += i
            minnum = min(minnum, cumsum)
        return 1 if minnum >= 0 else 1 - minnum
