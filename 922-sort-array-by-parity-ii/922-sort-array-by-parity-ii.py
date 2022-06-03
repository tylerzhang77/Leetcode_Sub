class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i,j,L = 0,1,len(nums)
        while j < L:
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
            else:
                j += 2
        return nums