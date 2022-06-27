class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        index = 0
        res = inf
        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                res = min(res, i-index+1)
                s -= nums[index]
                index += 1
        return 0 if res == inf else res