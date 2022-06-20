class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        dic = {}
        res = []
        for i, val in enumerate(s):
            if val not in dic:
                dic[val] = i
        for i in nums:
            res.append(dic[i])
        return res            
        