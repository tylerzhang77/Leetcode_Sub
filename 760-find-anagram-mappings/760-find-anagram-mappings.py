class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {val:ind for ind,val in enumerate(nums2)}
        return [dic[num] for num in nums1]