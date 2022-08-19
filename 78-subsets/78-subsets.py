class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.bktk(sorted(nums),0,[], res)
        return res
    def bktk(self, nums, ind, path, res):
        res.append(path)
        for i in range(ind, len(nums)):
            self.bktk(nums, i+1, path + [nums[i]], res)
            