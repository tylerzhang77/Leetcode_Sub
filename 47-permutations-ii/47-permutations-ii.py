class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.helper(nums, [], res)
        return res
    
    def helper(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            self.helper(nums[:i]+nums[i+1:], path+[nums[i]], res)