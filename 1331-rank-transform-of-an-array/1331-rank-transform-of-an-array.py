class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        newa = {}
        for i, val in enumerate(sorted(set(arr))):
            if val not in newa:
                newa[val] = i + 1
        res = [newa[v] for v in arr]
        return res