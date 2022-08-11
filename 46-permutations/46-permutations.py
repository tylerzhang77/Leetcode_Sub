class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, [], res)
        return res
    def helper(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            self.helper(nums[:i]+nums[i+1:], path+[nums[i]], res)