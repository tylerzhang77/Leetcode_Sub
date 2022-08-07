class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(sorted(candidates), target, [], res)
        return res
    
    def helper(self, nums, tar, path, res):
        if tar < 0:
            return
        if tar == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.helper(nums[i+1:], tar - nums[i], path + [nums[i]], res)