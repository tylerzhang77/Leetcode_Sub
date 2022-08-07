class Solution:
    def combinationSum(self, candidates, target):
        res = []
        self.helper(candidates, target, [], res)
        return res
    
    def helper(self, nums, tar, path, res):
        if tar < 0:
            return
        if tar == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            self.helper(nums[i:], tar - nums[i], path + [nums[i]], res)

        