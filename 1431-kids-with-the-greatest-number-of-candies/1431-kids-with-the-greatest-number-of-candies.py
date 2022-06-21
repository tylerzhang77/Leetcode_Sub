class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        tgt = max(candies)
        res = []
        for i in candies:
            if (i + extraCandies) >= tgt:
                res.append(True)
            else:
                res.append(False)
        return res