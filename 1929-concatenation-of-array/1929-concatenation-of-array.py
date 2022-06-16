class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:     
        return [nums[i] if i < len(nums) else nums[i-len(nums)] for i in range(2*len(nums))]
        