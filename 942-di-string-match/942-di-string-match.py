class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        res = []
        for i in s:
            if i == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
        res.append(high)
        return res