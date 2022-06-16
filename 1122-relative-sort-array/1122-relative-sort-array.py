class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        temp = collections.Counter(arr1)
        res = []
        for i in arr2:
            res += [i]*temp.pop(i)
        return res + sorted(temp.elements())