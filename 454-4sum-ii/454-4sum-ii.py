class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic = dict()
        count = 0
        for a in nums1:
            for b in nums2:
                if a+b in dic:
                    dic[a+b] += 1
                else:
                    dic[a+b]= 1

        for n3 in nums3:
            for n4 in nums4:
                key = - n3 - n4
                if key in dic:
                    count += dic[key]
        return count