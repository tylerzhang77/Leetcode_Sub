class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rec = dict()
        for ind, val in enumerate(nums):
            if target - val not in rec:
                rec[val] = ind
            else:
                return [rec[target-val],ind]