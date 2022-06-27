class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        counter = len(nums) - 1
        res = [0] * len(nums)
        while counter >= 0:
            ls = nums[l] ** 2
            rs = nums[r] ** 2
            if ls < rs:
                res[counter] = rs
                counter -= 1
                r -= 1
            else:
                res[counter] = ls
                counter -= 1
                l += 1
        return res
            