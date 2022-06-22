class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        L, R = 0, len(nums) - 1
        res = -1
        while L < R:
            s = nums[L] + nums[R]
            if s >= k:
                R -= 1
            else:
                res = max(res, s)
                L += 1
        return res
                
                