class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        temp = [(sum(i), ind) for ind, i in enumerate(mat)]
        temp = sorted(temp, key = lambda x: x[0])
        res = [i[1] for i in temp]
        return res[:k]
        