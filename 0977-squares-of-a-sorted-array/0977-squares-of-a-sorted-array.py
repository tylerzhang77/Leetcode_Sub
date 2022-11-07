class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        ind = len(nums) - 1
        res = [0] * len(nums)
        while ind >= 0:
            lv, rv = nums[l]**2, nums[r]**2
            if lv > rv:
                res[ind] = lv
                l += 1
            else:
                res[ind] = rv
                r -= 1
            ind -= 1
        return res
            